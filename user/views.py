from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

# def login(request):
#     return render(request,'user/register.html')

# def logout(request):
#     return render(request,'user/register.html')
