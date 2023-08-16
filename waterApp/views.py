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
    X.append(request.POST['sulfate'])
    X.append(request.POST['hardness'])
    X.append(request.POST['solids'])

    pH = pH_model.predict(pH_scaler.transform([X]))

    X.append(pH)

    turb = turb_model.predict(turb_scaler.transform([X]))

    X.append(turb)

    X_in = main_scaler.transform(main_transformer.transform([X]))
    potability = main_model.predict(X_in)

    if potability:
        pot = 'potable'
    else:
        pot = 'NOT potable'

    print(potability,type(potability))

    return render(request,'result.html',{'pot':pot,'X':X})