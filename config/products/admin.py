from django.contrib import admin

from products.models import Product, Lesson, Group

admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(Group)