# from django.db import models
# from django.contrib.auth.models import User



# departments=[('Cardiologist','Cardiologist'),
# ('Dermatologists','Dermatologists'),
# ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
# ('Allergists/Immunologists','Allergists/Immunologists'),
# ('Anesthesiologists','Anesthesiologists'),
# ('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
# ]
# class Doctor(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20,null=True)
#     department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
#     status=models.BooleanField(default=False)
#     @property
#     def get_name(self):
#         return self.user.first_name+" "+self.user.last_name
#     @property
#     def get_id(self):
#         return self.user.id
#     def __str__(self):
#         return "{} ({})".format(self.user.first_name,self.department)



# class Patient(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20,null=False)
#     symptoms = models.CharField(max_length=100,null=False)
#     assignedDoctorId = models.PositiveIntegerField(null=True)
#     admitDate=models.DateField(auto_now=True)
#     status=models.BooleanField(default=False)
#     @property
#     def get_name(self):
#         return self.user.first_name+" "+self.user.last_name
#     @property
#     def get_id(self):
#         return self.user.id
#     def __str__(self):
#         return self.user.first_name+" ("+self.symptoms+")"


# class Appointment(models.Model):
#     patientId=models.PositiveIntegerField(null=True)
#     doctorId=models.PositiveIntegerField(null=True)
#     patientName=models.CharField(max_length=40,null=True)
#     doctorName=models.CharField(max_length=40,null=True)
#     appointmentDate=models.DateField(auto_now=True)
#     description=models.TextField(max_length=500)
#     status=models.BooleanField(default=False)



# class PatientDischargeDetails(models.Model):
#     patientId=models.PositiveIntegerField(null=True)
#     patientName=models.CharField(max_length=40)
#     assignedDoctorName=models.CharField(max_length=40)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20,null=True)
#     symptoms = models.CharField(max_length=100,null=True)

#     admitDate=models.DateField(null=False)
#     releaseDate=models.DateField(null=False)
#     daySpent=models.PositiveIntegerField(null=False)

#     roomCharge=models.PositiveIntegerField(null=False)
#     medicineCost=models.PositiveIntegerField(null=False)
#     doctorFee=models.PositiveIntegerField(null=False)
#     OtherCharge=models.PositiveIntegerField(null=False)
#     total=models.PositiveIntegerField(null=False)






































# from django.db import models
# from django.contrib.auth.models import User

# # departments = [
# #     ('Cardiologist', 'Cardiologist'),
# #     ('Dermatologists', 'Dermatologists'),
# #     ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
# #     ('Allergists/Immunologists', 'Allergists/Immunologists'),
# #     ('Anesthesiologists', 'Anesthesiologists'),
# #     ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
# # ]

# departments = [
#     ('Cardiologist', 'Cardiologist'),
#     ('Dermatologists', 'Dermatologists'),
#     ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
#     ('Allergists/Immunologists', 'Allergists/Immunologists'),
#     ('Anesthesiologists', 'Anesthesiologists'),
#     ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'),
#     ('Neurologists', 'Neurologists'),
#     ('Psychiatrists', 'Psychiatrists'),
#     ('Orthopedic Surgeons', 'Orthopedic Surgeons'),
#     ('Pediatricians', 'Pediatricians'),
#     ('Gynecologists', 'Gynecologists'),
#     ('Endocrinologists', 'Endocrinologists'),
#     ('Oncologists', 'Oncologists'),
#     ('Ophthalmologists', 'Ophthalmologists'),
#     ('Otolaryngologists (ENT)', 'Otolaryngologists (ENT)'),
#     ('Nephrologists', 'Nephrologists'),
#     ('Pulmonologists', 'Pulmonologists'),
#     ('Rheumatologists', 'Rheumatologists'),
#     ('Gastroenterologists', 'Gastroenterologists'),
#     ('General Surgeons', 'General Surgeons')
# ]


# class Doctor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20, null=True)
#     department = models.CharField(max_length=50, choices=departments, default='Cardiologist')
#     status = models.BooleanField(default=False)

