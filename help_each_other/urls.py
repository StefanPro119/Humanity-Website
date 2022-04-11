from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('leave_charity/', views.leave_charity, name='leave_charity'),
    path('address_list/', views.address_list, name='address_list'),
    path('show_item/<int:id>/', views.show_item, name='show_item'),
    path('show_current_item/<int:id>/', views.show_current_item, name='show_current_item'),

]
