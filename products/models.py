from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self',verbose_name='parent',blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField('title',max_length=255)
    description = models.TextField('description',blank=True)
    avatar = models.ImageField('avatar',blank=True,upload_to='creat')
    is_enable = models.BooleanField('is_enable',default=True)
    date_time = models.DateTimeField('date_time',auto_now_add=True)
    updated_time = models.DateTimeField('update_time',auto_now=True)
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

class Product(models.Model):
        title = models.CharField('title',max_length=255)
        description = models.TextField('description',blank=True)
        avatar = models.ImageField('avatar',blank=True,upload_to='creat')
        is_enable = models.BooleanField('is_enable',default=True)
        categories = models.ManyToManyField('Category',verbose_name='Category',blank=True)
        date_time = models.DateTimeField('date_time',auto_now_add=True)
        updated_time = models.DateTimeField('update_time',auto_now=True)
    
        class Meta:
            db_table = 'products'
            verbose_name = 'product'
            verbose_name_plural = 'products'

class File(models.Model):
        Product = models.ForeignKey('Product',verbose_name='Product',on_delete=models.CASCADE)
        title = models.CharField('title',max_length=255)
        file = models.FileField('file',upload_to='files/%Y/%m/%d/')
        is_enable = models.BooleanField('is_enable',default=True)
        date_time = models.DateTimeField('date_time',auto_now_add=True)
        updated_time = models.DateTimeField('update_time',auto_now=True)
    
        class Meta:
            db_table = 'files'
            verbose_name = 'file'
            verbose_name_plural = 'files'