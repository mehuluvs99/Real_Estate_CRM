from django.contrib import admin
from .models import FollowUpUpdate, Project_Name, Fields, Inquiry_Type, Inquiry_Stage, Selected_Unit, Assign_To, Payment_Terms, \
    Payment_Type, Add_Inquiry, Accounts, Payment, Agents

# Register your models here.

admin.site.register(Project_Name)
admin.site.register(Fields)
admin.site.register(Inquiry_Type)
admin.site.register(Inquiry_Stage)
admin.site.register(Selected_Unit)
admin.site.register(Assign_To)
admin.site.register(Payment_Terms)
admin.site.register(Payment_Type)
admin.site.register(Add_Inquiry)
admin.site.register(Accounts)
admin.site.register(Payment)
admin.site.register(Agents)
admin.site.register(FollowUpUpdate)
