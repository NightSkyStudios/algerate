from django.shortcuts import render, HttpResponseRedirect
from .models import *
from random import randint
from django.http import HttpResponse, Http404
from django.shortcuts import redirect


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
           'avg': avg,
           'count': count}

    return render(request, 'image_details.html', ctx)


def images_list(request):
    if not request.user.is_authenticated:
        return redirect('/admin/')

    ctx = {'images': PostedImage.objects.all()}

    return render(request, 'image_list.html', ctx)


def verified_page(request):
    if not request.user.is_authenticated:
        return redirect('/admin/')
    image = PostedImage.objects.filter(isVerified=False)

    if request.method == "POST":
        if request.POST.get('delete_image') is not None:
            id = request.POST.get('delete_image')
            PostedImage.objects.get(pk=id).delete()
            # return render(request, 'verified_page.html')

        if request.POST.get('verified') is not None:
            id = request.POST.get('verified')
            item = PostedImage.objects.get(pk=id)
            item.isVerified = True
            item.save()
            # return render(request, 'verified_page.html')
    image = PostedImage.objects.filter(isVerified=False)

    ctx = {'image': image}

    return render(request, 'verified_page.html', ctx)


def get_image(request, mode):
    if mode == 0:
        images = PostedImage.objects.all()
    elif mode == 1:
        images = PostedImage.objects.filter(sex='Male')
    elif mode == 2:
        images = PostedImage.objects.filter(sex='Female')
    else:
        images = PostedImage.objects.all()

    image = images[randint(0, len(images) - 1)]
    ratings = Rating.objects.filter(ratedImage=image)
    count = len(ratings)
    s = 0
    for r in ratings:
        s += r.rating
    try:
        avg = format(s/count, ".1f")
    except ZeroDivisionError:
        avg = 'not rated yet'

    request.session.__setitem__('uuid', image.unique_link.__str__())

    return HttpResponse(f'{image.image.url}\n{avg}')


def rate_image(request, rate):
    if int(rate) in range(1, 11):
        image = PostedImage.objects.get(unique_link=request.session.get('uuid'))
        print(request.session.get('uuid'))
        request.session.__delitem__('uuid')
        Rating.objects.create(ratedImage=image, rating=rate)
    else:
        ...

    return HttpResponse('')


def about(request):

    return render(request, 'about.html')


def contact(request):

    return render(request, 'contact.html')


def submit_photo(request):

    if request.POST:
        email = request.POST.get('email')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        image = request.FILES['file']
        # print(f)
        instance = PostedImage.objects.create(email=email,
                                   age=age,
                                   sex=sex,
                                   image=image)
        instance.save()

    return render(request, 'submit_photo.html')
