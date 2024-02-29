from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import (
    ProductAccessView,
    LessonListView,
    ProductStatisticsView,
    ProductViewSet,
    LessonViewSet,
    GroupViewSet
)

router = DefaultRouter()
router.register(r'сreation-products', ProductViewSet)
router.register(r'сreation-lessons', LessonViewSet)
router.register(r'сreation-groups', GroupViewSet)

urlpatterns = [
    path('product/access/', ProductAccessView.as_view(), name='product-access'),
    path('products/', ProductStatisticsView.as_view(), name='product-list'),
    path('products/<int:product_id>/lessons/', LessonListView.as_view(), name='lesson-list'),


    path('', include(router.urls)),
]
