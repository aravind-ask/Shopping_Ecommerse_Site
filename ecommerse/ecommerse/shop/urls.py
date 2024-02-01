from . import views
from django.urls import path

app_name= 'shop'

urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetail,name='prodCatdetail'),
    #path('product/create/',views.ProductCreateView.as_view(template_name='product/create.html'),name='add_product'),
]