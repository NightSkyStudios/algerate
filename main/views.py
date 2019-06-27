from django.shortcuts import render, HttpResponseRedirect
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


def verified_page(request):
    image = PostedImage.objects.filter(isVerified=False)

    if request.method == "POST":
       if request.POST.get('delete_image') is not None:
           id = request.POST.get('delete_image')
           PostedImage.objects.get(pk=id).delete()
           return HttpResponseRedirect('verified')


    if request.method == "POST":
       if request.POST.get('verified') is not None:
            id = request.POST.get('verified')
            item = PostedImage.objects.get(pk=id)
            item.isVerified = True
            item.save()
            return HttpResponseRedirect('verified')


    ctx = {'image': image}

    return render(request, 'verified_page.html', ctx)
