from django.shortcuts import render, redirect
from django.contrib.auth.hashers import Argon2PasswordHasher
from customers.models import Customer
from django.http import HttpResponseRedirect

# Create your views here.

def customer_pc_register(request):
    # register
    if request.method == "POST":
        if request.POST.get('password_register') == request.POST.get('password2_register'):
            hasher = Argon2PasswordHasher()
            request.POST._mutable = True
            # post = Customer.save(commit=False)
            post=Customer()
            post.fullname = str(request.POST.get('fullname'))
            post.email = str(request.POST.get('email').lower())
            post.password = str(hasher.encode(request.POST.get('password_register'), 'TTC241101'))  # (password: str, salt: str))
            post.phone_number = str(request.POST.get('phone_number'))
            post.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")

def customer_pc_login(request):
    # login
    if request.method == "POST":   
        email = str(request.POST.get('email_login').lower())
        password = str(request.POST.get('password_login'))
        hasher = Argon2PasswordHasher()
        password_encode = hasher.encode(password, 'TTC241101')

        # Lấy thông tin người dùng đăng nhập
        user = Customer.objects.filter(email=email, password=password_encode)

        # query = "SELECT * FROM customers_customer WHERE email = '%s' AND password = '%s';" % (email,password_encode)
        # user = Customer.objects.raw(query)
        if user.count():
            user_login = list(user.values())[0]  # dict
            user_login['create_date'] = user_login['create_date'].strftime('%d-%m-%Y %H:%M:%S')
            request.session['s_user'] = user_login
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")

def customer_pc_logout(request):
    if 's_user' in request.session:
        del request.session['s_user']
    return redirect("main:index")


def my_account(request):
    if 's_user' not in request.session:
        return redirect('main:index')
    return render(request,"customers/my-account.html")