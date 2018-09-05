from django.db import models

# class Goods_shopcar(models.Model):
#     car_id = models.AutoField(primary_key=True)
#     uid = models.IntegerField()
#     goods_id = models.IntegerField()
#     num = models.IntegerField()
#     status = models.BooleanField()
#     create_time = models.DateField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)
# #
# class Order(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     order_number = models.CharField(max_length=64)
#     uid = models.IntegerField()
#     pay_price = models.DecimalField(20,2)
#     is_pay = models.BooleanField()
#     pay_time = models.DateField(auto_now_add=True)
#     is_ship = models.BooleanField()
#     is_receipt = models.BooleanField()
#     receipt_time = models.DateField(auto_now_add=True)
#     ship_number = models.CharField(max_length=64)
#     status = models.BooleanField()
#     create_time = models.DateField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)
# #
# class Order_goods(models.Model):
#     id = models.AutoField(primary_key=True)
#     order_id = models.IntegerField()
#     goods_id = models.IntegerField()
#     goods_num = models.IntegerField()
#     goods_price = models.DecimalField(20,2)
#     status = models.BooleanField()
#     create_time = models.DateField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)

class USER(models.Model):
    USERID =models.CharField(max_length=20, primary_key=True)
    USERNAME = models.CharField(max_length=50, unique=True)
    REALNAME = models.CharField(max_length=50, null=True)
    EMAIL = models.CharField(max_length=100)
    TELNO = models.CharField(max_length=20, null=True)
    MOBILE = models.CharField(max_length=20, null=True)
    QUESTION = models.CharField(max_length=50,null=True)
    ANSWER = models.CharField(max_length=50, null=True)
    PASSWORD = models.CharField(max_length=32)
    USERSTATE = models.IntegerField(default=1)
    class Meta:
        db_table = 'USER'
