from django.db import models
import uuid
from django.contrib.auth.models import User 

# Create your models here.
class CategoryModel(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False)
    cat_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name
  
class SubCategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=200, unique=True)
    sub_cat_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sub_category_name

class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/')

class ProductModel(models.Model):
    category = models.ForeignKey(to=CategoryModel, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(to=SubCategoryModel, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    stock_quantity = models.PositiveIntegerField()
    images = models.ManyToManyField(ProductImage, blank=True)
    

    def __str__(self):
        return self.product_name

