from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tools/', views.tools_index, name='index'),
  path('tools/<int:tool_id>/', views.tools_detail, name='detail'),
  path('tools/create/',views.ToolCreate.as_view(),name = 'tools_create'),
  path('tools/<int:pk>/update/', views.ToolUpdate.as_view(), name='tools_update'),
  path('tools/<int:pk>/delete/', views.ToolDelete.as_view(), name='tools_delete'),
  path('tools/<int:tool_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
  path('storages/', views.StorageList.as_view(), name='storages_index'),
  path('storages/<int:pk>/', views.StorageDetail.as_view(), name='storages_detail'),
  path('storages/create/', views.StorageCreate.as_view(), name='storages_create'),
  path('storages/<int:pk>/update/', views.StorageUpdate.as_view(), name='storages_update'),
  path('storages/<int:pk>/delete/', views.StorageDelete.as_view(), name='storages_delete'),
  path('tools/<int:tool_id>/assoc_storage/<int:storage_id>/', views.assoc_storage, name='assoc_storage'),
]

