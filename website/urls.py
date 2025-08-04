from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('a-propos/', views.AProposView.as_view(), name='a-propos'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('communaute/', views.CommunauteView.as_view(), name='communaute'),
    path('confirmation/', views.ConfirmationView.as_view(), name='confirmation'),
    path('consulting/', views.ConsultingView.as_view(), name='consulting'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('coworking/', views.CoworkingView.as_view(), name='coworking'),
    path('offres/', views.OffresView.as_view(), name='offres'),
    path('suite/', views.SuiteView.as_view(), name='suite'),
]
