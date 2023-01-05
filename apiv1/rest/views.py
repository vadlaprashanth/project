from rest_framework import viewsets
from apiv1.models import Locations, Departments, Categories, SubCategories, SKUdata
from rest_framework.response import Response
from .serializer import LocationsSerializer, DepartmentsSerializer, CategoriesSerializer, SubCategoriesSerializer, \
    CustomSKUFilterSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationsSerializer

    def get_queryset(self):
        location = Locations.objects.all()
        return location

    @action(detail=True, methods=["GET"], url_path='departments')
    def locations(self, request, pk=True):
        location = Locations.objects.filter(id=pk)
        serializer = LocationsSerializer(location, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], url_path='departments/(?P<dept_pk>[^/.]+)')
    def departments(self, request, dept_pk, pk=None):
        department = Departments.objects.filter(id=dept_pk)
        serializer = DepartmentsSerializer(department, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], url_path='departments/(?P<dept_pk>[^/.]+)/category')
    def categories(self, request, dept_pk, pk=None):
        department = Departments.objects.filter(id=dept_pk)
        serializer = DepartmentsSerializer(department, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], url_path='departments/(?P<dept_pk>[^/.]+)/category/(?P<cat_pk>[^/.]+)')
    def get_categories(self, request, dept_pk, cat_pk, pk=None):
        category = Categories.objects.filter(id=cat_pk)
        serializer = CategoriesSerializer(category, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], url_path='departments/(?P<dept_pk>[^/.]+)/category/(?P<cat_pk>['
                                                   '^/.]+)/subcategory')
    def subcategories(self, request, dept_pk, cat_pk, pk=None):
        category = Categories.objects.filter(id=cat_pk)
        serializer = CategoriesSerializer(category, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], url_path='departments/(?P<dept_pk>[^/.]+)/category/(?P<cat_pk>['
                                                   '^/.]+)/subcategory/(?P<sub_pk>[^/.]+)')
    def get_subcategories(self, request, dept_pk, cat_pk, sub_pk, pk=None):
        subcategory = SubCategories.objects.filter(id=sub_pk)
        serializer = SubCategoriesSerializer(subcategory, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        new_location = Locations.objects.create(location_name=data['location_name'],
                                                location_desc=data['location_desc'])
        new_location.save()

        for department in data["departments"]:
            department_obj = Departments.objects.get(department_name=department["department_name"])
            new_location.departments.add(department_obj)

            serializer = LocationsSerializer(new_location)
            return Response(serializer.data)

    def delete(self, request, id):
        obj = Locations.objects.get(id=id)
        obj.delete()


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentsSerializer

    def get_queryset(self):
        department = Departments.objects.all()
        return department


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        category = Categories.objects.all()
        return category


class SubCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SubCategoriesSerializer

    def get_queryset(self):
        subcategory = SubCategories.objects.all()
        return subcategory


class CustomSKUFilterApiView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = SKUdata.objects.all()

        # Custom Filters Parameters
        check_locations = self.request.query_params.get('check_locations', None)
        check_depts = self.request.query_params.get('check_depts', None)
        check_cats = self.request.query_params.get('check_cats', None)
        check_subcats = self.request.query_params.get('check_subcats', None)

        if check_locations:
            queryset = queryset.filter(location_name=check_locations)

        if check_depts:
            queryset = queryset.filter(dept_name=check_depts)

        if check_cats:
            queryset = queryset.filter(cat_name=check_cats)

        if check_subcats:
            queryset = queryset.filter(subcat_name=check_subcats)

        serializer = CustomSKUFilterSerializer(queryset, many=True)

        return Response(serializer.data)
