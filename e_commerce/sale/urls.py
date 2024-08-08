from django.urls import path
from .views import *
urlpatterns = [
 
    # Category 
    path('',CategoryView.as_view(), name='category'),
    path('delete_category/<int:id>/',DeleteCategoryView.as_view(), name="del_category"),
    path('update_category/<int:id>/',UpdateCategoryView.as_view(), name="update_category"),


    # Sub Category 
    path('sub_category/<int:id>/', SubCategoryView.as_view(), name='sub_category'),
    path('del_sub_category/<int:id>/', DeleteSubCategoryView.as_view(), name='del_sub_category'),
    path('update_sub_category/<int:id>/', UpdateSub_CategoryView.as_view(), name='update_sub_category'),

    # Product
    path('product/<int:id>/', ProductView.as_view(), name='product'),
    path('deleteproduct/<int:id>/', DeleteProductView.as_view(), name='deleteproduct'),
    path('updateproduct/<int:id>/', UpdateProductView.as_view(), name='updateproduct'),


] 
