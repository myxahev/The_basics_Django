from django.shortcuts import render, HttpResponseRedirect
# from django.urls import reverse
from orderapp.models import Order
from users.models import User
from products.models import Product, ProductCategory
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from products.forms import ProductUpdateForm, ProductCategoryUpdateForm
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Geekshop - Админ панель'}
    return render(request, 'admins/index.html', context)


# Create Class
class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admins:admin_users')
    template_name = 'admins/admin-users-create.html'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Создание пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


# Create Class
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('admins:read_products')
    template_name = 'admins/admin-products-create.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Создание товара'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)


# Create Class
class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryUpdateForm
    success_url = reverse_lazy('admins:category_read_products')
    template_name = 'admins/admin-products-category-create.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Создание Категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryCreateView, self).dispatch(request, *args, **kwargs)


# Read Class
class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Пользователи'
        return context


# Read Class
class ProductListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Продукты'
        return context


# Read Class
class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-products-category-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Категории'
        return context


# Read Class
class OrderListView(ListView):
    model = Order
    template_name = 'admins/admin-orders-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(OrderListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Заказы'
        return context


# Update Class
class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    template_name = 'admins/admin-users-update-delete.html'

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Редактирование пользовтаеля'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


# Update Class
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    success_url = reverse_lazy('admins:read_products')
    template_name = 'admins/admin-products-update-delete.html'

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Редактирование продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


# Update Class
class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryUpdateForm
    success_url = reverse_lazy('admins:category_read_products')
    template_name = 'admins/admin-products-category-update-delete.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Редактирование категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryUpdateView, self).dispatch(request, *args, **kwargs)


# Delete Class
class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.safe_delete()
    #     return HttpResponseRedirect(success_url)


# Delete Class
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:read_products')


# Delete Class
class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-products-category-update-delete.html'
    success_url = reverse_lazy('admins:category_read_products')

# # Delete
# @user_passes_test(lambda u: u.is_staff)
# def product_delete(request, id):
#     product = Product.objects.get(id=id)
#     product.delete()
#     return HttpResponseRedirect(reverse('admins:read_products'))

# # Create
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, 'Вы успешно зарегестрировались!')
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'title': 'Geekshop - создание пользователя', 'form': form}
#     return render(request, 'admins/admin-users-create.html', context)

# # Create
# @user_passes_test(lambda u: u.is_staff)
# def products_create(request):
#     if request.method == 'POST':
#         form = ProductUpdateForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, 'Вы успешно зарегестрировались!')
#             return HttpResponseRedirect(reverse('admins:read_products'))
#         else:
#             print(form.errors)
#     else:
#         form = ProductUpdateForm()
#     context = {'title': 'Geekshop - создание продукта', 'form': form}
#     return render(request, 'admins/admin-products-create.html', context)


# # Read
# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {
#         'title': 'Geekshop - польователи',
#         'users': User.objects.all(),
#     }
#     return render(request, 'admins/admin-users-read.html', context)

# @user_passes_test(lambda u: u.is_staff)
# def products_read(request):
#     context = {
#         'title': 'Geekshop - продукты',
#         'products': Product.objects.all(),
#     }
#     return render(request, 'admins/admin-products-read.html', context)
# Update
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#
#     context = {
#         'title': 'Geekshop - обновление польователя',
#         'form': form,
#         'selected_user': selected_user,
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)


# # Update
# @user_passes_test(lambda u: u.is_staff)
# def products_update(request, id):
#     selected_product = Product.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProductUpdateForm(instance=selected_product, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:read_products'))
#     else:
#         form = ProductUpdateForm(instance=selected_product)
#
#     context = {
#         'title': 'Geekshop - редактирование продукта',
#         'form': form,
#         'selected_product': selected_product,
#     }
#     return render(request, 'admins/admin-products-update-delete.html', context)

# # Delete
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     # user.is_active = False
#     # user.save()
#     user.safe_delete()
#     return HttpResponseRedirect(reverse('admins:admin_users'))