from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Project_Name, Fields, Inquiry_Type, Inquiry_Stage, Selected_Unit, Assign_To, Payment_Terms, \
    Payment_Type, Add_Inquiry, Accounts, Payment, Agents


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control form-control-lg', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control form-control-lg', 'placeholder': 'Last Name'}))
    email_id = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email ID'}))
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Confirm Password'}))
    project_name = forms.ModelChoiceField(queryset=Project_Name.objects.all(), empty_label=None,
                                          widget=forms.Select(attrs={'class': 'form-control form-control-lg'}))
    fields = forms.ModelChoiceField(queryset=Fields.objects.all(), empty_label=None,
                                    widget=forms.Select(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = User  # Replace with your custom user model if you have one
        fields = ('first_name', 'last_name', 'email_id', 'username', 'password1', 'password2', 'project_name', 'fields')


class AddInquiryForm(forms.ModelForm):
    class Meta:
        model = Add_Inquiry
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Last Name'}),
            'mobile_number': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Mobile Number'}),
            'whatsapp_mobile_number': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'WhatsApp Mobile Number'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Address'}),
            'area': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Area'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'State'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Country'}),
            'follow_up_data': forms.DateTimeInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Converted Date'},
                format='%d-%m-%Y HH:MM:SS'),
            'remarks': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Remarks'}),
            'next_follow_up_data': forms.DateTimeInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Converted Date'},
                format='%d-%m-%Y HH:MM:SS'),
            'converted_date': forms.DateTimeInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Converted Date'},
                format='%d-%m-%Y HH:MM:SS'),
            'unique_key': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'readonly': 'readonly'}),
            'inquiry_type': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'inquiry_stage': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'interested_project': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'selected_unit': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'assign_to': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'fields': forms.Select(attrs={'class': 'form-control form-control-lg'}),
        }


class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Last Name'}),
            'mobile_number': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Mobile Number'}),
            'whatsapp_mobile_number': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'WhatsApp Mobile Number'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Address'}),
            'area': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Area'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'State'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Country'}),
            'interested_project': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'selected_unit': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'sq_ft': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Square Feet'}),
            'sq_meter': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Square Meter'}),
            'rate_per_ft': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Rate per Square Feet'}),
            'rate_per_meter': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Rate per Square Meter'}),
            'cash': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Cash'}),
            'gst': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'GST'}),
            'total_amount': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Total Amount'}),
            'payment_terms': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'due_date': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Due Date'}),
            'unique_key': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'readonly': 'readonly'}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'unit': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Unit'}),
            'amount_receive': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Amount Received'}),
            'payment_type': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'gst': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'GST'}),
            'current_outstanding': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Current Outstanding'}),
            'unique_key': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'readonly': 'readonly'}),
        }


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agents
        fields = '__all__'
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'First Name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Last Name'}),
            "email": forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': "Email"}),
            "phone_number": forms.NumberInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Phone Number'}),
            "whatsapp_number": forms.NumberInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'WhatsApp Number'}),
            "address": forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Address'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project_Name
        fields = ['projectname']


class FieldForm(forms.ModelForm):
    class Meta:
        model = Fields
        fields = ['fields']

class Inquiry_TypeForm(forms.ModelForm):
    class Meta:
        model = Inquiry_Type
        fields = ['inquiry_type']

class Inquiry_StageForm(forms.ModelForm):
    class Meta:
        model = Inquiry_Stage
        fields = ['inquiry_stage']

class Selected_UnitForm(forms.ModelForm):
    class Meta:
        model = Selected_Unit
        fields = ['selected_unit']

class Assign_ToForm(forms.ModelForm):
    class Meta:
        model = Assign_To
        fields = ['assign_to']

class Payment_TermsForm(forms.ModelForm):
    class Meta:
        model = Payment_Terms
        fields = ['payment_terms']

class Payment_TypeForm(forms.ModelForm):
    class Meta:
        model = Payment_Type
        fields = ['payment_type']