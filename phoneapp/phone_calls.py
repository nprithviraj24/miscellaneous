from twilio.rest import TwilioRestClient


# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"

#Also the number that you are provided with must be registered...
TWILIO_PHONE_NUMBER = ""

# list of one or more phone numbers to dial, in "+19732644210" format
#these numbers must be verified.

DIAL_NUMBERS = ["",] #Fill the numbers. I have tried my personal number.


# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"
#Finding ways to make it more dynamic. Have to build my own XML file.


# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = TwilioRestClient("ACxxxxxxx", "")


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)


'''
what additional things you can do?

- Customize in such a way that it is flexible enough to call any number. I will work on it.
- You can book gas online just with a simple command, which was the main intention.

'''