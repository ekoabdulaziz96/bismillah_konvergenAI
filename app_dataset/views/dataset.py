from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#--------------models
from app_dataset import models

#--------------forms
from app_dataset import forms

#--------------views

#---------------------------------------------------------------------extra_context
EC_dataset_listView = {
        'page_judul': 'Tabel Dataset',
        'page_deskripsi': 'untuk mengelola data Dataset',
        'page_role': 'Dataset',
    }

EC_dataset_createView= {
        'page_judul': 'Tambah Dataset',
        'page_deskripsi': 'untuk menambah data Dataset',
        'page_role': 'Dataset',
        'role': 'create',
    }

EC_dataset_updateView = {
        'page_judul': 'Edit Dataset',
        'page_deskripsi': 'untuk memperbarui data Dataset',
        'page_role': 'Dataset',
        'role': 'update',
    }

EC_dataset_detailView ={
        'page_judul': 'Detail Dataset',
        'page_deskripsi': 'untuk melihat detail data Dataset',
        'page_role': 'Dataset',
    }
#----------------------------------------------------------------------------------------------Class view
#---------------------------------------------------------------------Read (list)
@method_decorator(login_required, name='dispatch')
class DatasetListView(ListView):
    model = models.Dataset
    ordering = ['id']
    template_name = "app_dataset/dataset/index.html"
    context_object_name = 'datasets'
    extra_context = EC_dataset_listView

    # def get_queryset(self):
        # queryset = self.model.objects.exclude(username=settings.USERNAME_DEVELOPER)
        # return queryset

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(DatasetListView, self).get_context_data(*args, **kwargs)
        return context
#---------------------------------------------------------------------Create
@method_decorator(login_required, name='dispatch')
class DatasetCreateView(SuccessMessageMixin, CreateView):
    form_class = forms.DatasetForm
    template_name = "app_dataset/dataset/create.html"
    success_url = reverse_lazy('ad:dataset-index')
    context_object_name = 'forms'
    extra_context = EC_dataset_createView

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(DatasetCreateView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_message(self, cleaned_data):
        return 'Data Dataset berhasil ditambahkan'

#---------------------------------------------------------------------Update
@method_decorator(login_required, name='dispatch')
class DatasetUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Dataset
    form_class = forms.DatasetForm
    template_name = "app_dataset/dataset/create.html"
    context_object_name = 'dataset'
    success_url = reverse_lazy('ad:dataset-index')
    extra_context = EC_dataset_updateView
    
    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(DatasetUpdateView, self).get_context_data(*args, **kwargs)

        return context

    def get_success_message(self, cleaned_data):
        return 'Data Dataset berhasil diperbarui'

#---------------------------------------------------------------------Delete
@method_decorator(login_required, name='dispatch')
class DatasetDeleteView(DeleteView):
    model = models.Dataset
    # template_name = "app_dataset/dataset/create.html"
    success_url = reverse_lazy('ad:dataset-index')
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        self.object.delete()
        return HttpResponseRedirect(success_url)

#---------------------------------------------------------------------Detail
@method_decorator(login_required, name='dispatch')
class DatasetDetailView(DetailView):
    model = models.Dataset
    template_name = "app_dataset/dataset/detail.html"
    context_object_name = 'dataset'
    extra_context = EC_dataset_detailView

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(DatasetDetailView, self).get_context_data(*args, **kwargs)

        return context


