from django.db import models

# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 



class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    text = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

        
class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                 related_name='reviews')
                                 
    def __str__(self):
        return self.text