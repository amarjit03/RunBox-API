from fastapi import FastAPI
from config import get_settings

settings = get_settings()

app = FastAPI(title=settings.app_name)

@app.get('/')
def main():
    return {"hello":"fastAPI",
            "app":settings.app_name}

