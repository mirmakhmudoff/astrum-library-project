from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from library.models.user import User
from library.serializers.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return [IsAuthenticated()]
