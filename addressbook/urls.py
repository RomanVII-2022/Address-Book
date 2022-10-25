"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register-address', AddressCreateView.as_view(), name='createaddress'),
    path('edit-address/<int:pk>', AddressEditView.as_view(), name='editaddress'),
    path('delete-address/<int:pk>', AddressDeleteView.as_view(), name='deleteaddress'),
    path('search-results', SearchView.as_view(), name='searchaddress'),
]
