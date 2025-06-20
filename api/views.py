from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .tasks import send_welcome_email
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .forms import UserRegistrationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
# Create your views here.

class PublicView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "This is a public view accessible to everyone."})
    

class PrivateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}! This is a private view."})
    
    def post(self, request):
        data = request.data
        return Response({"message": "Data received", "data": data})
    

from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]  # <-- Set here, at the class level

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        # ...existing validation...
        user = User.objects.create_user(username=username, password=password, email=email)
        refresh = RefreshToken.for_user(user)
        # Call the Celery task
        send_welcome_email.delay(username, email)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': 'User registered successfully.'
        }, status=status.HTTP_201_CREATED)
    

class RegisterWebView(FormView):
    template_name = 'registration/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        # Call the Celery task
        send_welcome_email.delay(user.username, user.email)
        return super().form_valid(form)
