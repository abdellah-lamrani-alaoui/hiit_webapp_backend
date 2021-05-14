class Workout:
    duration_minutes = None


class ImageWorkout:
    duration_minutes = None
    image_basename = ""
    timer_url = ""


class VideoWorkout:
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


class WorkoutJustineGallice(VideoWorkout):
    video_url = "https://www.youtube.com/embed/HVjgH1pXqBM"
    duration_minutes = 30


class WorkoutLucile(VideoWorkout):
    video_url = "https://www.youtube.com/embed/Wh-R-hW5lv4"
    duration_minutes = 20


class WorkoutSelf1(VideoWorkout):
    video_url = "https://www.youtube.com//embed/ml6cT4AZdqI"
    duration_minutes = 30
    body_focus = "leg"
    cool_down = True
    cool_down_duration = 5
    difficulty = 2


class WorkoutPamelaQuick(VideoWorkout):
    video_url = "https://www.youtube.com/embed/6VFLKdfxA24"
    duration_minutes = 10


class WorkoutMadFit1(VideoWorkout):
    video_url = "https://www.youtube.com/embed/r1c72WMpfI0"
    duration_minutes = 15

class WorkoutPamela1(VideoWorkout):
    video_url = "https://www.youtube.com/embed/UBMk30rjy0o"
    duration_minutes = 20


class WorkoutPopsugar1(VideoWorkout):
    video_url = "https://www.youtube.com/embed/XIeCMhNWFQQ"
    duration_minutes = 30
    workout_type = "tabata"


class WorkoutJason1(VideoWorkout):
    video_url = "https://www.youtube.com/embed/DrhV1L6kJ-A"
    duration_minutes = 23


class WorkoutGrowing1(VideoWorkout):
    video_url = "https://www.youtube.com/embed/-YpRYNREDV8"
    duration_minutes = 30


class WorkoutPamela2(VideoWorkout):
    video_url = "https://www.youtube.com/embed/UItWltVZZmE"
    duration_minutes = 20


class WorkoutJordanYeoh1(VideoWorkout):
    video_url = "https://www.youtube.com/embed/DOtr16U8V2M"
    duration_minutes = 30

class WorkoutPopsugar2(VideoWorkout):
    video_url = "https://www.youtube.com/embed/_Zem0_qsDg0"
    duration_minutes = 45


class WorkoutPopsugar3(VideoWorkout):
    video_url = "https://www.youtube.com/embed/s3F6R92s6_o"
    duration_minutes = 60


class WorkoutAllblanc(VideoWorkout):
    video_url = "https://www.youtube.com/embed/Tz9d7By2ytQ"
    duration_minutes = 5
    difficulty = 2
    body_focus = ["leg", "core", "chest"]



LIST_AVAILABLE_WORKOUTS = [
    WorkoutSelf1,
    WorkoutPamela1,
    WorkoutPopsugar1,
    WorkoutJason1,
    WorkoutGrowing1,
    WorkoutPamela2,
    WorkoutJordanYeoh1,
    WorkoutPamelaQuick,
    WorkoutMadFit1,
    WorkoutPopsugar2,
    WorkoutPopsugar3,
    WorkoutAllblanc,
]
