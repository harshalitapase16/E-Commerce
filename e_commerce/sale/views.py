from django.shortcuts import render, redirect
from django.views import View
from .models import *

# Create your views here.
class CategoryView(View):
 def get(self, request):
  category_obj = CategoryModel.objects.all()
  return render(request, 'sale/category.html',{'cat_obj':category_obj})
 
 def post(self, request):
  category_name = request.POST.get('categoryname')
  cat_description = request.POST.get('description')

  if not cat_description:
        cat_description = "No description"

  CategoryModel.objects.create(category_name=category_name,
                               cat_description=cat_description)
  return redirect('/')
 
class DeleteCategoryView(View):
 def get(self, request):
  return render(request, 'sale/category.html')

 def post(self, request, id=None):
  category_obj = CategoryModel.objects.get(id=id)
  category_obj.delete()
  return redirect('/')
 
class UpdateCategoryView(View):
  def get(self, request, id=None):
    category_obj   = CategoryModel.objects.get(id=id) 
    return render(request, 'sale/updatecategory.html',{'cat_obj':category_obj})
  
  def post(self, request, id=None):
    category_name = request.POST.get('categoryname')
    cat_description = request.POST.get('description')

    category_obj = CategoryModel.objects.get(id=id)
    category_obj.category_name = category_name
    category_obj.cat_description = cat_description
    category_obj.save()
    return redirect('/')
   

class SubCategoryView(View):
 def get(self, request, id=None):
  category_obj = CategoryModel.objects.get(id=id)
  subcategory_obj = SubCategoryModel.objects.filter(category=category_obj)
  return render(request, 'sale/sub-category.html',{'subcat_obj':subcategory_obj, 'cat_obj':category_obj})
 
 def post(self, request, id=None):
  sub_category_name = request.POST.get('subcategoryname')
  sub_cat_description = request.POST.get('subdescription')

  if not sub_cat_description:
        sub_cat_description = "No description"

  category_obj = CategoryModel.objects.get(id=id)
  SubCategoryModel.objects.create(category=category_obj, sub_category_name=sub_category_name,
                                              sub_cat_description=sub_cat_description)
  return redirect(f'/sub_category/{id}')
 
class DeleteSubCategoryView(View):
    def get(self, request, id=None):
        return render(request, 'sale/sub-category.html')

    def post(self, request, id=None):
            sub_category_obj = SubCategoryModel.objects.get(id=id)
            sub_category_obj.delete()
            return redirect(f'/sub_category/{sub_category_obj.category.id}')
    

class UpdateSub_CategoryView(View):
  def get(self, request, id=None):
    sub_category_obj  = SubCategoryModel.objects.get(id=id) 
    return render(request, 'sale/updatesubcategory.html',{'sub_cat_obj':sub_category_obj})
  
  def post(self, request, id=None):
    sub_category_name = request.POST.get('subcategoryname')
    sub_cat_description = request.POST.get('subdescription')
  
    sub_category_obj = SubCategoryModel.objects.get(id=id)
    print(sub_category_obj)
    sub_category_obj.sub_category_name = sub_category_name
    sub_category_obj.sub_cat_description = sub_cat_description
    sub_category_obj.save()
    return redirect(f'/sub_category/{sub_category_obj.category.id}')
  

class ProductView(View):
    def get(self, request, id=None):
        sub_category_obj = SubCategoryModel.objects.get(id=id)
        product_obj = ProductModel.objects.filter(sub_category=sub_category_obj).prefetch_related('images')
        return render(request, 'sale/product.html', {'sub_cat_obj': sub_category_obj, 'product_obj': product_obj})
  
    def post(self, request, id=None):
        product_name = request.POST.get('product')
        product_description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image_files = request.FILES.getlist('images')  # Use getlist to handle multiple files
        sub_cat_obj = SubCategoryModel.objects.get(id=id)
        category_obj = sub_cat_obj.category

        # Create product without images first
        product = ProductModel.objects.create(
            sub_category=sub_cat_obj,
            category=category_obj,
            product_name=product_name,
            product_description=product_description,
            price=price,
            stock_quantity=stock
        )

        # Create ProductImage instances and associate them with the product
        product_images = []
        for img in image_files:
            product_image = ProductImage.objects.create(image=img)
            product_images.append(product_image)

        # Set the product's images to the newly created ProductImage instances
        product.images.set(product_images)

        return redirect(f'/product/{id}')


class DeleteProductView(View):
    def get(self, request, id=None):
        return render(request, 'sale/product.html')

    def post(self, request, id=None):
            product_obj = ProductModel.objects.get(id=id)
            print(product_obj)
            product_obj.delete()
            return redirect(f'/product/{product_obj.sub_category.id}')

class UpdateProductView(View):
  def get(self, request, id=None):
    product_obj  = ProductModel.objects.get(id=id) 
    return render(request, 'sale/updateproduct.html',{'product_obj':product_obj})
  
  def post(self, request, id=None):
    product = request.POST.get('product')
    description = request.POST.get('decription')
    stock = request.POST.get('stock')
    price = request.POST.get('price')

    product_obj = ProductModel.objects.get(id=id)
    product_obj.product_name = product
    product_obj.product_description = description
    product_obj.price = price
    product_obj.stock_quantity = stock

    product_obj.save()
    print(product_obj.sub_category.id)
    return redirect(f'/product/{product_obj.sub_category.id}')
  
