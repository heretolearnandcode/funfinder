#!/usr/bin/env python

import urllib
import json
import os


from flask import Flask
from flask import make_response
from flask import request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "fun.activity":
                return {}
    result = req.get("result")
    parameters = result.get("parameters")
    activity = parameters.get("activity")
    time = parameters.get("time")

    bookedforbasketball = {('Steve','1 PM'), ('Kishore','4 PM')}
    bookedforboardgame = {('Steve','2 PM'), ('Ruel','2:30 PM')}
    bookedforparty = {('Steve','7 PM'), ('Kishore','7:30 PM'),('Ruel','7:30 PM')}
    bookedformovie = {('Nisha', '9 PM')}

    if activity == "basketball":
        speech = "I found cruiser "+ bookedforbasketball[0] + " is booked to play"+ 'activity' +"at" + bookedforbasketball[0][1]
    if activity == "boardgame":
        speech = "I found cruiser " + bookedforboardgame[1] + " is booked to play" + 'activity' + "at" + bookedforboardgame[0][1]
    if activity == "party":
        speech = "I found cruiser " + bookedforparty[1] +" is booked to play" + 'activity' + "at" + bookedforparty[0][1]
    if activity == "movie":
        speech = "I found cruiser " + bookedformovie[0] +" is booked to play" + 'activity' + "at" + bookedformovie[0][0]
        print("Response:")

        print(speech)

    return {
    "speech": speech,
            "displayText": speech,
            #"data": {},
            # "contextOut": [],
            "source": "apiai-onlinestore-shipping"
        }



if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')