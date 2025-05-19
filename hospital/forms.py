# from django import forms
# from django.contrib.auth.models import User
# from . import models



# #for admin signup
# class AdminSignupForm(forms.ModelForm):
#     class Meta:
#         model=User
#         # fields=['first_name','last_name','username','password']
#         fields = ['first_name', 'last_name', 'username', 'email', 'password']

#         widgets = {
#         'password': forms.PasswordInput()
#         }


# #for student related form
# class DoctorUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }
# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model=models.Doctor
#         fields=['address','mobile','department','status','profile_pic']



# #for teacher related form
# # class PatientUserForm(forms.ModelForm):
# #     class Meta:
# #         model=User
# #         fields=['first_name','last_name','username','password']
# #         widgets = {
# #         'password': forms.PasswordInput()
# #         }
# # class PatientUserForm(forms.ModelForm):
# #     class Meta:
# #         model = User
# #         fields = ['first_name', 'last_name', 'username', 'email', 'password']
# #         widgets = {
# #             'password': forms.PasswordInput(),
# #         }

# # class PatientForm(forms.ModelForm):
# #     #this is the extrafield for linking patient and their assigend doctor
# #     #this will show dropdown __str__ method doctor model is shown on html so override it
# #     #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
# #     assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
# #     class Meta:
# #         model=models.Patient
# #         fields=['address','mobile','status','symptoms','profile_pic']

# from django import forms
# from django.contrib.auth.models import User
# from . import models

# class PatientUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'password']
#         widgets = {
#             'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
#         }

#     # Additional validation can be added if needed
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("This email is already registered.")
#         return email


# # class PatientForm(forms.ModelForm):
# #     # Extra field for linking patient and their assigned doctor
# #     assignedDoctorId = forms.ModelChoiceField(
# #         queryset=models.Doctor.objects.all().filter(status=True), 
# #         empty_label="Choose Doctor (Name and Department)", 
# #         to_field_name="user_id", 
# #         required=True
# #     )

# #     class Meta:
# #         model = models.Patient
# #         fields = ['address', 'mobile', 'status', 'symptoms', 'profile_pic']
        
# #         # Optional: If you want to provide a better file input UI
# #         widgets = {
# #             'profile_pic': forms.ClearableFileInput(attrs={'multiple': True}),
# #         }
# class PatientForm(forms.ModelForm):
#     assignedDoctorId = forms.ModelChoiceField(
#         queryset=models.Doctor.objects.all().filter(status=True),
#         empty_label="Choose Doctor (Name and Department)",
#         to_field_name="user_id",
#         required=True
#     )

#     def __init__(self, *args, **kwargs):
#         super(PatientForm, self).__init__(*args, **kwargs)
#         self.fields['assignedDoctorId'].queryset = models.Doctor.objects.filter(status=True)
#         self.fields['assignedDoctorId'].label_from_instance = lambda obj: f"{obj.name} ({obj.department})"
    
#     class Meta:
#         model = models.Patient
#         fields = ['address', 'mobile', 'status', 'symptoms', 'profile_pic']

# widgets = {
#     'profile_pic': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
# }









#     # Additional validation for mobile (if required)
# def clean_mobile(self):
#         mobile = self.cleaned_data.get('mobile')
#         if len(mobile) != 10:
#             raise forms.ValidationError("Mobile number must be 10 digits.")
#         return mobile

#     # You can also add validation to ensure no profile picture is missing, if you want it mandatory
#     # def clean_profile_pic(self):
#     #     profile_pic = self.cleaned_data.get('profile_pic')
#     #     if not profile_pic:
#     #         raise forms.ValidationError("Please upload a profile picture.")
#     #     return profile_pic


# class AppointmentForm(forms.ModelForm):
#     doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
#     patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
#     class Meta:
#         model=models.Appointment
#         fields=['description','status']


# class PatientAppointmentForm(forms.ModelForm):
#     doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
#     class Meta:
#         model=models.Appointment
#         fields=['description','status']


# #for contact us page
# class ContactusForm(forms.Form):
#     Name = forms.CharField(max_length=30)
#     Email = forms.EmailField()
#     Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))








from django import forms
from django.contrib.auth.models import User
from . import models

# For admin signup
class AdminSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


# For doctor-related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['address', 'mobile', 'department', 'status', 'profile_pic']


# For patient signup
class PatientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        }




    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email






class PatientForm(forms.ModelForm):
    assignedDoctorId = forms.ModelChoiceField(
        queryset=models.Doctor.objects.filter(status=True),
        empty_label="Choose Doctor (Name and Department)",
        to_field_name="user_id",
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['assignedDoctorId'].queryset = models.Doctor.objects.filter(status=True)
        self.fields['assignedDoctorId'].label_from_instance = lambda obj: f"{obj.get_name} ({obj.department})"

    class Meta:
        model = models.Patient
        fields = ['address', 'mobile', 'status', 'symptoms', 'profile_pic']
        widgets = {
            'profile_pic': forms.ClearableFileInput(attrs={'multiple': True}),
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be 10 digits.")
        return mobile

    def save(self, commit=True):
        patient = super().save(commit=False)
        # Assign the model's assignedDoctor field from the form field assignedDoctorId
        patient.assignedDoctor = self.cleaned_data['assignedDoctorId']
        if commit:
            patient.save()
        return patient

# class PatientForm(forms.ModelForm):
#     assignedDoctorId = forms.ModelChoiceField(
#         queryset=models.Doctor.objects.all().filter(status=True),
#         empty_label="Choose Doctor (Name and Department)",
#         to_field_name="user_id",
#         required=True
#     )

#     def __init__(self, *args, **kwargs):
#         super(PatientForm, self).__init__(*args, **kwargs)
#         self.fields['assignedDoctorId'].queryset = models.Doctor.objects.filter(status=True)
#         self.fields['assignedDoctorId'].label_from_instance = lambda obj: f"{obj.get_name} ({obj.department})"
    
#     class Meta:
#         model = models.Patient
#         fields = ['address', 'mobile', 'status', 'symptoms', 'profile_pic']

#     # Optional: If you want to provide a better file input UI
#     widgets = {
#         'profile_pic': forms.ClearableFileInput(attrs={'multiple': True}),
#     }

#     # Additional validation for mobile (if required)
#     def clean_mobile(self):
#         mobile = self.cleaned_data.get('mobile')
#         if len(mobile) != 10:
#             raise forms.ValidationError("Mobile number must be 10 digits.")
#         return mobile


class AppointmentForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True), empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId = forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True), empty_label="Patient Name and Symptoms", to_field_name="user_id")
    
    class Meta:
        model = models.Appointment
        fields = ['description', 'status']


class PatientAppointmentForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True), empty_label="Doctor Name and Department", to_field_name="user_id")
    
    class Meta:
        model = models.Appointment
        fields = ['description', 'status']


# For the contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

