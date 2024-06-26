from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextSerializer, ReplaceHashtagsSerializer
from .hashtags_functionality import remove_hashtags, get_hashtags, replace_hashtags, count_hashtags
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RemoveHashtagsView(APIView):
    @swagger_auto_schema(request_body=TextSerializer, responses={200: openapi.Response('Success', TextSerializer)})
    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            cleaned_text = remove_hashtags(text)
            return Response({'cleaned_text': cleaned_text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetHashtagsView(APIView):
    @swagger_auto_schema(request_body=TextSerializer, responses={200: openapi.Response('Success', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'hashtags': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))
        }
    ))})
    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            hashtags = get_hashtags(text)
            return Response({'hashtags': hashtags}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplaceHashtagsView(APIView):
    @swagger_auto_schema(request_body=ReplaceHashtagsSerializer,
                         responses={200: openapi.Response('Success', TextSerializer)})
    def post(self, request):
        serializer = ReplaceHashtagsSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            replacement = serializer.validated_data['replacement']
            replaced_text = replace_hashtags(text, replacement)
            return Response({'replaced_text': replaced_text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountHashtagsView(APIView):
    @swagger_auto_schema(request_body=TextSerializer, responses={200: openapi.Response('Success', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'count': openapi.Schema(type=openapi.TYPE_INTEGER)
        }
    ))})
    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            count = count_hashtags(text)
            return Response({'count': count}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
