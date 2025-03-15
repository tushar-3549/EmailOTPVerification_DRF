from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import *
from .emails import *

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data 
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': 200,
                    'message': 'registration successfully check email',
                    'data': serializer.data
                })
            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data': serializer.errors
            })
        # except Exception as e:
        #     print(e)
        except Exception as e:
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'error': str(e)
            }, status=500)
        
class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data 
            serializer = VerifyEmailSerializer(data = data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = User.objects.filter(email = email)
                if not user.exists():
                    return Response({
                        'status': 400,
                        'message': 'something went wrong',
                        'data': 'invalid email'
                    })
                if user[0].otp != otp:
                    return Response({
                        'status': 400,
                        'message': 'something went wrong',
                        'data': 'wrong otp'
                    })
                user = user.first()
                user.is_verified = True
                user.save()

                return Response({
                    'status': 200,
                    'message': 'account verified...',
                    'data': {}
                })
            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data': serializer.errors
            })
            
        except Exception as e:
            print(e)