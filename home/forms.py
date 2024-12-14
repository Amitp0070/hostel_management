from django import forms
from .models import Contact, Student

class ContactForm(forms.ModelForm):
    class Meta:  
        model = Contact
        fields = ('name','email', 'message')



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'father_name', 'roll_number', 'email',
            'phone_number', 'address', 'date_of_birth',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': forms.NumberInput(),
            'roll_number': forms.NumberInput(),
            'address': forms.Textarea(attrs={'rows': 2}),
        }