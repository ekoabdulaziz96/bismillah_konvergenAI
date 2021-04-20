from django.urls import path, include

from . import views

app_name = 'app_dataset'

urlpatterns = [
     #---------------------------------------------------------PATH DATASET
    path('dataset/detail/<int:pk>',views.DatasetDetailView.as_view(), name='dataset-detail'),
    path('dataset/update/<int:pk>',views.DatasetUpdateView.as_view(), name='dataset-update'),
    path('dataset/delete/<int:pk>',views.DatasetDeleteView.as_view(), name='dataset-delete'),
    path('dataset/create/', views.DatasetCreateView.as_view(),name='dataset-create'),
    path('dataset/', views.DatasetListView.as_view(), name='dataset-index'),

     #---------------------------------------------------------PATH TASK
    path('task/cancel-soft-delete/<int:pk>',views.cancel_softDelete, name='task-cancel-soft-delete'),
    path('task/set-booking/<int:pk>',views.set_booking, name='task-set-booking'),
    path('task/detail/<int:pk>',views.TaskDetailView.as_view(), name='task-detail'),
    path('task/update/<int:pk>',views.TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<int:pk>',views.TaskDeleteView.as_view(), name='task-delete'),
    path('task/delete-soft/<int:pk>',views.TaskSoftDeleteView.as_view(), name='task-soft-delete'),
    path('task/create/', views.TaskCreateView.as_view(),name='task-create'),
    path('task/', views.TaskListView.as_view(), name='task-index'),
]