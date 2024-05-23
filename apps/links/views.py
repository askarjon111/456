from django.shortcuts import render

from apps.links.models import Link


def home_view(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        link = Link.objects.create(original_url=original_url)
        link.save()
    return render(request, 'index.html')
