from azure.servicebus import ServiceBusService, Message, Queue
import json
import unicornhat

def build_succeeded():
    for x in range(8):
        for y in range(8):
            unicornhat.set_pixel(x,y,0,100,0)
    unicornhat.show()
    print('succeeded')

def build_failed():
    for x in range(8):
        for y in range(8):
            unicornhat.set_pixel(x,y,100,0,0)
    unicornhat.show()
    print('failed')

bus_service = ServiceBusService(
    service_namespace='vsobuildalert',
    shared_access_key_name='listen',
    shared_access_key_value='72rKCQ01AV+Cjvx1ee7qYVcWrwa3NJ8JO2tKY+M53+A=')

while(True):
    msg = bus_service.read_delete_queue_message('build')
   
    if msg.body is None:
        print('No new message')
    else:
        print(msg.body)
        data = json.loads(msg.body.decode('utf-8'))
        if(data['resource']['status'] == 'succeeded'):
            build_succeeded()
        else:
            build_failed()


print("stop")
