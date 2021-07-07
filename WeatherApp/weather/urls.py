from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name='home'),
    path('about', v.about, name='about'),
]
