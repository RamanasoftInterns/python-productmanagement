from django.db.models import Q
from django.shortcuts import redirect, render
from .models import Product, Category
from .forms import ProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django import template


# main page all products
def ShowAllProducts(request):
    category = request.GET.get('category')
    if category == None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__name=category)

    page_num = request.GET.get('page')
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    all_category = Category.objects.all()
    context = {
        'products': products,
        'all_category': all_category
    }
    return render(request, 'allProducts.html', context)


# product detail page
@login_required(login_url='allProducts')
def productDetail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'productDetail.html', context)


# to add a product
@login_required(login_url='allProducts')
def addProduct(request):
    all_category = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        if name and price and image:

            Product.objects.create(
                name=name, price=price, description=description, image=image, category_id=category)
            return redirect('allProducts')
    return render(request, 'addProduct.html', {"all_category": all_category})


@login_required(login_url='allProducts')
def updateProduct(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        product.save()
        return redirect('allProducts')
    context = {
        'product': product
    }
    return render(request, 'updateProduct.html', context)


# deleteing the product
@login_required(login_url='allProducts')
def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('allProducts')

# searched product


def searchProduct(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Product.objects.filter(
                Q(name__icontains=query) | Q(price__icontains=query))
            return render(request, 'searchPage.html', {'products': products})
        else:
            return render(request, 'noProduct.html')
    else:
        return redirect('allProducts')
