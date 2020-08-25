from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='insert'),
    path('list/', views.employee_list, name='display'),
    path('update_employee/<str:pk>/',
         views.employee_update, name='update'),
   path('delete/<int:id>/',views.employee_delete,name = 'delete')      
]
