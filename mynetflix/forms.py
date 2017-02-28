from django import forms

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
    (PRICES, 'Prices'),
    (ACTOR, 'Actor')
    )
    search_text = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'width':'50', 'id':'insearch', 'placeholder':'Search...'}), max_length=100)
    search_by = forms.ChoiceField(label='Search by', label_suffix='', choices=SEARCH_BY_CHOICES)