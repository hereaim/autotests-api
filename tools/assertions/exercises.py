from clients.exercises.exercises_schema import CreateExerciseResponseSchema, \
    CreateExerciseRequestSchema, GetExerciseResponseSchema, ExerciseSchema, \
    UpdateExerciseResponseSchema, UpdateExerciseRequestSchema, \
    GetExercisesResponseSchema
from clients.errors_schema import InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response


def assert_create_exercise_response(expected: CreateExerciseRequestSchema,
                                    actual: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ на создание урока соответствует данным из запроса.

    :param expected: Исходный запрос на создание урока.
    :param actual: Ответ API с созданными данными урока.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.exercise.title, expected.title, 'title')
    assert_equal(actual.exercise.max_score, expected.max_score, 'max_score')
    assert_equal(actual.exercise.min_score, expected.min_score, 'min_score')
    assert_equal(actual.exercise.order_index, expected.order_index,
                 'order_index')
    assert_equal(actual.exercise.description, expected.description,
                 'description')
    assert_equal(actual.exercise.estimated_time, expected.estimated_time,
                 'estimated_time')
    assert_equal(actual.exercise.course_id, expected.course_id, 'course_id')


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные урока соответствуют ожидаемым.

    :param actual: Фактические данные урока.
    :param expected: Ожидаемые данные урока.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.title,
                 expected.title, 'title')
    assert_equal(actual.max_score,
                 expected.max_score, 'max_score')
    assert_equal(actual.min_score,
                 expected.min_score, 'min_score')
    assert_equal(actual.order_index,
                 expected.order_index, 'order_index')
    assert_equal(actual.description,
                 expected.description, 'description')
    assert_equal(actual.estimated_time,
                 expected.estimated_time, 'estimated_time')
    assert_equal(actual.course_id,
                 expected.course_id, 'course_id')


def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ на получение задания соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе данных задания.
    :param create_exercise_response: Ответ API при создании задания.
    :raises AssertionError: Если данные задания не совпадают.
    """
    assert_exercise(get_exercise_response.exercise,
                    create_exercise_response.exercise)


def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: UpdateExerciseResponseSchema
):
    """
    Проверяет, что ответ на обновление урока соответствует данным из запроса.

    :param request: Исходный запрос на обновление урока.
    :param response: Ответ API с обновленными данными урока.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.exercise.title, 'title')
    assert_equal(request.max_score, response.exercise.max_score, 'max_score')
    assert_equal(request.min_score, response.exercise.min_score, 'min_score')
    assert_equal(request.order_index, response.exercise.order_index,
                 'order_index')
    assert_equal(request.description, response.exercise.description,
                 'description')
    assert_equal(request.estimated_time, response.exercise.estimated_time,
                 'estimated_time')


def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если урон не найден.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)


def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]):
    """
        Проверяет, что ответ на получение списка уроков соответствует ответам на их создание.

        :param get_exercises_response: Ответ API при запросе списка уроков.
        :param create_exercise_responses: Список API ответов при создании уроков.
        :raises AssertionError: Если данные уроков не совпадают.
    """
    assert_length(get_exercises_response.exercises, create_exercise_responses,
                  "exercises")

    for index, create_exercise_responses in enumerate(
            create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index],
                        create_exercise_responses.exercise)
