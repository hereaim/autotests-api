import allure
from httpx import Response
from clients.api_client import ApiClient
from clients.private_http_builder import AuthenticationUserSchema, \
    get_private_http_client
from clients.exercises.exercises_schema import GetExercisesQuerySchema, \
    GetExercisesResponseSchema, GetExerciseResponseSchema, \
    CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from tools.routes import APIRoutes


class ExercisesClient(ApiClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    @allure.step("Get exercises")
    def get_exercises_api(self, params: GetExercisesQuerySchema) -> Response:
        """
        Метод на получение уроков определенного курса
        :param params: Параметр с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'{APIRoutes.EXERCISES}', params=params.model_dump(by_alias=True))

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения урока
        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'{APIRoutes.EXERCISES}/{exercise_id}')

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema):
        """
        Метода создания урока
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f'{APIRoutes.EXERCISES}',
                         json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(self, exercise_id: str,
                            request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления урока
        :param exercise_id: Идентификатор урока
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'{APIRoutes.EXERCISES}/{exercise_id}',
                          json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления урока
        :param exercise_id: Идентификатор урока
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'{APIRoutes.EXERCISES}/{exercise_id}')

    def get_exercises(self, course_id: str) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(
            GetExercisesQuerySchema(courseId=course_id))
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self,
                        request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self,
                        exercise_id: str,
                        request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(get_private_http_client(user))
