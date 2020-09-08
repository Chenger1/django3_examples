from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .forms import ImageForm
from .models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        image_form = ImageForm(data=request.POST)
        if image_form.is_valid():
            cd = image_form.cleaned_data
            new_image = image_form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image has been successfully added')
            return redirect(new_image.get_absolute_url())
    else:
        image_form = ImageForm(data=request.GET)

    return render(request, 'images/image/create.html',
                  {'section': 'images',
                   'form': image_form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)

    return render(request, 'images/image/detail.html',
                  {'section': 'images',
                   'image': image})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'error'})
