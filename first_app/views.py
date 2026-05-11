from django.shortcuts import render

from first_app.forms import LoginForm

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process the login logic here
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Username: {username}, Password: {password}")
            # You can authenticate the user here and redirect as needed         
    return render(request, 'login.html', {'form': form})
