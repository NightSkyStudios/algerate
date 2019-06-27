from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def rate(request):
    print(request.COOKIES['csrftoken'])
    if request.POST:
        print(request.COOKIES['csrftoken'])

    ctx = {'rate': range(1, 11)}

    return render(request, 'rate.html', ctx)


def get_image(request, hash):
    ctx = {}

    return render(request, 'image_tag.html', ctx)


def image_details(request, uuid):
    image = PostedImage.objects.get(unique_link=uuid)
    ctx = {'image': image}

    return render(request, 'image_details.html', ctx)


def images_list(request):
    ctx = {'images': PostedImage.objects.all()}

    return render(request, 'image_list.html', ctx)
