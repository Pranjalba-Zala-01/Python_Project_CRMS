from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('login',views.login,name='login'),
    path('writer_page',views.writer_page,name='writer_page'),
    path('logout',views.logout,name='logout'),
]