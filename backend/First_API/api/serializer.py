from rest_framework import serializers
from django.contrib.auth.models import User

#Pour fuit les importation circulaire
class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name = 'product-detail', lookup_field ='pk')
    email = serializers.EmailField(write_only = True) 
    name = serializers.CharField()


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only = True) 
    id = serializers.CharField(read_only = True)
    has_perms = serializers.BooleanField(read_only = True)
    number = serializers.CharField(read_only = True)
    user_product = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        field = {'username', 'id', 'has_perms', 'user_product'}

    def get_user_product(self, obj): 
        #user.product_set_all() relation inverse
        user = obj 
        request = self.context.get('context')
        product = user.product_set.all()[:3]  #limiter le nombre de produit
        return ProductInlineSerializer(product, many=True, context= {'request': request}).data