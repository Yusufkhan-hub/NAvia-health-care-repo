from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from ..models import primary_model


class test_serializer(ModelSerializer):
    
    class Meta:
        model = primary_model
        fields = "__all__"

