from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from guardian.admin import GuardedModelAdmin
from .models import Doctor, Patient, Contact


# Register your models here.
# class UserAdmin(GuardedModelAdmin):
#     prepopulated_fields = {"slug": ("username",)}
#     list_display = ("username", "email", "title", "created_at",)
#     search_fields = ('title', "username")
#     ordering = ('created_at',)
#     date_hierarchy = 'created_at'
#
#
# admin.site.register(User, UserAdmin)


class DoctorInline(admin.StackedInline):
    model = Doctor
    can_delete = False
    verbose_name = 'Doctor'
    verbose_name_plural = 'Doctors'


class PatientInline(admin.StackedInline):
    model = Patient
    can_delete = False
    verbose_name = 'Patient'
    verbose_name_plural = 'Patients'


class UserAdmin(GuardedModelAdmin):
    inlines = (DoctorInline, PatientInline,)


class PatientAdmin(GuardedModelAdmin):
    # prepopulated_fields = {"slug": ("get_username",)}
    list_display = ("get_username", "get_email", "treated_by", "created_at",)
    search_fields = ('get_username', "treated_by",)
    ordering = ('created_at',)
    date_hierarchy = 'created_at'


admin.site.register(Patient, PatientAdmin)


class DoctorAdmin(GuardedModelAdmin):
    # prepopulated_fields = {"slug": ("get_username",)}
    list_display = ("get_username", "get_email", "department", "get_patients", "title", "created_at",)
    search_fields = ('get_username', "department",)
    ordering = ('created_at',)
    date_hierarchy = 'created_at'


admin.site.register(Doctor, DoctorAdmin)


class ContactAdmin(GuardedModelAdmin):
    list_display = ("contact_name", "created_at",)
    search_fields = ("contact_name",)
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Contact, ContactAdmin)
