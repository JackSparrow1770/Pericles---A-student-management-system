from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Staff/home.html')


@login_required(login_url='/')
def ADD_TEACHER(request):
    return render(request, 'Staff/add_teacher.html')

def VIEW_TEACHER(request):
    return render(request, 'Staff/view_teacher.html')

def EDIT_TEACHER(request):
    return render(request, 'Staff/edit_teacher.html')
