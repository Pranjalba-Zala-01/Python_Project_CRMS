from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('login',views.login,name='login'),
    path('writer_page',views.writer_page,name='writer_page'),
    path('logout',views.logout,name='logout'),

    path('writer_form',views.writer_form,name='writer_form'),
    path('writer_form/<int:id>/',views.writer_form,name='writer_update'),
    path('writer_delete/<int:id>/',views.writer_delete,name='writer_delete'),
    path('writer_list',views.writer_list,name='writer_list'),

    path('criminal_form',views.criminal_form,name='criminal_form'),
    path('criminal_form/<int:id>/',views.criminal_form,name='criminal_update'),
    path('criminal_delete/<int:id>/',views.criminal_delete,name='criminal_delete'),
    path('criminal_list',views.criminal_list,name='criminal_list'),

    path('victim_form',views.victim_form,name='victim_form'),
    path('victim_form/<int:id>/',views.victim_form,name='victim_update'),
    path('victim_delete/<int:id>/',views.victim_delete,name='victim_delete'),
    path('victim_list',views.victim_list,name='victim_list'),
]