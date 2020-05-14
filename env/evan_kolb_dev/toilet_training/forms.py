from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Trainee

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    user_type = forms.ChoiceField(choices=(
        ('BCBA', 'BCBA'),
        ('RBT' , 'RBT'),
        ('GUARDIAN', 'Guardian')), help_text='User Type')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'user_type', 'password1', 'password2',)
        

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ('alias', 'age', 'trainers', 'dry_checks', 'underwear', 'positive_practice', 'liquid_intake',) 

    
