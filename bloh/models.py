from customer.models import CustomerModel
from django.db import models
from ckeditor.fields import RichTextField
from autoslug.fields import AutoSlugField
from django.contrib.auth.models import User
from django.db.models.enums import Choices
from django.db.models.fields import CharField

# Create your models here.
class AreaCategorymodel(models.Model):
    STATUS=(
        ('DAĞLIQ','DAĞLIQ'),
        ('DÜZƏNLİK','DÜZƏNLİK'),
        ('DƏNİZQIRAĞI','DƏNİZQIRAĞI'),
        ('SƏHRA','SƏHRA')
    )
    REGİON=(
        ('HEÇBİRİ','-'),
        ('ARAN','ARAN'),
        ('GƏNCƏ-QAZAX','GƏNCƏ-QAZAX'),
        ('ABŞERON','ABŞERON'),
        ('LƏNKƏRAN','LƏNKƏRAN'),
        ('NAXÇIVAN','NAXÇIVAN'),
        ('KƏLBƏCƏR-LAÇIN','KƏLBƏCƏR-LAÇIN'),
        ('DAĞLIQ QARABAĞ','DAĞLIQ QARABAĞ'),
        ('DAĞLIQ ŞİRVAN','DAĞLIQ ŞİRVAN'),
        ('QUBA-XAÇMAZ','QUBA-XAÇMAZ'),
        ('ŞƏKİ-ZAQATALA','ŞƏKİ-ZAQATALA'),

        )
    economic_region=models.CharField(choices=REGİON,max_length=40,default='HEÇBİRİ',null=True)
    specify=models.CharField(choices=STATUS,max_length=20,default='DAĞLIQ',null=True)
    content=RichTextField(null=True)
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='image')
    author=models.ForeignKey('customer.CustomerModel',on_delete=models.CASCADE,related_name='region',null=True)
    population=models.FloatField(null=True)


    class Meta:
        db_table='ərazi'
        verbose_name='ərazi'
        verbose_name_plural='ərazilər'
    def __str__(self):
        return self.name
    
class Addermodel(models.Model):
    name=models.CharField(max_length=100,null=True)
    area=models.ForeignKey(AreaCategorymodel,on_delete=models.CASCADE,related_name='yazi')
    photo=models.ImageField(upload_to='images')
    content=RichTextField()
    author=models.ForeignKey('customer.CustomerModel',on_delete=models.CASCADE,related_name='yazıs')
    wdate=models.DateTimeField(auto_now_add=True)
    udate=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='Yazılanlar'
        verbose_name='Yazı'
        verbose_name_plural='Yazılar'
    def __str__(self):
        return self.name

class Commentarticle(models.Model):
    entry=models.ForeignKey(Addermodel,on_delete=models.CASCADE,related_name='comment',null=True,blank=True)
    content=RichTextField(null=True)
    author=models.ForeignKey('customer.CustomerModel',on_delete=models.CASCADE,related_name='comments')
    wdate=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='Commentlər'
        verbose_name='Comment'
        verbose_name_plural='Commentlər'
    def __str__(self):
        return str(self.entry)
        
