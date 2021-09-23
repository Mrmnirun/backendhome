from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import CustomerSerializer, RegisterCustomerSerializer, LoginCustomerSerializer


# Register API
class RegisterCustomerAPI(generics.GenericAPIView):
    serializer_class = RegisterCustomerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.save()
        return Response({
            "user": CustomerSerializer(customer, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(customer)[1],
            "user_class": 0
        })


# Login API
class LoginCustomerAPI(generics.GenericAPIView):
    serializer_class = LoginCustomerSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.validated_data
        return Response({
            "user": CustomerSerializer(customer, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(customer)[1],
            "user_class:": 0
        })


# Get Customer User API
class CustomerAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = CustomerSerializer

    def get_object(self):
        return self.request.user
