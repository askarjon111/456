from django.urls import path

from apps.links.views import home_view, redirect_to_original


urlpatterns = [
    path('', home_view, name='home'),
    path('<str:short_code>', redirect_to_original, name='redirect_to_original'),
]

