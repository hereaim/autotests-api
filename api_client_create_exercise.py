from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client, \
    CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from config import settings

# Инициализация публичного клиента пользователя
public_user_client = get_public_users_client()

# Создание пользователя
create_user_request = CreateUserRequestSchema()
create_user_response = public_user_client.create_user(create_user_request)

# Аутентификация
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Инициализация клиентов
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercise_client(authentication_user)

# Загрузка файла
create_file_request = CreateFileRequestSchema(upload_file=settings.test_data.image_png_file)
create_file_response = files_client.create_file(request=create_file_request)
print(f"Create file data: {create_file_response}")

# Создание курса
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print(f"Create course data: {create_course_response}")

# Создание урока
create_exercise_request = CreateExerciseRequestSchema(
    course_id=create_course_response.course.id
)
create_exercise_response = exercises_client.create_exercise(
    create_exercise_request)
print(f"Create exercise data: {create_exercise_response}")
