from django.urls import path
from .views import PublicView, PrivateView, RegisterView,RegisterWebView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('public/', PublicView.as_view(), name='public-view'),
    path('private/', PrivateView.as_view(), name='private-view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('register/', RegisterWebView.as_view(), name='register-web'),
    ]