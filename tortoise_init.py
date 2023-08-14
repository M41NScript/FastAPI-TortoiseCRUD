from tortoise import Tortoise, run_async


async def init():
    await Tortoise.init(
        db_url="asyncpg://postgres:0000@localhost:5432/crud",
        modules={'models': ['models.users']}
    )
    await Tortoise.generate_schemas()
    
run_async(init())    
