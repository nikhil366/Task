from django.urls import path
from app import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('items/', views.ItemViewSet.as_view(), name='itemview'),
    path('price/', views.ItemPriceViewSet.as_view(), name='item_price')
    
]