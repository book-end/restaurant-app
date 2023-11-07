# link urls to view

from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('item/<int:pk>/', views.MenuItemDescription.as_view(), name="menu_item") # int primary key pk for each item id, for dynamic urls
]
