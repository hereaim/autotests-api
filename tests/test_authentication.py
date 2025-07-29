from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import \
    AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, \
    LoginResponseSchema
from tests.conftest import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.authentication import assert_login_response


@pytest.mark.authentication
@pytest.mark.regression
def test_login(function_user: UserFixture,
               authentication_client: AuthenticationClient):
    # Формируем тело запроса на аутентификацию
    request = LoginRequestSchema(email=function_user.email,
                                 password=function_user.password)
    # Отправляем запрос на аутентификацию
    response = authentication_client.login_api(request)
    # Инициализируем модель ответа на основе полученного JSON в ответе
    response_date = LoginResponseSchema.model_validate_json(
        response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_date)
    validate_json_schema(response.json(),
                         response_date.model_json_schema())
