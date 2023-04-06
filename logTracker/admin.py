from django.contrib import admin
from .models import Member, MembersHistory


# Register your models here.
class MembersAdmin(admin.ModelAdmin):
    list_display = 'name', 'surname', 'date_of_birth', 'serial_number'


class MembersHistoryAdmin(admin.ModelAdmin):
    list_display = 'member', 'changed_at', 'name', 'surname', 'date_of_birth', 'serial_number'


admin.site.register(Member, MembersAdmin)
admin.site.register(MembersHistory, MembersHistoryAdmin)