from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Department, Faculty
from .forms import FacultyForms, DepartmentForms
from django.contrib import messages
import csv


def faculty(request):
    form = FacultyForms()
    if request.method == "POST":
        form = FacultyForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Successfully added")
            return redirect("/")
        else:
            messages.error(request, "An error accured while register")
    return render(request, "faculty/index.html", {"form": form})


def employee_info(request):
    form = DepartmentForms()
    depts = Department.objects.all()
    context = {"emp_infos": "", "form": form, "depts": depts}
    if request.method=='POST' and 'getFaculty' in request.POST:
        form = DepartmentForms(request.POST)
        context['emp_infos'] = Faculty.objects.filter(department__departmentName = request.POST["dropdown"])
        return render(request, "faculty/view_data.html", context)
    if request.method=='POST' and 'exportCsv' in request.POST:
        form = DepartmentForms(request.POST)
        data = Faculty.objects.filter(department__departmentName = request.POST["dropdown"])
        print(data)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users.csv"'
        writer = csv.writer(response)
        writer.writerow(['Faculty Name','Department', 'Date of Joining', 'Subject'])
        faculties = Faculty.objects.filter(department__departmentName = request.POST["dropdown"]).values_list('facultyName','department', 'dateOfJoining', 'subject')
        for faculty in faculties:
            writer.writerow(faculty)
        return response

    return render(request, "faculty/view_data.html", context)