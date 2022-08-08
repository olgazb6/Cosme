from django.db import models
from django.utils import timezone
# from decimal import Decimal
# from django.db import transaction
# from django.dispatch import receiver
# from django.db.models import Sum
# from django.db.models.signals import post_save, post_delete
# from django.contrib.auth.models import User
# from catalog.models import Catalog
# # Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='shop/static/shop/img/')
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий:')
    created_on = models.DateTimeField(auto_now_add=True)
    blog =  models.ForeignKey(Blog, on_delete=models.CASCADE, related_name= 'blog_comment')








# class Payment(models.Model):                                                                   #ПЛАТЕЖ
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)       #сумма платежа
#     time = models.DateTimeField(auto_now_add=True)
#     comment = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return f'{self.user}  --- {self.amount} '
#
#     @staticmethod
#     def get_balance(user:User):
#         amount = Payment.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum']
#         return amount or Decimal(0)
#
#
# class Order(models.Model):                                                                      #ЗАКАЗ
#     STATUS_CART = '1_cart'                                                                      #статус корзина
#     STATUS_WAITING_FOR_PAYMENT = '2_waiting_for_payment'                                        #статус ждет оплаты
#     STATUS_PAID = '3_paid'                                                                      #статус оплачен
#     STATUS_CHOICES = [
#         (STATUS_CART, 'cart'),
#         (STATUS_WAITING_FOR_PAYMENT, 'waiting_for_payment'),
#         (STATUS_PAID, 'paid')
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # items = models.ManyToManyField(OrderItem, related_name='orders')
#     status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=STATUS_CART)        #статус заказа
#     amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)         #сумма
#     creation_time = models.DateTimeField(auto_now_add=True)
#     payment = models.ForeignKey(Payment, on_delete=models.PROTECT, blank=True, null=True)
#     comment = models.TextField(blank=True, null=True)
#
#
#     def __str__(self):
#         return f'{self.user}  --- {self.amount} --- {self.status}'


    # def get_cart(user: User):                                         #находит или создает корзину
    #     cart = Order.object.filter(user = user, status = Order.STATUS_CART).first()
    #     if not cart:
    #         cart = Order.object.create(user = user, status = Order.STATUS_CART,amount = 0)
    #     return cart
    #
    # def get_amount(self):
    #     amount = Decimal(0)
    #     for item in orderitem_set.all():                    #Сумма в корзине
    #         amount += item.amount
    #     return amount
    #
    # def make_order(self):                                   #офрмление заказа, смена статуса
    #     items = orderitem_set.all()
    #     if items and self.status == Order.STATUS_CART:
    #         self.status = Order.STATUS_WAITING_FOR_PAYMENT
    #         self.save()
    #         auto_payment_unpaid_orders(self.user)
    #
    # @staticmethod
    # def get_amount_of_unpaid_orders(user: User):                                               #общая сумма неоплаченных заказов юзера
    #     amount = Order.objects.filter(user=user, status = Order.STATUS_WAITING_FOR_PAYMENT
    #                                   ).aggregate(Sum('amount'))['amount__sum']
    #     return amount or Decimal(0)

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Catalog, on_delete=models.PROTECT)
#     quantity = models.PositiveIntegerField(default=1)
#     price = models.DecimalField(max_digits=20, decimal_places=2)
#     discount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
#
#     def __str__(self):
#         return f'{self.product}  --- {self.price}'

#     @property
#     def amount(self):                                                    #стоимость каждого
#         return self.quantity * (self.price - self.discount)
#
# @transaction.atomic()
# def auto_payment_unpaid_orders(user: User):                             #платеж неоплаченных заказов
#     unpaid_orders = Order.objects.filter(user=user, status = Order.STATUS_WAITING_FOR_PAYMENT)
#     for order in unpaid_orders:
#         if Payment.get_balance(user) < order.amount:
#             break
#         order.payment = Payment.objects.all().last()
#         order.status = Order.STATUS_PAID
#         oreder.save()
#         Payment.object.create(user=user, amount = order.amount)
#
#
# @receiver(post_save, sender = OrderItem)                                # пересчет стоимости после добавления
# def recalculate_order_amount_after_save(sender, instance, **kwargs):
#     order = instance.order
#     order.amount = order.get_amount()
#     order.save()
#
#
# @receiver(post_delete, sender = OrderItem)                                # пересчет стоимости после удаления
# def recalculate_order_amount_after_delete(sender, instance, **kwargs):
#     order = instance.order
#     order.amount = order.get_amount()
#     order.save()
#
# @receiver(post_save, sender = Payment)                                # пересчет стоимости после добавления
# def auto_pay(sender, instance, **kwargs):
#     user = instance.user
#     auto_payment_unpaid_orders(user)
