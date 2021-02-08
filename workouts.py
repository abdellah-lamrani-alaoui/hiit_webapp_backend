class Workout():
    duration_minutes = None
    image_basename = ""
    timer_url = ""


class WorkoutDay2(Workout):
    image_basename = "day_2.png"
    timer_url = "http://www.intervaltimer.com/timers/10171876-day2"
    duration_minutes = 33


class WorkoutDay3(Workout):
    image_basename = "day_3.png"


class WorkoutDay17(Workout):
    image_basename = "day_17.png"
    timer_url = "http://www.intervaltimer.com/timers/10177970-day-17"
    duration_minutes = 29


class WorkoutDay8(Workout):
    image_basename = "day_8.png"


class WorkoutDay8Bis(Workout):
    image_basename = "day_8_bis.png"


class WorkoutDay15(Workout):
    image_basename = "day_15.png"


LIST_AVAILABLE_WORKOUTS = [WorkoutDay2, WorkoutDay3, WorkoutDay17,
                            WorkoutDay8, WorkoutDay8Bis, WorkoutDay15]