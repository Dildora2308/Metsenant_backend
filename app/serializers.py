from rest_framework import serializers
from . import models
from django.db.models import Sum


class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sponsor
        fields =  ("full_name", "phone_number", "donation_amount","org_name","type",

        )



class SponsorListSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Sponsor
            exclude = ("org_name","type","payment_type")

class StudentSponsorSerializer(serializers.ModelSerializer):

        class Meta:
            model = models.StudentSponsor
            fields = "__all__"


def validate(self, attrs):
        amount = attrs['amount']
        student = attrs ['student']
        sponsor = attrs['sponsor']




        sponsor_amount = sponsor.donation_amount
        sponsor_spent_money = models.StudentSponsor.objects.filter(sponsor = sponsor).aggregate(total_amount = Sum('amount'))['total_amount'] or 0
        difference = sponsor_amount - sponsor_spent_money

        if sponsor_amount - sponsor_spent_money < amount:
            raise serializers.ValidationError(
                detail = {'error': f'bu homiyda {difference} sum pul qolgan , bundan ortiq mablag yubora olmaysiz'}
            )


      
        Student_contract = student.contract_amount
        student_recievedd_money = models.StudentSponsor.objects.filter(student=student).aggregate (total_amount = Sum('amount'))['total_amount'] or 0
        difference = Student_contract - student_recievedd_money
        if difference < amount:
            raise serializers.ValidationError(
                detail = {'error': f' Bu talabaga {difference} dan kop pul bera olmaysiz'})

        return attrs
    
#    # 1 contract,  qancha ajratishgan, 3 shartini to'iq o'ylash ,berilgan pul-so'ralgan pul, qoldiq bl solishtirish

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields =  ("full_name", "student_type", "university","contract_amount"

        )

class StudentListSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Student
            fields = ("full_name","contract_amount","university")


class StudentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Student
            fields = ("full_name","contract_amount","university")


class StudentUpdateSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Student
            exclude = ("id","created_at")

#sponsor

class SponsorUpdateSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Sponsor
            exclude = ("id","created_at")