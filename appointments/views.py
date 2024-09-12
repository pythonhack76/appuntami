from django.shortcuts import render, redirect, get_object_or_404 
from django.http import JsonResponse, HttpResponse
from .models import Appointment

def homepage(request):
    return HttpResponse("Benvenuto nella gestione appuntamenti!")

def create_appointment(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        service = request.POST.get('service')
        appointment_date = request.POST.get('appointment_date')

        # Verifica che tutti i campi siano presenti
        if customer_name and service and appointment_date:
            # Crea l'appuntamento
            Appointment.objects.create(
                customer_name=customer_name,
                service=service,
                appointment_date=appointment_date
            )
            return redirect('list_appointments')  # Reindirizza alla lista degli appuntamenti dopo la creazione
        else:
            return JsonResponse({'error': 'Missing fields'}, status=400)

    return render(request, 'appointments/create.html')  # Renderizza il form per creare un appuntamento

def home_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/home.html', {'appointments': appointments})

def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/list.html', {'appointments': appointments})

def appointment_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    return render(request, 'appointments/detail.html', {'appointment': appointment})

def update_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    
    if request.method == 'POST':
        appointment.customer_name = request.POST.get('customer_name')
        appointment.service = request.POST.get('service')
        appointment.appointment_date = request.POST.get('appointment_date')
        appointment.save()
        return redirect('appointment_detail', id=id)

    return render(request, 'appointments/update.html', {'appointment': appointment})

