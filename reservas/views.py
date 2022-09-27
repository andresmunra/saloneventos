from reservas.models import Salones, Reservas
from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
import uuid

def salonesView(request):
    salones = Salones.objects.all().order_by('id')
    return render(request, "salones.html", {'salones': salones})

def homeView(request):
    return render(request, "home.html")

def saveReservaView(request, salon):
    if request.method == "POST":
        date = request.POST['date']
        codigo = str(uuid.uuid4().fields[-1])[:5] + 'ID' + salon
        try:
            Reservas.objects.create(
                date=date,
                codReserva=codigo,
                salon_id=salon,
                user_id=request.user.id,
            )
            messages.success(request, 'Reserva realizada con éxito')
            return redirect('/salones/')
        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})
    else:
        messages.error(request, "Hay un error en la petición")
        return redirect('/salones/')

def misReservasView(request):
    reservas = Reservas.objects.raw('select rr.id, rr.date, rr."codReserva",  rs.name  from \n' + 'reservas_reservas rr \n' + 
    'inner join reservas_salones rs on rr.salon_id = rs.id \n' +
    'inner join users_userprofile uu on rr.user_id = uu.id  where uu.id=%s',[request.user.id])
    return render(request, "misReservas.html",{'reservas':reservas})