#
# Notify secret santas of their assignments via the Twilio api
#
from twilio.rest import TwilioRestClient
import time

def test_sms(twilio_conf):
    client = TwilioRestClient(twilio_conf["sid"], twilio_conf["token"])

    client.messages.create(
    	to=twilio_conf["test_number"],
    	from_=twilio_conf["from_number"],
    	body=("Test Message sent at %s" % time.strftime("%Y-%m-%d %I:%M:%S")),
    )


def notify_santas(twilio_conf, assignments):
    client = TwilioRestClient(twilio_conf["sid"], twilio_conf["token"])
    for santa in assignments.keys():
        print "Alerting %s (%s)" % (santa, assignments[santa]["phone"])
        client.messages.create(
        	to=assignments[santa]["phone"],
        	from_=twilio_conf["from_number"],
        	body=("Hey %s - your secret santa assignee is %s" % (santa, assignments[santa]["assignee"])),
        )
