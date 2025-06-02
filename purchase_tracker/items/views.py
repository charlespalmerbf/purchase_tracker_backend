# items/views.py

from rest_framework import viewsets, permissions
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show items belonging to the logged-in user
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate item with the logged-in user
        serializer.save(user=self.request.user)
