import csv
import pandas as pd
import openpyxl
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, AddInquiryForm, AccountsForm, PaymentForm, AgentForm
from .models import Project_Name, Fields, Inquiry_Type, Inquiry_Stage, Selected_Unit, Assign_To, Payment_Terms, \
    Payment_Type, Add_Inquiry, Accounts, Payment, Agents
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    records = Add_Inquiry.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("index")
        else:
            messages.success(request, "There was an Error, Please try again")
            return redirect('index')
    else:
        return render(request, 'index.html', {'records': records})


def login_user(request):
    records = Add_Inquiry.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("index")
        else:
            messages.success(request, "There was an Error, Please try again")
            return redirect('index')
    else:
        return render(request, 'index.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  # Check form validity before saving
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully signed up.")
            return redirect('index')  # Replace 'home' with the appropriate URL name
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def add_inquiry(request):
    if request.method == 'POST':
        form = AddInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            # Do any additional processing or redirects here
            return redirect('index')  # Replace 'home' with the appropriate URL name
    else:
        form = AddInquiryForm()
    return render(request, 'add_inquiry.html', {'form': form})


def account_data(request):
    account_records = Accounts.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("index")
        else:
            messages.success(request, "There was an Error, Please try again")
            return redirect('index')
    else:
        return render(request, 'index.html', {'account_records': account_records})


def accounts(request):
    if request.method == 'POST':
        account = AccountsForm(request.POST)
        if account.is_valid():
            account_form = account.save()
            # Do any additional processing or redirects here
            return redirect('index')  # Replace 'home' with the appropriate URL name
    else:
        account = AccountsForm()
    return render(request, 'account.html', {'form': account})


def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            # Do any additional processing or redirects here
            return redirect('index')  # Replace 'home' with the appropriate URL name
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form})


def agent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'home' with the appropriate URL name
    else:
        form = AgentForm()

    return render(request, 'agent.html', {'form': form})

def agent_data(request):
    agent_records = Agents.objects.all()
    print(agent_records)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("index")
        else:
            messages.success(request, "There was an Error, Please try again")
            return redirect('index')
    else:
        return render(request, 'agent_data.html', {'agent_records': agent_records})


# def upload_file(request):
#     if request.method == 'POST':
#         file = request.FILES['file_upload']
#         print("Done")

#         if file.name.endswith('.csv') | file.name.endswith('.xlsx'):
#             # Process the uploaded CSV file
#             decoded_file = file.read().decode('utf-8')
#             csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
#             for row in csv_data:
#                 # Assuming your CSV file structure matches the order of fields in the Inquiry model
#                 Add_Inquiry.objects.create(
#                     created_date=row[1],
#                     first_name=row[2],
#                     middle_name=row[3],
#                     last_name=row[4],
#                     mobile_number=row[5],
#                     whatsapp_mobile_number=row[6],
#                     email_id=row[7],
#                     address=row[8],
#                     area=row[9],
#                     city=row[10],
#                     state=row[11],
#                     country=row[12],
#                     inquiry_type=row[13],
#                     inquiry_stage=row[14],
#                     interested_project=row[15],
#                     selected_unit=row[16],
#                     follow_up_date=row[17],
#                     remarks=row[18],
#                     next_follow_up_date=row[19],
#                     converted_date=row[20],
#                     assign_to=row[21],
#                     fields=row[22],
#                 )
#             return redirect('home')  # Redirect to a page after successful upload
#     return render(request, 'upload_inquiry.html')  # Render the form for file upload


