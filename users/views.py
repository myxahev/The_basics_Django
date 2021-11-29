from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserProfileEditForm
from django.db import transaction


# from baskets.models import Basket
# from admins.views import UserCreateView
# from django.urls import reverse_lazy
# from django.contrib.auth.decorators import user_passes_test
# from django.utils.decorators import method_decorator


@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {'title': 'GeekShop - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

@transaction.atomic
@login_required
def profile(request):
    user = request.user
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form_user = UserProfileForm(instance=user, files=request.FILES, data=request.POST)
        form_user_profile = UserProfileEditForm(instance=user_profile, files=request.FILES, data=request.POST)
        if form_user.is_valid() and form_user_profile.is_valid():
            form_user.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form_user = UserProfileForm(instance=user)
        form_user_profile = UserProfileEditForm(instance=user.userprofile)
    context = {
        'title': 'GeekShop - Профиль',
        'form': form_user,
        'form_user_profile': form_user_profile,
        # 'baskets': Basket.objects.filter(user=user),
        # 'total_quantity': sum(basket.quantity for basket in baskets),
        # 'total_sum': sum(basket.sum() for basket in baskets),
    }

    return render(request, 'users/profile.html', context)


@csrf_exempt  # This skips csrf validation. Use csrf_protect to have validation
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                print('Сообщение пользователю отправлено.')
                messages.success(request, f'Письмо с кодом активации аккаунта отправлено вам на почту: {user.email}')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                print('Сообщение пользователю НЕ отправлено.')
                return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


def verify(request, email, activation_key):

    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'users/verify.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'users/verify.html')
    except Exception as err:
        print(f'error activation user: {err.args}')
        return HttpResponseRedirect(reverse('products:index'))


def send_verify_mail(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])

    title = f'Подтвердите учетную запись {user.username}'

    message = f'Для подтверждения учетной записи {user.username} ' \
              f'на портале {settings.DOMAIN_NAME} перейдите по ссылке: \n' \
              f'{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

# Create Class
# class UserRegistrationView(UserCreateView):
#     success_url = reverse_lazy('users:login')
#     template_name = 'users/registration.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(UserCreateView, self).get_context_data(**kwargs)
#         context['title'] = 'GeekShop - Регистрация'
#         return context
#
#     @method_decorator(user_passes_test(lambda u: not u.is_staff))
#     def dispatch(self, request, *args, **kwargs):
#         return super(UserCreateView, self).dispatch(request, *args, **kwargs)