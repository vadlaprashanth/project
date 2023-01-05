from django.urls import re_path, include
from .views import LocationViewSet, DepartmentViewSet, CategoryViewSet, SubCategoryViewSet, CustomSKUFilterApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("department", DepartmentViewSet, basename='department')
router.register("location", LocationViewSet, basename='location')
router.register("category", CategoryViewSet, basename='category')
router.register("subcategory", SubCategoryViewSet, basename='subcategory')
# router.register('skudata', CustomSKUFilterApiView, basename='skudata')

urlpatterns = [
    re_path('', include(router.urls)),
    # re_path('skudata', views.CustomSKUFilterApiView.as_view())
]
