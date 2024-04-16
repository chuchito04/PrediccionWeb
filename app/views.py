from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group
import pandas as pd
from pycaret.regression import load_model, predict_model
from django.http import HttpResponse

# Create your views here.
@login_required
def home(request):
    if request.user.is_authenticated:
        user_groups = request.user.groups.all()
        group_names = [group.name for group in user_groups]
        
        
        data = {
            'username': request.user.username,
            'email': request.user.email,
            'groups': group_names,
            
        }


    return render(request, "home.html",data)

def formulario(request):
    return render(request, "formulario.html")

def get_model():
    return load_model("app/prediccion/final_et_pauta_3")

def predict(request):
    if request.method == 'POST':
        Importe_gastado = float(request.POST.get('importe_gastado'))
        Clasificacion_descripcion = request.POST.get('clasificacion_descripcion')
        Objetivo_descripcion = request.POST.get('objetivo_descripcion')
        Redsocial_descripcion = request.POST.get('redsocial_descripcion')

        input_dict = {
            'Importe_gastado': Importe_gastado,
            'Clasificacion_descripcion': Clasificacion_descripcion,
            'Objetivo_descripcion': Objetivo_descripcion,
            'Red_Social_descripcion': Redsocial_descripcion
        }

        input_df = pd.DataFrame([input_dict])
        model = get_model()
        prediction = predict_model(model, data=input_df)['prediction_label'][0]
        prediction_formatted = '{0:,.2f}'.format(prediction)
        
        return render(request, 'formulario.html', {'prediction': prediction_formatted})
    else:
        # Manejo de otro método HTTP (GET u otros)
        return HttpResponse("Método no permitido.")
    

def signout(request):
    logout(request)
    return redirect('login')
