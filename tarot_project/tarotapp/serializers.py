# serializers.py
from rest_framework import serializers
from .models import TarotCard

class TarotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarotCard
        fields = ('number', 'name','image_url','meaning')
