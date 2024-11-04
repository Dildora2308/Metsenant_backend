from django.db import models

# Create your models here


class Sponsor(models.Model):
    class SponsorType(models.TextChoices):
        PERSONAL = 'personal','jismoniy shaxs'
        LEGAL = 'legal', 'yuridik shaxs'


    class StatusChoice(models.TextChoices):
        NEW = "New", 'yangi'
        MODERATION = 'Modeartion', 'Moderatsiya'
        CONFIRMED = 'confirmed', 'Tasdiqlangan'
        CANCELLED = 'cancelled', 'Bekor qilingan'

    class SponsorPaymentType(models.TextChoices):
        CASH = 'Cash', "Naqd"
        CREDIT_CARD = 'credit card', 'Plastik karta'


    full_name = models.CharField(max_length=250)
    phone_number = models.IntegerField(max_length=13)
    donation_amount = models.PositiveBigIntegerField()
    org_name = models.CharField(max_length=250)
    type = models.CharField(max_length=250,
                choices= SponsorType.choices) 
    status= models.CharField (max_length=50, 
        choices=StatusChoice.choices, 
        default=StatusChoice.NEW
    )
   
    created_at = models.DateTimeField(auto_now_add=True)
    payment_type=models.CharField(
        max_length=50,
        choices=SponsorPaymentType.choices, 
        null=True)
    

    def __str__(self):
        return self.full_name
    


class University(models.Model):
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name




class Student(models.Model):


    class StudentType(models.TextChoices):
        BACHELOR = 'Bachelor', 'Bakalavr'
        MASTER =  "Master", 'Magistr'

    full_name = models.CharField(max_length=250)
    student_type = models.CharField(max_length=250,
                                    choices=StudentType)
    university= models.ForeignKey(University, on_delete=models.PROTECT)
    contract_amount = models.PositiveIntegerField()
    created_at = models.DateTimeField( auto_now_add=True)
    

class StudentSponsor(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete= models.PROTECT)
    student = models.ForeignKey(Student , on_delete=models. PROTECT)
    amount= models.PositiveIntegerField()
    
    def __str__(self)-> str:
        return f"{ self.sponsor.full_name}-{ self.student.full_name}"