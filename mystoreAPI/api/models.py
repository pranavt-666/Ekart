from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class UserProfile(AbstractUser):
    # user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profilepics', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)


    
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.CharField(max_length=120)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='productimage', null=False)

    def __str__(self) -> str:
        return self.name 
    

class Reviews(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5),
    ] )
    created_date = models.DateTimeField(auto_now_add=True)
    reviews = models.CharField(max_length=200)
    class Meta:
        unique_together = ("user", "product")
    def __str__(self):
        return self.reviews
    




class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    options = (('in-cart','in-cart'),
               ('cancelled', 'cancelled'),
               ('order-placed', 'order-placed'))

