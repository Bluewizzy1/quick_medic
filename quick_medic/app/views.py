from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

from .models import (
    Doctor,
    RequestConsultation,
    Appointment,
    Symptoms,
    Drugs,
    MedicalHistory,
    Specialization
)

# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse("This is the homepage")
    

class CreateUser(CreateView):
    model = User
    fields = ('first_name', 'last_name', 'email', 'password')
    template_name = 'app/create_user.html'
    success_url = "/accounts/login"
    # def post(self, request):
    #     content_type = ContentType.objects.get_for_model(RequestConsultation)
    #     user_permission = Permission.objects.filter(content_type = content_type)
    #     user = User(username = 'user1', first_name ='maru', last_name='koch', password='1234')
    #     user.user_permissions.add(user_permission)
    #     user.save()

    # DOCTOR VIEWS
class CreateDoctor(CreateView):
    model = Doctor
    fields = "__all__"
    exclude = ['is_verified', 'is_booked']
    success_url = "/"

class DoctorDetail(DetailView):
    model = Doctor

class DoctorList(ListView):
    model = Doctor


class RemoveDoctor(LoginRequiredMixin, DetailView):
    model = Doctor
    login_url = "/"


class UpdateDoctor(UpdateView):
    model = Doctor
    fields = "__all__"

# SPECIALIZATION VIEWS

class CreateSpecialization(CreateView):
    model = Specialization
    fields = "__all__"


class SpecializationDetail(PermissionRequiredMixin, DetailView):
    model = Specialization
    # permission_required = ['app.change_specialization']


class SpecializationList(PermissionRequiredMixin, DetailView):
    model = Specialization


class RemoveSpecialization(LoginRequiredMixin, DeleteView):
    model = Specialization


class UpdateSpecialization(UpdateView):
    model = Specialization
    fields = "__all__"

    # REQUEST VIEWS
class CreateRequest(CreateView):
    model = RequestConsultation
    fields = "__all__"
    template_name = "app/doctor_form.html"


class RequestDetail(PermissionRequiredMixin, DetailView):
    model = RequestConsultation
    permission_required = ['can_consult']

class RequestList(ListView):
    model = RequestConsultation
    login_url = "/"

class RemoveRequest(LoginRequiredMixin, DeleteView):
    model = RequestConsultation
    fields = "/"


class UpdateRequest(UpdateView):
    model = RequestConsultation
    fields = "__all__"


# APPOINTMENT VIEWS
class CreateAppointment(CreateView):
    model = Appointment
    template_name = "app.doctor_form.html"
    fields = "__all__"
    # success_url = "/"


class AppointmentDetail(PermissionRequiredMixin, DetailView):
    model = Appointment

class AppointmentList(ListView):
    model = Appointment
    login_url = "/"

class RemoveAppointment(LoginRequiredMixin, DeleteView):
    model = Appointment
    fields = "/"


class UpdateAppointment(UpdateView):
    model = Appointment
    fields = "__all__"


# MEDICAL HISTORY VIEWS

class CreateRequest(CreateView):
    model = RequestConsultation
    fields = "__all__"


class RequestDetail(PermissionRequiredMixin, DetailView):
    model = RequestConsultation

class RequestList(ListView):
    model = RequestConsultation
    login_url = "/"

class RemoveRequest(LoginRequiredMixin, DeleteView):
    model = RequestConsultation
    fields = "/"


class UpdateRequest(UpdateView):
    model = RequestConsultation
    fields = "__all__"


# APPOINTMENT VIEWS
class CreateMedicalHistory(CreateView):
    model = RequestConsultation
    fields = "__all__"


class MedicalHistoryDetail(PermissionRequiredMixin, DetailView):
    model = MedicalHistory

class MedicalHistoryList(ListView):
    model = MedicalHistory
    login_url = "/"

class RemoveMedicalHistory(LoginRequiredMixin, DeleteView):
    model = MedicalHistory
    fields = "/"


class UpdateMedicalHistory(UpdateView):
    model = MedicalHistory
    fields = "__all__"