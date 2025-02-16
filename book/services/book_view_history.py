from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from book.models import UserBookView
from book.serializers import UserBookViewSerializer
from drf_yasg.utils import swagger_auto_schema


class UserBookViewCreate(APIView):
    serializer_class = UserBookViewSerializer

    @swagger_auto_schema(request_body=serializer_class) #e
    def post(self, request):
        serializer = UserBookViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


