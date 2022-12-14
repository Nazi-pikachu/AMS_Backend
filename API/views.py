from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import DocSerializer, PatientSerializer, AppointmentSerializer, AdminSerializer
from .models import Doctor, Patient, Appointment, Admin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

def apiOverview(request):
    return HttpResponse('API Overview')


# create a get method to get all the data from the Doctor model

@api_view(['GET'])
def getDoctor(request):
    # get all the data from the Doctor model
    doctor = Doctor.objects.all()
    # serialize the data
    serializer = DocSerializer(doctor, many=True)
    # return the data in json format
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createDoctor(request):

    if Doctor.objects.filter(email=request.data['email']).exists():
        return Response({'message': 'Doctor already exists'}, status=status.HTTP_400_BAD_REQUEST)

    # serialize the data
    serializer = DocSerializer(data=request.data)

    # if the data is valid
    if serializer.is_valid():
        # save the data
        serializer.save()
    # return the data in json format
    return JsonResponse(serializer.data, safe=False)


@api_view(['PATCH', 'PUT'])
def updateDoctor(request, pk):
    # get the data from the Doctor model
    try:
        doctor = Doctor.objects.get(id=pk)
    except:
        return JsonResponse({'error': 'Doctor does not exist'}, safe=False)
    # serialize the data
    serializer = DocSerializer(
        instance=doctor, data=request.data, partial=True)
    # if the data is valid
    if serializer.is_valid():
        # save the data
        serializer.save()
    # return the data in json format
    return Response(serializer.data)


@api_view(['GET'])
def getPatient(request):
    # get all the data from the Patient model
    patient = Patient.objects.all()
    # serialize the data
    serializer = PatientSerializer(patient, many=True)
    # return the data in json format
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createPatient(request):
    # serialize the data
    serializer = PatientSerializer(data=request.data)

    # check if the patient already exists
    if Patient.objects.filter(email=request.data['email']).exists():
        return JsonResponse({'error': 'Patient already exists'}, safe=False)

    # if the data is valid
    if serializer.is_valid():
        # save the data
        serializer.save()
    # return the data in json format

    return JsonResponse(serializer.data, safe=False)


@api_view(['PATCH', 'PUT'])
def updatePatient(request, pk):
    # get the data from the Patient model
    try:
        patient = Patient.objects.get(id=pk)
    except:
        return JsonResponse({'error': 'Patient does not exist'}, safe=False)

    # serialize the data
    serializer = PatientSerializer(
        instance=patient, data=request.data, partial=True)
    # if the data is valid
    if serializer.is_valid():
        # save the data
        serializer.save()
    # return the data in json format
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getAppointment(request):
    # get all the data from the Appointment model
    appointment = Appointment.objects.all()
    # serialize the data
    serializer = AppointmentSerializer(appointment, many=True)
    # return the data in json format
    return JsonResponse(serializer.data, safe=False)


#  TO DO validate the appointment
@api_view(['POST'])
def createAppointment(request):

    if Doctor.objects.filter(id=request.data['doctor']).exists() == False:
        return JsonResponse({'error': 'Doctor does not exist'}, safe=False)

    if Patient.objects.filter(id=request.data['patient']).exists() == False:
        return JsonResponse({'error': 'Patient does not exist'}, safe=False)

    if Appointment.objects.filter(patient=request.data['patient'], doctor=request.data['doctor'], date=request.data['date'], time=request.data['time']).exists():
        return JsonResponse({'error': 'Appointment already exists'}, safe=False)

    # serialize the data
    serializer = AppointmentSerializer(data=request.data)

    # if the data is valid
    if serializer.is_valid():
        # save the data
        serializer.save()
    # return the data in json format
    return JsonResponse(serializer.data, safe=False)


# TO DO validate the appointment
@api_view(['PATCH', 'PUT'])
def updateAppointment(request, pk):
    # get the data from the Appointment model
    try:
        appointment = Appointment.objects.get(id=pk)
    except:
        return JsonResponse({'error': 'Appointment does not exist'}, safe=False, partial=True)

    # serialize the data
    serializer = AppointmentSerializer(
        instance=appointment, data=request.data, partial=True)
    # if the data is valid
    if serializer.is_valid():
        # save the data
        serializer.save()
    else:
        return JsonResponse(serializer.errors, safe=False)
    # return the data in json format
    return JsonResponse(serializer.data, safe=False)


def getAdmin(request):
    # get all the data from the Admin model
    admin = Admin.objects.all()
    # serialize the data
    serializer = AdminSerializer(admin, many=True)
    # return the data in json format
    return Response(serializer.data)


