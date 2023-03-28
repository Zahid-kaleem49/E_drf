from.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializers(ModelSerializer):

    class Meta:
        table = User
