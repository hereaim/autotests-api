from typing import TypedDict
from httpx import Response
from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client


class User(TypedDict):
    """
    Описание структуры данных пользователя
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    firstName: str
    lastName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа на создание пользователя.
    """
    user: User


class PublicUsersClient(ApiClient):
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с данными для создания пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/users', json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        """
        Метод для выполнения создания пользователя и получения json ответа
        :param request: Словарь с данными для создания пользователя
        :return: Развернутый json ответ
        """
        response = self.create_user_api(request)
        return response.json()



def get_public_users_client() -> PublicUsersClient:
    """
    Функция создает экземпляр PublicUsersClient с уже настроенным http клиентом
    :return: Готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())
