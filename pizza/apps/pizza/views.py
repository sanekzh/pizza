import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.mail import EmailMessage

from pizza.apps.pizza.form import OrderForm
from pizza.apps.pizza.models import Order, Category, Product

SUCCESS = 1


class MainPage(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all().values('id', 'category').order_by('category')
        products = Product.objects.all().values('id', 'name', 'price', 'category_id')
        return render(request, self.template_name, {'categories': categories, 'products': products})


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
