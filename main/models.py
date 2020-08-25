from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Country(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length = 20)
    country = models.ForeignKey(Country,on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Employee(models.Model):
    fullname = models.CharField(max_length = 20)
    empcode = models.CharField(max_length = 10)
    mobile = models.CharField(max_length = 20)
    position = models.ForeignKey(Position,on_delete = models.CASCADE)
    fullname = models.CharField(max_length = 20)
    country = models.ForeignKey(Country,on_delete = models.SET_NULL,null = True)    
    city = models.ForeignKey(City,on_delete = models.SET_NULL,null = True)  
    
        

    