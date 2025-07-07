from typing import TypedDict
from httpx import Response
from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client


class Token(TypedDict):
    """
    Описание структуры токена.
    """
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class LoginResponseDict(TypedDict):
    """
    Описание структуры ответа на аутентификацию.
    """
    token: Token


class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление токена.
    """
    refreshToken: str


class AuthenticationClient(ApiClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/authentication/login', json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод выполняет обновление токена.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/authentication/refresh', json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        """
        Метод для выполнения аутентификации и получения json ответа
        :param request: Словарь с email и password
        :return: Извлеченный json
        """
        response = self.login_api(request)
        return response.json()


def get_authentication_client() -> AuthenticationClient:
    """
    Функция создает экземпляр AuthenticationClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию AuthenticationClient
    """
    return AuthenticationClient(client=get_public_http_client())
