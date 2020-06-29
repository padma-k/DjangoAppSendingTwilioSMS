from twilio.rest import Client


class TwilioService:
    client = None

    def __init__(self):
        # Find these values at https://twilio.com/user/account
        account_sid = 'AC2db85943534ca50e7d2bac1c0ddeac72'
        auth_token = '996c202e8f163f8f509d21a8da81d3f0'
        print(auth_token)
        self.client = Client(account_sid, auth_token)

    def send_message(self, message, recipientphone):

        twilio_phone_number = '+12058518364'
        print(recipientphone)
        self.client.messages.create(to=recipientphone,
                                    from_=twilio_phone_number,
                                    body=message)
