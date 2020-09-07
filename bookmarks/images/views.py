from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ImageForm


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
