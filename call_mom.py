__author__ = 'andriod'

import plivo


auth_id =
auth_token =

p = plivo.RestAPI(auth_id, auth_token)

# Make a call
params = {'from': "14245550100", 'to': '14245550100', 'answer_url': "http://google.com/", 'answer_method': "GET"}

response = p.make_call(params)
print response # with a developer account you will get the error that regular phone calls are not allowed here

# Send a SMS
params = {
    'src': '12013455154', # Caller Id this must be a number you own
    'dst': '14245550100', # User Number to Text
    'text': "Hi,  from Plivo",
    'type': "sms",
}

response = p.send_message(params)
print response


#params = {'from':"14245550100",'to':'14245550100','answer_url':"http://ciemaar.pythonanywhere.com/static/call_mom/answer.xml",'answer_method':"GET"}
params = {'from': "14245550100", 'to': '12015550164',
          'answer_url': "http://ciemaar.pythonanywhere.com/static/call_mom/answer.xml", 'answer_method': "GET"}

response = p.make_call(params)
print response
