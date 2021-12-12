from django.db import models

# Create your models here.
class primary_model(models.Model):
    
    id = models.AutoField(primary_key=True)
    sku_id = models.CharField(max_length=200,null=True,blank=True)
    product_id = models.CharField(max_length=200,null=True,blank=True)
    sku_name = models.CharField(max_length=200,null=True,blank=True)
    price = models.CharField(max_length=200,null=True,blank=True)
    manufacturer_name = models.CharField(max_length=350,null=True,blank=True)
    salt_name = models.CharField(max_length=500,null=True,blank=True)
    drug_form = models.CharField(max_length=100,null=True,blank=True)
    pack_size = models.CharField(max_length=100,null=True,blank=True)
    strength = models.CharField(max_length=300,null=True,blank=True)
    product_banned_flag = models.CharField(max_length=100,null=True,blank=True)
    unit = models.CharField(max_length=50,null=True,blank=True)
    price_per_unit = models.CharField(max_length=200, null=True,blank=True)
    
    class Meta:
        db_table = 'primary_medicine_details'
        managed = True
    
    def __str__(self):
        
        return "sku name" + self.sku_name + "and salt name is " + self.salt_name

    
    