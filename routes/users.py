from fastapi import APIRouter
from models.users import User
from dto.users import UserIn, UserOut, UserDel, UserUpd
from fastapi import HTTPException, status

router = APIRouter()

@router.get("/get-users")
async def get_users():
    try:
        users = await User.all()
        if users is not None:
            return users
        raise HTTPException(status_code=404, detail="Users not found")
    except Exception as e:
        return {"response": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
    
@router.get("/get-user/{user_id}")
async def get_user(id: int):
    try:
        user = await User.get(id=id)
        if user is not None:
            return user
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        return {"response": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
    
@router.post("/create-user")
async def create_user(user_data: UserIn):
    try:
        user = await User.create(**user_data.dict(exclude_unset=True))
        if user is not None:
            return user
        raise HTTPException(status_code=404, detail="User not created")
    except Exception as e:
        return {"response": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
    
@router.put("/update-user/{user_id}")
async def update_user(user_id: int, user_data: UserUpd):
    try:
        user = await User.get(id=user_id)
        if user is not None:
            await user.update_from_dict(user_data.dict(exclude_unset=True)).save()
            return user
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        return {"response": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}

@router.delete("/delete-user/{user_id}")
async def delete_user(user_id: int):
    try:
        user = await User.get(id=user_id)
        if user is not None:
            await user.delete()
            return {"response": status.HTTP_200_OK, "message": "User deleted"}
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        return {"response": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(e)}
