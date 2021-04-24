import os
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import config
import workouts


app = FastAPI()

# Add static paths
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/workout")
async def workout():
    workout_selected = random.choice(workouts.LIST_AVAILABLE_WORKOUTS)
    if issubclass(workout_selected, workouts.ImageWorkout):
        image_url = config.BACK_END_URL + config.BASE_PATH_IMAGES + workout_selected.image_basename
        return {"url": image_url,
                "timer_url": workout_selected.timer_url,
                "duration_minutes": workout_selected.duration_minutes,
                "workout_type": "image"}
    elif issubclass(workout_selected, workouts.VideoWorkout):
        return {"url": workout_selected.video_url,
                "timer_url": workout_selected.timer_url,
                "duration_minutes": workout_selected.duration_minutes,
                "workout_type": "video"}
    else:
        raise NotImplementedError("Only video and image workout are supported")
