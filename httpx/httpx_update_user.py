import httpx
from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users",
                                  json=create_user_payload)

create_user_response_data = create_user_response.json()

print(f"Create user data: {create_user_response_data}")
print(f"Status code: {create_user_response.status_code}")

login_payload = {
    "email": create_user_response_data["user"]["email"],
    "password": "string"
}

login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login",
    json=login_payload)
login_response_data = login_response.json()

print(f"Login data: {login_response_data}")
print(f"Status code: {login_response.status_code}")

update_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
update_user_payload = {
    "email": fake.email(),
    "lastName": "Test",
    "firstName": "Test",
    "middleName": "Test"
}

update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
    headers=update_user_headers,
    json=update_user_payload)
update_user_response_data = update_user_response.json()

print(f"Update user data: {update_user_response_data}")
print(f"Status code: {update_user_response.status_code}")
