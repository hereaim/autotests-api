from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.faker import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    firstName="string",
    lastName="string",
    middleName="string"
)
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(request=create_user_request)
print(f"Create user data: {create_user_response}")

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(user=authentication_user)

# Отправляем GET запрос на получение данных пользователя
get_user_response = private_users_client.get_user(create_user_response['user']['id'])
print(f"Get user data: {get_user_response}")
