from django.urls import path
from . import views
urlpatterns = [
    path('', views.ShowAllProducts, name='allProducts'),
    path('productDetail/<int:id>', views.productDetail, name='productDetail'),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('updateProduct/<int:id>', views.updateProduct, name="updateProduct"),
    path('deleteProduct/<int:id>', views.deleteProduct, name="deleteProduct"),
    path('searchProduct/', views.searchProduct, name="searchProduct"),
]
