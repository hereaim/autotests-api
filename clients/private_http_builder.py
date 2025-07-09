from httpx import Client
from pydantic import BaseModel

from clients.authentication.authentication_schema import LoginRequestSchema
from clients.authentication.authentication_client import get_authentication_client


class AuthenticationUserSchema(BaseModel):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создает httpx.Client с аутентификацией пользователя
    :param user: Объект AuthenticationUser с полями email и password
    :return: Готовый к использованию httpx.Client с установленными заголовками Authorization
    """
    # Инициализация AuthenticationClient для выполнения аутентификации
    authentication_client = get_authentication_client()

    # Ициализация запроса  на аутентификацию
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={
            "Authorization": f"Bearer {login_response.token.access_token}"
        }
    )
