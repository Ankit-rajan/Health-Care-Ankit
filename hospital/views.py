from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
# Import necessary views
from hospital import views  # This imports the views.py file
from .forms import PatientUserForm, PatientForm
from hospital import views



# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/index.html')


#for showing signup/login button for admin(by Ankit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/adminclick.html')


#for showing signup/login button for doctor(by Ankit)
def doctorclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/doctorclick.html')


#for showing signup/login button for patient(by Ankit)
def patientclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/patientclick.html')



# change no.2

# def admin_signup_view(request):
#     form=forms.AdminSigupForm()
#     if request.method=='POST':
#         form=forms.AdminSigupForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             user.set_password(user.password)
#             user.save()
#             my_admin_group = Group.objects.get_or_create(name='ADMIN')
#             my_admin_group[0].user_set.add(user)
#             return HttpResponseRedirect('adminlogin')
#     return render(request,'hospital/adminsignup.html',{'form':form})

# from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth.models import Group
# from . import forms
# from django.contrib import messages
# from django.core.mail import send_mail
# from django.shortcuts import render, redirect
# from django.conf import settings
# from . import forms
# from django.contrib.auth.models import Group

def admin_signup_view(request):
    form = forms.AdminSignupForm()

    if request.method == 'POST':
        form = forms.AdminSignupForm(request.POST)
        if form.is_valid():
            # Check if the username already exists
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.warning(request, "Username already exists. Please choose a different one.")
                return render(request, 'hospital/adminsignup.html', {'form': form})

            # Save the user and set the password
            user = form.save(commit=False)
            user.set_password(user.password)  # Hash the password before saving
            user.save()

            # Assign the user to the 'ADMIN' group
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            # Send confirmation email to the new admin user
            subject = "Admin Account Created"
            message = f"Hello {user.first_name},\n\nYour admin account has been successfully created! You can now log in using your credentials.\n\nBest regards,\nHealth Care Management Team"
            
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            # Success message
            messages.success(request, "Admin registered successfully! Please log in.")
            return redirect('adminlogin')

        else:
            # Optional: Print form errors for debugging (can be removed in production)
            print(form.errors)
            messages.error(request, "Please correct the errors below.")

    return render(request, 'hospital/adminsignup.html', {'form': form})







#admin login view


#     def get(self, request):
#         form = AuthenticationForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = AuthenticationForm(request, data=request.POST)

#         if form.is_valid():
#             # Authenticate the user
#             user = form.get_user()
#             login(request, user)
            
#             # Send confirmation email to the admin user
#             subject = "Admin Login Successful"
#             message = f"Hello {user.first_name},\n\nYou have successfully logged in to the Hospital Management System.\n\nBest regards,\nHospital Management System"
            
#             send_mail(
#                 subject,
#                 message,
#                 settings.EMAIL_HOST_USER,  # The email address configured in settings.py
#                 [user.email],  # Send the email to the admin's registered email
#                 fail_silently=False,
#             )
            
#             # Display success message
#             messages.success(request, "Login successful! A confirmation email has been sent to your email address.")

#             # Redirect to the admin dashboard or any other page after login
#             return redirect('admin-dashboard')  # Change this to the appropriate view

#         # If form is not valid, re-render the page with form errors
#         messages.error(request, "Invalid username or password.")
#         return render(request, self.template_name, {'form': form})

# class AdminLoginConfirmationView(View):
#     template_name = 'hospital/adminlogin.html'

# def get(self, request):
#     # When the login page is first loaded (GET request),
#     # we simply create an empty login form
#     form = AuthenticationForm()

#     # show_messages is False because we don't want to show any messages on initial load
#     return render(request, self.template_name, {
#         'form': form,
#         'show_messages': False
#     })

# def post(self, request):
#     # When the form is submitted (POST request),
#     # bind the form with submitted data
#     form = AuthenticationForm(request, data=request.POST)

#     if form.is_valid():
#         # If form credentials are correct, authenticate the user
#         user = form.get_user()
#         login(request, user)

#         # Prepare and send a confirmation email after successful login
#         subject = "Admin Login Successful"
#         message = (
#             f"Hello {user.first_name},\n\n"
#             "You have successfully logged in to the Hospital Management System.\n\n"
#             "Best regards,\nHospital Management System"
#         )
#         send_mail(
#             subject,
#             message,
#             settings.EMAIL_HOST_USER,  # Sender (configured in settings)
#             [user.email],              # Recipient (admin's email)
#             fail_silently=False
#         )

#         # Show a success message (this will display on the next page after redirect)
#         messages.success(request, "Login successful! A confirmation email has been sent to your email address.")

#         # Redirect to the admin dashboard after login — prevents form from resubmitting and avoids showing login form again
#         return redirect('admin-dashboard')

#     # If login fails (invalid credentials), re-render the login page
#     # and show an error message
#     messages.error(request, "Invalid username or password.")
#     return render(request, self.template_name, {
#         'form': form,
#         'show_messages': True  # Allow messages to be shown after POST
#     })

# class AdminLoginConfirmationView(View):
#     template_name = 'hospital/adminlogin.html'

