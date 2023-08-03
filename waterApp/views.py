from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,'home.html')

def result(request):

    pH_scaler = joblib.load('pH_scaler.sav')
    pH_model = joblib.load('pH_model.sav')

    turb_scaler = joblib.load('turb_scaler.sav')
    turb_model = joblib.load('turb_model.sav')

    main_transformer = joblib.load('transformer.sav')
    main_scaler = joblib.load('scaler.sav')
    main_model = joblib.load('model.sav')

    X = []
    X.append(request.GET['sulfate'])
    X.append(request.GET['hardness'])
    X.append(request.GET['solids'])

    print(X)

    pH = pH_model(pH_scaler.transform([X]))

    X.append(pH)

    turb = turb_model(turb_scaler.transform([X]))

    X.append(turb)

    X_in = main_scaler.transform(main_transformer.transform(X))
    potability = main_model([X_in])

    return render(request,'result.html')