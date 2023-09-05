from pydantic import BaseModel, field_validator, FieldValidationInfo


class CreateUser(BaseModel):
    email: str
    password: str
    confirm_password: str

    @field_validator("email")
    def validate_email(cls, value):
        if "admin" in value:
            raise ValueError("This email is not allowed")
        return value

    @field_validator("confirm_password")
    def validate_passwords(cls, value, info: FieldValidationInfo):
        if "password" in info.data and value != info.data["password"]:
            raise ValueError("passwords do not match")
        return value


user1 = CreateUser(
    email="glen@gmail.com", password="password123", confirm_password="password123"
)
print(user1)
user2 = CreateUser(
    email="glen@gmail.com", password="password123", confirm_password="password123"
)
print(user2)
