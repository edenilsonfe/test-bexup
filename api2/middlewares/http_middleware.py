from fastapi import Request
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse

from api2.main import app


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse({"detail": exc.errors(), "body": exc.body}, status_code=400)


@app.exception_handler(HTTPException)
async def validation_http_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        {"detail": exc.detail, "status_code": exc.status_code, "body": exc.args},
        status_code=exc.status_code,
    )


@app.middleware("http")
async def error_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail={"detail": exc, "status_code": exc.args, "body": exc},
        )
        response = JSONResponse({"detail": "Internal Server Error"}, status_code=500)
    return response
