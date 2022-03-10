from django.urls import path
from . import views
from .views import MyTokenObtainPairView, getNotes,getRoutes

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', getRoutes.as_view(), name='getRoutes'),
    path('notes/', getNotes.as_view(), name='getNotes'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
