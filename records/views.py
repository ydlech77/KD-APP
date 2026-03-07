from django.shortcuts import render, redirect
from .models import Patient
from django.shortcuts import get_object_or_404

ADMIN_PASSWORD = "ketty"


def add_patient(request):
    if request.method == "POST":
        Patient.objects.create(
            full_name=request.POST['full_name'],
            date_of_birth=request.POST['date_of_birth'],
            gender=request.POST['gender'],
            phone_number=request.POST['phone_number'],
            address=request.POST['address'],
            emergency_contact=request.POST['emergency_contact'],
        )
        return redirect('/')

    return render(request, 'records/add_patient.html')


def admin_login(request):
    if request.method == "POST":
        if request.POST['password'] == ADMIN_PASSWORD:
            request.session['admin'] = True
            return redirect('/dashboard/')
        return render(request, 'records/admin_login.html', {'error': True})

    return render(request, 'records/admin_login.html')


def admin_dashboard(request):
    if not request.session.get('admin'):
        return redirect('/admin-login/')

    query = request.GET.get('q')
    patients = Patient.objects.all()

    if query:
        patients = patients.filter(full_name__icontains=query)

    return render(request, 'records/admin_dashboard.html', {'patients': patients})


def delete_patient(request, id):
    if request.session.get('admin'):
        Patient.objects.filter(id=id).delete()
    return redirect('/dashboard/')
from django.shortcuts import get_object_or_404

def print_patient(request, id):
    if not request.session.get('admin'):
        return redirect('/admin-login/')

    patient = get_object_or_404(Patient, id=id)
    return render(request, 'records/patient_print.html', {'patient': patient})




def edit_patient(request, id):
    if not request.session.get('admin'):
        return redirect('/admin-login/')

    patient = get_object_or_404(Patient, id=id)

    if request.method == "POST":
        patient.full_name = request.POST.get('full_name')
        patient.gender = request.POST.get('gender')
        patient.phone_number = request.POST.get('phone_number')
        patient.address = request.POST.get('address')
        patient.emergency_contact = request.POST.get('emergency_contact')
        patient.additional_info = request.POST.get('additional_info')

        dob = request.POST.get('date_of_birth')
        patient.date_of_birth = dob if dob else None

        patient.save()  # 👈 updates SAME file

        return redirect('/dashboard/')

    return render(request, 'records/edit_patient.html', {'patient': patient})


def print_patient(request, id):
    if not request.session.get('admin'):
        return redirect('/admin-login/')

    patient = get_object_or_404(Patient, id=id)
    return render(request, 'records/patient_print.html', {'patient': patient})

def delete_patient(request, id):
    if not request.session.get('admin'):
        return redirect('/admin-login/')

    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return redirect('/dashboard/')