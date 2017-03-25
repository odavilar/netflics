from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SearchForm(forms.Form):
    TITLE = 'TI'
    DIRECTOR = 'DI'
    COUNTRY = 'CO'
    PRICES = 'PR'
    ACTOR = 'AC'
    SEARCH_BY_CHOICES = (
    (TITLE, 'Title'),
    (DIRECTOR, 'Director'),
    (COUNTRY, 'Country'),
    (PRICES, 'Award'),
    (ACTOR, 'Actor')
    )
    search_text = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'width':'50', 'id':'insearch', 'placeholder':'Search...'}), max_length=100)
    search_by = forms.ChoiceField(label='Search by', label_suffix='', choices=SEARCH_BY_CHOICES)

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user