from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import *
from buyer.models import *
from django.core.mail import send_mail
from random import randrange
from django.conf import settings



# create your views here

def seller_edit_profile(request):
    try:
        seller_obj = Seller.objects.get(email = request.session['seller_email'])
        if request.method == 'GET':
            return render(request, 'seller_edit_profile.html',{'seller_data': seller_obj})
        else:
            seller_obj.full_name = request.POST['full_name']
            seller_obj.address = request.POST['address']
            seller_obj.gst_no = request.POST['gst_no']
            try:
                seller_obj.pic = request.FILES['pic']
                seller_obj.save() #database me change karne ke liye call karna padega
            except:
                seller_obj.save()
            return redirect('seller_edit_profile')
    except:
        return render(request, 'seller_login.html')

def seller_edit_product(request, pk):
        p_obj = Product.objects.get(id = pk)
        if request.method == 'GET':
            seller_obj = Seller.objects.get(email = request.session['seller_email'])
            return render(request, 'seller_edit_product.html',{'seller_data': seller_obj, 'product_data':p_obj})
        else:
            p_obj.product_name = request.POST['product_name']
            p_obj.des = request.POST['des']
            p_obj.price = request.POST['price']
            p_obj.product_stock = request.POST['product_stock']
            try:
                p_obj.pic = request.FILES['pic']
                p_obj.save()
            except:
                p_obj.save()
            return redirect('seller_edit_product',pk)
        return redirect('seller_edit_product',pk)


def seller_index(request):
    try:
        seller_obj=Seller.objects.get(email=request.session['seller_email'])
        return render(request,'seller_index.html',{'seller_data':seller_obj})
    except:
        return render(request,'seller_login.html')



def seller_login(request):
    if request.method == 'POST':
        try:
            seller_obj = Seller.objects.get(email = request.POST['email'])
            if request.POST['password'] == seller_obj.password:
                request.session['seller_email'] = request.POST['email']
                return render(request, 'seller_index.html',{'seller_data': seller_obj})
            else:
                return render(request, 'seller_login.html', {'msg': 'Wrong Password!!'})
        except:
            return render(request, 'seller_login.html', {'msg':'Email is Not Registered!!'})

    else:
        return render(request, 'seller_login.html')

def seller_logout(request):
    del request.session['seller_email']
    return redirect('seller_login')    


def seller_products(request):
    try:
        seller_obj = Seller.objects.get(email = request.session['seller_email'])
        my_product = Product.objects.filter(seller = seller_obj)
        return render(request, 'seller_products.html',{'seller_data': seller_obj, 'my_all_products':my_product})
    except:
        return render(request, 'seller_login.html')


def seller_register(request):
    if request.method == 'GET':
        return render(request, 'seller_register.html')    
    else:
        try:
            Seller.objects.get(email = request.POST['email'])
            return render(request, 'seller_register.html', {'msg': 'Email Is Already registered!!'})
        except:
            if request.POST['password'] == request.POST['repassword']:
                s = "Registration!!"
                global seller_data
                seller_data = [request.POST['full_name'], request.POST['email'], request.POST['password']]
                global a_otp
                a_otp = randrange(1000,9999)
                m = f'Hello User!!\nYour OTP is {a_otp}'
                f = settings.EMAIL_HOST_USER
                r = [request.POST['email']]
                send_mail(s, m, f, r)
                return render(request, 'seller_otp.html', {'msg': 'Check Your MailBox'})
            else:
                return render(request, 'seller_register.html', {'msg': 'Both Passwords do not match!!'})

def seller_otp(request):
        if str(a_otp) == request.POST['u_otp']:
            Seller.objects.create(
                full_name = seller_data[0],
                email = seller_data[1],
                password = seller_data[2]
            )
            return render(request, 'seller_register.html', {'msg' : 'Account created successfully!!'})
        else:
            return render(request, 'seller_otp.html', {'msg' : 'Wrong OTP enter again!'})


def seller_add_product(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    if request.method == 'GET':
        return render(request, 'seller_add_product.html', {'seller_data':seller_obj})
    else:
        Product.objects.create(
            product_name = request.POST['product_name'],
            des = request.POST['des'],
            price = request.POST['price'],
            product_stock = request.POST['product_stock'],
            pic = request.FILES['pic'],
            seller = seller_obj
        )
        return redirect('seller_add_product')

def product_delete(request, pk):
    p_obj = Product.objects.get(id = pk)
    p_obj.delete()
    return redirect('seller_products')
    
