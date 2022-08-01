"""Views for the prispevok APIs"""
import requests
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Prispevok
from prispevok import serializers


class PrispevokViewSet(viewsets.ModelViewSet):
    """View for managing prispevok APIs."""
    serializer_class = serializers.PrispevokDetailSerializer
    queryset = Prispevok.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve prispevok for authenticated user"""
        uid = self.request.user.user_id
        response = self.queryset.filter(user=self.request.user).filter(
            userId=uid).order_by('-id')
        if response:
            return response
        else:
            url = f'https://jsonplaceholder.typicode.com/posts/?userId={uid}'
            r = requests.get(url, headers={'Content-Type': 'application/json'})
            prispevky = r.json()
            for prispevok in prispevky:
                Prispevok.objects.create(user=self.request.user, **prispevok)
            return prispevky

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.PrispevokSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create new prispevok"""
        serializer.save(user=self.request.user)
