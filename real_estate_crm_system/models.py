import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Project_Name(models.Model):
    projectname = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.projectname


class Fields(models.Model):
    fields = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.fields


class Inquiry_Type(models.Model):
    inquiry_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.inquiry_type


class Inquiry_Stage(models.Model):
    inquiry_stage = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.inquiry_stage


class Selected_Unit(models.Model):
    selected_unit = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.selected_unit


class Assign_To(models.Model):
    assign_to = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.assign_to


class Payment_Terms(models.Model):
    payment_terms = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.payment_terms


class Payment_Type(models.Model):
    payment_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.payment_type


class Add_Inquiry(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    email_id = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    inquiry_type = models.ForeignKey(Inquiry_Type, on_delete=models.CASCADE,blank=True,null=True)
    inquiry_stage = models.ForeignKey(Inquiry_Stage, on_delete=models.CASCADE,blank=True,null=True)
    interested_project = models.ForeignKey(Project_Name, on_delete=models.CASCADE,blank=True,null=True)
    selected_unit = models.ForeignKey(Selected_Unit, on_delete=models.CASCADE,blank=True,null=True)
    follow_up_date = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.TextField(max_length=200, blank=True, null=True)
    next_follow_up_date = models.CharField(max_length=50, blank=True, null=True)
    converted_date = models.CharField(max_length=50, blank=True, null=True)
    assign_to = models.ForeignKey(Assign_To, on_delete=models.CASCADE,blank=True,null=True)
    fields = models.ForeignKey(Fields, on_delete=models.CASCADE,blank=True,null=True)
    unique_key = models.CharField(max_length=100, default=uuid.uuid4, editable=False, blank=True)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.selected_unit)


class Accounts(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    email_id = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    interested_project = models.ForeignKey(Project_Name, on_delete=models.CASCADE)
    selected_unit = models.ForeignKey(Selected_Unit, on_delete=models.CASCADE)
    sq_ft = models.CharField(max_length=100, blank=True, null=True)
    sq_meter = models.CharField(max_length=100, blank=True, null=True)
    rate_per_ft = models.CharField(max_length=100, blank=True, null=True)
    rate_per_meter = models.CharField(max_length=100, blank=True, null=True)
    cash = models.CharField(max_length=100, blank=True, null=True)
    gst = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.CharField(max_length=100, blank=True, null=True)
    payment_terms = models.ForeignKey(Payment_Terms, on_delete=models.CASCADE)
    due_date = models.CharField(max_length=100, blank=True, null=True)
    unique_key = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.selected_unit)


class Payment(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    unit = models.CharField(max_length=100, blank=True, null=True)
    amount_receive = models.CharField(max_length=100, blank=True, null=True)
    payment_type = models.ForeignKey(Payment_Type, on_delete=models.CASCADE)
    gst = models.CharField(max_length=100, blank=True, null=True)
    current_outstanding = models.CharField(max_length=100, blank=True, null=True)
    unique_key = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format(self.unit, self.amount_receive, self.payment_type)


class Agents(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


