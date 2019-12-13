from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.UsernameInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password'
            ]
        # labels = {
        #     'username': 'username',
        #     'password': 'password',
        # }
        # widgets = {
        #     'password':forms.PasswordInput(),
        # }

    # username = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('User with this username did not sign up in our system!')
        user = User.objects.get(username=username)
        if user and not user.check_password(password):
            raise forms.ValidationError('Wrong password!')





class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password_check',
            'first_name',
            'last_name',
            'email'
        ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'
        self.fields['password'].help_text = 'Invent a password'
        self.fields['password_check'].label = 'Re-enter password'
        self.fields['first_name'].label = 'Name'
        self.fields['last_name'].label = 'Last name'
        self.fields['email'].label = 'E-mail'
        self.fields['email'].help_text = 'Please, enter your real email address'


    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']
        email = self.cleaned_data['email']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('User with this username exists in our system!')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email exists in our system!')

        if password != password_check:
            raise forms.ValidationError('Your password did not match! Try again!')





class OrderForm(forms.Form):


    name = forms.CharField()
    last_name = forms.CharField(required=False)
    phone = forms.CharField()
    buying_type = forms.ChoiceField(widget=forms.Select(), choices=([("Self", "Self"), ("Delivery", "Delivery")]))
    date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())
    address = forms.CharField(required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Name'
        self.fields['last_name'].label = 'Surname'
        self.fields['phone'].label = 'Phone number'
        self.fields['phone'].help_text = 'Please enter your real phone number, to contact you'
        self.fields['buying_type'].label = 'Receiving type'
        self.fields['address'].label = 'Delivery address'
        self.fields['address'].help_text = '*Necessary to enter your city!'
        self.fields['comments'].label = 'Comments to order'
        self.fields['date'].label = 'Delivery date'
        self.fields['date'].help_text = 'Delivery will be realize a next day after order, our manager will contact to you'
