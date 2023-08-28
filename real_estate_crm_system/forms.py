from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Project_Name, Fields, Inquiry_Type, Inquiry_Stage, Selected_Unit, Assign_To, Payment_Terms, \
    Payment_Type, Add_Inquiry, Accounts, Payment, Agents


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email_id = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email ID'}))
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    project_name = forms.ModelChoiceField(queryset=Project_Name.objects.all(), empty_label=None,
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    fields = forms.ModelChoiceField(queryset=Fields.objects.all(), empty_label=None,
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User  # Replace with your custom user model if you have one
        fields = ('first_name', 'last_name', 'email_id', 'username', 'password1', 'password2', 'project_name', 'fields')


class AddInquiryForm(forms.ModelForm):
    class Meta:
        model = Add_Inquiry
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'whatsapp_mobile_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'WhatsApp Mobile Number'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'follow_up_data': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Converted Date'},
                                                       format='%d-%m-%Y HH:MM:SS'),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Remarks'}),
            'next_follow_up_data': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Converted Date'},
                                                  format='%d-%m-%Y HH:MM:SS'),
            'converted_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Converted Date'}, format='%d-%m-%Y HH:MM:SS'),
            'unique_key': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'inquiry_type': forms.Select(attrs={'class': 'form-control'}),
            'inquiry_stage': forms.Select(attrs={'class': 'form-control'}),
            'interested_project': forms.Select(attrs={'class': 'form-control'}),
            'selected_unit': forms.Select(attrs={'class': 'form-control'}),
            'assign_to': forms.Select(attrs={'class': 'form-control'}),
            'fields': forms.Select(attrs={'class': 'form-control'}),
        }


class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'whatsapp_mobile_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'WhatsApp Mobile Number'}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'interested_project': forms.Select(attrs={'class': 'form-control'}),
            'selected_unit': forms.Select(attrs={'class': 'form-control'}),
            'sq_ft': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Square Feet'}),
            'sq_meter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Square Meter'}),
            'rate_per_ft': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rate per Square Feet'}),
            'rate_per_meter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rate per Square Meter'}),
            'cash': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cash'}),
            'gst': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GST'}),
            'total_amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total Amount'}),
            'payment_terms': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Due Date'}),
            'unique_key': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'unit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unit'}),
            'amount_receive': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount Received'}),
            'payment_type': forms.Select(attrs={'class': 'form-control'}),
            'gst': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GST'}),
            'current_outstanding': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Current Outstanding'}),
            'unique_key': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agents
        fields = '__all__'
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
            "phone_number": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            "whatsapp_number": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'WhatsApp Number'}),
            "address": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
        }