def upload_inquiry_file(request):
    if request.method == 'POST':
        file = request.FILES['file_upload']
        print("Done")

        if file.name.endswith('.xlsx'):
            # Process the uploaded XLSX file using pandas
            df = pd.read_excel(file)

            for index, row in df.iterrows():
                for field in ['inquiry_type', 'inquiry_stage', 'interested_project', 'selected_unit', 'assign_to', 'fields']:
                    if pd.isna(row[field]):
                        row[field] = None

                follow_up_date = None
                next_follow_up_date = None
                converted_date = None

                inquiry_type_instance = None
                inquiry_stage_instance = None
                interested_project_instance = None
                selected_unit_instance = None
                assign_to_instance = None
                fields_instance = None

                if pd.notna(row['follow_up_date']):
                    follow_up_date_str = row['follow_up_date']
                    # print(follow_up_date)
                    # follow_up_date = datetime(follow_up_date_str, "%d/%m/%Y %H:%M:%S")
                else:
                    follow_up_date = None

                if pd.notna(row['next_follow_up_date']):
                    next_follow_up_date_str = row['next_follow_up_date']
                    # next_follow_up_date = datetime(next_follow_up_date_str, "%d/%m/%Y %H:%M:%S")
                else:
                    next_follow_up_date = None

                if pd.notna(row['converted_date']):
                    converted_date_str = str(row['converted_date'])  # Assuming the date is stored as a string
                    # converted_date = datetime(converted_date_str, "%d/%m/%Y %H:%M:%S")
                else:
                    converted_date = None

                if row['inquiry_type'] is not None:
                    try:
                        inquiry_type_instance = Inquiry_Type.objects.get(inquiry_type=row['inquiry_type'])
                    except Inquiry_Type.DoesNotExist:
                        print(f"Inquiry_Type '{row['inquiry_type']}' does not exist.")

                if row['inquiry_stage'] is not None:
                    try:
                        inquiry_stage_instance = Inquiry_Stage.objects.get(inquiry_stage=row['inquiry_stage'])
                    except Inquiry_Stage.DoesNotExist:
                        print(f"Inquiry_Stage '{row['inquiry_stage']}' does not exist.")

                if row['interested_project'] is not None:
                    try:
                        interested_project_instance = Project_Name.objects.get(projectname=row['interested_project'])
                    except Project_Name.DoesNotExist:
                        print(f"Project_Name '{row['interested_project']}' does not exist.")

                if row['selected_unit'] is not None:
                    try:
                        selected_unit_instance = Selected_Unit.objects.get(selected_unit=row['selected_unit'])
                    except Selected_Unit.DoesNotExist:
                        print(f"Selected_Unit '{row['selected_unit']}' does not exist.")

                if row['assign_to'] is not None:
                    try:
                        assign_to_instance = Assign_To.objects.get(assign_to=row['assign_to'])
                    except Assign_To.DoesNotExist:
                        print(f"Assign_To '{row['assign_to']}' does not exist.")

                if row['fields'] is not None:
                    try:
                        fields_instance = Fields.objects.get(fields=row['fields'])
                    except Fields.DoesNotExist:
                        print(f"Fields '{row['fields']}' does not exist.")

                Add_Inquiry.objects.create(
                    created_date=row['created_date'],
                    first_name=row['first_name'],
                    middle_name=row['middle_name'],
                    last_name=row['last_name'],
                    mobile_number=row['mobile_number'],
                    whatsapp_mobile_number=row['whatsapp_mobile_number'],
                    email_id=row['email_id'],
                    address=row['address'],
                    area=row['area'],
                    city=row['city'],
                    state=row['state'],
                    country=row['country'],
                    inquiry_type=inquiry_type_instance,
                    inquiry_stage=inquiry_stage_instance,
                    interested_project=interested_project_instance,
                    selected_unit=selected_unit_instance,
                    follow_up_date=follow_up_date,
                    remarks=row['remarks'],
                    next_follow_up_date=next_follow_up_date,
                    converted_date=converted_date,
                    assign_to=assign_to_instance,
                    fields=fields_instance,
                )

            return redirect('index')  # Redirect to a page after successful upload
    return render(request, 'upload_inquiry.html')


