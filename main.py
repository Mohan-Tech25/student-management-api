from fastapi import FastAPI

from API.V1.user import router as user_router
from API.V1.Dashboard import router as dashboard_router


app = FastAPI(
    title="Student Management API"
)

#app.include_router(...) attaches a router (a group of endpoints) into the main FastAPI app, merging its routes so they become part of the application
app.include_router(#to include the user_router with the specified prefix
    user_router,
    prefix="/api/v1"
)


app.include_router(
    dashboard_router,
    prefix="/api/v1"
)


@app.get("/")
def root():

    return {
        "message": "Student Management API - Feature Branch"
    }