from rest_framework import serializers
from apiv1.models import Locations, Departments, Categories, SubCategories, SKUdata


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ['id', 'location_name', 'location_desc', 'departments']
        depth = 3


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id', 'department_name', 'categories']
        depth = 3


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'category_name', 'subcategories']
        depth = 3


class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = ['id', 'subcategory_name']


class CustomSKUFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKUdata
        fields = ('location_name', 'dept_name', 'cat_name', 'subcat_name')
