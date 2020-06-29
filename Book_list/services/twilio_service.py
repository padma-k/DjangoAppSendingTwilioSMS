from twilio.rest import Client


class TwilioService:
    client = None

    def __init__(self):
        # Find these values at https://twilio.com/user/account
        account_sid = 'account_sid'
        auth_token = 'auth_token'
        print(auth_token)
        self.client = Client(account_sid, auth_token)

    def send_message(self, message, recipientphone):

        twilio_phone_number = 'twilio_phone_number'
        print(recipientphone)
        self.client.messages.create(to=recipientphone,
                                    from_=twilio_phone_number,
                                    body=message)
