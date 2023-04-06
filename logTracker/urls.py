from .views import register, logIn, allMembers, editMember, memberCheckIn, allCheckIn, checkIn, AllMembersGetApi, CheckInMemberApi
from django.urls import path

# start path with /app/ when entering in browser
urlpatterns = [
    path('login/', logIn, name='login'),
    path('register/', register, name='register'),
    path('members/', allMembers, name='members'),
    path('member/<int:member_id>/edit/', editMember, name='edit_member'),
    path('member/<int:member_id>/check_in/', memberCheckIn, name='check_in_member'),
    path('check_in_members/', allCheckIn, name='check_in_all'),
    path('check_in/', checkIn, name='member_check_in'),
    path('get_members_info/', AllMembersGetApi.as_view(), name='getMembersAPI'),
    path('post_check_in/', CheckInMemberApi.as_view(), name='checkInAPI')
]