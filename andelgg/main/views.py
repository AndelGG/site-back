from django.shortcuts import render
from rest_framework.views import APIView
from .models import DB
from .serializer import DB_Serializer
from rest_framework.response import Response


class DB_View(APIView):
    def get(self, request):
        output = [
            {
                "name": output.name,
                "text": output.text
            } for output in DB.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = DB_Serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
