from django.db import models


# Create your models here.
class SubCategories(models.Model):
    subcategory_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subcategory_name


class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    subcategories = models.ManyToManyField(SubCategories)

    def __str__(self):
        return self.category_name


class Departments(models.Model):
    department_name = models.CharField(max_length=50)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.department_name


class Locations(models.Model):
    location_name = models.CharField(max_length=50)
    location_desc = models.CharField(max_length=50, null=True)
    departments = models.ManyToManyField(Departments)

    def __str__(self):
        return self.location_name


class SKUdata(models.Model):
    sku_name = models.CharField(max_length=50)
    location_name = models.CharField(max_length=50)
    dept_name = models.CharField(max_length=50)
    cat_name = models.CharField(max_length=50)
    subcat_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sku_name
