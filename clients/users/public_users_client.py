import allure
from httpx import Response
from clients.api_client import ApiClient
from clients.api_coverage import tracker
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema
from tools.routes import APIRoutes


class PublicUsersClient(ApiClient):
    @allure.step("Create user")
    @tracker.track_coverage_httpx(APIRoutes.USERS)
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с данными для создания пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.USERS, json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Метод для выполнения создания пользователя и получения json ответа
        :param request: Словарь с данными для создания пользователя
        :return: Развернутый json ответ
        """
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создает экземпляр PublicUsersClient с уже настроенным http клиентом
    :return: Готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())
