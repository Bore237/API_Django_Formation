from rest_framework import serializers  
from rest_framework.reverse import reverse

from api.serializer import UserPublicSerializer
from .models import Product 
from .validators import validate_product_name


# class UserProductInlineSerializer(serializers.Serializer):
#     url = serializers.HyperlinkedIdentityField(view_name = 'product-detail', many=True, lookup_field ='pk')
#     email = serializers.EmailField(write_only = True) 
#     name = serializers.CharField()

class ProductSerializer(serializers.ModelSerializer):  
    #Affichier le title dans le dictionaire
    #Lorque un utilise une serializer method fiel il faut créer sa une méthode pour lui
    #permet de:
    my_discount = serializers.SerializerMethodField(read_only =True) 
    #owner = UserProductInlineSerializer(source="user.product_set.all",many=True, read_only = True)
    #owner = UserPublicSerializer(source="user", read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name = 'product-detail', lookup_field ='pk')
    email = serializers.EmailField(write_only = True) #Informe  que cechamps n'appartient pas a la base de données
    name = serializers.CharField(validators = [validate_product_name])
    user_name = serializers.CharField(source="user.username", read_only = True)
    #owner = serializers.SerializerMethodField(read_only = True)
    class Meta :
        model = Product
        fields = ('user_name', 'email', 'url', 'pk', 'name', 'content', 'price', 'my_discount', 'public')
    
    #Vilidation des champs (validate_nom)
    # def validate_name(self, value):
    #     qs = Product.objects.filter(name__iexact = value) 
    #     if qs.exists(): 
    #         raise serializers.ValidationError(f"Le produit {value} exict deja")
    #     return value
    
    
    def create(self, validated_data): 
        print(validated_data)
        email = validated_data.pop('email') 
        print(email)
        print(validated_data)
        #return Product.objects.create(**validated_data)
        obj = super().create(validated_data)
        return obj
    
    def update(self,instance, validated_data): 
        print(validated_data)
        email = validated_data.pop('email') 
        print(email)
        print(validated_data)
        #return Product.objects.create(**validated_data)
        obj = super().update(instance, validated_data)
        return obj
    #marche sur les objects
    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None: 
    #         return None
    #     return reverse("product-detail", kwargs= {'pk': obj.pk}, request = request)
    #     #return f"/product/{obj.pk}/detail"
    
    # def get_owner(self, obj): 
    #     return {'username': obj.user.username, 'id':obj.user.pk}


    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):  
            return None 
        if not isinstance(obj, Product):
            return None
        return obj.get_discount