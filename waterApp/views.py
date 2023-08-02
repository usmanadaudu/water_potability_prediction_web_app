from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,'home.html')

def result(request):

    pH_list = []
    pH_list.append(request.GET['sulfate'])
    pH_list.append(request.GET['hardness'])
    pH_list.append(request.GET['solids'])

    print(pH_list)

    pH_scaler = joblib.load('pH_scaler.sav')
    pH_model = joblib.load('pH_model.sav')

    turb_scaler = joblib.load('turb_scaler.sav')
    turb_model = joblib.load('turb_model.sav')

    main_transformer = joblib.load('transformer.sav')
    main_scaler = joblib.load('scaler.sav')
    main_model = joblib.load('model.sav')

    return render(request,'result.html')