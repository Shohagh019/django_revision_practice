from django import forms
from django.core import validators

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    
    
class DetailsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    file = forms.FileField(label='Upload File')
    # email = forms.EmailField(label='Email')
    # age = forms.IntegerField(label='Age')
    # balance = forms.DecimalField(label='Balance', max_digits=10, decimal_places=2)
    # birth_date = forms.DateField(label='Birth Date', widget=forms.DateInput(attrs={'type': 'date'}))
    # size = forms.ChoiceField(label='Size', choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')])
    # meal = forms.MultipleChoiceField(label='Meal Preferences', choices=[('veg', 'Vegetarian'), ('nonveg', 'Non-Vegetarian'), ('vegan', 'Vegan')], widget=forms.CheckboxSelectMultiple) 

# validation using clean method

# class StudentForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)
#     age = forms.IntegerField(label='Age')
#     email = forms.EmailField(label='Email')

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         valage = self.cleaned_data['age']

#         if valname and len(valname) > 20:
#             raise forms.ValidationError("Name should be less than 20 characters")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Email should contain '.com'")
#         if valage < 0:
#             raise forms.ValidationError("Age should be a positive integer")


# validation using validators

class StudentForm(forms.Form):
    name = forms.CharField(label = 'Student Name', widget=forms.TextInput, validators= [validators.MaxLengthValidator(20, message="Name should be less than 20 characters")])
    email = forms.CharField(label = 'Email', widget=forms.EmailInput, validators= [validators.EmailValidator(message="Enter a valid email address")])
    age = forms.IntegerField(label = 'Age', widget=forms.NumberInput, validators= [validators.MinValueValidator(0, message="Age should be a positive integer")])
    file = forms.FileField(label='Upload File', validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'], message="Only PDF and DOCX files are allowed")])

