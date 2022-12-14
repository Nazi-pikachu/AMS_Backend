# write a serializer for the model
from rest_framework import serializers
from .models import Admin, Doctor, Patient, Appointment


class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        # fields = ('id', 'name', 'email', 'password', 'phone',
        #           'address', 'speciality', 'experience', '  qualification   ')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'name', 'email', 'gender',  'password', 'phone',
                  'address', 'age')


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'doctor', 'patient', 'date', 'time', 'status')


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'username', 'password')
