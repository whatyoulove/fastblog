from django.shortcuts import render

from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/login.html', {'user':user})
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'user_form':user_form})
