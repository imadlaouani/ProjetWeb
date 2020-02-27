from django.urls import path,include
from django.conf import settings
from annonces import views
from django.conf.urls import url,include


urlpatterns = [
    #url(r'^$', views.liste_annonces),
    url(r'^ajouter/$', views.ajouter_annonce,name="ajouter_annonce"),
    
    
   ]