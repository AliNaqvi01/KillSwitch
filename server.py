import nexmo
from flask import jsonify
import os

def send_sms(request):
    if request.method == 'POST':
        os.environ['BUTTON'] = 'TRUE'
        data = request.get_json()

        client = nexmo.Client(key='4239626e', secret='S8hJeMKRUzW6l5Jt')
        
        msg = "Hey, killSwitch is turning off your mic and camera. Enjoy your break!"    

        # you need some more data checking here. just an example...
        args = {
            'from': '18077883740',
            'to': data['phone'],
            'text': msg
        }
        
        response = client.send_message(args)
        return jsonify(response)

    elif request.method == 'GET':
        response = os.environ.get('BUTTON', 'Specified environment variable is not set.')
        os.environ['BUTTON'] = 'FALSE'
        return jsonify(response)
