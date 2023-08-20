from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLogin.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('', TaskList.as_view(), name = 'index'),
    path('task/<str:pk>/', TaskDetail.as_view(), name = 'taskdetail' ),
    path('task-create', TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<str:pk>/', TaskUpdate.as_view(), name = 'task-update' ),
    path('task-delete/<str:pk>/', TaskDelete.as_view(), name = 'task-delete' ),
]