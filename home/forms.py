from django import forms
from .models import Contact, Student

class ContactForm(forms.ModelForm):
    class Meta:  
        model = Contact
        fields = ('name','email', 'message')



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'roll_number', 'email', 'phone_number', 'address', 'date_of_birth']
