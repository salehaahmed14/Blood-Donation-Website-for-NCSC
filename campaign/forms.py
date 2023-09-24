from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Personal_Information, Medical_Information, Volunteer

class DateInput(forms.DateInput):
    input_type = 'date'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = Personal_Information
        fields = '__all__'
        exclude = ['person_id']
        widgets = {'dob': DateInput()}

class InitialMedicalInformationForm(forms.ModelForm):
    class Meta:
        model = Medical_Information
        fields = '__all__'
        exclude = ['person_id', 'last_donation', 'campaign_id']

class MedicalInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_donation'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Medical_Information
        fields = '__all__'
        exclude = ['person_id']
        widgets = {
            'last_donation': DateInput(),
            'blood_type': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'campaign': forms.Select(attrs={'class': 'form-control'}),
        }

class VolunteerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campaign_id'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Volunteer
        fields = '__all__'
        exclude = ['volunteer_id']
        widgets = {
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            # 'campaign_id': forms.ModelMultipleChoiceField(attrs={'class': 'form-control'}),
        }