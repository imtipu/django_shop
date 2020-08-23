from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(HomePageBannerSlider)
class HomePageBannerSliderAdmin(admin.ModelAdmin):
    list_display = ['get_heading', 'filename', 'is_published']
    list_editable = ['is_published']

    def get_heading(self, instance):
        if not instance.heading:
            return 'No Heading'
        else:
            return '%s' % instance.heading

    get_heading.short_description = 'Heading'


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'is_published', 'created', 'updated']
    list_editable = ['is_published']


class ProductTagsAdminInline(admin.StackedInline):
    model = ProductTags
    # filter_horizontal = ['tags']
    extra = 1


# class ProductVariantValuesAdminInline(admin.StackedInline):
#     model = ProductVariantValue
#     # filter_horizontal = ['tags']
#     extra = 1


class ProductVariantsAdminInline(admin.TabularInline):
    model = ProductVariant
    # filter_horizontal = ['tags']
    extra = 1


class ProductImagessAdminInline(admin.TabularInline):
    model = ProductImage
    # filter_horizontal = ['tags']
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'updated']
    # filter_horizontal = ('tags',)
    inlines = [ProductVariantsAdminInline, ProductImagessAdminInline, ProductTagsAdminInline]
    # list_editable = ['tags']

    def queryset(self, request):
        return super(ProductAdmin, self).queryset(request).prefetch_related('product_variants')


@admin.register(ProductVariant)
class ProductVariantsAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'option', 'value', 'created', 'updated']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']


@admin.register(ProductImage)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
