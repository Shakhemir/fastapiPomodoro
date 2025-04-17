from fastapi import FastAPI
from handlers import routers

app = FastAPI(title="Учебный курс по FastAPI")


for router in routers:
    app.include_router(router=router)

