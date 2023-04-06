from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateField(blank=False)
    serial_number = models.CharField(max_length=6, blank=False)

    def __str__(self):
        return f"{self.name}"


class MembersHistory(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    changed_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateField(blank=False)
    serial_number = models.CharField(max_length=6, blank=False)

    def __str__(self):
        return f"{self.member.name} - {self.changed_at}"


class CheckInMembers(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    checked_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member}"