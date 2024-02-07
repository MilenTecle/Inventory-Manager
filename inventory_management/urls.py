"""
URL configuration for inventory_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventory.views import *



urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('contact/', include("contact.urls")),
    path('', landing_page, name='landing_page'),
    path('inventory/', inventory_page, name='inventory'),
    path('categories/', add_category, name='add_category'),
    # path('dasboard/', dashboard, name='dashboard'),
    path('summernote/', include('django_summernote.urls')),
    path('inventory/<int:pk>/', inventory_detail, name="inventory_detail"),
    path('edit_item/<int:item_id>/', edit_item, name="edit_item"),
    path('clone/<int:item_id>/', clone_list, name="clone_list"),
    path('delete_item/<int:item_id>/', delete_item, name="delete_item"),
    path('inventory/<int:inventory_id>/saved/', saved_list, name="saved_list"),
    path('delete_list/<int:pk>/', delete_list, name="delete_list"),
    path('delete_category/<int:category_id>/', delete_category, name="delete_category"),
    path('edit_category/<int:category_id>/', edit_category, name="edit_category"),
]
