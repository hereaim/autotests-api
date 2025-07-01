import httpx

# Данные для входа в систему
payload = {"email": "email@mail.ru", "password": "password"}

# Выполняем запрос на аутентификацию
login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

# Выводим полученные токены и статус
print(f"Login response: {login_response_data}")
print(f"Status code: {login_response.status_code}")

# Настраиваем заголовки и передаем accessToken
headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

# Формируем сессию для работы
with httpx.Client() as client:
    users_me_response = client.get(url="http://localhost:8000/api/v1/users/me",
                                   headers=headers)
    users_me_response_data = users_me_response.json()

# Выводим данные о пользователе и статус
print(f"User data: {users_me_response_data}")
print(f"Status code: {users_me_response.status_code}")
