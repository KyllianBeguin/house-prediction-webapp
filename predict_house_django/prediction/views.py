from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from func.house_prediction import predict

# import your machine learning model and any necessary preprocessing modules
# from myapp.models import HousePriceModel
# from myapp.preprocessing import preprocess_data

@csrf_exempt
def prediction(request):
    if request.method == 'POST':
        # retrieve the input data from the form
        surface = float(request.POST.get('surface'))
        rooms = int(request.POST.get('rooms'))
        town = request.POST.get('town')

        print(town)

        price = predict(surface=surface, rooms=rooms, town=town)

        # return the predicted price as a JSON response
        # return JsonResponse({'price': price})
        return render(request, 'result.html', {'price': price})
    else:
        # if the request method is not POST, render the form template
        return render(request, 'prediction.html')