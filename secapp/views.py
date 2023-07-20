from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Bike
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.views.generic import ListView
from django.core.paginator import Paginator

def index(request):
    return HttpResponse("hey")

def bikes(request,):
    page_obj = bikes = Bike.objects.all()
    bikes_name = request.GET.get('bikes_name')

    if bikes_name!='' and bikes_name is not None:
       page_obj =  bikes.filter(name__icontains = bikes_name)

    paginator = Paginator(page_obj,3)
    page_number = request.GET.get('page') # to get page num 
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
    }
    return render(request , 'secapp/products.html' , context)


class Bikes1(ListView):
    model = Bike
    template_name = 'secapp/products.html'
    context_object_name = 'bikes'
    paginate_by = 3

def product_details(request , id):
    bike = Bike.objects.get(id=id )
    context = {
           'bike' : bike
    }
    return render(request , 'secapp/detail.html' , context)


@login_required
def add_bike(request):
    if request.method ==  'POST':
        name = request.POST.get('name')
        bikenum = request.POST.get('bikenum')
        desc= request.POST.get('desc')
        seller_name = request.user
        image = request.FILES['upload']
        bike = Bike(name=name , desc=desc ,bikenum=bikenum, image=image , seller_name = seller_name)
        bike.save()


    return render(request , 'secapp/addbike.html')

def update_bike(request , id):
    bike = Bike.objects.get(id=id)
    if request.method == 'POST':
        bike.name =  request.POST.get('name')
        bike.bikenum = request.POST.get('bikenum')
        bike.desc= request.POST.get('desc')
        bike.image = request.FILES['upload']
        bike.save()
        return redirect('/secapp/bikes')

    context = {
        'bike' : bike 
    }
    return render(request , 'secapp/updatebike.html' , context)

def delete_bike(request , id):
    bike = Bike.objects.get(id=id)
    context = {
        'bike':bike
    }
    if request.method == 'POST' :
        bike.delete()
        return redirect('/secapp/bikes')
    return render(request , 'secapp/delete.html' , context)

def my_listings(request):
    bikes = Bike.objects.filter(seller_name = request.user)
    context = {
        'bikes': bikes,
    }

    return render(request , 'secapp/mylistings.html' , context)

