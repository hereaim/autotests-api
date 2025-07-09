import uuid
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Модель валидации данных пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(BaseModel):
    """
    Модель валидации данных запроса на создание пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str
    first_name: str
    middle_name: str


class CreateUserResponseSchema(BaseModel):
    """
    Модель валидации данных ответа на запрос на создание пользователя
    """
    user: UserSchema


# Проверка схем валидации
request_data = {
    "email": "test@example.com",
    "password": "secret123",
    "lastName": "Иванов",
    "firstName": "Иван",
    "middleName": "Иванович"
}

# Валидация входных данных
create_user_request = CreateUserRequestSchema.model_validate(request_data)

# Создание пользователя
user = UserSchema(
    email=create_user_request.email,
    last_name=create_user_request.last_name,
    first_name=create_user_request.first_name,
    middle_name=create_user_request.middle_name
)

# Ответ
response = CreateUserResponseSchema(user=user)
print(response.model_dump(by_alias=True))
