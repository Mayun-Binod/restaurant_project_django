from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    message=models.TextField()

class Category(models.Model):
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Momo(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image') # pip install Pillow
    price=models.DecimalField(max_digits=5,decimal_places=2)
    
    