from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        address_list = Address.objects.all().order_by('first_name')
        context["address_list"] = address_list
        return context
    
    

class AddressCreateView(SuccessMessageMixin, CreateView):
    form_class = AddressCreateForm
    template_name = 'createaddress.html'
    success_message = 'Address was registered successfully'
    success_url = reverse_lazy('home')


class AddressEditView(SuccessMessageMixin, UpdateView):
    model = Address
    form_class = AddressEditForm
    template_name = 'editaddress.html'
    success_message = 'Address was edited successfully'
    success_url = reverse_lazy('home')

class AddressDeleteView(SuccessMessageMixin, DeleteView):
    model = Address
    template_name = 'deleteaddress.html'
    success_message = 'Address was deleted successfully'
    success_url = reverse_lazy('home')

class SearchView(TemplateView):
    template_name = 'addresssearch.html'

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            search = request.GET['search']
            address_list = Address.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search) | 
            Q(email__icontains=search) | Q(phone__icontains=search) | Q(address__icontains=search) | Q(created_on__icontains=search))
            return render(request, 'addresssearch.html', {'address_list':address_list, 'search':search})
        return super().get(request, *args, **kwargs)
    
