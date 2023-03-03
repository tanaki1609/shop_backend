from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView


class AuthorizationAPIView(APIView):
    """ Authorization for client users """
    def post(self, request):
        username, password = request.data.get('username'), request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)

            return Response(data={'token': token.key}, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def registration_api_view(request):
    username, password = request.data.get('username'), request.data.get('password')
    User.objects.create_user(username=username, password=password)

    return Response(status=status.HTTP_200_OK)
