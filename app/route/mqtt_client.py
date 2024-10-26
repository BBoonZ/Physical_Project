import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

def create_mqtt_client(broker_address="mqtt-dashboard.com", port=1883, topic="phycom/66070108"):
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(broker_address, port)
    client.subscribe(topic)
    return client

