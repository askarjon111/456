from django.urls import path

from apps.links.views import home_view, my_links, redirect_to_original


urlpatterns = [
    path('', home_view, name='home'),
    path('<str:short_code>', redirect_to_original, name='redirect_to_original'),
    path('my-links/', my_links, name='my_links'),
]

