from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema,
                                response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.email, response.user.email, 'email')
    assert_equal(request.first_name, response.user.first_name, 'first_name')
    assert_equal(request.last_name, response.user.last_name, 'last_name')
    assert_equal(request.middle_name, response.user.middle_name, 'middle_name')