from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    
    try:
        data = JSONParser().parse(request)

        username = data['username']
        password = data['password']
    except:
          return Response("Los valores deben ser username y password")  

    try:
        user = User.objects.get(username=username)
    except:
        return Response("Usuario no encontrado")

    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Password incorrecta")

    token, created = Token.objects.get_or_create(user=user)
    print(f"token {token}")
    print(f"created {created}")

    json_response = '{"token":"'+token.key+'", "created":"'+str(created)+'"}'

    return Response(token.key)