def upload_account_file(request):
    if request.method == 'POST':
        file = request.FILES['file_upload']
        print("Done")

        if file.name.endswith('.xlsx'):
            # Process the uploaded XLSX file using pandas
            df = pd.read_excel(file)

            for index, row in df.iterrows():
                for field in ['inquiry_type', 'inquiry_stage', 'interested_project', 'selected_unit', 'assign_to', 'fields']:
                    if pd.isna(row[field]):
                        row[field] = None

                follow_up_date = None
                next_follow_up_date = None
                converted_date = None

                inquiry_type_instance = None
                inquiry_stage_instance = None
                interested_project_instance = None
                selected_unit_instance = None
                assign_to_instance = None
                fields_instance = None

                if pd.notna(row['follow_up_date']):
                    follow_up_date_str = row['follow_up_date']
                    # print(follow_up_date)
                    # follow_up_date = datetime(follow_up_date_str, "%d/%m/%Y %H:%M:%S")
                else:
                    follow_up_date = None

                if pd.notna(row['next_follow_up_date']):
                    next_follow_up_date_str = row['next_follow_up_date']
                    # next_follow_up_date = datetime(next_follow_up_date_str, "%d/%m/%Y %H:%M:%S")
                else:
                    next_follow_up_date = None

                if pd.notna(row['converted_date']):
                    converted_date_str = str(row['converted_date'])  # Assuming the date is stored as a string
                    # converted_date = datetime(converted_date_str, "%d/%m/%Y %H:%M:%S")
                else:
                    converted_date = None

                if row['inquiry_type'] is not None:
                    try:
                        inquiry_type_instance = Inquiry_Type.objects.get(inquiry_type=row['inquiry_type'])
                    except Inquiry_Type.DoesNotExist:
                        print(f"Inquiry_Type '{row['inquiry_type']}' does not exist.")

                if row['inquiry_stage'] is not None:
                    try:
                        inquiry_stage_instance = Inquiry_Stage.objects.get(inquiry_stage=row['inquiry_stage'])
                    except Inquiry_Stage.DoesNotExist:
                        print(f"Inquiry_Stage '{row['inquiry_stage']}' does not exist.")

                if row['interested_project'] is not None:
                    try:
                        interested_project_instance = Project_Name.objects.get(projectname=row['interested_project'])
                    except Project_Name.DoesNotExist:
                        print(f"Project_Name '{row['interested_project']}' does not exist.")

                if row['selected_unit'] is not None:
                    try:
                        selected_unit_instance = Selected_Unit.objects.get(selected_unit=row['selected_unit'])
                    except Selected_Unit.DoesNotExist:
                        print(f"Selected_Unit '{row['selected_unit']}' does not exist.")

                if row['assign_to'] is not None:
                    try:
                        assign_to_instance = Assign_To.objects.get(assign_to=row['assign_to'])
                    except Assign_To.DoesNotExist:
                        print(f"Assign_To '{row['assign_to']}' does not exist.")

                if row['fields'] is not None:
                    try:
                        fields_instance = Fields.objects.get(fields=row['fields'])
                    except Fields.DoesNotExist:
                        print(f"Fields '{row['fields']}' does not exist.")

                Add_Inquiry.objects.create(
                    created_date=row['created_date'],
                    first_name=row['first_name'],
                    middle_name=row['middle_name'],
                    last_name=row['last_name'],
                    mobile_number=row['mobile_number'],
                    whatsapp_mobile_number=row['whatsapp_mobile_number'],
                    email_id=row['email_id'],
                    address=row['address'],
                    area=row['area'],
                    city=row['city'],
                    state=row['state'],
                    country=row['country'],
                    inquiry_type=inquiry_type_instance,
                    inquiry_stage=inquiry_stage_instance,
                    interested_project=interested_project_instance,
                    selected_unit=selected_unit_instance,
                    follow_up_date=follow_up_date,
                    remarks=row['remarks'],
                    next_follow_up_date=next_follow_up_date,
                    converted_date=converted_date,
                    assign_to=assign_to_instance,
                    fields=fields_instance,
                )

            return redirect('index')  # Redirect to a page after successful upload
    return render(request, 'upload_account.html')