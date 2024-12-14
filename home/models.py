from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 
       
        
class Room(models.Model):
    room_number = models.CharField(max_length=50)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed

    def __str__(self):
        return self.room_number

class Room(models.Model):
    room_number = models.CharField(max_length=20)
    capacity = models.IntegerField()

    def __str__(self):
        return self.room_number




# class Stafflist(models.Model):
#     name = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=15)
#     address = models.TextField()
#     # Add other fields as needed

#     def __str__(self):
#         return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    date_of_birth = models.DateField()
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
# class Student(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     roll_number = models.CharField(max_length=20, unique=True)
#     email = models.EmailField()
#     # Add other fields as needed

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    roll_number = models.IntegerField( unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField()
    address = models.TextField()
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



    
