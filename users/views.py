from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User 

def register(request):
    if request.method == 'POST':
          form = NewUserForm(request.POST)
          if form.is_valid():
               user = form.save()
               return redirect('/users/login')

    form = NewUserForm()
    context = {

        'form': form,
    }
    return render(request ,'users/register.html', context )

@login_required
def profile(request):
     return render(request ,'users/profile.html')


def create_profile(request):
     if request.method == 'POST':
          contact_num = request.POST.get('contact_num')
          image = request.FILES['upload']
          user = request.user
          profile = Profile( user=user , image=image , contact_num=contact_num)
          profile.save()
          
     return render(request,'users/createprofile.html')

def seller_profile(request , id):
     seller = User.objects.get(id = id )
     context = {
          'seller' : seller , 
     }
     return render(request , 'users/sellerprofile.html' , context)


# Create your views here.
