from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
urlpatterns = [path('signup/',SignUp.as_view(),name='signup'),
                path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
                path('user/',UserView.as_view()),
                path('password/',UserPasswordChangeView.as_view(),name='password_change_view')]