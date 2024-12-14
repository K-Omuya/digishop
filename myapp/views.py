from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product, ProductPrice
from .models import Product
from django.shortcuts import render, redirect

import json
from requests.auth import HTTPBasicAuth
import requests
from django.http import HttpResponse


from myapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required



def home(request):
    # Fetch featured products from the database
    products = Product.objects.all()[:6]  # Limit to 6 products for featured section

    product_data = []
    for product in products:
        prices = ProductPrice.objects.filter(product=product)
        price_details = []
        for price in prices:
            price_details.append({
                'platform': price.platform.name,
                'price': price.price,
                'url': price.platform.url,
            })
        product_data.append({
            'name': product.name,
            'description': product.description,
            'prices': price_details
        })

    return render(request, 'home.html', {'product_data': product_data})


def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def blog(request):
    return render(request, 'blog.html')
def contacts(request):
    return render(request, 'contacts.html')


# views.py
from django.shortcuts import render

def search_results(request):
    # Add your search logic here, for example:
    query = request.GET.get('q', '')
    # Implement your search logic to fetch the search results from the database
    context = {
        'query': query,
        # Add your search results to the context, e.g., 'results': results
    }
    return render(request, 'search_results.html', context)




def product_search(request):
    search_query = request.GET.get('search', '').lower()
    if search_query:
        # Query the database for products that match the search query
        products = Product.objects.filter(name__icontains=search_query)
        product_list = [
            {
                'product': product.name,
                'platform': product.platform,
                'price': f"KSh {product.price}",
                'image': product.image,
                'url': product.url
            }
            for product in products
        ]
        return JsonResponse({'products': product_list})
    else:
        return JsonResponse({'products': []})




# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ItemPrice
import json

@csrf_exempt  # Temporarily disable CSRF for simplicity. In production, use proper CSRF handling.
def update_item_price(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Parse the incoming JSON data
        item_id = data.get('item_id')  # Updated variable name to item_id
        new_price = data.get('new_price')
        platform = data.get('platform')

        try:
            # Find the item by ID
            item_price = ItemPrice.objects.get(item_id=item_id, platform=platform)
            item_price.price = new_price
            item_price.save()
            return JsonResponse({'message': 'Item price updated successfully!'})
        except ItemPrice.DoesNotExist:
            return JsonResponse({'error': 'Item price for this platform not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=400)




def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")