from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep



class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        variable = 0

        for i in range(100000):
            if variable < 50:
                variable += 1
                #self.send(json.dumps({'variable': variable}))
                sleep(0.5)

            else:
                variable = 1
                #self.send(json.dumps({'variable': variable}))
                sleep(0.5)
            
            self.send(json.dumps({'variable': variable}))