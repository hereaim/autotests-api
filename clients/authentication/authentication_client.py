from typing import TypedDict
from httpx import Response
from clients.api_client import ApiClient


class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


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
