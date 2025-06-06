from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, UserViewSet, ClientViewSet, AddressViewSet, PhoneViewSet, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'phones', PhoneViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
    # Login and token generation
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
