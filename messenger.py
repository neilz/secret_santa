#
# Notify secret santas of their assignments via the Twilio api
#
from twilio.rest import TwilioRestClient
import time

def test_sms(twilio_conf):
    client = TwilioRestClient(twilio_conf["sid"], twilio_conf["token"])

    print client.messages.create(
    	to=twilio_conf["test_number"],
    	from_=twilio_conf["from_number"],
    	body=("Test Message sent at %s" % time.strftime("%Y-%m-%d %I:%M:%S")),
    )


def notify_santas(twilio_conf, santa_assignments):
    # client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
#
    # client.messages.create(
    # 	to="+15852811227",
    # 	from_="+15855074892",
    # 	body="test1 blah \n this is kinda cool",
    # )
    return 0
