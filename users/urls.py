from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "users"

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', views.UserLogoutViews.as_view(), name='logout'),
]