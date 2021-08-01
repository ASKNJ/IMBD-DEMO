from django import forms


class GenerateApiToken(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off', 'title': 'Your username here.'}),
                               max_length=50,
                               label='Username', required=True)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'title': 'Your password here.', 'autocomplete': "current-password"}),
                               max_length=200, label='Password', required=True)



