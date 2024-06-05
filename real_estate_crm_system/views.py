import csv
from numpy import true_divide
import pandas as pd
import openpyxl
from datetime import datetime
import xlsxwriter
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, AddInquiryForm, AccountsForm, PaymentForm, AgentForm, ProjectForm, FieldForm, Inquiry_TypeForm, Inquiry_StageForm, Selected_UnitForm, Assign_ToForm, Payment_TermsForm, \
    Payment_TypeForm, FollowUpUpdateForm
from .models import FollowUpUpdate, Project_Name, Fields, Inquiry_Type, Inquiry_Stage, Selected_Unit, Assign_To, Payment_Terms, \
    Payment_Type, Add_Inquiry, Accounts, Payment, Agents
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View


def home(request):
    records = Add_Inquiry.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("home")
        else:
            messages.success(request, "There was an Error, Please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def login_user(request):
    records = Add_Inquiry.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("home")
        else:
            messages.success(request, "There was an Error, Please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


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
            return redirect('home')  # Replace 'home' with the appropriate URL name
    else:
        form = SignUpForm()
    return render(request, 'login_signup/signup.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    # print(users)
    return render(request, 'users.html', {'users': users})


def add_inquiry(request):
    if request.method == 'POST':
        form = AddInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            # Do any additional processing or redirects here
            return redirect('home')  # Replace 'home' with the appropriate URL name
    else:
        form = AddInquiryForm()
    return render(request, 'inquiry/add_inquiry.html', {'form': form})


def account_data(request):
    account_records = Accounts.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("account_data")
        else:
            messages.success(request, "There was an Error, Please try again")
            return redirect('account_data')
    else:
        return render(request, 'account/account_data.html', {'account_records': account_records})


def accounts(request):
    if request.method == 'POST':
        account = AccountsForm(request.POST)
        if account.is_valid():
            account_form = account.save()
            # Do any additional processing or redirects here
            return redirect('home')  # Replace 'home' with the appropriate URL name
    else:
        account = AccountsForm()
    return render(request, 'account/account.html', {'form': account})


def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            # Do any additional processing or redirects here
            return redirect('home')  # Replace 'home' with the appropriate URL name
    else:
        form = PaymentForm()
    return render(request, 'account/payment.html', {'form': form})


def agent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agent/agent.html')  # Replace 'home' with the appropriate URL name
    else:
        form = AgentForm()

    return render(request, 'agent/agent.html', {'form': form})


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
            return redirect("home")
        else:
            messages.success(request, "There was an Error, Please try again")
            return redirect('home')
    else:
        return render(request, 'agent/agent_data.html', {'agent_records': agent_records})


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

            return redirect('home')  # Redirect to a page after successful upload
    return render(request, 'inquiry/upload_inquiry.html')


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

            return redirect('upload_account')  # Redirect to a page after successful upload
    return render(request, 'account/upload_account.html')


def download_xlsx(request):
    # Fetch data from MySQL
    queryset = Add_Inquiry.objects.all()

    # Convert queryset to a pandas DataFrame
    data = pd.DataFrame(list(queryset.values()))

    # Ensure datetime columns are timezone unaware
    date_columns = ['created_date']  # Adjust with your datetime column names
    for col in date_columns:
        if col in data.columns:
            data[col] = data[col].dt.tz_localize(None)  # Convert to timezone-unaware

    # Create a BytesIO buffer to write the Excel file
    # buffer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
    date_time = datetime.now().strftime('%Y%m%d_%H%M%S')  # Format: YYYYMMDD_HHMMSS
    file_name = f"InquiryData_{date_time}.xlsx"
    data.to_excel(file_name, index=False,engine="openpyxl")

    # Save the ExcelWriter object to a file
    # buffer.save()

    # Open the saved file for reading
    file_path = file_name
    with open(file_path, 'rb') as excel:
        # Prepare response with appropriate content type
        response = HttpResponse(excel.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response

class ManageModelsView(View):
    def get(self, request):
        # Initialize all forms
        project_form = ProjectForm()
        field_form = FieldForm()
        inquiry_type_form = Inquiry_TypeForm()
        inquiry_stage_form = Inquiry_StageForm()
        selected_unit_form = Selected_UnitForm()
        assign_to_form = Assign_ToForm()
        payment_terms_form = Payment_TermsForm()
        payment_type_form = Payment_TypeForm()

        # Get all existing objects from each model
        project_forms = Project_Name.objects.all()
        field_forms = Fields.objects.all()
        inquiry_type_forms = Inquiry_Type.objects.all()
        inquiry_stage_forms = Inquiry_Stage.objects.all()
        selected_unit_forms = Selected_Unit.objects.all()
        assign_to_forms = Assign_To.objects.all()
        payment_terms_forms = Payment_Terms.objects.all()
        payment_type_forms = Payment_Type.objects.all()

        # Render the form page with all form instances and existing objects
        return render(request, 'manage_models.html', {
            'project_form': project_form,
            'field_form': field_form,
            'inquiry_type_form': inquiry_type_form,
            'inquiry_stage_form': inquiry_stage_form,
            'selected_unit_form': selected_unit_form,
            'assign_to_form': assign_to_form,
            'payment_terms_form': payment_terms_form,
            'payment_type_form': payment_type_form,
            'project_forms': project_forms,
            'field_forms': field_forms,
            'inquiry_type_forms': inquiry_type_forms,
            'inquiry_stage_forms': inquiry_stage_forms,
            'selected_unit_forms': selected_unit_forms,
            'assign_to_forms': assign_to_forms,
            'payment_terms_forms': payment_terms_forms,
            'payment_type_forms': payment_type_forms,
        })

    def post(self, request):
        # Dictionary mapping form names to their corresponding form classes
        form_instances = {
            'project_form': ProjectForm,
            'field_form': FieldForm,
            'inquiry_type_form': Inquiry_TypeForm,
            'inquiry_stage_form': Inquiry_StageForm,
            'selected_unit_form': Selected_UnitForm,
            'assign_to_form': Assign_ToForm,
            'payment_terms_form': Payment_TermsForm,
            'payment_type_form': Payment_TypeForm,
        }

        # Check which form was submitted
        for form_name, form_class in form_instances.items():
            if form_name in request.POST:
                form = form_class(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('manage_models')

        # If no form was submitted or form is invalid, render the page with all forms
        return render(request, 'manage_models.html', {
            'project_form': ProjectForm(),
            'field_form': FieldForm(),
            'inquiry_type_form': Inquiry_TypeForm(),
            'inquiry_stage_form': Inquiry_StageForm(),
            'selected_unit_form': Selected_UnitForm(),
            'assign_to_form': Assign_ToForm(),
            'payment_terms_form': Payment_TermsForm(),
            'payment_type_form': Payment_TypeForm(),
            'project_forms': Project_Name.objects.all(),
            'field_forms': Fields.objects.all(),
            'inquiry_type_forms': Inquiry_Type.objects.all(),
            'inquiry_stage_forms': Inquiry_Stage.objects.all(),
            'selected_unit_forms': Selected_Unit.objects.all(),
            'assign_to_forms': Assign_To.objects.all(),
            'payment_terms_forms': Payment_Terms.objects.all(),
            'payment_type_forms': Payment_Type.objects.all(),
        })


def delete_object(request, object_type, object_id):
    # Define a dictionary mapping object types to their corresponding models
    object_models = {
        'project': Project_Name,
        'field': Fields,
        'inquiry_type': Inquiry_Type,
        'inquiry_stage':Inquiry_Stage,
        'unit':Selected_Unit,
        'assign_to':Assign_To,
        'payment_terms':Payment_Terms,
        'payment_type':Payment_Type,
    }
    
    # Retrieve the appropriate model based on the object type
    model = object_models.get(object_type)
    
    if not model:
        # Handle invalid object types gracefully
        return render(request, 'manage_models.html', {'error_message': 'Invalid object type'})
    
    # Retrieve the object instance using the provided object_id
    obj = get_object_or_404(model, pk=object_id)
    
    if request.method == 'POST':
        # If the request is a POST (typically from a form submission), proceed with deletion
        obj.delete()
        return redirect('manage_models')  # Redirect to a success URL after deletion

    # If the request is not a POST (e.g., GET request), render a confirmation template
    return render(request, 'confirm_delete.html', {'object': obj, 'object_type': object_type})


def update_project(request, project_id):
    # Retrieve the project instance to be updated from the database
    project = get_object_or_404(Project_Name, pk=project_id)

    if request.method == 'POST':
        # Create a form instance and populate it with the POST data and existing instance
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            # Save the updated project object to the database
            form.save()
            # Redirect to a success URL (e.g., project detail page) after updating
            return redirect('manage_models', project_id=project_id)
    else:
        # If it's a GET request, pre-fill the form with the existing project data
        form = ProjectForm(instance=project)


def update_follow_up(request, unique_key):
    follow_up_instance = get_object_or_404(Add_Inquiry, id=unique_key)

    if request.method == 'POST':
        followupform = FollowUpUpdateForm(request.POST, instance=follow_up_instance)
        if followupform.is_valid():
            followupform.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': followupform.errors}, status=400)
    
    followupform = FollowUpUpdateForm(instance=follow_up_instance)
    return render(request, 'update_remarks_modal.html', {'followupform': followupform, 'unique_key': unique_key})