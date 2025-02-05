from fastapi import FastAPI

app = FastAPI()

# Include your routes here
from .api.routes import router 
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)