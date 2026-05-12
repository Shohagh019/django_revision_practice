from django import forms

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