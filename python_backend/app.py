import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Specifies the allowed origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(auth_router)

@app.get("/status")
async def get_status():
    return {"status": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
