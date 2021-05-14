from filtering_logics import is_workout_in_duration_filter


def test_workout_duration_in_allowed_durations_but_different_from_filter():
    duration_filter = 10
    duration_workout = 20
    allowed_durations_filter = [5, 10, 20, 30]

    expected_result = False
    assert expected_result == is_workout_in_duration_filter(
        duration_workout, duration_filter, allowed_durations_filter
    )


def test_workout_duration_allowed_durations_closest_to_filter():
    duration_filter = 15
    duration_workout = 20
    allowed_durations_filter = [5, 10, 15, 30]

    expected_result = True
    assert expected_result == is_workout_in_duration_filter(
        duration_workout, duration_filter, allowed_durations_filter
    )
