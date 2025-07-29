from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Stats
from .serializers import StatsSerializer, UserSerializer

# view class are called from urls.py
# note to myself: once backend is done, in the frontend I to write code to pass the necessary parameters
# for example, if I'm at /register then you need to pass username and password (from the serializer.py reference)

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

class StatsListCreateView(generics.ListCreateAPIView):
    serializer_class = StatsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Stats.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StatsUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = StatsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Stats.objects.filter(user=self.request.user)