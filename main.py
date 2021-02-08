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
    "http://localhost",
    "http://localhost:8080",
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
    image_url = config.BACK_END_URL + config.BASE_PATH_IMAGES + workout_selected.image_basename
    print(image_url)
    return {"image_url": image_url,
            "timer_url": workout_selected.timer_url,
            "duration_minutes": workout_selected.duration_minutes}

