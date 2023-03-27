from django.shortcuts import render, HttpResponse, redirect
from .models import Donacion
from .forms import DonaForm
from django.conf import settings
from django.db.models import Q
from datetime import datetime
from django.core.mail import EmailMessage

def refe(request):
	formulario_contacto=DonaForm()
	if request.method=="POST":
		formulario_contacto=DonaForm(data=request.POST)
		if formulario_contacto.is_valid():
			formulario_contacto.save()

			return redirect("/Grac/?valido")
		else:
			return redirect("/Eli/?Novalido")

	return render(request, "index.html", {'formulario':formulario_contacto})

def Inicio(request):

    Donac=Donacion.objects.all()

    return render(request, "ent.html" , {"Donacio": Donac})

def Gra(request):

    return render(request, "gra.html" )


def Elim(request):

    return render(request, "eli.html" )



