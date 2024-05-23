from rest_framework import serializers


class TextSerializer(serializers.Serializer):
    text = serializers.CharField()


class ReplaceHashtagsSerializer(serializers.Serializer):
    text = serializers.CharField()
    replacement = serializers.CharField()
