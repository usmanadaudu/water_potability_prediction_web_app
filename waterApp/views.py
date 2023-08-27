from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,'home.html')

def result(request):

    pH_model = joblib.load('pH_model.sav')

    nitr_model = joblib.load('nitr_model.sav')

    main_model = joblib.load('model.sav')

    X = []
    X.append(request.POST['tempr'])
    X.append(request.POST['do'])
    X.append(request.POST['cond'])
    X.append(request.POST['bod'])
    X.append(request.POST['tclf'])

    pH = pH_model.predict([X])

    X = []
    X.append(request.POST['tempr'])
    X.append(request.POST['do'])
    X.append(pH)
    X.append(request.POST['cond'])
    X.append(request.POST['bod'])
    X.append(request.POST['tclf'])

    nitr = nitr_model.predict([X])

    X = []
    X.append(request.POST['tempr'])
    X.append(request.POST['do'])
    X.append(pH)
    X.append(request.POST['cond'])
    X.append(request.POST['bod'])
    X.append(nitr)
    X.append(request.POST['tclf'])

    potability = main_model.predict(X)

    if potability:
        pot = 'potable'
    else:
        pot = 'NOT potable'

    print(potability,type(potability))

    return render(request,'result.html',{'pot':pot,'X':X})