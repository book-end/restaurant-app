from django.db import models
from django.contrib.auth.models import User

FOOD_CATEGORY = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("entree", "Entree"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

# Create your models here.
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    desc = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    food_category = models.CharField(max_length=200, choices=FOOD_CATEGORY)
    author = models.ForeignKey(User, on_delete=models.PROTECT) # author can be deleted from db but not their meal 
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True) # records whenever item is added
    date_updated = models.DateTimeField(auto_now=True) # records whenever item is edited

    # returns obj in str format
    def __str__(self):
        return self.meal