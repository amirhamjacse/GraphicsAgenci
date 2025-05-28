# shortener/views.py
from django.shortcuts import render, redirect, get_object_or_404
from urlshortner.forms import URLForm
from .models import ShortURL


def home(request):
    form = URLForm()
    short_url = None

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            short = form.save()
            short_url = request.build_absolute_uri(f"/{short.short_code}")
    return render(request, 'home.html', {'form': form, 'short_url': short_url})


def redirect_url(request, short_code):
    link = get_object_or_404(ShortURL, short_code=short_code)
    link.clicks += 1
    link.save()
    return redirect(link.original_url)
