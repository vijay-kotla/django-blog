from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>/', views.category_by_id, name='category_by_id'),
]