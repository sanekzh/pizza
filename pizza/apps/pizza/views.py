import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.mail import EmailMessage

from pizza.apps.pizza.form import OrderForm
from pizza.apps.pizza.models import Order

SUCCESS = 1


class MainPage(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        data = {
            'salmon': 2,
            'sea_bass': 1.5,
            'cod': 2,
            'crab_fillet': 1,
            'pork': 1.5,
            'beef': 2,
            'salami': 1.5,
            'lamb': 1,
            'tomato': 1,
            'cucumber': 1.1,
            'onions': 2,
            'pepper': 1,
            'cheddar': 1.5,
            'camembert': 1,
            'gouda': 1.2,
            'edam': 2.5,
        }
        return render(request, self.template_name, data)


class CreateOrder(View):

    @staticmethod
    def send_notification(request, order_number):
        body = f'''     
                       Hello {request.POST['name']}
                       Phone number: {request.POST['telephone']}
                       Order #{order_number}: {request.POST['order']}
                       Price: ${request.POST['price']}
                       '''
        email = EmailMessage('Order', body, to=[request.POST['email']])
        return email.send()

    @staticmethod
    def post_main(request):
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                order_save = Order(email=request.POST['email'],
                                   telephone=request.POST['telephone'],
                                   name=request.POST['name'],
                                   price=request.POST['price'])
                order_save.save()
            except Exception as e:
                return HttpResponse(json.dumps({'STATUS': 'ERROR', 'ERROR': 'Error saving to database!'}),
                                    content_type='application/json')
            send = CreateOrder.send_notification(request, order_save.id)
            if send != SUCCESS:
                return HttpResponse(json.dumps({'STATUS': 'ERROR', 'ERROR': 'Error send notification!'}),
                                    content_type='application/json')
        else:
            return HttpResponse(json.dumps({'STATUS': 'ERROR', 'ERROR': str(form.errors)}),
                                content_type='application/json')
        return HttpResponse(json.dumps({'STATUS': 'OK', 'Message': 'Thank you for the order'}),
                            content_type='application/json')

    def post(self, request):
        return self.post_main(request)
