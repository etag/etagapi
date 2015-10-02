from rest_framework import serializers

from models import Readers,ReaderLocation, Animal, Tags,TagReads

class ReaderSerializer(serializers.HyperlinkedModelSerializer):
    #source = LuSourceSerializer()
    class Meta:
        model = Readers
        fields = ('url','reader_id','name', 'description','user_id')
    #def create(self, validated_data):
     #   return Roosts.objects.using('purple').create(**validated_data)

class ReaderLocationSerializer(serializers.HyperlinkedModelSerializer):
    #source = LuSourceSerializer()
    class Meta:
        model = ReaderLocation
        fields = ('url','latitude','longitude', 'start_date','end_date','active')
    #def create(self, validated_data):
     #   return Roosts.objects.using('purple').create(**validated_data)

class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    #source = LuSourceSerializer()
    class Meta:
        model = Animal
        fields = ('url','field_data',)
    #def create(self, validated_data):
     #   return Roosts.objects.using('purple').create(**validated_data)
class TagsSerializer(serializers.HyperlinkedModelSerializer):
    animal = AnimalSerializer()
    class Meta:
        model = Tags
        fields = ('url','tag_id','start_date', 'end_date',)
    #def create(self, validated_data):
     #   return Roosts.objects.using('purple').create(**validated_data)

class TagReadsSerializer(serializers.HyperlinkedModelSerializer):
    #source = LuSourceSerializer()
    class Meta:
        model = TagReads
        fields = ('url','reader_id','tag_id', 'timestamp',)
    #def create(self, validated_data):
     #   return Roosts.objects.using('purple').create(**validated_data)
