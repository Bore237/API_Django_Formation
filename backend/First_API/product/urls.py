from django.urls import path
from .views import DetailProductView, ListCreateProductView, \
                    UpdateProductView, DeleteProductView, ListProductView, \
                    ProductMixinsViews    
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    # path('<int:pk>/', DetailProductView.as_view()),
    # path('create/', CreateProductView.as_view()), 
    # path('list/', ListProductView.as_view()),
    # path('<int:pk>/update/', UpdateProductView.as_view()),
    # path('<int:pk>/delete/', DeleteProductView.as_view()), 
    path('auth', obtain_auth_token),
    path('createlist/', ListCreateProductView.as_view()), 
    path('<int:pk>/detail', ProductMixinsViews.as_view(), name="product-detail"),
    path('create/', ProductMixinsViews.as_view()), 
    path('list/', ProductMixinsViews.as_view()),
    path('<int:pk>/update/', ProductMixinsViews.as_view()),
    path('<int:pk>/delete/', ProductMixinsViews.as_view()),
]