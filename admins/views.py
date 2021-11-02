from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.models import User
from products.models import Product
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from products.forms import ProductUpdateForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Geekshop - Админ панель'}
    return render(request, 'admins/index.html', context)

# Create
@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('admins:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'Geekshop - создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)

# Create
@user_passes_test(lambda u: u.is_staff)
def products_create(request):
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('admins:read_products'))
        else:
            print(form.errors)
    else:
        form = ProductUpdateForm()
    context = {'title': 'Geekshop - создание продукта', 'form': form}
    return render(request, 'admins/admin-products-create.html', context)


# Read
@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    context = {
        'title': 'Geekshop - польователи',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)

# Read
@user_passes_test(lambda u: u.is_staff)
def products_read(request):
    context = {
        'title': 'Geekshop - продукты',
        'products': Product.objects.all(),
    }
    return render(request, 'admins/admin-products-read.html', context)


# Update
@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)


    context = {
        'title': 'Geekshop - обновление польователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)

# Update
@user_passes_test(lambda u: u.is_staff)
def products_update(request, id):
    selected_product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductUpdateForm(instance=selected_product, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:read_products'))
    else:
        form = ProductUpdateForm(instance=selected_product)


    context = {
        'title': 'Geekshop - редактирование продукта',
        'form': form,
        'selected_product': selected_product,
    }
    return render(request, 'admins/admin-products-update-delete.html', context)


# Delete
@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    # user.is_active = False
    # user.save()
    user.safe_delete()
    return HttpResponseRedirect(reverse('admins:admin_users'))

# Delete
@user_passes_test(lambda u: u.is_staff)
def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(reverse('admins:read_products'))