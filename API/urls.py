from django.urls import path
from . import views

urlpatterns = [


    path('listAppointment', views.getAppointment, name='list-appointment'),
    path('bookAppointment', views.createAppointment, name='book-appointment'),
    path('updateAppointment/<int:pk>', views.updateAppointment,
         name='update-appointment'),

    path('listPatient', views.getPatient, name='list-patient'),
    path('addPatient', views.createPatient, name='add-patient'),
    path('updatePatient/<int:pk>', views.updatePatient, name='update-patient'),


    path('listDoctor', views.getDoctor, name='list-doctor'),
    path('addDoctor', views.createDoctor, name='add-doctor'),
    path('updateDoctor/<int:pk>', views.updateDoctor, name='update-doctor'),

    path('listAdmin', views.getAdmin, name='list-Admin'),
    path('addAdmin', views.createAdmin, name='add-Admin'),
    path('updateAdmin/<int:pk>', views.updateAdmin, name='update-Admin'),
    path('authAdmin', views.authAdmin, name='auth-Admin'),

]
