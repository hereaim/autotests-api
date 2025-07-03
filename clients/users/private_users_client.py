from typing import TypedDict
from httpx import Response
from clients.api_client import ApiClient


class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: str | None
    firstName: str | None
    lastName: str | None
    middleName: str | None


class PrivateUsersClient(ApiClient):
    """
    Клиент для работы с /api/v1/users.
    """
    def get_user_me_api(self) -> Response:
        """
        Метод выполняет получение информации о текущем пользователе.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/users/me')

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод выполняет получение информации о пользователе.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/users/{user_id}')

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Метод выполняет обновление пользователя.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с данными для обновления пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/users/{user_id}', json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод выполняет удаление пользователя.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/users/{user_id}')
    