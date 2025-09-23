from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/.well-known", StaticFiles(directory=".well-known"), name="well-known")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/oprotest", include_in_schema=False)
async def get_openapi():
    rreturn {"message": "Testing orange pro AI"}

@app.get("/openapi.yaml", include_in_schema=False)
async def get_openapi():
    return FileResponse("openapi.yaml", media_type="text/yaml")

@app.get("/hello")
def hello():
    return {"message": "Hello from your Copilot plugin! OPRO v22 some changes!"}
