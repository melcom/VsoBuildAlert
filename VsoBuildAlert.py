from azure.servicebus import ServiceBusService, Message, Queue
import json
import unicornhat

def build_succeeded():
    for x in range(8):
        for y in range(8):
            unicornhat.set_pixel(x,y,0,255,0)
    unicornhat.show()
    print('succeeded')

def build_failed():
    for x in range(8):
        for y in range(8):
            unicornhat.set_pixel(x,y,255,0,0)
    unicornhat.show()
    print('failed')

bus_service = ServiceBusService(
    service_namespace='buildvsomessagerie',
    shared_access_key_name='sasStrategy',
    shared_access_key_value='F4ALNAFvq7RqJhspB1AbXk/q2fZ7gedegN2rCYB9ehk=')

while(True):
    msg = bus_service.read_delete_queue_message('buildqueue')
   
    if msg.body is None:
        print('No new message')
    else:
        data = json.loads(msg.body.decode("utf-8"))
        if(data['resource']['status'] == 'succeeded'):
            build_succeeded()
        else:
            build_failed()


print("stop")
