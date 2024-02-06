from rest_framework.serializers import ModelSerializer
from .models import enquery

class enquery_serializer(ModelSerializer):
    class Meta:
        model = enquery
        fields = '__all__'