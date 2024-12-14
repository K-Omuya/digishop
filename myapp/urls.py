from . import views
from django.urls import path
urlpatterns = [

    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),


    path('contacts/', views.contacts, name='contacts'),
    path('api/search/', views.product_search, name='product_search'),

    path('search_results/', views.search_results, name='search_results'),
    # path('upload_second/', views.upload_second, name='upload_second'),
    path('update_item_price/', views.update_item_price, name='update_item_price'),


    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token')

]
