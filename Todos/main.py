from fastapi import FastAPI
from .models import Base
from .database import engine
from .Router import auth, todos, admin, users


"""
This three variables/tokens are used to disable the swaggers.
If want to use any of doc or redoc can remove all or if want to use single url
we can give url to them and also we need to enable openapi_url.  
"""
app = FastAPI(

    # docs_url=None,
    redoc_url=None,
    # openapi_url=None,

    docs_url = "/docs",    # Disable Swagger UI
    # redoc_url = "/redoc", # Keep ReDoc at /redoc
    # openapi_url = "/openapi.json"
)

Base.metadata.create_all(bind=engine)

@app.get("/healthy")
def health_check():
    return {"status": "Healthy"}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)