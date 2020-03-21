from allauth.account.forms import LoginForm, PasswordField
from django import forms

class LoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        print(self.fields)
        self.fields['login'].widget = forms.TextInput(attrs={'class':"form-control",
                                                             'type':"input",
                                                             'placeholder':"usser",
                                                             'required':"true" ,})

        self.fields['password'].widget = forms.PasswordInput(attrs={
                                                                'class':"form-control",
                                                                 'type':"password",
                                                                 'placeholder':"password",
                                                                 'required':"true" ,
        })
        self.fields['remember'].widget = forms.PasswordInput(attrs={
                                                                    'class':"custom-control-input" ,
                                                                    'type':"checkbox" ,
                                                                    'checked': '',
                                                                    'id':"remember-me",
                                                                    })

