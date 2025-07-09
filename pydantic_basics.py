import uuid
from pydantic import BaseModel, ConfigDict, Field, EmailStr, HttpUrl
from pydantic.alias_generators import to_camel


class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str


class UserSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    max_score: int = Field(default=100)
    min_score: int = Field(default=10)
    description: str = Field(default="Playwright course")
    preview_file: FileSchema
    estimated_time: str = Field(default="1 week")
    created_by_user: UserSchema


course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file-filename",
        directory="file-directory"
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="user-id",
        email="user@email.ru",
        lastName="user-last-name",
        firstName="user-first-name",
        middleName="user-middle-name"
    )
)
print(f"Course default model: {course_default_model}")

course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@email.ru",
        "lastName": "user-last-name",
        "firstName": "user-first-name",
        "middleName": "user-middle-name"
    }
}
course_dict_model = CourseSchema(**course_dict)
print(f"Course dict model: {course_dict_model}")

course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print(f"Course JSON model:\n {course_json_model}")
