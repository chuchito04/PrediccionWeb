import pandas as pd
from pycaret.regression import load_model, predict_model
from django.http import HttpResponse
from django.shortcuts import render

def get_model():
    return load_model("app/prediccion/final_et_pauta_3")

def predict(request):
    if request.method == 'POST':
        importe_gastado = float(request.POST.get('importe_gastado'))
        clasificacion_descripcion = request.POST.get('clasificacion_descripcion')
        objetivo_descripcion = request.POST.get('objetivo_descripcion')
        redsocial_descripcion = request.POST.get('redsocial_descripcion')

        input_dict = {
            'Importe_gastado': importe_gastado,
            'Clasificacion_descripcion': clasificacion_descripcion,
            'Objetivo_descripcion': objetivo_descripcion,
            'Redsocial_descripcion': redsocial_descripcion
        }

        input_df = pd.DataFrame([input_dict])
        model = get_model()
        prediction = predict_model(model, data=input_df)['prediction_label'][0]
        prediction_formatted = '{0:,.2f}'.format(prediction)
        
        return render(request, 'resultado.html', {'prediction': prediction_formatted})
    else:
        # Manejo de otro método HTTP (GET u otros)
        return HttpResponse("Método no permitido.")
