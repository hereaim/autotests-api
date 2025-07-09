from typing import TypedDict
from httpx import Response
from clients.api_client import ApiClient
from clients.private_http_builder import AuthenticationUserDict, \
    get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры данных урока
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение уроков
    """
    courseId: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение уроков
    """
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение урока
    """
    exercise: list[Exercise]


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание урока
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на создание урока
    """
    exercises: list[Exercise]


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление урока
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление урока
    """
    exercise: list[Exercise]


class ExercisesClient(ApiClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, params: GetExercisesQueryDict) -> Response:
        """
        Метод на получение уроков определенного курса
        :param params: Параметр с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises', params=params)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения урока
        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestDict):
        """
        Метода создания урока
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str,
                            request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления урока
        :param exercise_id: Идентификатор урока
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления урока
        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

    def get_exercises(self, course_id: str) -> GetExercisesResponseDict:
        response = self.get_exercises_api({'courseId': course_id})
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self,
                        request: CreateExerciseRequestDict) -> CreateExercisesResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self,
                        exercise_id: str,
                        request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(get_private_http_client(user))
