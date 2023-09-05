from typing import Optional

from pydantic import BaseModel, EmailStr, Field,validator
from bson.objectid import ObjectId
from server.database import user_collection


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password:str = Field(...)
    role:str = Field(...)

    @validator("role")
    def validate_role(cls,value):
        if value not in ['questioner','interviewee']:
            raise ValueError('role must be either questioner or interviewee')
        return value
  
    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "password",
                "role": "questioner",
            }
        }


class UpdateUserModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    role: Optional[int]
    
    @validator("role")
    def validate_role(cls,value):
        if value not in ['questioner','interviewee']:
            raise ValueError('role must be either questioner or interviewee')
        return value

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "password123",
                "role": "interviewee",
            }
        }


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "role": user["role"],
    }

async def retrieve_users():
    students = []
    async for student in user_collection.find():
        students.append(user_helper(student))
    return students


async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)


async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True