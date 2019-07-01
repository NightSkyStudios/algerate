from django.shortcuts import render, HttpResponseRedirect
from .models import *
from random import randint
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def rate(request):

    ctx = {'rate': range(1, 11)}

    return render(request, 'rate.html', ctx)


def image_details(request, uuid):
    image = PostedImage.objects.get(unique_link=uuid)
    ratings = Rating.objects.filter(ratedImage=image)
    count = len(ratings)
    s = 0
    for r in ratings:
        s += r.rating
    try:
        avg = s / count
    except ZeroDivisionError:
        avg = 'not rated yet'
    ctx = {'image': image,
           'avg': avg}

    return render(request, 'image_details.html', ctx)


def images_list(request):
    ctx = {'images': PostedImage.objects.all()}

    return render(request, 'image_list.html', ctx)


def verified_page(request):
    image = PostedImage.objects.filter(isVerified=False)

    if request.method == "POST":
        if request.POST.get('delete_image') is not None:
            id = request.POST.get('delete_image')
            PostedImage.objects.get(pk=id).delete()
            return HttpResponseRedirect('verified')

        if request.POST.get('verified') is not None:
            id = request.POST.get('verified')
            item = PostedImage.objects.get(pk=id)
            item.isVerified = True
            item.save()
            return HttpResponseRedirect('verified')

    ctx = {'image': image}

    return render(request, 'verified_page.html', ctx)


def get_image(request):
    images = PostedImage.objects.all()
    id = randint(0, len(images) - 1)
    image = images[id]

    request.session.__setitem__('uuid', image.unique_link.__str__())

    return HttpResponse(image.image.url)


def rate_image(request, rate):
    if int(rate) in range(1, 11):
        image = PostedImage.objects.get(unique_link=request.session.get('uuid'))
        request.session.__delitem__('uuid')
        Rating.objects.create(ratedImage=image, rating=rate)
    else:
        ...

    return HttpResponse('')
