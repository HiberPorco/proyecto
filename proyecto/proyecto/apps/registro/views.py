#encoding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#para importar los campos de usuario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
def principal(request):
	return render_to_response("inicio.html",{},RequestContext(request))

def registro_usuarios(request):
	if request.method=="POST":
		fusuario=UserCreationForm(request.POST)
		if fusuario.is_valid():
			fusuario.save()
			usuario=request.POST["username"]
			nick=request.POST["nick"]
			email=request.POST["email"]

			#buscando al usuario qe emos creado
			nuevo_usuario=User.objects.get(username=usuario)
			#creamos su perfil
			perfil=PerfilUser.objects.create(user=nuevo_usuario,nick=nick,email=email)
			return HttpResponse("registrado")
	else:
		fusuario=UserCreationForm()	
	return render_to_response("usuario.html",{'formulario':fusuario},context_instance=RequestContext(request))
def login_usuario(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if(form.is_valid()==False):
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			if resultado:
				login(request,resultado)
				request.session["name"]=username
				return HttpResponseRedirect("/blog/perfil/")
	form=AuthenticationForm()
	return render_to_response("login.html",{"form":form},RequestContext(request))
def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect("/blog/")
def perfil(request):
	return render_to_response("perfil.html",{"nombre":request.session["name"]},RequestContext(request))