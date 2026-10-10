from fastapi import FastAPI
from getinvoice import router as get_router
from createinvoice import router as create_router
from deleteinvoice import router as delete_router



app = FastAPI()
app.include_router(get_router)
app.include_router(create_router)
app.include_router(delete_router)