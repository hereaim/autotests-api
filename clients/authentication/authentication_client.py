import allure
from httpx import Response
from clients.api_client import ApiClient
from clients.authentication.authentication_schema import LoginRequestSchema, \
    LoginResponseSchema, RefreshRequestSchema
from clients.public_http_builder import get_public_http_client


class AuthenticationClient(ApiClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    @allure.step("Authentication user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/authentication/login',
                         json=request.model_dump(by_alias=True))

    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод выполняет обновление токена.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/authentication/refresh',
                         json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """
        Метод для выполнения аутентификации и получения json ответа
        :param request: Словарь с email и password
        :return: Извлеченный json
        """
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создает экземпляр AuthenticationClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию AuthenticationClient
    """
    return AuthenticationClient(client=get_public_http_client())
