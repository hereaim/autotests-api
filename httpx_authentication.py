import httpx

# Данные для входа в систему
payload = {"email": "email@mail.ru", "password": "password"}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

# Выводим полученные токены
print(f"Login response: {login_response_data}")
print(f"Status code: {login_response.status_code}")

# Формируем payload для обновления токена
refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

# Выполняем запрос на обновление токена
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

# Выводим обновленные токены
print(f"Refresh response: {refresh_response_data}")
print(f"Status code: {refresh_response.status_code}")