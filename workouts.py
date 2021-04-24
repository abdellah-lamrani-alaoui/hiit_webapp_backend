class Workout():
    duration_minutes = None

class ImageWorkout():
    duration_minutes = None
    image_basename = ""
    timer_url = ""

class VideoWorkout():
    duration_minutes = None
    video_url = ""
    timer_url = ""


class WorkoutDay2(ImageWorkout):
    image_basename = "day_2.png"
    timer_url = "http://www.intervaltimer.com/timers/10171876-day2"
    duration_minutes = 33


class WorkoutDay3(ImageWorkout):
    image_basename = "day_3.png"


class WorkoutDay17(ImageWorkout):
    image_basename = "day_17.png"
    timer_url = "http://www.intervaltimer.com/timers/10177970-day-17"
    duration_minutes = 29


class WorkoutDay8(ImageWorkout):
    image_basename = "day_8.png"


class WorkoutDay8Bis(ImageWorkout):
    image_basename = "day_8_bis.png"


class WorkoutDay15(ImageWorkout):
    image_basename = "day_15.png"


class WorkoutSissyMua(VideoWorkout):
    video_url = "https://www.youtube.com/embed/t7xdvBN-y1g"
    duration_minutes = 23


LIST_AVAILABLE_WORKOUTS = [WorkoutDay2, WorkoutDay3, WorkoutDay17,
                            WorkoutDay8, WorkoutDay8Bis, WorkoutDay15, WorkoutSissyMua]