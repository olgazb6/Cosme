from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm, CommentForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.contrib import messages
# from catalog.models import Catalog
# from django.views.decorators.http import require_POST
# from .cart import Cart
from django.views.generic import ListView, DetailView
from .models import Blog, Comment

# Create your views here.

def login_user(request):
    context = {'login_form': LoginForm()}

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                context = {
                    'login_form': login_form,
                    'attention': f'Пользователь с именем {username} не зарегистрирован!'}
        else:
            context = {
                'login_form': login_form,}

    return render (request, 'shop/login.html', context)

class Register(TemplateView):
    template_name = 'register.html'

    def get(self, request):
        user_form = RegisterForm()
        context = {'user_form': user_form}
        return render(request, 'shop/register.html', context)

    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            messages.success(request, f'Аккаунт успешно создан!')
            return redirect('index')

        context = {'user_form': user_form}
        return render(request, 'shop/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def cart_detail(request):
    return render(request, 'shop/cart_detail.html')

def blog(request):
    return render(request, 'shop/blog.html')



class BlogListView(ListView):
    model = Blog
    template_name = 'shop/blog.html'
    context_object_name = "blog_item"

class BlogDetailView(FormMixin, DetailView):
    model = Blog
    template_name = 'shop/blog_detail.html'
    context_object_name = 'blog_item'
    form_class = CommentForm

    # success_url = 'index.html'

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.blog = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)












# def blog_detail(request, pk):
#     blog_item = Blog.objects.get(pk=pk)
#     context = {
#         'blog_item': blog_item}
#     return render(request, 'shop:blog_detail.html', context)

# @login_required(login_url=reverse_lazy('login'))
# def add_item_to_cart(request, pk):
#     if request.method == 'POST':
#         # quantity_form = AddQuantityForm(request.POST)
#         # if quantity_form.is_valid():
#             quantity = 1
#             if quantity:
#                 cart = Order.get_cart
#                 product = Catalog.objects.get(pk=pk)
#                 # product = get_object_or_404(Catalog, pk=pk)
#                 cart.orderitem_set.create(product=product,
#                                           quantity=quantity,
#                                           price=product.cost)
#                 cart.save()
#                 return redirect('shop_item')
#             else:
#                 pass
#     return redirect('catalog')



# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Catalog, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('shop:cart_detail')
#
#
# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Catalog, id=product_id)
#     cart.remove(product)
#     return redirect('shop:cart_detail')
#
#
# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
#                                                                    'update': True})
#     return render(request, 'shop/cart_detail.html', {'cart': cart})
#
# def product_detail(request, id):
#     cart_product_form = CartAddProductForm()
#     product = get_object_or_404(Catalog, id=id, available=True)
#     return render(request, 'catalog/catalog_detail.html', {'product': product, 'cart_product_form': cart_product_form})

