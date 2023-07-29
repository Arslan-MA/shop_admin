from django.shortcuts import render, redirect
from shop_admin_app.models import Product


def main_page(request):
    context = {'products': Product.objects.all()}

    return render(request, 'mainPage.html', context)


def buy_product(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(id=product_id)
        product.purchase_status = "Нет наличии"
        product.save()

        return redirect('user_app:home')


def product_info(request, product_id):
    context = {'product': Product.objects.get(id=product_id)}

    return render(request, 'productInfo.html', context)
