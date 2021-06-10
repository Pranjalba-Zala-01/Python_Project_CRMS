from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name='welcome'),
    path('index',views.index,name='index'),
    path('writer_page',views.writer_page,name='writer_page'),
    path('logout',views.logout,name='logout'),
    path('writer_form',views.writer_form,name='writer_form'),
    path('writer_form/<int:id>/',views.writer_form,name='writer_update'),
    path('writer_delete/<int:id>/',views.writer_delete,name='writer_delete'),
    path('writer_list',views.writer_list,name='writer_list')
] 