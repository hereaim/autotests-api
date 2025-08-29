from functools import lru_cache

from httpx import Client
from pydantic import BaseModel
from config import settings

from clients.event_hooks import curl_event_hook, log_response_event_hook, \
    log_request_event_hook
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.authentication.authentication_client import \
    get_authentication_client


class AuthenticationUserSchema(BaseModel, frozen=True):
    email: str
    password: str


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создает httpx. Client с аутентификацией пользователя
    :param user: Объект AuthenticationUser с полями email и password
    :return: Готовый к использованию httpx. Client с установленными заголовками Authorization
    """
    # Инициализация AuthenticationClient для выполнения аутентификации
    authentication_client = get_authentication_client()

    # Ициализация запроса на аутентификацию
    login_request = LoginRequestSchema(email=user.email,
                                       password=user.password)
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        headers={
            "Authorization": f"Bearer {login_response.token.access_token}"
        },
        event_hooks={"request": [curl_event_hook, log_request_event_hook],
                     "response": [log_response_event_hook]}
    )
