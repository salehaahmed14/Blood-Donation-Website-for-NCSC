from django.contrib import admin
from .models import Personal_Information, Blood_Type,Blood_Record, Medical_Information, Volunteer, Campaign, Location, Blood_Test,Performed_Test, Hospital, Blood_Bank, Staff, Doctor, HealthCare_Worker, Lab_Technician

admin.site.register(Personal_Information)
admin.site.register(Medical_Information)
admin.site.register(Volunteer)
admin.site.register(Blood_Type)
admin.site.register(Blood_Record)
admin.site.register(Campaign)
admin.site.register(Location)
admin.site.register(Blood_Test)
admin.site.register(Performed_Test)
admin.site.register(Hospital)
admin.site.register(Blood_Bank)
admin.site.register(Staff)
admin.site.register(Doctor)
admin.site.register(HealthCare_Worker)
admin.site.register(Lab_Technician)

