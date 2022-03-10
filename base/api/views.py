from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
#Seralizers
from .serializers import MyTokenObtainPairSerializer,NoteSerializer
#Models
from base.models import Note




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class getRoutes(APIView):
    """
    List all routes.
    """
    def get(self, request, format=None):
        routes=[
        "/api/token",
        "/api/token/refresh",
        ]
        return Response(routes)

class getNotes(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        user = request.user
        notes = user.note_set.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)