from django.urls import path
from . import views

urlpatterns = [
    path('', views.repository_list, name='repository_list'),
    path('repository/<int:pk>/', views.repository_detail, name='repository_detail'),
    path('repository/create/', views.create_repository, name='create_repository'),
    path('repository/<int:repository_pk>/file/create/', views.create_file, name='create_file'),
    path('file/<int:file_pk>/version/create/', views.create_version, name='create_version'),
    path('file/<int:file_pk>/compare/<int:version1_pk>/<int:version2_pk>/', views.compare_versions, name='compare_versions'),
]


