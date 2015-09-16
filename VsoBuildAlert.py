from azure.servicebus import ServiceBusService, Message, Queue
import json

def build_succeeded():
    print('succeeded')

def build_failed():
    print('failed')

bus_service = ServiceBusService(
    service_namespace='buildvsomessagerie',
    shared_access_key_name='sasStrategy',
    shared_access_key_value='F4ALNAFvq7RqJhspB1AbXk/q2fZ7gedegN2rCYB9ehk=')

while(True):
    msg = bus_service.receive_queue_message('buildqueue', peek_lock=False, timeout=5)
   
    if msg.body is None:
        print('No new message')
    else:
        data = json.loads(msg.body.decode("utf-8"))
        if(data['resource']['status'] == 'succeeded'):
            build_succeeded()
        else:
            build_failed()


print("stop")