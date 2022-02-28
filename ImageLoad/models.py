from django.db import models
from django.utils import timezone

# Create your models here.
class TablaArchivo(models.Model):
    name_img= models.CharField(max_length=50, null=False)
    url_img = models.ImageField(null=True,blank=True, default='', upload_to='assets/img/')
    format_img= models.CharField(max_length=10, null=False)
    created= models.DateTimeField(default=timezone.now)
    edited=models.DateTimeField(blank=True,default=None,null=True)

    class Meta:
        managed: True
        db_table: 'TablaArchivo'