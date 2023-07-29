from django import forms
from shop_admin_app.models import Product


class ProductModelForm(forms.ModelForm):
    # name = models.CharField(max_length=80)
    #
    # CATEGORY = [
    #     ('ТЕХ', 'Техника'),
    #     ('БЫТ', 'Бытовое'),
    #     ('ПИТ', 'Питание')
    # ]
    #
    # category = models.CharField(max_length=50)
    # price = models.PositiveIntegerField()
    # purchase_status = models.BooleanField()
    # purchase_date = models.DateField()

    class Meta:
        model = Product
        exclude = ('purchase_date',)
        labels = {
            'name': 'Название',
            'category': 'Категория',
            'price': 'Цена',
            'purchase_status': 'Статус покупки',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'inp_class'}),
            'category': forms.Select(attrs={'class': 'sel_class'}),
            'price': forms.NumberInput(attrs={'class': 'inp_class'}),
            'purchase_status': forms.Select(attrs={'class': 'sel_class'}),
        }
