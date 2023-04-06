from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm, LogInForm, EditMemberForm, CheckInForm
from .models import Member, CheckInMembers
from datetime import datetime
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import MemberSerializer, CheckInSerializer
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def logIn(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            serial_number = form.cleaned_data.get('serial_number')
            try:
                member = Member.objects.get(name=name, serial_number=serial_number)
                return render(request, 'members_view.html', {'member': member})
            except:
                messages.success(request, 'Error, either Name or Number is not correct')
                pass
    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form})


def allMembers(request):
    members = Member.objects.all()
    return render(request, 'members_view.html', {'members': members})


def allCheckIn(request):
    checkList = CheckInMembers.objects.all()
    return render(request, 'checks_view.html', {'checkList': checkList})


def checkIn(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST)
        if form.is_valid():
            serial_number = form.cleaned_data['serial_number']
            try:
                member = Member.objects.get(serial_number=serial_number)
                time = datetime.now()
                print('member', member.name)
                checkIn = CheckInMembers.objects.create(member=member)
                print('chek in created')
                checkIn.save()
                checkList = CheckInMembers.objects.all()
                return render(request, 'checks_view.html', {'checkList': checkList})
            except:
                messages.success(request, 'Error, Number is not correct')
                pass
    else:
        form = CheckInForm()
    return render(request, 'checkin.html', {'form': form})


def editMember(request, member_id):
    member = Member.objects.get(pk=member_id)
    if request.method == 'POST':
        form = EditMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = EditMemberForm(instance=member)
    return render(request, 'edit_member.html', {'form': form})


def memberCheckIn(request, member_id):
    member = Member.objects.get(pk=member_id)
    CheckInMembers.objects.create(member=member,)
    return redirect('members')


class AllMembersGetApi(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class CheckInMemberApi(generics.ListCreateAPIView):
    queryset = CheckInMembers.objects.all()
    serializer_class = CheckInSerializer

    def create(self, request, *args, **kwargs):
        try:
            serial_number = request.data['serial_number']
            print(serial_number)
            member = Member.objects.get(serial_number=serial_number)
            checked_in = datetime.now()
            serializer = self.get_serializer(data={'member': member.id, 'checked_in': checked_in})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)