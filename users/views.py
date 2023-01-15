from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import User
from users.models import Profile
from users.serializers import UserSerializer
from users.serializers import CustomObtainPairSerializer
from users.serializers import LogoutSerializer
from users.serializers import UserProfileSerializers
from users.utils import Util

# Create your views here.
class UserView(APIView):
    # signup
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=request.data["email"])
            Util.email_authentication_send(user)
            return Response({"message": "회원가입 완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer
    
class UserLogoutViews(APIView):
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "로그아웃 완료"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProfileView(APIView):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer_user = UserProfileSerializers(profile)
        return Response(serializer_user.data, status=status.HTTP_201_CREATED)
    
    def post(self, request):
        serializer = UserProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = UserProfileSerializers(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

