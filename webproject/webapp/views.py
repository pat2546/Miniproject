from django.shortcuts import render, redirect
from django.http import HttpResponse
from webapp.models import Person
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    all_person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_person})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        person = Person.objects.create(name=name, age=age)
        person.save()
        messages.success(request, "บันทึกข้อมูลเรียบร้อย")
        return redirect("/")
    else:
        return render(request, "form.html")

def delete(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request, "ลบข้อมูลเรียบร้อยแล้ว")
    return redirect("/")

def edit(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "อัพเดตข้อมูลเรียบร้อย")
        return redirect("/")
    else:
        person = Person.objects.get(id=person_id)
        return render(request, "edit.html", {"person": person})

# ฟังก์ชันสำหรับ login
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "เข้าสู่ระบบเรียบร้อย")
            return redirect("/")
        else:
            messages.error(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    return render(request, "login.html")

# ฟังก์ชันสำหรับ signup
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"สมัครสมาชิกสำเร็จสำหรับผู้ใช้ {username}")
            return redirect("/login/")
        else:
            messages.error(request, "เกิดข้อผิดพลาดในการสมัครสมาชิก")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

# ฟังก์ชันสำหรับ logout
def logout(request):
    auth_logout(request)
    messages.success(request, "ออกจากระบบเรียบร้อย")
    return redirect("/")
