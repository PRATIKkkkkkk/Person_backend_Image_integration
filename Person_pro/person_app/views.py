from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings


class PersonAPI(APIView):

    def get(self, request):
        objs = Person.objects.all()
        serializer = PersonSerializer(objs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            subject = 'Welcome Email'
            fname = request.data.get('fname')
            email = request.data.get('email')
            message = f'Hello {fname}, Thank you for registering with us. We will get back to you shortly.'
            from_email = settings.EMAIL_HOST_USER
            send_mail(
                subject=subject,
                recipient_list=[email],
                message=message,
                from_email=from_email,
            )
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class PersonDetailAPI(APIView):

    def get(self, request, pk):
        obj = get_object_or_404(Person, id=pk)
        serializer = PersonSerializer(obj)
        return Response(serializer.data, status=200)
    def put(self, request, pk):
        obj = get_object_or_404(Person, id=pk)
        serializer = PersonSerializer(data=request.data, instance=obj)
        if serializer.is_valid():
            subject = 'Update Email'
            fname = obj.fname
            email = obj.email
            message = f'Hello {fname}, Your data has been updated'
            from_email = settings.EMAIL_HOST_USER
            send_mail(
                subject=subject,
                recipient_list=[email],
                message=message,
                from_email=from_email,
            )
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    
    def patch(self, request, pk):
        obj = get_object_or_404(Person, id=pk)
        serializer = PersonSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            subject = 'Update Email'
            fname = obj.fname
            email = obj.email
            message = f'Hello {fname}, Your data has been updated'
            from_email = settings.EMAIL_HOST_USER
            send_mail(
                subject=subject,
                recipient_list=[email],
                message=message,
                from_email=from_email,
            )
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        obj = get_object_or_404(Person, id=pk)
        subject = 'Delete Email'
        fname = obj.fname
        email = obj.email
        message = f'Hello {fname}, Sorry For the Inconvinience.'
        from_email = settings.EMAIL_HOST_USER
        send_mail(
            subject=subject,
            recipient_list=[email],
            message=message,
            from_email=from_email,
        )
        obj.profile_pic.delete()
        obj.delete()
        return Response(data=None)