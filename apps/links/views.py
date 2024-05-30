from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from apps.links.models import Click, Link
from apps.links.utils import generate_short_code


def home_view(request):
    context = {
        'url': ''
    }
    if request.method == 'POST' and request.user.is_authenticated:
        
        original_url = request.POST.get('original_url')
        short_code = generate_short_code()
        link = Link.objects.create(original_url=original_url,
                                   short_code=''.join(short_code), user=request.user)
        link.save()
        context['url'] = 'http://127.0.0.1:8000/' + link.short_code
    return render(request, 'index.html', context=context)


def redirect_to_original(request, short_code):
    link = Link.objects.filter(short_code=short_code)
    if link.exists():
        click = Click.objects.create(link=link.first())
        click.save()
        return redirect(link.first().original_url)
    return render(request, '404.html')


@login_required(login_url='login')
def my_links(request):
    user = request.user
    links = Link.objects.filter(user=user).order_by('-id')
    return render(request, 'link_list.html', {'links': links})
