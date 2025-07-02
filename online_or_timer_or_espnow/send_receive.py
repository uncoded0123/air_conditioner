import urequests

def send(x):
    response = urequests.get("http://<something.com>/data_test1/" + str(x))
    response.close()

def receive():
    #response = urequests.get('http://<something.com>/sensor_data_to_buzzer')
    #return response.text # response.<whatever> (eg, response.text, or response.json())
    
    # uncomment below for on_off
    response = urequests.get("http://<something.com>/on_off_test")
    return response.json()['test']
