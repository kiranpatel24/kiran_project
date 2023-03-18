from django.db import models

class Seller(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=70)
    address = models.TextField(max_length=50)
    mobile_no = models.CharField(max_length=15) #or we can use IntegerFieldf
    gst_no = models.CharField(max_length=15)
    pic = models.FileField(upload_to= 'profile_pics', default='sad.png')


    def __str__(self):
        return self.email


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    des = models.TextField(max_length=255)
    price = models.FloatField(default=10.0)
    product_stock = models.IntegerField(default=0)
    pic = models.FileField(default='sad.jpg', upload_to='product_pics')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


        
# class OrderSummery(models.Model):
#     all_status = [
#         ('pending', 'pending'),
#         ('dispatched', 'dispatched')
#     ]

#     buyer = models.ForeignKey(to='buyer.Buyer', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     status = models.CharField(choices= all_status,max_length=50, default='pending')

#     def __str__(self):
#         return str(self.id)
        
