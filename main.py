from fastapi import FastAPI, Request, status 
from produtos import produto_router
from categoria import categoria_router
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(produto_router)
app.include_router(categoria_router)

@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Ocorreu um erro inesperado."}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for err in exc.errors():
        errors.append({
            'field': err.get('loc')[-1],
            'message': err.get('msg')   
        })
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"errors": errors}
    )