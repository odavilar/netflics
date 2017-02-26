from django import forms

class SearchForm(forms.Form):
    search_text = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'width':'50','id':'insearch','placeholder':'Search per title, actor, price, country...'}), max_length=100)