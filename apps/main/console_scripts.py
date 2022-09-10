
from random import randint
import json
import time

from cent import Client

from config import CENTRIFUGO_HTTP_URL
from config import CENTRIFUGO_WS_URL
from config import CENTRIFUGO_API_KEY



def push():
    #python run.py main.console_scripts "push()"
    client = Client(CENTRIFUGO_HTTP_URL, api_key=CENTRIFUGO_API_KEY, timeout=1)

    channel = "channel"
    

    while True:
        data = {"title": randint(1,100)}
        client.publish(channel, data)
        time.sleep(0.4)

    # publish data into channel
    # channel = "public:chat"
    # data = {"input": "test"}
    # client.publish(channel, data)


# if __name__ == "__main__":
#     app.run(debug=True, host=APP_HOST, port=APP_PORT)

