from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings

#--------------models
from app_dataset import models

#--------------forms
from app_dataset import forms

#--------------views

#---------------------------------------------------------------------extra_context
EC_task_listView = {
        'page_judul': 'Tabel Task',
        'page_deskripsi': 'untuk mengelola data Task',
        'page_role': 'Task',
    }

EC_task_createView= {
        'page_judul': 'Tambah Task',
        'page_deskripsi': 'untuk menambah data Task',
        'page_role': 'Task',
        'role': 'create',
    }

EC_task_updateView = {
        'page_judul': 'Edit Task',
        'page_deskripsi': 'untuk memperbarui data Task',
        'page_role': 'Task',
        'role': 'update',
    }

EC_task_detailView ={
        'page_judul': 'Detail Task',
        'page_deskripsi': 'untuk melihat detail data Task',
        'page_role': 'Task',
    }
#----------------------------------------------------------------------------------------------Class view
#---------------------------------------------------------------------Read (list)
class TaskListView(ListView):
    model = models.Task
    ordering = ['id']
    template_name = "app_dataset/task/index.html"
    context_object_name = 'tasks'
    extra_context = EC_task_listView

    def get_queryset(self):
        print(self.request.user)
        if self.request.user.is_superuser:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(deleted_at = None).filter(user_id=self.request.user.id)
        return queryset

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(TaskListView, self).get_context_data(*args, **kwargs)
        return context
#---------------------------------------------------------------------Create
class TaskCreateView(SuccessMessageMixin, CreateView):
    form_class = forms.TaskForm
    template_name = "app_dataset/task/create.html"
    success_url = reverse_lazy('ad:task-index')
    context_object_name = 'forms'
    extra_context = EC_task_createView

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(TaskCreateView, self).get_context_data(*args, **kwargs)
        return context
    
    # def form_invalid(self, form):
    #     print('invalid',self.get_context_data(form=form)['form']['user'])
    #     """If the form is invalid, render the invalid form."""
    #     return self.render_to_response(self.get_context_data(form=form))
        
    def get_success_message(self, cleaned_data):
        return 'Data Task berhasil ditambahkan'

#---------------------------------------------------------------------Update
class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Task
    form_class = forms.TaskForm
    template_name = "app_dataset/task/create.html"
    context_object_name = 'task'
    success_url = reverse_lazy('ad:task-index')
    extra_context = EC_task_updateView
    
    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(TaskUpdateView, self).get_context_data(*args, **kwargs)

        return context

    def get_success_message(self, cleaned_data):
        return 'Data Task berhasil diperbarui'

#---------------------------------------------------------------------Delete
class TaskDeleteView(DeleteView):
    model = models.Task
    # template_name = "app_dataset/task/create.html"
    success_url = reverse_lazy('ad:task-index')
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        # self.object.delete()
        self.object.hard_delete()
        return HttpResponseRedirect(success_url)

class TaskSoftDeleteView(DeleteView):
    model = models.Task
    # template_name = "app_dataset/task/create.html"
    success_url = reverse_lazy('ad:task-index')
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        self.object.delete()
        # self.object.hard_delete()
        return HttpResponseRedirect(success_url)

#---------------------------------------------------------------------Detail
class TaskDetailView(DetailView):
    model = models.Task
    template_name = "app_dataset/task/detail.html"
    context_object_name = 'task'
    extra_context = EC_task_detailView

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(TaskDetailView, self).get_context_data(*args, **kwargs)

        return context


#---------------------------------------------------------------------Set booking
def set_booking(request, pk):
    if request.method == 'POST':
        task = models.Task.objects.get(pk=pk)
        task.isBooking = not task.isBooking
        task.save()
        return JsonResponse('success', safe=False)

def cancel_softDelete(request, pk):
    if request.method == 'POST':
        task = models.Task.objects.get(pk=pk)
        task.deleted_at = None
        task.save()
        return JsonResponse('success', safe=False)