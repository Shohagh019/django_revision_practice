from django.shortcuts import render

from first_app.forms import LoginForm, DetailsForm, StudentForm

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'login.html', {'form': form})


def details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'details.html', {'form': form})
    else:
        form = DetailsForm()
    return render(request, 'details.html', {'form': form})

def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'student.html', {'form': form})
    else:
        form = StudentForm()
    return render(request, 'student.html', {'form': form})

