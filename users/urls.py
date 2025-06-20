from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, UserViewSet, ClientViewSet, AddressViewSet, PhoneViewSet, login_user, login_client

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'phones', PhoneViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/user/', login_user, name='login_user'),
    path('login/client/', login_client, name='login_client'),
]
