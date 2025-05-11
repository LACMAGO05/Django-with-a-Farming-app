from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Product, Cart
# from .forms import signform
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'index.html')


def register(request):
    # if request.method == "POST":
    #     form = signform(request.POST)
    #     if form.is_valid():
    #         form.save()  # Saves to the database (for ModelForm)
    #         return redirect('success')  # Redirect after successful submission
    #         return render(request, 'login.html')
    #     else:
    #         return redirect('/')
    # else:
    #     form = signform()
    # return render(request, "register.html", {"form": form})
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        nationality = request.POST['nationality']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already in use')
                return redirect('register')
            else:
                user = User.objects.create_user( username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'Account created successfully')
                return redirect('login')
        else:
          messages.info(request,'Password not matching')
          return redirect('register')  
        return redirect('/')
    else:
        return render(request,'register.html')

@login_required
def about(request):
    return render(request, 'about.html') 

@login_required
def blog(request):
    return render(request, 'blog.html') 

@login_required
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # send an email
        send_mail(
            name , # name
            subject , # subject
            message , # message
            email, 
            ['rebeccalacmago@gmail.com'], # to email
            fail_silently= False,
        )
        messages.info(request,'Your mail has been sent. We shall get back to you')
    else:
     return render(request, 'contact.html') 

@login_required
def feature(request):
    return render(request, 'feature.html') 

@login_required
def product(request):
    return render(request, 'product.html') 

@login_required
def testimonial(request):
    return render(request, 'testimonial.html') 

@login_required
def mes(request):
    return render(request, '404.html') 


def footer(request):
    return render(request, 'footer.html') 

def base(request):
    return render(request, 'base.html') 


def login(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:   
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def services(request):
    return render(request, 'services.html')


@login_required
def farm(request):
    return render(request, 'farm.html')


def moreproducts(request):
    return render(request, 'moreproducts.html')

def services1(request):
    return render(request, 'services1.html')


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_view') 

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})