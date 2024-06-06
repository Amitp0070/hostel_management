from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContactForm , StudentForm
from .models import Room, Staff, Student
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home.html')

def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅Your message has been sent!')
        else:
            messages.error(request, 'Please fill in the form corrently!.')
           
    else:
        form = ContactForm()
    
    #todo add contact form
    return render(request, 'contact.html', {'form':form})


def register_view(request):
    # agar form submit ho to
    if request.method == "POST":
        # form se data alag alag variable me store karo
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        cpassword = request.POST.get('cpass')
        if password != cpassword or len(password) == 0 or len(cpassword) == 0:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        # more validation can be added here
        # check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')
        # user create karo
        user = User.objects.create_user(username, email, password)
        messages.success(request, "Account created successfully")
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')

    
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        if len(username) == 0 or len(password) == 0:
            messages.error(request, "Bad Login details!")
            return redirect('login')
        # user authenticate karo
        user = authenticate(request,username=username, password=password)
        if user is not None:
            messages.success(request, "Logged in successfully")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')


def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})


@login_required
def room_management(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        room_capacity = request.POST.get('room_capacity')
        Room.objects.create(name=room_name, capacity=room_capacity)
        return redirect('room_management')
    else:
        return render(request, 'room_management.html', {})



@login_required
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'staff_list.html', {'staff': staff})




@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Assuming there is a URL named 'student_list' for listing students
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

# def edit_student(request, roll_number):
#     student = get_object_or_404(Student, roll_number=roll_number)
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm(instance=student)
#     return render(request, 'edit_student.html', {'form': form, 'student': student})

# def delete_student(request, roll_number):
#     student = get_object_or_404(Student, roll_number=roll_number)
#     if request.method == 'POST':
#         student.delete()
#         return redirect('student_list')
#     return render(request, 'delete_student.html', {'student': student})


# # def add_staff(request):
# #     if request.method == 'POST':
# #         form = StaffForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('staff_list')
# #     else:
# #         form = StaffForm()
# #     return render(request, 'add_staff.html', {'form': form})

# # def edit_staff(request, staff_id):
# #     staff = get_object_or_404(Staff, pk=staff_id)
# #     if request.method == 'POST':
# #         form = StaffForm(request.POST, instance=staff)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('staff_list')
# #     else:
# #         form = StaffForm(instance=staff)
# #     return render(request, 'edit_staff.html', {'form': form, 'staff': staff})

# # def delete_staff(request, staff_id):
#     staff = get_object_or_404(Staff, pk=staff_id)
#     if request.method == 'POST':
#         staff.delete()
#         return redirect('staff_list')
#     return render(request, 'delete_staff.html', {'staff': staff})



@login_required
def search_room(request):
    if 'query' in request.GET:
        query = request.GET['query']
        rooms = Room.objects.filter(room_number__icontains=query)
    else:
        rooms = Room.objects.none()
    return render(request, 'search_room.html', {'rooms': rooms})


@login_required
def book_room(request):
    return render(request, 'book_room.html')
