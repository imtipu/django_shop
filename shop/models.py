import os

from django.db import models
from django_extensions.db.models import AutoSlugField


# Create your models here.
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class HomePageBannerSlider(models.Model):
    # image = models.ImageField(upload_to='homepage/slider/', null=False, default=None)
    image = ProcessedImageField(upload_to='homepage/slider/',
                                format='WEBP',
                                processors=[ResizeToFill(1600, 600)],
                                null=False,
                                default=None)
    heading = models.CharField(max_length=120, null=True, blank=True)
    sub_heading = models.CharField(max_length=250, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        str_text = self.heading
        if not self.heading:
            str_text = self.filename

        return '%s' % str_text

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Homepage Slider'
        verbose_name_plural = 'Homepage Sliders'


class ProductCategory(models.Model):
    title = models.CharField(max_length=120, null=False)
    slug = AutoSlugField(populate_from='title', null=False)
    image = models.ImageField(upload_to='category/', null=True, blank=True, default=None)
    is_published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title

    def __unicode__(self):
        return '%s' % self.slug

    class Meta:
        ordering = ('title',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tags(models.Model):
    tag = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s' % self.tag


class Product(models.Model):
    WEIGHT_UNITS_CHOICES = (
        ('kg', 'kg'),
        ('gm', 'gm'),
        ('lb', 'lb'),
    )

    LENGTH_UNITS_CHOICES = (
        ('in', 'in'),
        ('cm', 'cm'),
        ('m', 'm'),
        ('ft', 'ft'),
    )

    title = models.CharField(max_length=500, null=False, help_text='Product Title')
    slug = AutoSlugField(populate_from=['title'], unique=True)
    description = models.TextField(null=True)
    featured_image = models.ImageField(upload_to='product/featured_images/', null=True)
    # tags = models.ManyToManyField(Tags, through='ProductTags', related_name='product_tags', blank=True)

    is_published = models.BooleanField(default=False)

    category = models.ForeignKey('shop.ProductCategory',
                                 on_delete=models.CASCADE,
                                 related_name='product_category', null=True)

    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False)
    compare_at_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False)
    height = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False)
    width = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False)
    length = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False)
    weight = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False)
    length_unit = models.CharField(choices=LENGTH_UNITS_CHOICES, max_length=4, default='cm', )
    weight_unit = models.CharField(choices=WEIGHT_UNITS_CHOICES, max_length=4, default='kg', )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # variants = models.ManyToManyField('shop.ProductVariant', related_name='product_variants')
    # product_images = models.ManyToManyField('shop.ProductImage', related_name='product_images')

    def __str__(self):
        return '%s' % self.title

    def __unicode__(self):
        return '%s' % self.slug

    class Meta:
        ordering = ('title',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductVariant(models.Model):
    # label = models.CharField(max_length=32, blank=True)
    # variant_options = models.ManyToManyField('shop.ProductVariantOption',)

    WEIGHT_UNITS_CHOICES = (
        ('kg', 'kg'),
        ('gm', 'gm'),
        ('lb', 'lb'),
    )

    LENGTH_UNITS_CHOICES = (
        ('in', 'in'),
        ('cm', 'cm'),
        ('m', 'm'),
        ('ft', 'ft'),
    )

    product = models.ForeignKey('shop.Product',
                                default=None,
                                on_delete=models.CASCADE,
                                related_name='product_variants',
                                null=False)

    option = models.CharField(max_length=32, blank=True)
    value = models.CharField(max_length=32, blank=True)

    image = models.ImageField(upload_to='products/variants/', default=None, null=True, blank=True)

    # values = models.ManyToManyField('shop.ProductVariantValue')

    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False)
    compare_at_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False)
    height = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False)
    width = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False)
    length = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False)
    weight = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False)
    length_unit = models.CharField(choices=LENGTH_UNITS_CHOICES, max_length=4, default='cm', )
    weight_unit = models.CharField(choices=WEIGHT_UNITS_CHOICES, max_length=4, default='kg', )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def height_with_unit(self):
        return '{} {}'.format(self.height, self.length_unit)

    @property
    def length_with_unit(self):
        return '{} {}'.format(self.length, self.length_unit)

    @property
    def width_with_unit(self):
        return '{} {}'.format(self.width, self.length_unit)

    @property
    def weight_with_unit(self):
        return '{} {}'.format(self.weight, self.weight_unit)


class ProductImage(models.Model):
    product = models.ForeignKey('shop.Product',
                                default=None,
                                on_delete=models.CASCADE,
                                related_name='product_images',
                                null=False)
    image = models.ImageField(unique='products/variants/', default=None, null=False)


# class ProductVariantOption(models.Model):
#     # product = models.ForeignKey('shop.Product',
#     #                             default=None,
#     #                             on_delete=models.CASCADE,
#     #                             null=False)
#     #
#     varaint = models.ForeignKey('shop.ProductVariant',
#                                 default=None,
#                                 on_delete=models.CASCADE,
#                                 null=False)
#
#     values = models.ManyToManyField('shop.ProductVariantValue')
#
#
# class ProductVariantValue(models.Model):
#     # product = models.ForeignKey('shop.Product',
#     #                             default=None,
#     #                             on_delete=models.CASCADE,
#     #                             null=False)
#     # variant = models.ForeignKey('shop.ProductVariant',
#     #                             default=None,
#     #                             on_delete=models.CASCADE,
#     #                             related_name='variant_values')
#
#     value = models.CharField(max_length=255)


class ProductTags(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags', )
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.tag


class City(models.Model):
    name = models.CharField(unique=True, max_length=50, help_text='City Name')


class State(models.Model):
    name = models.CharField(unique=True, max_length=50, help_text='State Name')

# class Country(models.Model):
#     name = models.CharField(unique=True, max_length=50, help_text='Country Name')
