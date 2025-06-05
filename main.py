from fastapi import FastAPI
from importlib import import_module
from pkgutil import iter_modules

from app.infrastructure.database import init_db

app = FastAPI(title="Clean FastAPI Project")

# Dynamically load routers from app.interfaces.api package
package_name = "app.interfaces.api"
package = import_module(package_name)

for _, module_name, _ in iter_modules(package.__path__):
    module = import_module(f"{package_name}.{module_name}")
    if hasattr(module, "router"):
        app.include_router(module.router)

@app.on_event("startup")
def on_startup():
    init_db()
