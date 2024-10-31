import uvicorn
from core.config import FITSYNC_BACKEND_SETTINGS
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()
HOST = FITSYNC_BACKEND_SETTINGS.HOST
PORT = int(FITSYNC_BACKEND_SETTINGS.PORT)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get(path='/', response_class=HTMLResponse)
def get_root():
    return """
    <html><body><h1>Welcome to FitSync Backend App!</h1></body></html>
    """

if __name__ == "__main__":
    uvicorn.run(app='main:app', host=HOST, port=PORT, reload=True)
