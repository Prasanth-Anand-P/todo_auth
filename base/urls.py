from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskList.as_view(), name = 'index'),
    path('task/<str:pk>/', TaskDetail.as_view(), name = 'taskdetail' ),
    path('task-create', TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<str:pk>/', TaskUpdate.as_view(), name = 'task-update' ),
    path('task-delete/<str:pk>/', TaskDelete.as_view(), name = 'task-delete' ),
]