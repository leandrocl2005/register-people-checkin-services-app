from django.contrib import admin

from checkin.models import (ChangeCompanion, CompanionCheckin,
                            OtherPeopleCheckin, PatientCheckin)

# Register your models here.
admin.site.register(PatientCheckin)
admin.site.register(CompanionCheckin)
admin.site.register(OtherPeopleCheckin)
admin.site.register(ChangeCompanion)
