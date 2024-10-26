# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.db import models
from app.db.database import SessionLocal, engine
from app.route.RecordSalesRoute import SalesRouter
from app.route.StockRoute import StockRouter
from app.route.UploadFile import UploadRoute
from app.route.mqtt_route import EventRoute
from app.route.mqtt_event import startup_event, shutdown_event
import paho.mqtt.client as mqtt


app = FastAPI()

app.mount("/static", StaticFiles(directory="website/static/"), name="static")   # Locate css file
app.mount("/js", StaticFiles(directory="website/static/javascript"), name="script")   # Locate js file
app.mount("/img", StaticFiles(directory="app/img"), name="img")                    # Locate img Product file


#app route
# app.include_router(test.router)
# app.include_router(RecordSales.router)
sales_router = SalesRouter()
stock_router = StockRouter()
upload_router = UploadRoute()
mqtt_router = EventRoute()

app.include_router(sales_router.router)
app.include_router(stock_router.router)
app.include_router(mqtt_router.router)
app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)
# app.include_router(upload_router.router)

# Create the database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#เวลา run พิมพ์ uvicorn main:app ใน terminal
#python -m uvicorn main:app ใช้คำสั่งนี้รันได้ by คิว
#route /recordsales แสดง html