from rest_framework.serializers import ModelSerializer
from direction.models import UserDirection

class DirectionSerializer(ModelSerializer):
    class Meta:
        model = UserDirection
        fields = '__all__'
