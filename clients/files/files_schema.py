from pydantic import BaseModel, HttpUrl


class FileSchema(BaseModel):
    """
    Описание структуры файла
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания файла
    """
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос создания файла
    """
    file: FileSchema
