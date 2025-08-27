from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/dynamic", response_class=HTMLResponse)
async def dynamic_page(request: Request):
    return templates.TemplateResponse(
        "dynamic.html",
        {"request": request, "username": "User"}
    )

@app.get("/{path:path}")
async def catch_all(path: str):
    return FileResponse("static/index.html", media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    