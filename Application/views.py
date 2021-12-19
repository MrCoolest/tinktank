
from django.shortcuts import render , redirect
from .models import Students, User
from django.contrib import messages
from django.contrib.messages.api import error



def index(request):
     if request.method == "POST":
          student_name = request.POST.get('Student_name')
          college_name = request.POST.get('College_name')
          specialisation = request.POST.get('Specialisation')
          degree_name = request.POST.get('Degree_name')
          internship = request.POST.get('internship')
          ph_no = request.POST.get('Ph_no')
          email = request.POST.get('email_id')
          location = request.POST.get('location')
          gender = request.POST.get('gender')
          notes = request.POST.get('notes')

          student = Students(student_name=student_name, college_name = college_name, Specialisation = specialisation, Degree_name = degree_name, Internship = internship, Phone_no = ph_no, Email = email, Location = location, Gender = gender, note = notes)
          student.save()

     return render(request, 'index.html')


def userLogin(request):
     if request.method == "POST":
          username = request.POST.get('username')
          passwd = request.POST.get('passwd')
     
          try:
               check_user = User.objects.get(user_name = username)          
               check_passwd = check_user.password == passwd
               if check_passwd:
                    request.session['user'] = username
                    return redirect('/')
          except:
               messages.error(request, f"Your username and Password Not Matching!")
               return redirect('/')
     return redirect('/')
     

def userLogout(request):
     try:
          del request.session['user']
     except:
          return redirect('/')
     return redirect('/')


  

def search(request):
     query = request.GET.get('search')
     search_student = Students.objects.values_list('student_name' , 'Specialisation', 'Location', "Gender", 'Email','Phone_no','Degree_name','id')
     student_list = []

     for i in search_student:
          for j in range(0,7):
               if(query.lower() in i[j] or query.upper() in i[j] or query.capitalize() in i[j]):
                    student_list.append(i)

     student_set = set()
     for content in student_list:
          name = content[0]
          item = Students.objects.filter(student_name = name)
          student_set.add(item)
     print("SEcond list", student_set)     

     all_students = Students.objects.all()
     return render(request, 'search.html', {'students' : all_students, 'search_students':student_set})


