from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This should map /nice/ to the index view
]
