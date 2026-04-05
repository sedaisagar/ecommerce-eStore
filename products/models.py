from django.db import models

from utils.models import CommonModel



class ProductCategory(CommonModel):
    name = models.CharField(max_length=255, unique=True) 

    class Meta:
        db_table = "product_categories"

    def __str__(self):
        return self.name

class ProductType(CommonModel):
    name = models.CharField(max_length=255, unique=True) 

    class Meta:
        db_table = "product_types"
        
    def __str__(self):
        return self.name
class Product(CommonModel):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    short_description = models.CharField(max_length=500)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField()

    # images = models.JSONField(default=list) # [list of image URLs]
    class Meta:
        db_table = "products"

class ProductImages(CommonModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    class Meta:
        db_table = "product_images"