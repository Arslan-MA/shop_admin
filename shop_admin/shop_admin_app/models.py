from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=80)

    CATEGORY = [
        ('Техника', 'Техника'),
        ('Бытовое', 'Бытовое'),
        ('Питание.', 'Питание')
    ]

    category = models.CharField(max_length=50, choices=CATEGORY)
    price = models.PositiveIntegerField()

    STATUS = [
        ('В наличии', 'В наличии'),
        ('Нет наличии', 'Нет наличии'),
    ]

    purchase_status = models.CharField(max_length=20, choices=STATUS)
    purchase_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.category} - {self.price} - " \
               f"{self.purchase_status} - {self.purchase_date}"

    def get_absolut_url(self):
        return f"product_info/{self.pk}"
