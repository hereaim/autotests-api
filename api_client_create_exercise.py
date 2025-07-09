from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercise_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.faker import get_random_email


# Инициализация публичного клиента пользователя
public_user_client = get_public_users_client()

# Создание пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    first_name="string",
    last_name="string",
    middle_name="string"
)
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
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file='./testdata/files/image.png'
)
create_file_response = files_client.create_file(request=create_file_request)
print(f"Create file data: {create_file_response}")

# Создание курса
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Testing description",
    estimatedTime="1 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print(f"Create course data: {create_course_response}")

# Создание урока
create_exercise_request = CreateExerciseRequestDict(
    title="Hello, World",
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=10,
    orderIndex=1,
    description="Hello, World in Python. First step",
    estimatedTime='1 day'
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print(f"Create exercise data: {create_exercise_response}")
