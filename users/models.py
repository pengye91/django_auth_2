from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    is_doctor = models.BooleanField(default=False, blank=False)
    department = models.CharField(max_length=120, blank=False)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        permissions = (
            ('view_doctor', 'Can view doctor profile'),
        )

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_email(self):
        return self.user.email

    def get_patients(self):
        patients_objects = self.patients.all()
        patients_list = [patient for patient in patients_objects]
        return patients_list


class Contact(models.Model):
    contact_name = models.CharField(max_length=120, blank=False, unique=True)
    # whose_contact = models.OneToOneField(Patient, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    is_patient = models.BooleanField(default=False, blank=False)
    treated_by = models.ForeignKey(Doctor, related_name='patients', blank=False)
    contact = models.OneToOneField(Contact, blank=False)
    slug = models.SlugField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        permissions = (
            ('view_patient', 'Can view patients.'),
        )

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_email(self):
        return self.user.email
