from typing import TypedDict
from httpx import Response
from clients.api_client import ApiClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    firstName: str
    lastName: str
    middleName: str


class PublicUsersClient(ApiClient):
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с данными для создания пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/users', json=request)
