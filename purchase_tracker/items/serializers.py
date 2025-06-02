# items/serializers.py

from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    cost_per_day = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['id', 'name', 'image', 'price', 'purchase_date', 'cost_per_day', 'user']
        read_only_fields = ['user', 'cost_per_day']

    def get_cost_per_day(self, obj):
        return round(obj.cost_per_day(), 2)