#     def get(self, request):
#         # When the login page is first loaded (GET request),
#         # we simply create an empty login form
#         form = AuthenticationForm()

#         # show_messages is False because we don't want to show any messages on initial load
#         return render(request, self.template_name, {
#             'form': form,
#             'show_messages': False
#         })

#     def post(self, request):
#         # When the form is submitted (POST request),
#         # bind the form with submitted data
#         form = AuthenticationForm(request, data=request.POST)

#         if form.is_valid():
#             # If form credentials are correct, authenticate the user
#             user = form.get_user()
#             login(request, user)

#             # Prepare and send a confirmation email after successful login
#             subject = "Admin Login Successful"
#             message = (
#                 f"Hello {user.first_name},\n\n"
#                 "You have successfully logged in to the Hospital Management System.\n\n"
#                 "Best regards,\nHospital Management System"
#             )
#             send_mail(
#                 subject,
#                 message,
#                 settings.EMAIL_HOST_USER,  # Sender (configured in settings)
#                 [user.email],              # Recipient (admin's email)
#                 fail_silently=False
#             )

#             # Show a success message (this will display on the next page after redirect)
#             messages.success(request, "Login successful! A confirmation email has been sent to your email address.")

#             # Redirect to the admin dashboard after login — prevents form from resubmitting and avoids showing login form again
#             return redirect('admin-dashboard')

#         # If login fails (invalid credentials), re-render the login page
#         # and show an error message
#         messages.error(request, "Invalid username or password.")
#         return render(request, self.template_name, {
#             'form': form,
#             'show_messages': True  # Allow messages to be shown after POST
#         })


# class AdminLoginConfirmationView(View):
#     template_name = 'hospital/adminlogin.html'

#     def get(self, request):
#         # When the login page is first loaded (GET request),
#         # we simply create an empty login form
#         form = AuthenticationForm()

#         # show_messages is False because we don't want to show any messages on initial load
#         return render(request, self.template_name, {
#             'form': form,
#             'show_messages': False
#         })

#     def post(self, request):
#         # When the form is submitted (POST request),
#         # bind the form with submitted data
#         form = AuthenticationForm(request, data=request.POST)

#         if form.is_valid():
#             # If form credentials are correct, authenticate the user
#             user = form.get_user()
#             login(request, user)

#             # Prepare and send a confirmation email after successful login
#             subject = "Admin Login Successful"
#             message = (
#                 f"Hello {user.first_name},\n\n"
#                 "You have successfully logged in to the Hospital Management System.\n\n"
#                 "Best regards,\nHospital Management System"
#             )
#             send_mail(
#                 subject,
#                 message,
#                 settings.EMAIL_HOST_USER,  # Sender (configured in settings)
#                 [user.email],              # Recipient (admin's email)
#                 fail_silently=False
#             )

#             # Add success message for Toastr
#             messages.success(request, "Login successful! A confirmation email has been sent to your email address.")

#             # Redirect to the admin dashboard after login — prevents form from resubmitting and avoids showing login form again
#             return redirect('admin-dashboard')

#         # If login fails (invalid credentials), re-render the login page and show an error message
#         messages.error(request, "Invalid username or password.")
#         return render(request, self.template_name, {
#             'form': form,
#             'show_messages': True  # Allow messages to be shown after POST
#         })
class AdminLoginConfirmationView(View):
    template_name = 'hospital/adminlogin.html'

    def get(self, request):
        # Create an empty login form when the login page is first loaded
        form = AuthenticationForm()

        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            # Authenticate the user and log them in
            user = form.get_user()
            login(request, user)

            # Prepare and send confirmation email
            subject = "Admin Login Successful"
            message = (
                f"Hello {user.first_name},\n\n"
                "You have successfully logged in to the Hospital Management System.\n\n"
                "Best regards,\nHospital Management System"
            )
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # Sender (configured in settings)
                [user.email],              # Recipient (admin's email)
                fail_silently=False
            )

            # Add success message for Toastr
            messages.success(request, "Login successful! A confirmation email has been sent to your email address.")

            # Redirect to the admin dashboard after successful login
            return redirect('admin-dashboard')

        # If login fails, add error message
        messages.error(request, "Invalid username or password.")
        return render(request, self.template_name, {
            'form': form
        })




def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request,'hospital/doctorsignup.html',context=mydict)


# def patient_signup_view(request):
#     userForm=forms.PatientUserForm()
#     patientForm=forms.PatientForm()
#     mydict={'userForm':userForm,'patientForm':patientForm}
#     if request.method=='POST':
#         userForm=forms.PatientUserForm(request.POST)
#         patientForm=forms.PatientForm(request.POST,request.FILES)
#         if userForm.is_valid() and patientForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             patient=patientForm.save(commit=False)
#             patient.user=user
#             patient.assignedDoctorId=request.POST.get('assignedDoctorId')
#             patient=patient.save()
#             my_patient_group = Group.objects.get_or_create(name='PATIENT')
#             my_patient_group[0].user_set.add(user)
#         return HttpResponseRedirect('patientlogin')
#     return render(request,'hospital/patientsignup.html',context=mydict)



# def patient_signup_view(request):
#     userForm = forms.PatientUserForm()
#     patientForm = forms.PatientForm()
#     mydict = {'userForm': userForm, 'patientForm': patientForm}
    
