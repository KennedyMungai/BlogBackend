"""The main file for the application"""
from fastapi import FastAPI

app = FastAPI(title="Blog Application",
              description="This is a blog application", version="0.1.0")


@app.get("/")
async def root() -> dict[str, str]:
    """The root endpoint for the application

    Returns:
        dict[str, str]: The root endpoint message
    """
    return {"message": "Hello World"}
