from rest_framework import serializers

from models import Readers

class ReaderSerializer(serializers.HyperlinkedModelSerializer):
    #source = LuSourceSerializer()
    class Meta:
        model = Readers
        fields = ('reader_id','name', 'description','user_id')
    #def create(self, validated_data):
     #   return Roosts.objects.using('purple').create(**validated_data)
