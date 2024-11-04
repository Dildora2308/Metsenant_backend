from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.views import Response
from django.utils import timezone

# Create your views here.

class SponsorCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.SponsorSerializer



class SponsorListAPIView(generics.ListAPIView):
    serializer_class = serializers.SponsorSerializer
    queryset = models.Sponsor.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['full_name','phone_number']
    filterset_fields = ['status', 'created_at', 'donation_amount']


class CreateStudentSponsorAPIView(generics.CreateAPIView):
    serializer_class = serializers.StudentSponsorSerializer


class StudentSposorUpdateAPIView(generics.UpdateAPIView):
   serializer_class = serializers.StudentSponsorSerializer



class StudentCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.StudentSerializer
    


class StudentListAPIView(generics.ListAPIView):
    serializer_class = serializers.StudentListSerializer
    queryset = models.Student.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['full_name','phone_number']
  

class SponsorDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.SponsorListSerializer
    queryset = models.Sponsor.objects.all()


class SponsorDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.SponsorListSerializer
    queryset = models.Sponsor.objects.all()



class StudentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.StudentListSerializer
    queryset = models.Student.objects.all()

def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.StudentListSerializer
        return serializers.StudentUpdateSerializer


class SponsorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.SponsorListSerializer
    queryset = models.Sponsor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.SponsorListSerializer
        return serializers.SponsorUpdateSerializer
    



class StatisticNumberAPIView(APIView):
    def get (self,request):
        approved_amount = models.StudentSponsor.objects.aggregate(total_amount=Sum('amount')) ['total_amount']
        requested_amount = models.Student.objects.aggregate(total=Sum('contract_amount')) ['total']
        return Response ({
            'approved_amount' : approved_amount,
            'requested_amount' : requested_amount


        })
    



class GraphAPIView(APIView):
    def get (self,request):

        this_year = timezone.now().year
        students = models.Student.objects.filter(created_at= this_year)
        sponsors = models.Sponsor.objects.filter(created_at= this_year)

        result = []
        for i in range(1,13):
            result.append( {
                'students_count': students.filter(created_at_month = i),
                'ponsors_count': sponsors.filter(created_at_month = i)

            })

        return Response(result)