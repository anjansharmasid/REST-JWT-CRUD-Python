from django.urls import path, include

# rest_framework_simplejwt.views framework  provides TokenObtainPairView, TokenRefreshView
# to create token pair and manage them.
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CustomerView
from . import  views

# rest_framework provider routers CRUD url for application out of the box.
# no need to create separate view for CRUD url when using routers.
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customers',views.CustomerView)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view())

]