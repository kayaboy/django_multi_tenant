from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.main, name='main'),
    path('contact/add-contact/', views.addContact, name='add-contact'),
    path('contact/edit-contact/<str:pk>', views.editContact, name='edit-contact'),
    path('contact/delete/<str:pk>', views.deleteContact, name='delete'),
    path('contact/profile/<str:pk>', views.contactProfile, name='profile')
]