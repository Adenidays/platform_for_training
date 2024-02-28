from django.urls import path

from products.views import ProductAccessView, ProductListView, LessonListView

urlpatterns = [
    path('product/access/', ProductAccessView.as_view(), name='product-access'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:product_id>/lessons/', LessonListView.as_view(), name='lesson-list')

]
