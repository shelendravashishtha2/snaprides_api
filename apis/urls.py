
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
app_name = 'api'
router.register('user', UserView, basename='UserAPI')

urlpatterns = [
    path('user/', CustomAuthToken.as_view(), name="tokenView"),
    path('api/', include(router.urls)),
    path('api/<int:pk>/', include(router.urls)),
    path('api/<str:pk>/', include(router.urls)),
    path('api/<slug:pk>/', include(router.urls)),
]