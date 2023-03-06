from rest_framework.routers import DefaultRouter 
from product.viewset import ProductViewset, ProductListRetrieve

router = DefaultRouter() 

router.register('product-b', ProductListRetrieve, basename='product-a')


print (router.urls)
urlpatterns = router.urls