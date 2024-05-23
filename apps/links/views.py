from django.shortcuts import render

from apps.links.models import Link
from apps.links.utils import generate_short_code


def home_view(request):
    context = {
        'url': ''
    }
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        short_code = generate_short_code()
        link = Link.objects.create(original_url=original_url,short_code=''.join(short_code))
        link.save()
        context['url'] = 'http://127.0.0.1:8000/' + link.short_code
    return render(request, 'index.html', context=context)
