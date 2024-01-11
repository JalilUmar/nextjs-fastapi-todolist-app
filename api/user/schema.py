from pydantic import BaseModel, EmailStr, validator


class RegisterUserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator("password")
    def validate_password(cls, password: str):
        if len(password) < 5:
            raise ValueError("Password length must be greater than 5 characters")
        return password


class UserResponseSchema(BaseModel):
    id: str
    username: str
    email: str

    class Config:
        from_attributes = True


class LoginResponse(BaseModel):
    message: str
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str | None = None