def createAdmin(request):
    # serialize the data
    serializer = AdminSerializer(data=request.data)
    # if the data is valid
    if serializer.is_valid():
        # save the data
        serializer.save()
    # return the data in json format
    return Response(serializer.data)


def updateAdmin(request, pk):
    # get the data from the Admin model
    admin = Admin.objects.get(id=pk)
    # serialize the data
    serializer = AdminSerializer(instance=admin, data=request.data)
    # if the data is valid
    if serializer.is_valid():
        # save the data
        serializer.save()
    # return the data in json format
    return Response(serializer.data)


def deleteDoctor(request, pk):
    # get the data from the Doctor model
    doctor = Doctor.objects.get(id=pk)
    # delete the data
    doctor.delete()
    # return the data in json format
    return Response('Doctor Deleted')


def deletePatient(request, pk):
    # get the data from the Patient model
    patient = Patient.objects.get(id=pk)
    # delete the data
    patient.delete()
    # return the data in json format
    return Response('Patient Deleted')


def deleteAppointment(request, pk):
    # get the data from the Appointment model
    appointment = Appointment.objects.get(id=pk)
    # delete the data
    appointment.delete()
    # return the data in json format
    return Response('Appointment Deleted')


# def deleteAdmin(request, pk):
#     # get the data from the Admin model
#     admin = Admin.objects.get(id=pk)
#     # delete the data
#     admin.delete()
#     # return the data in json format
#     return Response('Admin Deleted')


def getDoctorById(request, pk):
    # get the data from the Doctor model
    doctor = Doctor.objects.get(id=pk)
    # serialize the data
    serializer = DocSerializer(doctor, many=False)
    # return the data in json format
    return Response(serializer.data)


def getPatientById(request, pk):
    # get the data from the Patient model
    patient = Patient.objects.get(id=pk)
    # serialize the data
    serializer = PatientSerializer(patient, many=False)
    # return the data in json format
    return Response(serializer.data)


def getAppointmentById(request, pk):
    # get the data from the Appointment model
    appointment = Appointment.objects.get(id=pk)
    # serialize the data
    serializer = AppointmentSerializer(appointment, many=False)
    # return the data in json format
    return Response(serializer.data)


def getAdminById(request, pk):
    # get the data from the Admin model
    admin = Admin.objects.get(id=pk)
    # serialize the data
    serializer = AdminSerializer(admin, many=False)
    # return the data in json format
    return Response(serializer.data)


def getDoctorBySpeciality(request, speciality):
    # get the data from the Doctor model
    doctor = Doctor.objects.filter(speciality=speciality)
    # serialize the data
    serializer = DocSerializer(doctor, many=True)
    # return the data in json format
    return Response(serializer.data)


def getallAppointmentByDoctorId(request, doctor_id):
    # get the data from the Appointment model
    appointment = Appointment.objects.filter(doctor_id=doctor_id)
    # serialize the data
    serializer = AppointmentSerializer(appointment, many=True)
    # return the data in json format
    return Response(serializer.data)


def getallAppointmentByPatientId(request, patient_id):
    # get the data from the Appointment model
    appointment = Appointment.objects.filter(patient_id=patient_id)
    # serialize the data
    serializer = AppointmentSerializer(appointment, many=True)
    # return the data in json format
    return Response(serializer.data)


def getallAppointmentByDate(request, date):
    # get the data from the Appointment model
    appointment = Appointment.objects.filter(date=date)
    # serialize the data
    serializer = AppointmentSerializer(appointment, many=True)
    # return the data in json format
    return Response(serializer.data)


def getallAppointmentByDoctorIdAndDate(request, doctor_id, date):
    # get the data from the Appointment model
    appointment = Appointment.objects.filter(doctor_id=doctor_id, date=date)
    # serialize the data
    serializer = AppointmentSerializer(appointment, many=True)
    # return the data in json format
    return Response(serializer.data)


def getallAppointmentByDoctorIdAndDateAndTime(request, doctor_id, date, time):
    # get the data from the Appointment model
    appointment = Appointment.objects.filter(
        doctor_id=doctor_id, date=date, time=time)
    # serialize the data
    serializer = AppointmentSerializer(appointment, many=True)
    # return the data in json format
    return Response(serializer.data)


def getallAppointmentByDoctorIdAndDateAndTimeAndPatientId(request, doctor_id, date, time, patient_id):
    # get the data from the Appointment model
    appointment = Appointment.objects.filter(
        doctor_id=doctor_id, date=date, time=time, patient_id=patient_id)
    # serialize the data
    serializer = AppointmentSerializer(appointment, many=True)
    # return the data in json format
    return Response(serializer.data)