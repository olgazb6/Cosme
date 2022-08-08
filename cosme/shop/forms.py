from django import forms
from django.forms import Textarea
from django.contrib.auth.models import User
from .models import Comment


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(f'Пользователь с именем: {username} не найден!')

        if not self.user.check_password(password):
            raise forms.ValidationError('Неверный пароль!')

        return cleaned_data


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-input'


    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']= 'form_comment'
        self.fields['text'].widget = Textarea(attrs = {'rows':5})   #кол-во строк









# class AddQuantityForm(forms.ModelForm):
#     class Meta:
#         model = OrderItem
#         fields = ['quantity']


# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
#
# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(
#                                 choices=PRODUCT_QUANTITY_CHOICES,
#                                 coerce=int)
#     update = forms.BooleanField(required=False,
#                                 initial=False,
#                                 widget=forms.HiddenInput)

