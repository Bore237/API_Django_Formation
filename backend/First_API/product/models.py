from django.db import models
from django.db.models import Q
#Pour avoir les informations de utilisateur
from django.conf import settings 
#from django.contrib.auth.models import User

# Create your models here.
User = settings.AUTH_USER_MODEL

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True) 
    
    def search(self, query, user=None):
        #Permet de gerer les condition or
        lookup = Q(name__icontains=query) | Q(content__icontains=query) 
        qs = self.filter(lookup)
        if user is not None:
            #filtre les user et apres lookup
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct() #Evite les doublons
        return qs

class ProductManager(models.Manager): 
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None): 
        return self.get_queryset().is_public().search(query, user)

class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) #si on suprime un product le personne reste et est  null
    name = models.CharField(max_length=100, unique = True) 
    content = models.TextField(blank =True)
    price = models.DecimalField(max_digits = 15, decimal_places=2)
    public = models.BooleanField(default = True)
    
    objects = ProductManager()

    @property
    def get_discount(self):
        return "%.2f"%(float(self.price) * 0.5)
    
    def __str__(self):
        return self.name