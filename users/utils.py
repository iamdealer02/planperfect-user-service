# user/utils.py
import requests

def register_service():
    service_name = 'userservice'
    address = 'http://userservice-backend-1:8000/' 
    port = 8000  # Port of the user service
    register_url = 'http://servicediscovery-backend-1:8003/service/register/'  

    response = requests.post(register_url, data={
        'name': service_name,
        'address': address,
        'port': port
    })

    if response.status_code == 201:
        print('Successfully registered the user service')
    else:
        print(f'Failed to register the user service')


def deregister_service():
    service_name = 'userservice'
    deregister_url = f'http://servicediscovery-backend-1:8003/service/deregister/{service_name}/' 
    response = requests.delete(deregister_url)

    if response.status_code == 204:
        print('Successfully deregistered the user service')
    else:
        print(f'Failed to deregister the user service: {response.text}')
