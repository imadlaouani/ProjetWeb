from django.conf.urls import url
from . import views 
app_name = 'comptes'

urlpatterns = [
	url(r'^inscription/$',views.inscription, name ='inscription'),
	url(r'^connexion/$',views.connexion, name ='connexion'),
	url(r'^deconnexion/$',views.logout_user, name ='deconnexion'),

	
]