from django .urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('read/<int:id>', views.read, name='reader'),
    path('articles/', views.articles, name='articles'),
    path('contact/', views.contact, name='contact'),
]