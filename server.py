from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files from the .well-known directory
app.mount("/.well-known", StaticFiles(directory=".well-known"), name="well-known")
app.mount("/openapi.yaml", StaticFiles(directory=".", html=False), name="openapi")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to GitHub Copilot's origin if known
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def hello():
    return {"message": "Hello from your Copilot plugin!"}

# Serve openapi.yaml from the current directory
# app.mount("/", StaticFiles(directory=".", html=False), name="root")