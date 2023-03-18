import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
from random import randrange
from django.conf import settings
from seller.models import *

# create your views here.


def about(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'about.html', {'user_data': buyer_row})
    except:
        return render(request, 'about.html')


def bread(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'bread.html', {'user_data': buyer_row})
    except:
        return render(request, 'bread.html')





def drinks(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'drinks.html', {'user_data': buyer_row})
    except:
        return render(request, 'drinks.html')


def events(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'events.html', {'user_data': buyer_row})
    except:
        return render(request, 'events.html')


def faqs(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'faqs.html', {'user_data': buyer_row})
    except:
        return render(request, 'faqs.html')


def frozen(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'frozen.html', {'user_data': buyer_row})
    except:
        return render(request, 'frozen.html')


def household(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'household.html', {'user_data': buyer_row})
    except:
        return render(request, 'household.html')


def index(request):
    all_products = Product.objects.all()
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'index.html', {'user_data': buyer_row, 'all_pro': all_products})
    except:
         return render(request, 'index.html', {'all_pro': all_products})


def kitchen(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'kitchen.html', {'user_data': buyer_row})
    except:
        return render(request, 'kitchen.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            buyer_row = Buyer.objects.get(email=request.POST['email'])
            if request.POST['password'] == buyer_row.password:
                request.session['email'] = request.POST['email']
                return redirect('index')
            else:
                return render(request, 'login.html', {'msg': 'wrong password!!'})
        except:
            return render(request, 'login.html', {'msg': 'email is not register!!'})


def mail(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'mail.html', {'user_data': buyer_row})
    except:
        return render(request, 'mail.html')


def payment(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'payment.html', {'user_data': buyer_row})
    except:
        return render(request, 'payment.html')


def pet(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'pet.html', {'user_data': buyer_row})
    except:
        return render(request, 'pet.html')


def privacy(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'privacy.html', {'user_data': buyer_row})
    except:
        return render(request, 'privacy.html')


def products(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'products.html', {'user_data': buyer_row})
    except:
        return render(request, 'products.html')


def services(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'services.html', {'user_data': buyer_row})
    except:
        return render(request, 'services.html')


def shortcodes(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'shortcodes.html', {'user_data': buyer_row})
    except:
        return render(request, 'shortcodes.html')


def single(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'single.html', {'user_data': buyer_row})
    except:
        return render(request, 'single.html')


def vegetables(request):
    try:
        buyer_row = Buyer.objects.get(email=request.session['email'])
        return render(request, 'vegetables.html', {'user_data': buyer_row})
    except:
        return render(request, 'vegetables.html')


def add_row(request):
    Buyer.objects.create(
        first_name='kiran',
        last_name='patel',
        email='kiran@gmail.com',
        password='123',
        address='123,newtown,berlin',
        mobile_no='9876543210'
    )
    return HttpResponse('row created')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        try:
            Buyer.objects.get(email=request.POST['email'])
            return render(request, 'register.html', {'msg': 'Email is already registered!'})
        except:
            if request.POST['password'] == request.POST['repassword']:
                s = "Registered!"
                global user_data
                user_data = [request.POST['first_name'], request.POST['last_name'],
                    request.POST['email'], request.POST['password']]
                global c_otp
                c_otp = randrange(1000, 10000)
                m = f'Hello user!!\nyour OTP is {c_otp}'
                f = settings.EMAIL_HOST_USER
                r = [request.POST['email']]
                send_mail(s, m, f, r)
                return render(request, 'otp.html', {'msg': 'Check your mailbox'})
            else:
                return render(request, 'register.html', {'msg': 'password not match!'})


def otp(request):
        if str(c_otp) == request.POST['u_otp']:
            Buyer.objects.create(
                first_name=user_data[0],
                last_name=user_data[1],
                email=user_data[2],
                password=user_data[3]
            )
            return render(request, 'register.html', {'msg': 'Account created successfully!!'})
        else:
            return render(request, 'otp.html', {'msg': 'Wrong OTP enter again!'})


def logout(request):
    del request.session['email']  # remove email from session
    return redirect('index')


def add_to_cart(request, pk):
    try:
        p_obj = Product.objects.get(id=pk)
        buyer_row = Buyer.objects.get(email=request.session['email'])
        Cart.objects.create(
            product_name=p_obj.product_name,
            price=p_obj.price,
            pic=p_obj.pic,
            buyer=buyer_row
        )
        return redirect('index')
    except:
        return render(request, 'login.html')


def del_cart_item(request, pk):
    c_obj = Cart.objects.get(id=pk)
    c_obj.delete()
    return redirect('cart')


#  authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
 	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


@csrf_exempt
def paymenthandler(request):
	# only accept POST request.
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }          
            try:
                global amount
                amount = amount
                razorpay_client.payment.capture(payment_id, amount)
                buyer_row = Buyer.objects.get(email=request.session['email'])
                my_product = Cart.objects.filter(buyer=buyer_row)
                for i in my_product:
                    # OrderSummery.objects.create(
                    #     buyer=buyer_row,
                    #     product=i.product,
                    #     status='panding'
                    # )
                    i.delete()
                return render(request, 'paymentsuccess.html')
            except:
                # if there is an error while capturing payment.
                return render(request, 'paymentfailed.html') 
        except:
			# if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
	# if other than POST request is made.
        return HttpResponseBadRequest()


def cart(request):
    u1 = Buyer.objects.get(email = request.session['email'])
    global c_pro
    c_pro = Cart.objects.filter(buyer = u1)
    global t_amount
    t_amount = 0
    for i in c_pro:
        t_amount += i.price
    
    #Payment buton activate karne ka code
    currency = 'INR'
    # print(t_amount * 100)
    global amount
    amount = t_amount * 100 # total amount in paisa will accepted here so we have to multiply amount with 100
    if t_amount == 0 :
        return render(request, 'empty_cart.html')
	# Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

	# we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    context.update({'user_data':u1, 'cart_product': c_pro, 'total_amount':t_amount})

    return render(request, 'cart.html' ,context=context)
