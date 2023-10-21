from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Item

# Create your views here.
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("date_created") # connect Item model to menu list view
    template_name = "index.html"

    def get_context_data(self):
        context = {"item": "Pizza"}
        return context

class MenuItemDescription(generic.DetailView):
    # model is predefined var name
    model = Item
    template_name = "menu_item_detail.html"