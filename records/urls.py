from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', add_patient),
    path('admin-login/', admin_login),
    path('dashboard/', admin_dashboard),
    path('delete/<int:id>/', delete_patient),  
    path('print/<int:id>/', print_patient),
    path('edit/<int:id>/', edit_patient),
    path('add-patient/', views.add_patient),
]

