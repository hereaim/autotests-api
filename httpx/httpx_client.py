import httpx

login_payload = {
    "email": "email@mail.ru",
    "password": "password"
}

login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f"Login response: {login_response_data}")

client = httpx.Client(base_url="http://localhost:8000",
                      timeout=100,
                      headers={
                          "Authorization": f"Bearer {login_response_data['token']['accessToken']}"})

get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()
print(f"Get user me response: {get_user_me_response_data}")
