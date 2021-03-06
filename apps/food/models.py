from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, null=False, related_name='client_profile', db_index=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='avatar/')


class Category(models.Model):
    name = models.CharField(max_length=60, db_index=True)

    def __str__(self):
        return  self.name


class DishFood(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    likes = models.PositiveSmallIntegerField(default=0)
    photo = models.ImageField(null=True, blank=True, upload_to='dishfood/')
    category = models.ForeignKey(Category, null=True, blank=True, related_name='dish_category', db_index=True, on_delete=models.SET_NULL)
    description = models.CharField(blank=True, null=True, max_length=5000)

    def __str__(self):
        return "{} {}".format(self.name, self.description)


class ClientListFood(models.Model):
    name = models.CharField(max_length=150, blank=True, db_index=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)



class ListItem(models.Model):
    item = models.ForeignKey(DishFood, null=True, blank=True, db_index=True, on_delete=models.SET_NULL)
    list = models.ForeignKey(ClientListFood, null=True, related_name="items", db_index=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)