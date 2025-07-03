from typing import TypedDict
from httpx import Response
from clients.api_client import ApiClient


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса для создания файла
    """
    filename: str
    directory: str
    upload_file: str


class FilesClient(ApiClient):
    """
    Клиент для работы с /api/v1/files
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        Метод выполняет получение информации о файле.
        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/files/{file_id}')

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод выполняет создание файла.
        :param request: Словарь с данными для создания файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/files', data=request,
                         files={"upload_file": open(request['upload_file'], 'rb')})

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод выполняет удаление файла.
        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/files/{file_id}')