#     if request.method == 'POST':
#         userForm = forms.PatientUserForm(request.POST)
#         patientForm = forms.PatientForm(request.POST, request.FILES)
        
#         if userForm.is_valid() and patientForm.is_valid():
#             # Save the user
#             user = userForm.save()
#             user.set_password(user.password)
#             user.save()
            
#             # Save the patient (but don't commit to DB yet, to link the user)
#             patient = patientForm.save(commit=False)
#             patient.user = user
#             patient.assignedDoctorId = request.POST.get('assignedDoctorId')
#             patient.save()  # Save the patient object

#             # Add the user to the 'PATIENT' group
#             my_patient_group = Group.objects.get_or_create(name='PATIENT')
#             my_patient_group[0].user_set.add(user)
            
#             # Send the email
#             send_mail(
#                 subject='Welcome to Our Hospital',
#                 message=f"Dear {user.first_name},\n\nThank you for registering with our Hospital Management System. Your assigned doctor will review your profile shortly.\n\nBest regards,\nHospital Admin",
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 recipient_list=[user.email],
#                 fail_silently=False,
#             )

#         return HttpResponseRedirect('patientlogin')
    
#     return render(request, 'hospital/patientsignup.html', context=mydict)



def patient_signup_view(request):
    userForm = forms.PatientUserForm()
    patientForm = forms.PatientForm()
    mydict = {'userForm': userForm, 'patientForm': patientForm}
    
    if request.method == 'POST':
        userForm = forms.PatientUserForm(request.POST)
        patientForm = forms.PatientForm(request.POST, request.FILES)
        
        if userForm.is_valid() and patientForm.is_valid():
            # Save the user
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            
            # Save the patient (but don't commit to DB yet, to link the user)
            patient = patientForm.save(commit=False)
            patient.user = user
            patient.assignedDoctorId = request.POST.get('assignedDoctorId')
            patient.save()  # Save the patient object

            # Add the user to the 'PATIENT' group
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
            
            # Send the professional email
            send_mail(
                subject='Welcome to Our Hospital Management System',
                message=f"""
                Dear {user.first_name} {user.last_name},
                
                We are pleased to inform you that your registration at our hospital has been successfully completed.
                Your assigned doctor will review your profile shortly. You will be notified for further actions regarding your treatment.
                
                If you have any questions or require assistance, feel free to reach out to us at any time.
                
                Best regards,
                Hospital Management Team
                {settings.HOSPITAL_NAME}
                Contact Us: {settings.HOSPITAL_CONTACT}
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

        return HttpResponseRedirect('patientlogin')
    
    return render(request, 'hospital/patientsignup.html', context=mydict)




#-----------for checking user is doctor , patient or admin(by Ankit)
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR OR PATIENT
def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_doctor(request.user):
        accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('doctor-dashboard')
        else:
            return render(request,'hospital/doctor_wait_for_approval.html')
    elif is_patient(request.user):
        accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('patient-dashboard')
        else:
            return render(request,'hospital/patient_wait_for_approval.html')

   







#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard
    doctors=models.Doctor.objects.all().order_by('-id')
    patients=models.Patient.objects.all().order_by('-id')
    #for three cards
    doctorcount=models.Doctor.objects.all().filter(status=True).count()
    pendingdoctorcount=models.Doctor.objects.all().filter(status=False).count()

    patientcount=models.Patient.objects.all().filter(status=True).count()
    pendingpatientcount=models.Patient.objects.all().filter(status=False).count()

    appointmentcount=models.Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount=models.Appointment.objects.all().filter(status=False).count()
    mydict={
    'doctors':doctors,
    'patients':patients,
    'doctorcount':doctorcount,
    'pendingdoctorcount':pendingdoctorcount,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,
    'appointmentcount':appointmentcount,
    'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,'hospital/admin_dashboard.html',context=mydict)


# this view for sidebar click on admin page
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_doctor_view(request):
    return render(request,'hospital/admin_doctor.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_doctor.html',{'doctors':doctors})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_doctor_from_hospital_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()
    return redirect('admin-view-doctor')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)

    userForm=forms.DoctorUserForm(instance=user)
    doctorForm=forms.DoctorForm(request.FILES,instance=doctor)
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST,instance=user)
        doctorForm=forms.DoctorForm(request.POST,request.FILES,instance=doctor)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.status=True
            doctor.save()
            return redirect('admin-view-doctor')
    return render(request,'hospital/admin_update_doctor.html',context=mydict)




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_doctor_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor.status=True
            doctor.save()

            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-view-doctor')
    return render(request,'hospital/admin_add_doctor.html',context=mydict)




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_doctor_view(request):
    #those whose approval are needed
    doctors=models.Doctor.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_doctor.html',{'doctors':doctors})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    doctor.status=True
    doctor.save()
    return redirect(reverse('admin-approve-doctor'))


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()
    return redirect('admin-approve-doctor')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_specialisation_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_doctor_specialisation.html',{'doctors':doctors})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_patient_view(request):
    return render(request,'hospital/admin_patient.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_patient_view(request):
    patients=models.Patient.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_patient.html',{'patients':patients})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_patient_from_hospital_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('admin-view-patient')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)

    userForm=forms.PatientUserForm(instance=user)
    patientForm=forms.PatientForm(request.FILES,instance=patient)
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST,instance=user)
        patientForm=forms.PatientForm(request.POST,request.FILES,instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.status=True
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient.save()
            return redirect('admin-view-patient')
    return render(request,'hospital/admin_update_patient.html',context=mydict)





# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_add_patient_view(request):
#     userForm=forms.PatientUserForm()
#     patientForm=forms.PatientForm()
#     mydict={'userForm':userForm,'patientForm':patientForm}
#     if request.method=='POST':
#         userForm=forms.PatientUserForm(request.POST)
#         patientForm=forms.PatientForm(request.POST,request.FILES)
#         if userForm.is_valid() and patientForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()

#             patient=patientForm.save(commit=False)
#             patient.user=user
#             patient.status=True
#             patient.assignedDoctorId=request.POST.get('assignedDoctorId')
#             patient.save()

#             my_patient_group = Group.objects.get_or_create(name='PATIENT')
#             my_patient_group[0].user_set.add(user)

#         return HttpResponseRedirect('admin-view-patient')
#     return render(request,'hospital/admin_add_patient.html',context=mydict)





# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_add_patient_view(request):
#     userForm = PatientUserForm()
#     patientForm = PatientForm()
#     mydict = {'userForm': userForm, 'patientForm': patientForm}
#     if request.method == 'POST':
#         userForm = PatientUserForm(request.POST)
#         patientForm = PatientForm(request.POST, request.FILES)
#         if userForm.is_valid() and patientForm.is_valid():
#             user = userForm.save()
#             user.set_password(user.password)
#             user.save()

#             patient = patientForm.save(commit=False)
#             patient.user = user
#             patient.status = True
#             # patient.assignedDoctor is already set by patientForm.save() override
#             patient.save()

#             my_patient_group = Group.objects.get_or_create(name='PATIENT')
#             my_patient_group[0].user_set.add(user)

#             return HttpResponseRedirect('admin-view-patient')
#     return render(request, 'hospital/admin_add_patient.html', context=mydict)





@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_patient_view(request):
    userForm = PatientUserForm()
    patientForm = PatientForm()
    mydict = {'userForm': userForm, 'patientForm': patientForm}
    
    if request.method == 'POST':
        userForm = PatientUserForm(request.POST)
        patientForm = PatientForm(request.POST, request.FILES)
        
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save(commit=False)
            user.set_password(user.password)
            user.save()

            patient = patientForm.save(commit=False)
            patient.user = user
            patient.status = True
            
            # Manually assign assignedDoctor here:
            assigned_doctor = patientForm.cleaned_data.get('assignedDoctorId')
            patient.assignedDoctor = assigned_doctor
            
            patient.save()

            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)

            return HttpResponseRedirect('admin-view-patient')
    
    return render(request, 'hospital/admin_add_patient.html', context=mydict)


#------------------FOR APPROVING PATIENT BY ADMIN----------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_patient_view(request):
    #those whose approval are needed
    patients=models.Patient.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_patient.html',{'patients':patients})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    patient.status=True
    patient.save()
    return redirect(reverse('admin-approve-patient'))



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('admin-approve-patient')



#--------------------- FOR DISCHARGING PATIENT BY ADMIN START-------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_discharge_patient_view(request):
    patients=models.Patient.objects.all().filter(status=True)
    return render(request,'hospital/admin_discharge_patient.html',{'patients':patients})



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def discharge_patient_view(request,pk):
#     patient=models.Patient.objects.get(id=pk)
#     days=(date.today()-patient.admitDate) #2 days, 0:00:00
#     assignedDoctor=models.User.objects.all().filter(id=patient.assignedDoctorId)
#     d=days.days # only how many day that is 2
#     patientDict={
#         'patientId':pk,
#         'name':patient.get_name,
#         'mobile':patient.mobile,
#         'address':patient.address,
#         'symptoms':patient.symptoms,
#         'admitDate':patient.admitDate,
#         'todayDate':date.today(),
#         'day':d,
#         'assignedDoctorName':assignedDoctor[0].first_name,
#     }
#     if request.method == 'POST':
#         feeDict ={
#             'roomCharge':int(request.POST['roomCharge'])*int(d),
#             'doctorFee':request.POST['doctorFee'],
#             'medicineCost' : request.POST['medicineCost'],
#             'OtherCharge' : request.POST['OtherCharge'],
#             'total':(int(request.POST['roomCharge'])*int(d))+int(request.POST['doctorFee'])+int(request.POST['medicineCost'])+int(request.POST['OtherCharge'])
#         }
#         patientDict.update(feeDict)
#         #for updating to database patientDischargeDetails (pDD)
#         pDD=models.PatientDischargeDetails()
#         pDD.patientId=pk
#         pDD.patientName=patient.get_name
#         pDD.assignedDoctorName=assignedDoctor[0].first_name
#         pDD.address=patient.address
#         pDD.mobile=patient.mobile
#         pDD.symptoms=patient.symptoms
#         pDD.admitDate=patient.admitDate
#         pDD.releaseDate=date.today()
#         pDD.daySpent=int(d)
#         pDD.medicineCost=int(request.POST['medicineCost'])
#         pDD.roomCharge=int(request.POST['roomCharge'])*int(d)
#         pDD.doctorFee=int(request.POST['doctorFee'])
#         pDD.OtherCharge=int(request.POST['OtherCharge'])
#         pDD.total=(int(request.POST['roomCharge'])*int(d))+int(request.POST['doctorFee'])+int(request.POST['medicineCost'])+int(request.POST['OtherCharge'])
#         pDD.save()
#         return render(request,'hospital/patient_final_bill.html',context=patientDict)
#     return render(request,'hospital/patient_generate_bill.html',context=patientDict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def discharge_patient_view(request, pk):
    patient = models.Patient.objects.get(id=pk)
    days = (date.today() - patient.admitDate)
    d = days.days

    assignedDoctor = patient.assignedDoctor
    assignedDoctorName = assignedDoctor.user.first_name if assignedDoctor else "No Doctor Assigned"

    patientDict = {
        'patientId': pk,
        'name': patient.get_name,
        'mobile': patient.mobile,
        'address': patient.address,
        'symptoms': patient.symptoms,
        'admitDate': patient.admitDate,
        'todayDate': date.today(),
        'day': d,
        'assignedDoctorName': assignedDoctorName,
    }

    if request.method == 'POST':
        room_charge = int(request.POST['roomCharge'])
        doctor_fee = int(request.POST['doctorFee'])
        medicine_cost = int(request.POST['medicineCost'])
        other_charge = int(request.POST['OtherCharge'])

        total = (room_charge * d) + doctor_fee + medicine_cost + other_charge

        feeDict = {
            'roomCharge': room_charge * d,
            'doctorFee': doctor_fee,
            'medicineCost': medicine_cost,
            'OtherCharge': other_charge,
            'total': total,
        }

        patientDict.update(feeDict)

        pDD = models.PatientDischargeDetails()
        pDD.patient = patient
        pDD.patientName = patient.get_name
        pDD.assignedDoctorName = assignedDoctorName
        pDD.address = patient.address
        pDD.mobile = patient.mobile
        pDD.symptoms = patient.symptoms
        pDD.admitDate = patient.admitDate
        pDD.releaseDate = date.today()
        pDD.daySpent = d
        pDD.medicineCost = medicine_cost
        pDD.roomCharge = room_charge * d
        pDD.doctorFee = doctor_fee
        pDD.otherCharge = other_charge
        pDD.total = total
        pDD.save()

        return render(request, 'hospital/patient_final_bill.html', context=patientDict)

    return render(request, 'hospital/patient_generate_bill.html', context=patientDict)

















#--------------for discharge patient bill (pdf) download and printing
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return



# def download_pdf_view(request,pk):
#     # dischargeDetails=models.PatientDischargeDetails.objects.all().filter(patientId=pk).order_by('-id')[:1]
#     dischargeDetails = models.PatientDischargeDetails.objects.filter(patient_id=pk).order_by('-id')[:1]




#     dict={
#         'patientName':dischargeDetails[0].patientName,
#         'assignedDoctorName':dischargeDetails[0].assignedDoctorName,
#         'address':dischargeDetails[0].address,
#         'mobile':dischargeDetails[0].mobile,
#         'symptoms':dischargeDetails[0].symptoms,
#         'admitDate':dischargeDetails[0].admitDate,
#         'releaseDate':dischargeDetails[0].releaseDate,
#         'daySpent':dischargeDetails[0].daySpent,
#         'medicineCost':dischargeDetails[0].medicineCost,
#         'roomCharge':dischargeDetails[0].roomCharge,
#         'doctorFee':dischargeDetails[0].doctorFee,
#         'OtherCharge':dischargeDetails[0].OtherCharge,
#         'total':dischargeDetails[0].total,
#     }
#     return render_to_pdf('hospital/download_bill.html',dict)

def download_pdf_view(request, pk):
    dischargeDetails = models.PatientDischargeDetails.objects.filter(patient_id=pk).order_by('-id')[:1]
    if not dischargeDetails:
        # Handle case when no discharge details found (optional)
        return HttpResponse("No discharge details found for this patient.")

    discharge = dischargeDetails[0]
    context = {
        'patientName': discharge.patientName,
        'assignedDoctorName': discharge.assignedDoctorName,
        'address': discharge.address,
        'mobile': discharge.mobile,
        'symptoms': discharge.symptoms,
        'admitDate': discharge.admitDate,
        'releaseDate': discharge.releaseDate,
        'daySpent': discharge.daySpent,
        'medicineCost': discharge.medicineCost,
        'roomCharge': discharge.roomCharge,
        'doctorFee': discharge.doctorFee,
        'OtherCharge': discharge.otherCharge,
        'total': discharge.total,
    }
    return render_to_pdf('hospital/download_bill.html', context)


#-----------------APPOINTMENT START--------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_appointment_view(request):
    return render(request,'hospital/admin_appointment.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_appointment_view(request):
    appointments=models.Appointment.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_appointment.html',{'appointments':appointments})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_appointment_view(request):
    appointmentForm=forms.AppointmentForm()
    mydict={'appointmentForm':appointmentForm,}
    if request.method=='POST':
        appointmentForm=forms.AppointmentForm(request.POST)
        if appointmentForm.is_valid():
            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.patientId=request.POST.get('patientId')
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.patientName=models.User.objects.get(id=request.POST.get('patientId')).first_name
            appointment.status=True
            appointment.save()
        return HttpResponseRedirect('admin-view-appointment')
    return render(request,'hospital/admin_add_appointment.html',context=mydict)



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_appointment_view(request):
    #those whose approval are needed
    appointments=models.Appointment.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_appointment.html',{'appointments':appointments})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.status=True
    appointment.save()
    return redirect(reverse('admin-approve-appointment'))



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('admin-approve-appointment')
#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------






#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    #for three cards
    patientcount=models.Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id).count()
    appointmentcount=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
    patientdischarged=models.PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name).count()

    #for  table in doctor dashboard
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
    appointments=zip(appointments,patients)
    mydict={
    'patientcount':patientcount,
    'appointmentcount':appointmentcount,
    'patientdischarged':patientdischarged,
    'appointments':appointments,
    'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'hospital/doctor_dashboard.html',context=mydict)



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_patient_view(request):
    mydict={
    'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'hospital/doctor_patient.html',context=mydict)



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_patient_view(request):
    patients=models.Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id)
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_view_patient.html',{'patients':patients,'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_discharge_patient_view(request):
    dischargedpatients=models.PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name)
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_view_discharge_patient.html',{'dischargedpatients':dischargedpatients,'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_appointment.html',{'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_view_appointment.html',{'appointments':appointments,'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_delete_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def delete_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})



#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------






# #---------------------------------------------------------------------------------
# #------------------------ PATIENT RELATED VIEWS START ------------------------------
# #---------------------------------------------------------------------------------
# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_dashboard_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id)
#     doctor=models.Doctor.objects.get(user_id=patient.assignedDoctor)
#     mydict={
#     'patient':patient,
#     'doctorName':doctor.get_name,
#     'doctorMobile':doctor.mobile,
#     'doctorAddress':doctor.address,
#     'symptoms':patient.symptoms,
#     'doctorDepartment':doctor.department,
#     'admitDate':patient.admitDate,
#     }
#     return render(request,'hospital/patient_dashboard.html',context=mydict)



# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_appointment_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     return render(request,'hospital/patient_appointment.html',{'patient':patient})



# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_book_appointment_view(request):
#     appointmentForm=forms.PatientAppointmentForm()
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     message=None
#     mydict={'appointmentForm':appointmentForm,'patient':patient,'message':message}
#     if request.method=='POST':
#         appointmentForm=forms.PatientAppointmentForm(request.POST)
#         if appointmentForm.is_valid():
#             print(request.POST.get('doctorId'))
#             desc=request.POST.get('description')

#             doctor=models.Doctor.objects.get(user_id=request.POST.get('doctorId'))
            
#             if doctor.department == 'Cardiologist':
#                 if 'heart' in desc:
#                     pass
#                 else:
#                     print('else')
#                     message="Please Choose Doctor According To Disease"
#                     return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})


#             if doctor.department == 'Dermatologists':
#                 if 'skin' in desc:
#                     pass
#                 else:
#                     print('else')
#                     message="Please Choose Doctor According To Disease"
#                     return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

#             if doctor.department == 'Emergency Medicine Specialists':
#                 if 'fever' in desc:
#                     pass
#                 else:
#                     print('else')
#                     message="Please Choose Doctor According To Disease"
#                     return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

#             if doctor.department == 'Allergists/Immunologists':
#                 if 'allergy' in desc:
#                     pass
#                 else:
#                     print('else')
#                     message="Please Choose Doctor According To Disease"
#                     return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

#             if doctor.department == 'Anesthesiologists':
#                 if 'surgery' in desc:
#                     pass
#                 else:
#                     print('else')
#                     message="Please Choose Doctor According To Disease"
#                     return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

#             if doctor.department == 'Colon and Rectal Surgeons':
#                 if 'cancer' in desc:
#                     pass
#                 else:
#                     print('else')
#                     message="Please Choose Doctor According To Disease"
#                     return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})





#             appointment=appointmentForm.save(commit=False)
#             appointment.doctorId=request.POST.get('doctorId')
#             appointment.patientId=request.user.id #----user can choose any patient but only their info will be stored
#             appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
#             appointment.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
#             appointment.status=False
#             appointment.save()
#         return HttpResponseRedirect('patient-view-appointment')
#     return render(request,'hospital/patient_book_appointment.html',context=mydict)





# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_view_appointment_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     appointments=models.Appointment.objects.all().filter(patientId=request.user.id)
#     return render(request,'hospital/patient_view_appointment.html',{'appointments':appointments,'patient':patient})



# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_discharge_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     dischargeDetails=models.PatientDischargeDetails.objects.all().filter(patientId=patient.id).order_by('-id')[:1]
#     patientDict=None
#     if dischargeDetails:
#         patientDict ={
#         'is_discharged':True,
#         'patient':patient,
#         'patientId':patient.id,
#         'patientName':patient.get_name,
#         'assignedDoctorName':dischargeDetails[0].assignedDoctorName,
#         'address':patient.address,
#         'mobile':patient.mobile,
#         'symptoms':patient.symptoms,
#         'admitDate':patient.admitDate,
#         'releaseDate':dischargeDetails[0].releaseDate,
#         'daySpent':dischargeDetails[0].daySpent,
#         'medicineCost':dischargeDetails[0].medicineCost,
#         'roomCharge':dischargeDetails[0].roomCharge,
#         'doctorFee':dischargeDetails[0].doctorFee,
#         'OtherCharge':dischargeDetails[0].OtherCharge,
#         'total':dischargeDetails[0].total,
#         }
#         print(patientDict)
#     else:
#         patientDict={
#             'is_discharged':False,
#             'patient':patient,
#             'patientId':request.user.id,
#         }
#     return render(request,'hospital/patient_discharge.html',context=patientDict)














#---------------------------------------------------------------------------------
#------------------------ PATIENT RELATED VIEWS START ----------------------------
#---------------------------------------------------------------------------------

# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_dashboard_view(request):
#     patient = models.Patient.objects.get(user_id=request.user.id)

#     # ⚠️ POTENTIAL ISSUE:
#     # The following line assumes 'assignedDoctor' is a user_id (ForeignKey to Doctor).
#     # If your Patient model does not have a field 'assignedDoctor', this will raise an error:
#     # 'Patient' object has no attribute 'assignedDoctor'
#     # You might need to use 'assignedDoctorId' or just 'assignedDoctor' as a ForeignKey.
#     doctor = models.Doctor.objects.get(user_id=patient.assignedDoctor)

#     mydict = {
#         'patient': patient,
#         'doctorName': doctor.get_name,
#         'doctorMobile': doctor.mobile,
#         'doctorAddress': doctor.address,
#         'symptoms': patient.symptoms,
#         'doctorDepartment': doctor.department,
#         'admitDate': patient.admitDate,
#     }
#     return render(request, 'hospital/patient_dashboard.html', context=mydict)
@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    patient = models.Patient.objects.get(user_id=request.user.id)

    # Fetch the assigned doctor from the ForeignKey
    doctor = patient.assignedDoctor  # This will give you the Doctor object directly

    # Prepare the context
    mydict = {
        'patient': patient,
        'doctorName': doctor.get_name if doctor else "Not Assigned",  # Handle the case where doctor might be None
        'doctorMobile': doctor.mobile if doctor else "N/A",
        'doctorAddress': doctor.address if doctor else "N/A",
        'symptoms': patient.symptoms,
        'doctorDepartment': doctor.department if doctor else "N/A",
        'admitDate': patient.admitDate,
    }

    return render(request, 'hospital/patient_dashboard.html', context=mydict)






@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_appointment_view(request):
    patient = models.Patient.objects.get(user_id=request.user.id)  # for profile picture of patient in sidebar
    return render(request, 'hospital/patient_appointment.html', {'patient': patient})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_book_appointment_view(request):
    appointmentForm = forms.PatientAppointmentForm()
    patient = models.Patient.objects.get(user_id=request.user.id)  # for profile picture of patient in sidebar
    message = None
    mydict = {'appointmentForm': appointmentForm, 'patient': patient, 'message': message}

    if request.method == 'POST':
        appointmentForm = forms.PatientAppointmentForm(request.POST)
        if appointmentForm.is_valid():
            print(request.POST.get('doctorId'))
            desc = request.POST.get('description')

            doctor = models.Doctor.objects.get(user_id=request.POST.get('doctorId'))

            # # 🔍 Disease-to-department validation logic
            # if doctor.department == 'Cardiologist' and 'heart' not in desc:
            #     message = "Please Choose Doctor According To Disease"
            #     return render(request, 'hospital/patient_book_appointment.html', mydict)

            # if doctor.department == 'Dermatologists' and 'skin' not in desc:
            #     message = "Please Choose Doctor According To Disease"
            #     return render(request, 'hospital/patient_book_appointment.html', mydict)

            # if doctor.department == 'Emergency Medicine Specialists' and 'fever' not in desc:
            #     message = "Please Choose Doctor According To Disease"
            #     return render(request, 'hospital/patient_book_appointment.html', mydict)

            # if doctor.department == 'Allergists/Immunologists' and 'allergy' not in desc:
            #     message = "Please Choose Doctor According To Disease"
            #     return render(request, 'hospital/patient_book_appointment.html', mydict)

            # if doctor.department == 'Anesthesiologists' and 'surgery' not in desc:
            #     message = "Please Choose Doctor According To Disease"
            #     return render(request, 'hospital/patient_book_appointment.html', mydict)

            # if doctor.department == 'Colon and Rectal Surgeons' and 'cancer' not in desc:
            #     message = "Please Choose Doctor According To Disease"
            #     return render(request, 'hospital/patient_book_appointment.html', mydict)
                        
            desc = desc.lower()  # Normalize input for consistent keyword checking

            if doctor.department == 'Cardiologist' and 'heart' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Dermatologists' and 'skin' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Emergency Medicine Specialists' and 'fever' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Allergists/Immunologists' and 'allergy' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Anesthesiologists' and 'surgery' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Colon and Rectal Surgeons' and 'cancer' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Neurologists' and 'brain' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Psychiatrists' and 'mental' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Orthopedic Surgeons' and 'bone' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Pediatricians' and 'child' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Gynecologists' and 'pregnancy' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Endocrinologists' and 'hormone' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Oncologists' and 'tumor' not in desc and 'cancer' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Ophthalmologists' and 'eye' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Otolaryngologists (ENT)' and 'ear' not in desc and 'throat' not in desc and 'nose' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Nephrologists' and 'kidney' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Pulmonologists' and 'lung' not in desc or 'breath' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Rheumatologists' and 'arthritis' not in desc and 'joint' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'Gastroenterologists' and 'stomach' not in desc and 'digest' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)

            if doctor.department == 'General Surgeons' and 'operation' not in desc and 'surgery' not in desc:
                message = "Please Choose Doctor According To Disease"
                return render(request, 'hospital/patient_book_appointment.html', mydict)









            # ✅ Saving appointment
            appointment = appointmentForm.save(commit=False)
            appointment.doctorId = request.POST.get('doctorId')
            appointment.patientId = request.user.id
            appointment.doctorName = models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.patientName = request.user.first_name
            appointment.status = False
            appointment.save()

            return HttpResponseRedirect('patient-view-appointment')

    return render(request, 'hospital/patient_book_appointment.html', context=mydict)


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_appointment_view(request):
    patient = models.Patient.objects.get(user_id=request.user.id)  # for profile picture of patient in sidebar
    appointments = models.Appointment.objects.filter(patientId=request.user.id)
    return render(request, 'hospital/patient_view_appointment.html', {'appointments': appointments, 'patient': patient})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_discharge_view(request):
    patient = models.Patient.objects.get(user_id=request.user.id)  # for profile picture of patient in sidebar
    dischargeDetails = models.PatientDischargeDetails.objects.filter(patientId=patient.id).order_by('-id')[:1]
    patientDict = None

    if dischargeDetails:
        patientDict = {
            'is_discharged': True,
            'patient': patient,
            'patientId': patient.id,
            'patientName': patient.get_name,
            'assignedDoctorName': dischargeDetails[0].assignedDoctorName,
            'address': patient.address,
            'mobile': patient.mobile,
            'symptoms': patient.symptoms,
            'admitDate': patient.admitDate,
            'releaseDate': dischargeDetails[0].releaseDate,
            'daySpent': dischargeDetails[0].daySpent,
            'medicineCost': dischargeDetails[0].medicineCost,
            'roomCharge': dischargeDetails[0].roomCharge,
            'doctorFee': dischargeDetails[0].doctorFee,
            'OtherCharge': dischargeDetails[0].OtherCharge,
            'total': dischargeDetails[0].total,
        }
        print(patientDict)
    else:
        patientDict = {
            'is_discharged': False,
            'patient': patient,
            'patientId': request.user.id,
        }

    return render(request, 'hospital/patient_discharge.html', context=patientDict)

#------------------------ PATIENT RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------

# #------------------------ PATIENT RELATED VIEWS END ------------------------------
# #---------------------------------------------------------------------------------








#---------------------------------------------------------------------------------
#------------------------ ABOUT US AND CONTACT US VIEWS START ------------------------------
#---------------------------------------------------------------------------------
def aboutus_view(request):
    return render(request,'hospital/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'hospital/contactussuccess.html')
    return render(request, 'hospital/contactus.html', {'form':sub})

# from django.core.mail import send_mail
# from django.conf import settings
# from django.shortcuts import render
# from . import forms

# # About Us View
# def aboutus_view(request):
#     return render(request, 'hospital/aboutus.html')

# # Contact Us View
# def contactus_view(request):
#     sub = forms.ContactusForm()  # Initialize the form
#     if request.method == 'POST':
#         sub = forms.ContactusForm(request.POST)  # Bind data to form
#         if sub.is_valid():  # If form is valid, proceed with sending email
#             name = sub.cleaned_data['Name']
#             email = sub.cleaned_data['Email']
#             message = sub.cleaned_data['Message']

#             # Sending the email
#             try:
#                 send_mail(
#                     subject=f"Message from {name} ({email})",  # Subject
#                     message=message,  # Body of the email
#                     from_email=email,  # Sender's email
#                     recipient_list=[settings.EMAIL_RECEIVING_USER],  # Receiver's email
#                     fail_silently=False,  # If True, errors will be ignored, otherwise, they will raise exceptions
#                 )
#                 return render(request, 'hospital/contactussuccess.html')  # Success page if email is sent
#             except Exception as e:
#                 # Log or show the error if needed
#                 print(f"Error sending email: {e}")
#                 # Optionally, you can send a failure message or display an error page
#                 return render(request, 'hospital/contactus.html', {'form': sub, 'error': 'There was an issue sending your message. Please try again later.'})

#     return render(request, 'hospital/contactus.html', {'form': sub})



#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------


# aboutus_view




def aboutus_view(request):
    return render(request, 'hospital/aboutus.html')