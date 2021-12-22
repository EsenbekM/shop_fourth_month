from django.contrib import admin
from .models import Category, Product, Review, Tag


# class ReviewInline(admin.StackedInline):
#     model = Review
#     extra = 1


# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ReviewInline]
#     search_fields = ['title', 'text']
#     list_display = 'title id price category'.split()
#     list_editable = 'category price'.split()
#     list_filter = 'tags category'.split()


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Tag)