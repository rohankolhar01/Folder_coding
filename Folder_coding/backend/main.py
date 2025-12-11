import uvicorn
from fastapi import FastAPI
from backend.database import Base, engine
from backend.routes import user_routes, product_routes, cart_routes, order_routes

# Initialize DB
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FolderCoding Backend API", version="1.0")

# Include routers
app.include_router(user_routes.router, prefix="/api/users", tags=["Users"])
app.include_router(product_routes.router, prefix="/api/products", tags=["Products"])
app.include_router(cart_routes.router, prefix="/api/carts", tags=["Carts"])
app.include_router(order_routes.router, prefix="/api/orders", tags=["Orders"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
