from django.db.models import Q
from django.shortcuts import render

from .models import Product


# Create your views here.

def home(request):
    product = Product.objects.all()

    return render(request, 'product/index.html', {'key': product})



def show(request, id):
    product = Product.objects.get(id = id);

    return render(request, 'product/detail.html', {'key': product})




def about(request):
    product = Product.objects.all()

    return render(request, 'product/about.html', {'key': product})


def shop(request):
        product = Product.objects.all()
        if request.method == "POST":
            if request.POST['search']:
                print("You Type" + request.POST['search'])
                product = Product.objects.filter(Q(name__icontains = request.POST['search']))
                if product:
                    return render(request, 'product/shop.html', {'key': product})
                else:
                    no_Record = "No Record Found"
                    return render(request, 'product/shop.html', {'Found': no_Record})
            else:
             print("Type Something")
        return render(request, 'product/shop.html', {'key': product})





def cart(request):
    product = Product.objects.all()

    return render(request, 'product/home.html', {'key': product})



def checkout(request):
        product = Product.objects.all()

        return render(request, 'product/home.html', {'key': product})

    # print(product)
