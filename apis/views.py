from rest_framework.views import APIView
from apis.serializers import BikesSerializer, UserSerializer
from django.core.checks import messages
from apis.models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your views here.
class CustomAuthToken(APIView):
    def get(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        phone = request.query_params.get('phone')
        try: 
            if(email is not None):
                usersModel = Users.objects.get(email=email)
                user = User.objects.get(username = email)
                token = Token.objects.get_or_create(user = user)
                return Response({
                    'success' : True,
                    'token' : token[0].key,
                    "first_name" : usersModel.first_name,
                    "last_name" : usersModel.last_name,
                    "email" : usersModel.email,
                    "phone" :usersModel.phone,
                    "phone_varified" : usersModel.phone_varified,
                    "kyc_varified" : usersModel.kyc_varified,
                }, status=200)
            elif (phone is not None):
                print("Hello")
                usersModel = Users.objects.get(phone=phone)
                user = User.objects.get(username = usersModel.email)
                token = Token.objects.get_or_create(user = user)
                return Response({
                    'success' : True,
                    'token' : token[0].key,
                    "first_name" : usersModel.first_name,
                    "last_name" : usersModel.last_name,
                    "email" : usersModel.email,
                    "phone" :usersModel.phone,
                    "phone_varified" : usersModel.phone_varified,
                    "kyc_varified" : usersModel.kyc_varified,
                }, status=200)
            else : 
                return Response({
                    'success' : False,
                    'message' : "please provied email or phone"
                })
        except : 
            return Response({
            'success' : False,
            'message' : "Couldn't not find user"
        }, status=404)
        
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        phone_varified = request.POST.get('phone_varified')
        kyc_varified = request.POST.get('kyc_varified')
        user_image_url = request.FILES.get('user_image_url')
        aadhar_card_url = request.FILES.get('aadhar_card_url')
        print(aadhar_card_url)
          
        try : 
         userObject = Users(first_name=first_name,last_name=last_name,email =email,phone=phone,phone_varified = phone_varified and phone_varified or False,kyc_varified = kyc_varified and kyc_varified or False, user_image_url = user_image_url, aadhar_card_url = aadhar_card_url)
         userObject.save()
         user = User.objects.create(username = email)
         user.set_password(email)  
         token = Token.objects.get_or_create(user = user)

         return Response({
                "token" : token[0].key,
                "first_name" : first_name,
                "last_name" : last_name,
                "email" : email,
                "phone" : phone,
                "phone_varified" : phone_varified and phone_varified or False,
                "kyc_varified" : kyc_varified and kyc_varified or  False,
                
            })
        except Exception as e: 
            print(e)
            return Response({
                "error" : True,
                "message": "Some Error Occurred"
            }, status=404)

    def put(self, request, *args, **kwargs):
        email = request.PUT.get('email')
        user_image_url = request.FILES('user_image_url')
        aadhar_card_url = request.FILES('aadhar_card_url')
        user = Users.objects.filter(email = email)
        try : 
            if(user_image_url and aadhar_card_url):
                user[0](aadhar_card_url = aadhar_card_url,user_image_url = user_image_url)
                return Response({"error" : False, "message" : "upload files"})
            elif(aadhar_card_url):
                user[0](aadhar_card_url = aadhar_card_url)
                return Response({"error" : False, "message" : messages})
            else:
                user[0](aadhar_card_url = user_image_url)
                return Response({"error" : False, "message" : messages})
        except : 
            Response({"error" : True, "message" : "could not process request"})    

class UserView(viewsets.ModelViewSet):
     queryset = Users.objects.all()
     serializer_class = UserSerializer

class BikesView(viewsets.ModelViewSet):
    queryset = Bikes.objects.all()
    serializer_class = BikesSerializer