from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm



# Create your views here.
def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account creation for {username} successful! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context= {'form': form}    
    return render(request, 'users/register.html', context)