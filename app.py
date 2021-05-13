import os
import random
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


import config
import workouts


app = FastAPI()

# Add static paths
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def is_workout_in_duration_filter(duration_workout: int, duration_filter: int):
    min_duration = 5
    max_duration = 60
    step = 5
    allowed_durations_filter = range(min_duration, max_duration, step)

    if duration_filter not in allowed_durations_filter:
        raise ValueError(f"Duration should be a multiple of {step} and between {min_duration} and  {max_duration}")

    closest_duration = min((elem for elem in allowed_durations_filter), key=lambda x:abs(x - duration_workout))
    return closest_duration == duration_filter


class NoWorkoutInFilter(Exception):
    """ Exception to be raised when there is no workout that respects the filtering conditions"""


def retreat_duration_filter(duration_filter):
    return int(duration_filter.split(" ")[0])


@app.get("/workout")
async def workout(duration_filter: Optional[str] = None):
    if not duration_filter:
        filtered_workouts = workouts.LIST_AVAILABLE_WORKOUTS
    else:
        duration_filter = retreat_duration_filter(duration_filter)
        filtered_workouts = [workout for workout in workouts.LIST_AVAILABLE_WORKOUTS if is_workout_in_duration_filter(workout.duration_minutes, duration_filter)]
        if not filtered_workouts:
            raise NoWorkoutInFilter
    workout_selected = random.choice(filtered_workouts)
    if issubclass(workout_selected, workouts.ImageWorkout):
        image_url = (
            config.BACK_END_URL
            + config.BASE_PATH_IMAGES
            + workout_selected.image_basename
        )
        return {
            "url": image_url,
            "timer_url": workout_selected.timer_url,
            "duration_minutes": workout_selected.duration_minutes,
            "workout_type": "image",
        }
    elif issubclass(workout_selected, workouts.VideoWorkout):
        return {
            "url": workout_selected.video_url,
            "timer_url": workout_selected.timer_url,
            "duration_minutes": workout_selected.duration_minutes,
            "workout_type": "video",
        }
    else:
        raise NotImplementedError("Only video and image workout are supported")
