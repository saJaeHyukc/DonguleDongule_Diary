from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

app_name = "users"

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('profile/', views.ProfileView.as_view(), name="profile_view"),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', views.UserLogoutViews.as_view(), name='logout'),
    path("api/auth/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path('kakao/login/', views.kakao_login, name='kakao_login'),
    path('kakao/callback/', views.kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),
]