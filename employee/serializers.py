from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    """
    Class for formating data.

    """
    
    first_name = serializers.CharField(max_length=120)
    last_name = serializers.CharField()
    speciality = serializers.CharField()