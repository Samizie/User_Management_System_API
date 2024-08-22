from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserMan
from .serializers import UserManSerializer
from  rest_framework import generics
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


@api_view(['GET'])
def home(request):
    data = {
        'status': 'success',
        'message': 'Welcome to User Management API by Agboola Olalekan'
    }
    return Response(data, status=status.HTTP_200_OK)
    


@swagger_auto_schema(
        operation_summary="List or Create Users",
        operation_description="GET: List all users. POST: Create a new user.",
        responses={200: UserManSerializer(many=True), 201: UserManSerializer},
        request_body=UserManSerializer,
        )
class UserManView(generics.ListCreateAPIView):
    queryset = UserMan.objects.all()
    serializer_class = UserManSerializer
    
    


@swagger_auto_schema(
        operation_summary="Retrieve, Update and Delete a User",
        operation_description="GET: Retrieve a user by ID or name. PUT: Update user details. DELETE: Delete a user.",
        responses={
            200: UserManSerializer,
            404: "User not found",
        },
        request_body=UserManSerializer,
    )
class UserGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset= UserMan.objects.all()
    serializer_class = UserManSerializer

    def get_object(self):
        input = self.kwargs['input']
        if search.isdigit():
            return get_object_or_404(UserMan, id=int(input))
        else:
            return get_object_or_404(UserMan, name=search)
        
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except UserMan.DoesNotExist:
            return Response({
                "status": "error",
                "message": "User not found"
            }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                "status": "success",
                "message": "User updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except UserMan.DoesNotExist:
            return Response({
                "status": "error",
                "message": "User not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "status": "error",
                "message": "User not found"
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "status": "success",
                "message": "User deleted successfully"
            }, status=status.HTTP_200_OK)
        except UserMan.DoesNotExist:
            return Response({
                "status": "error",
                "message": "User not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "status": "error",
                "message": "User not found"
            }, status=status.HTTP_400_BAD_REQUEST)
        




