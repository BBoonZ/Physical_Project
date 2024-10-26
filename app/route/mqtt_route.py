from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from .mqtt_event import mqtt_client
from .Stock import ProductManager

class EventRoute:
    def __init__(self):
        self.router = APIRouter()
        self.IStock = ProductManager()

        # Define routes
        self.router.add_api_route("/product_code/{code}", self.get_product_info, methods=["GET"])

    async def get_product_info(self, request: Request, code: str):
        topic = "phycom/66070108"
        message = "hahahhah"
        # print(id, name, info, file.filename, value, message_type, price, code)
        message = self.IStock.get_product_code(code)
        message = str(message[0]) + " " + str(message[1]) + " " + str(message[5]) + " " + str(message[7])
        
        mqtt_client.publish(topic, message)
        return None