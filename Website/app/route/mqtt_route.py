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
        message = "none"
        # print(id, name, info, file.filename, value, product_type, price, code)
        # product = await self.IStock.get_product_code(code)
        # product = tuple(product[0], product[1], product[6])
        product = "hahahhah"
        mqtt_client.publish(topic, product)
        return None