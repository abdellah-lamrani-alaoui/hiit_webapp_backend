def is_workout_in_duration_filter(
    duration_workout: int, duration_filter: int, allowed_durations_filter: list[int]
):
    if duration_filter not in allowed_durations_filter:
        raise ValueError(
            f"Duration Filter not authorized, should belong to :{','.join(map(str, allowed_durations_filter))}"
        )

    closest_duration = min(
        (elem for elem in allowed_durations_filter),
        key=lambda x: abs(x - duration_workout),
    )
    return closest_duration == duration_filter
