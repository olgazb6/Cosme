from django.shortcuts import render
from .models import Catalog
from django.views.generic.list import ListView
# from shop.forms import CartAddProductForm


# Create your views here.

# def catalog_index(request):
#     product = Catalog.objects.all()
#     context = {
#         'product': product,
#     }
#     return render(request, 'catalog/catalog.html', context)

class CatalogListView(ListView):
    model = Catalog      # shorthand for setting queryset = models.Car.objects.all()
    template_name = 'catalog/catalog.html'  # optional (the default is app_name/modelNameInLowerCase_list.html; which will look into your templates folder for that path and file)
    context_object_name = "product"    #default is object_list as well as model's_verbose_name_list and/or model's_verbose_name_plural_list, if defined in the model's inner Meta class
    paginate_by = 12

# def product_detail(request, id):
#     cart_product_form = CartAddProductForm()
#     product = get_object_or_404(Catalog, id=id, available=True)
#     return render(request, 'catalog/catalog_detail.html', {'product': product, 'cart_product_form': cart_product_form})


def dlya_tela(request):
    product = Catalog.objects.filter(category='Для тела')
    context = {
        'product': product,
    }
    return render(request, 'catalog/dlya_tela.html', context)

def face(request):
    product = Catalog.objects.filter(category='Для лица')
    context = {
        'product': product,
    }
    return render(request, 'catalog/face.html', context)

def dlya_volos(request):
    product = Catalog.objects.filter(category='Для волос')
    context = {
        'product': product,
    }
    return render(request, 'catalog/dlya_volos.html', context)

def catalog_detail(request, pk):
    product = Catalog.objects.get(pk=pk)
    context = {
        'product': product,}
    return render(request, 'catalog/catalog_detail.html', context)

def skin_type(request):
    product = Catalog.objects.filter(category='По типу кожи')
    context = {
        'product': product,
    }
    return render(request, 'catalog/skin_type.html', context)


def dry_skin(request):
    product = Catalog.objects.filter(product='Для сухой кожи')
    context = {
        'product': product,
    }
    return render(request, 'catalog/dry_skin.html', context)

def normal_skin(request):
    product = Catalog.objects.filter(product='Для нормальной кожи')
    context = {
        'product': product,
    }
    return render(request, 'catalog/normal_skin.html', context)

def oil_skin(request):
    product = Catalog.objects.filter(product='Для жирной кожи')
    context = {
        'product': product,
    }
    return render(request, 'catalog/oil_skin.html', context)