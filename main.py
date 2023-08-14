from fastapi import FastAPI
from routes.users import router
from tortoise.contrib.fastapi import register_tortoise
from models.users import User

app = FastAPI()
app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    return await User.create(
        name="John Doe",
        email="ninguno22",
        password="ninguno2",
    )
    
    
@app.on_event("startup")
async def startup():
    register_tortoise(
        app,
        db_url="asyncpg://postgres:0000@localhost:5432/crud",
        modules={'models': ['models.users']},
        generate_schemas=True,
        add_exception_handlers=True
    )
    