from django.urls import path
from relations import views

urlpatterns = [
    path('relations/', views.relation_list),
    path('relations/<int:pk>/', views.relation_detail),
]