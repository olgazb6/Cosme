from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='shop/password-reset.html'),name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='shop/done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='shop/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='shop/password_reset_complete.html'), name='password_reset_complete'),
    # path('add-item-to-cart/<int:pk>', views.add_item_to_cart, name='add_item_to_cart'),
    # path('detail', views.cart_detail, name='cart_detail'),
    # path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    # path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('blog/', views.blog, name='blog'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    # path('<int:pk>/', views.blog_detail, name='blog_detail'),
]