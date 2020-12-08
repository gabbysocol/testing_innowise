from rest_framework import serializers

from .models import Employee


class ArticleSerializer(serializers.Serializer):
    """
    Class for formating data for CRUD.

    """
    
    company_id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=120)
    last_name = serializers.CharField()
    speciality = serializers.CharField()

    def create(self, validated_data):

        return Employee.objects.create(**validated_data)


    def update(self, instance, validated_data):

        instance.company_id = validated_data.get('company_id', instance.company_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.speciality = validated_data.get('speciality', instance.speciality)
        instance.save()
        return instance