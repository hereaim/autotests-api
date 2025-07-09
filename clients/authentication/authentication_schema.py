from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    """
    Описание структуры токена.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа на аутентификацию.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление токена.
    """
    refresh_token: str = Field(alias="refreshToken")
