from django.contrib import admin
from django.urls import path
from . import views

app_name = 'secapp'
urlpatterns = [
    path('' ,views.index) ,
    path('bikes/' , views.bikes,name='bikes' ) , 
    path('bikes/<int:id>' , views.product_details , name = 'bike_details') ,  
    path('bikes/addbike' , views.add_bike , name = 'addbike'),
    path('bikes/updatebike/<int:id>' , views.update_bike , name='update_bike'),
    path('bikes/deletebike/<int:id>' , views.delete_bike , name='delete_bike'),
    path('bikes/mylist' , views.my_listings , name='mylist') , 
    
]