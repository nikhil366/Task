from django.urls import path
from app import views

urlpatterns = [
    path('category/', views.CategoryView.as_view(), name='category'),
    path('item/', views.ItemViewSet.as_view(), name='itemview'),
    path('price/', views.ItemPriceViewSet.as_view(), name='item_price')
    
]