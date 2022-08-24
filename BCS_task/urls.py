from django.urls import path

from BCS_task import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tx/<int:transaction_id>/', views.show_description, name='description'),
]