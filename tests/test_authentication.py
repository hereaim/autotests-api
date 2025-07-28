from http import HTTPStatus

from clients.users.public_users_client import get_public_users_client
from clients.authentication.authentication_client import \
    get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, \
    LoginResponseSchema
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.authentication import assert_login_response


def test_create_user():
    # Инициализируем API-клиент для работы с пользователями
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    # Формируем тело запроса на создание пользователя
    create_user_request = CreateUserRequestSchema()
    # Отправляем запрос на создание пользователя
    public_users_client.create_user_api(create_user_request)

    # Формируем тело запроса на аутентификацию
    login_request = LoginRequestSchema(email=create_user_request.email,
                                       password=create_user_request.password)
    # Отправляем запрос на аутентификацию
    login_response = authentication_client.login_api(login_request)
    # Инициализируем модель ответа на основе полученного JSON в ответе
    login_response_date = LoginResponseSchema.model_validate_json(
        login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_date)
    validate_json_schema(login_response.json(),
                         login_response_date.model_json_schema())
