import hashlib
import random

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User, UserProfile


# import datetime


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите отчество (если есть)'}))
    age = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите возраст'}))

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'middle_name', 'age')

    def clean_age(self):
        data = self.cleaned_data['age']
        if int(data) < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError(f'Пользователь с почтой {data} уже существует.')

        return data

    # if User.objects.filter(email=form.email).exists():
    #     print('Пользователь с данным email уже используется')
    #     messages.success(request, f'Пользователь с {form.email} уже существует.')

    #     return HttpResponseRedirect(reverse('users:login'))

    def save(self, **kwargs):
        user = super(UserRegistrationForm, self).save()

        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()

        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    age = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'middle_name', 'age')


class UserProfileEditForm(forms.ModelForm):
    tagline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    about_me = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = UserProfile
        fields = ('tagline', 'about_me', 'gender')


# class UserProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('tagline', 'about_me', 'gender')
#
#     def __init__(self, *args, **kwargs):
#         super(UserProfileEditForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control py-4'