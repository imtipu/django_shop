from django.db import models
from django_extensions.db.models import AutoSlugField

# Create your models here.


class Tags(models.Model):
    tag = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.tag


class Product(models.Model):
    title = models.CharField(max_length=500, null=False, help_text='Product Title')
    slug = AutoSlugField(populate_from=['title'], unique=True)
    description = models.TextField(null=True)
    featured_image = models.ImageField(upload_to='product/featured_images/', null=True)
    tags = models.ManyToManyField(Tags, through='ProductTags', related_name='product_tags', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('title', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductTags(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)



