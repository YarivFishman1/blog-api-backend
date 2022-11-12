import uvicorn
from fastapi import FastAPI
from src.endpoints.user import router as user_router
from src.endpoints.blog import router as blog_router
from src.endpoints.post import router as post_router

app = FastAPI()

app.include_router(user_router)
app.include_router(blog_router)
app.include_router(post_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info", reload=True)
    print("running")
