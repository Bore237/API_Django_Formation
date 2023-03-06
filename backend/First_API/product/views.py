from .models import Product 

from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from rest_framework import generics, mixins
from api.mixins import StaffEditorPermissionMixin, UserQuerrySetMixin
# Create your views here.

class DetailProductView(generics.RetrieveAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ListCreateProductView(StaffEditorPermissionMixin,
                            UserQuerrySetMixin,
                            generics.ListCreateAPIView
                            ): 
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    user_field = "user"
    #authentication_classes = [authentication.SessionAuthentication,TokenAuthentication]
    #authentication_classes = [authentication.SessionAuthentication]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    #Surcharger le constructeur
    def perform_create(self, serializer): 
        #email = serializer.validated_data.pop('email') 
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None  
        if(content is None): 
            content = name 
        serializer.save(content=content, user = self.request.user)

    # def get_queryset(self, *args, **kwargs):
    #     qs= super().get_queryset(*args, **kwargs)
    #     user= self.request.user
    #     return qs.filter(user = user)
    
class ListProductView(StaffEditorPermissionMixin,
                      UserQuerrySetMixin,
                      generics.ListAPIView): 
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #Surcharger le constructeur
    # def get_queryset(self): 
    #     return super().get_queryset().filter(name__icontains = 'Orange')
     
class UpdateProductView(StaffEditorPermissionMixin,
                        UserQuerrySetMixin,   
                        generics.UpdateAPIView): 

    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):  
        #email = serializer.validated_data.pop('email') 
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None  
        if(content is None): 
            content = name 
        serializer.save(content=content)
        
class DeleteProductView(StaffEditorPermissionMixin,
                        UserQuerrySetMixin, 
                        generics.DestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
        
class ProductMixinsViews(  
        mixins.CreateModelMixin, 
        mixins.UpdateModelMixin, 
        mixins.ListModelMixin, 
        mixins.DestroyModelMixin,  
        mixins.RetrieveModelMixin,
        StaffEditorPermissionMixin,
        UserQuerrySetMixin,   
        generics.GenericAPIView): 

    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer): 
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None  
        if(content is None): 
            content = name 
        serializer.save(content=content, user = self.request.user)
         
    def perform_update(self, serializer): 
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None  
        if(content is None): 
            content = name 
        serializer.save(content=content)
        
    def get(self, request, *args, **kwargs ): 
        pk = kwargs.get('pk')
        if (pk is None): 
            return self.list(request, *args, **kwargs) 
        return self.retrieve(request, *args, **kwargs) 
    
    def post(self, request, *args, **kwargs ): 
        return self.create(request, *args, **kwargs)   

    def delete(self, request, *args, **kwargs ): 
        return self.destroy(request, *args, **kwargs)  
    
    def put(self, request, *args, **kwargs ): 
        return self.update(request, *args, **kwargs)  
    
    def patch(self, request, *args, **kwargs ): 
        return self.partial_update(request, *args, **kwargs) 