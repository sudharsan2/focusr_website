from rest_framework.serializers import ModelSerializer
from .models import enquery,apply

class enquery_serializer(ModelSerializer):
    class Meta:
        model = enquery
        fields = '__all__'

class apply_serializer(ModelSerializer):
    class Meta:
        model = apply
        fields = '__all__'