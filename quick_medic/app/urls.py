from django.urls import path, include

from .views import (
    Home,
    CreateDoctor, DoctorDetail, DoctorList, RemoveDoctor, UpdateDoctor,
    CreateRequest, RequestDetail, RequestList, RemoveRequest, UpdateRequest,
    CreateAppointment, AppointmentDetail, AppointmentList, RemoveAppointment, UpdateAppointment,
    CreateSpecialization, SpecializationDetail, SpecializationList, RemoveSpecialization, UpdateSpecialization,
)

urlpatterns = [
    path('', Home.as_view(), name="home"),

    # DOCTORS URLS
    path('doctor/', include(
        [
            path('create', CreateDoctor.as_view(), name="create_doctor"),
            path('<pk>', DoctorDetail.as_view(), name="doctor_detail"),
            path('<pk>/remove', RemoveDoctor.as_view(), name="doctor_remove"),
            path('<pk>/update', UpdateDoctor.as_view(), name="doctor_update"),
            path('list', DoctorList.as_view(), name="doctor_list"),
        ])),

    # REQUESTCONSULTANCY URLS
    path('request/', include(
        [
            path('create', CreateRequest.as_view(), name="create_request"),
            path('<pk>', RequestDetail.as_view(), name="request_detail"),
            path('<pk>/remove', RemoveRequest.as_view(), name="request_remove"),
            path('<pk>/update', CreateRequest.as_view(), name="request_update"),
            path('list', DoctorList.as_view(), name="doctor_List"),
        ])),


    # APPOINTMENT URLS
    path('appointment/', include(
        [
            path('create', CreateAppointment.as_view(), name="appointment_create"),
            path('<pk>', AppointmentDetail.as_view(), name="appointment_detail"), 
            path('<pk>/remove', RemoveAppointment.as_view(), name="appointment_remove"), 
            path('<pk>/update', UpdateAppointment.as_view(), name="appointment_update"), 
            path('list', AppointmentList.as_view(), name="appointment_list"), 
        ])),


    # SPECIALIZATION URLS
    path('specialization/', include(
        [
            path('create', CreateSpecialization.as_view(), name="create_specialization"),
            path('<pk>', SpecializationDetail.as_view(), name="specialization_detail"),
            path('<pk>/remove', SpecializationList.as_view(), name="specialization_remove"),
            path('<pk>/update', SpecializationList.as_view(), name="specialization_update"),
            path('list', SpecializationList.as_view(), name="specialization_list"),
        ])),

    
]