#     @property
#     def get_name(self):
#         return f"{self.user.first_name} {self.user.last_name}"

#     @property
#     def get_id(self):
#         return self.user.id

#     def __str__(self):
#         return "{} ({})".format(self.user.first_name, self.department)


# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20, null=False)
#     symptoms = models.CharField(max_length=100, null=False)
#     assignedDoctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)  # ForeignKey instead of PositiveIntegerField
    
#     admitDate = models.DateField(auto_now=True)
#     status = models.BooleanField(default=False)

#     @property
#     def get_name(self):
#         return f"{self.user.first_name} {self.user.last_name}"

#     @property
#     def get_id(self):
#         return self.user.id

#     def __str__(self):
#         return f"{self.user.first_name} ({self.symptoms})"


# class Appointment(models.Model):
#     patientId = models.PositiveIntegerField(null=True)
#     doctorId = models.PositiveIntegerField(null=True)
#     patientName = models.CharField(max_length=40, null=True)
#     doctorName = models.CharField(max_length=40, null=True)
#     appointmentDate = models.DateField(auto_now=True)
#     description = models.TextField(max_length=500)
#     status = models.BooleanField(default=False)


# class PatientDischargeDetails(models.Model):
#     patientId = models.PositiveIntegerField(null=True)
#     patientName = models.CharField(max_length=40)
#     assignedDoctorName = models.CharField(max_length=40)
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20, null=True)
#     symptoms = models.CharField(max_length=100, null=True)
#     admitDate = models.DateField(null=False)
#     releaseDate = models.DateField(null=False)
#     daySpent = models.PositiveIntegerField(null=False)
#     roomCharge = models.PositiveIntegerField(null=False)
#     medicineCost = models.PositiveIntegerField(null=False)
#     doctorFee = models.PositiveIntegerField(null=False)
#     OtherCharge = models.PositiveIntegerField(null=False)
#     total = models.PositiveIntegerField(null=False)





from django.db import models
from django.contrib.auth.models import User

departments = [
    ('Cardiologist', 'Cardiologist'),
    ('Dermatologists', 'Dermatologists'),
    ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
    ('Allergists/Immunologists', 'Allergists/Immunologists'),
    ('Anesthesiologists', 'Anesthesiologists'),
    ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'),
    ('Neurologists', 'Neurologists'),
    ('Psychiatrists', 'Psychiatrists'),
    ('Orthopedic Surgeons', 'Orthopedic Surgeons'),
    ('Pediatricians', 'Pediatricians'),
    ('Gynecologists', 'Gynecologists'),
    ('Endocrinologists', 'Endocrinologists'),
    ('Oncologists', 'Oncologists'),
    ('Ophthalmologists', 'Ophthalmologists'),
    ('Otolaryngologists (ENT)', 'Otolaryngologists (ENT)'),
    ('Nephrologists', 'Nephrologists'),
    ('Pulmonologists', 'Pulmonologists'),
    ('Rheumatologists', 'Rheumatologists'),
    ('Gastroenterologists', 'Gastroenterologists'),
    ('General Surgeons', 'General Surgeons')
]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(max_length=50, choices=departments, default='Cardiologist')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    symptoms = models.CharField(max_length=100, null=False)
    assignedDoctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)

    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return f"{self.user.first_name} ({self.symptoms})"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    patientName = models.CharField(max_length=40, null=True)
    doctorName = models.CharField(max_length=40, null=True)
    appointmentDate = models.DateField(auto_now=True)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patientName} with {self.doctorName} on {self.appointmentDate}"


class PatientDischargeDetails(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    patientName = models.CharField(max_length=40)
    assignedDoctorName = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=100, null=True)
    admitDate = models.DateField(null=False)
    releaseDate = models.DateField(null=False)
    daySpent = models.PositiveIntegerField(null=False)

    roomCharge = models.PositiveIntegerField(null=False)
    medicineCost = models.PositiveIntegerField(null=False)
    doctorFee = models.PositiveIntegerField(null=False)
    otherCharge = models.PositiveIntegerField(null=False)
    total = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f"{self.patientName} discharged on {self.releaseDate}"

