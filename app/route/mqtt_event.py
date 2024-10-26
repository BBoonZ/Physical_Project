from .mqtt_client import create_mqtt_client

# สร้างไคลเอนต์ MQTT
mqtt_client = create_mqtt_client()

# ฟังก์ชันสำหรับ startup event
async def startup_event():
    mqtt_client.loop_start()  # เริ่ม loop สำหรับ MQTT

# ฟังก์ชันสำหรับ shutdown event
async def shutdown_event():
    mqtt_client.loop_stop()   # หยุด loop สำหรับ MQTT
    mqtt_client.disconnect()  # ยกเลิกการเชื่อมต่อ MQTT