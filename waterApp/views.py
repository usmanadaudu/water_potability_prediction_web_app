from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,'home.html')

def result(request):

    pH_model = joblib.load('pH_model.sav')

    do_model = joblib.load('do_model.sav')

    main_model = joblib.load('model.sav')

    X = []
    X.append(float(request.POST['tempr']))
    X.append(float(request.POST['cond']))
    X.append(float(request.POST['bod']))
    X.append(float(request.POST['nitr']))
    X.append(float(request.POST['tclf']))

    print(X)

    pH = pH_model.predict([X])

    X = []
    X.append(request.POST['tempr'])
    X.append(pH)
    X.append(request.POST['cond'])
    X.append(request.POST['bod'])
    X.append(request.POST['nitr'])
    X.append(request.POST['tclf'])

    do = do_model.predict([X])

    X = []
    X.append(request.POST['tempr'])
    X.append(do)
    X.append(pH)
    X.append(request.POST['cond'])
    X.append(request.POST['bod'])
    X.append(request.POST['nitr'])
    X.append(request.POST['tclf'])

    potability = main_model.predict([X])

    if potability:
        pot = 'potable'
    else:
        pot = 'NOT potable'

    print(potability,type(potability))

    return render(request,'result.html',{'pot':pot,'X':X})