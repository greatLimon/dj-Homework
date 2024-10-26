from django.shortcuts import render, redirect

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by =  request.GET.get('sort')
    match sort_by:
        case 'name':
            phone_objects = Phone.objects.all().order_by('name')
        case 'min_price':
            phone_objects = Phone.objects.all().order_by('price')
        case 'max_price':
            phone_objects = Phone.objects.all().order_by('-price')
        case Any:
            phone_objects = Phone.objects.all()
    phones = [{'name':phone.name, 'slug':phone.slug, 'price':phone.price, 'image':phone.image} for phone in phone_objects]
    context = {'phones':phones} #phones = {'slug', 'name', 'price', 'image'}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug = slug).first()
    phone = {
        'name':phone_object.name,
        'image':phone_object.image,
        'price':phone_object.price,
        'release_date':phone_object.release_data,
        'lte_exist':phone_object.lte_exist
    }
    context = {
        'phone':phone
    } #phone = {name, image, price, release_date, lte_exist}
    return render(request, template, context)
