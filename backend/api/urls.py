from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile/', views.getUserProfile, name='users-profile'),
    path('users/', views.getUserProfile, name='users-profiles'),
    path('users/register/', views.registerUser, name='register'),
    path('products/', views.getProducts, name="products"),
    path('products/<str:pk>', views.getProduct, name="products"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
                                        document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, 
                                       document_root=settings.MEDIA_ROOT)