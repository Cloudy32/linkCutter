import asyncio
from fastapi import FastAPI
import uvicorn

from DataB.models import async_main
from App import router

app = FastAPI()
app.include_router(router=router)

async def main():
    await async_main()
    uvicorn.run("App:app", reload=True)



if __name__ == "__main__":
    asyncio.run(main())