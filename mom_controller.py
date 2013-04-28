from time import sleep

try:
    import RPi.GPIO as GPIO
except ImportError:
    import RPiFake.GPIO as GPIO

import plivo

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)

auth_id = ""
auth_token = ""

p = plivo.RestAPI(auth_id, auth_token)
print "Ready!"
while True:
    if not GPIO.input(7):
        print "Calling Mom"
        params = {'from': "14242436227", 'to': '12019932664',
                  'answer_url': "http://ciemaar.pythonanywhere.com/static/call_mom/answerThenCallMom.xml",
                  'answer_method': "GET"}
        p.make_call(params)
    elif not GPIO.input(11):
        print "Calling Dad"
        params = {'from': "14242436227", 'to': '12019932664',
                  'answer_url': "http://ciemaar.pythonanywhere.com/static/call_mom/answerThenCallYou.xml",
                  'answer_method': "GET"}
        p.make_call(params)
    elif not GPIO.input(13):
        print "Texting Mom"
        params = {
            'src': '12013455154', # Caller Id this must be a number you own
            'dst': '14242436227', # User Number to Text
            'text': "Hi, mom!",
            'type': "sms",
        }

        p.send_message(params)
    elif not GPIO.input(15):
        print "Mother's day special!"
    sleep(.1)