from django.shortcuts import render


def home_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'index.html')
