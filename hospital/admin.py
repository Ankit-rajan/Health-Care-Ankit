from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails

# 🔧 To Change the Heading
from django.contrib import admin

admin.site.site_header = "Health Care Admin"
admin.site.site_title = "Hospital Admin Portal"
admin.site.index_title = "Welcome to the Health Care Admin Panel"

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)
