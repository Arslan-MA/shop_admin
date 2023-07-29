from django.shortcuts import render, redirect, get_object_or_404
from shop_admin_app.models import Product
from shop_admin_app.forms import ProductModelForm


def main_page(request):
    context = {'products': Product.objects.all()}

    return render(request, 'mainPageAdmin.html', context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    return redirect('admin_app:home')


def add_product(request):
    if request.method == "POST":
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_app:home')
    else:
        form = ProductModelForm()
        context = {'forms': form}

        return render(request, 'addProducts.html', context)


def edit_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if request.method == "POST":
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()

            return redirect('admin_app:home')
    else:
        form = ProductModelForm(instance=product)
        context = {'forms': form,
                   'product': product}

        return render(request, 'editProduct.html', context)
