from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import StaffSerializer, LoginSatffSerializer


# Login API
class LoginStaffAPI(generics.GenericAPIView):
    serializer_class = LoginSatffSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        staff_member = serializer.validated_data
        group = staff_member.groups.all()

        return Response({
            "user": StaffSerializer(staff_member, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(staff_member)[1],
            "user_class": group[0].id
        })


# Get Staff User API
class StaffAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = StaffSerializer

    def get_object(self):
        return self.request.user
