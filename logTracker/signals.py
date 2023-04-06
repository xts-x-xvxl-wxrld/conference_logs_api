from django.db.models.signals import pre_save
from .models import MembersHistory, Member


def memberPreSave(sender, instance, **kwargs):
    if instance.pk:
        original = sender.objects.get(pk=instance.pk)
        if (original.name != instance.name or
                original.surname != instance.surname or
                original.date_of_birth != instance.date_of_birth or
                original.serial_number != instance.serial_number):
            MembersHistory.objects.create(
                member=original,
                name=original.name,
                surname=original.surname,
                date_of_birth=original.date_of_birth,
                serial_number=original.serial_number
            )


pre_save.connect(memberPreSave, sender=Member)
