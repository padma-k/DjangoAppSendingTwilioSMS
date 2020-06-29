from django.shortcuts import render
from twilio.base.exceptions import TwilioRestException

from .models import Books
from .services.twilio_service import TwilioService


# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        recipientPhone = request.POST['recipientPhone']
        print(name, price)
        try:
            create(name, price, recipientPhone)
        except TwilioRestException as e:
            print(e)
            print('Oops! There was an error. Please try again.', 'danger')
            all_items = Books.objects.all
            return render(request, 'home.html', {'all_items': all_items})
        print('message sent')
        all_items = Books.objects.all
        return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = Books.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def create(name, price, recipientPhone):
    # get twilio client
    twilio_service = TwilioService()
    # build message
    formatted_message = build_message(name, price)
    print(formatted_message)
    # send message
    twilio_service.send_message(formatted_message, recipientPhone)


def build_message(name, price):
    # format message that will be sent in SMS
    template = 'You can get this book {}, in Amazon for {}'
    return template.format(name, price)
