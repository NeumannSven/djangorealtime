
import json
from random import randint
from time import sleep
from channels.generic.websocket import WebsocketConsumer



class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(100000):
            self.send(json.dumps({'variable': randint(1,5)}))
            sleep(1)