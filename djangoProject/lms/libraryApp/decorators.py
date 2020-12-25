from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

def unathenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            messages.success(request, "You are already logged in to LMS")
            return redirect("dashboard")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def staff_only_allowed(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        if not user.is_staff:
            messages.warning(request, "You are not allowed to access the previous requested page")
            return redirect("dashboard")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def student_only_allowed(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        if user.is_staff:
            messages.warning(request, "You are not allowed to access the previous requested page")
            return redirect("dashboard")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func