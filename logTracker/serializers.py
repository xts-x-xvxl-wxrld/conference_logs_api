from rest_framework import serializers
from .models import Member, CheckInMembers


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckInMembers
        fields = ('id', 'member', 'checked_in')