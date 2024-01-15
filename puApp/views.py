from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import csv

# Create your views here.

def datas_load(request):
    if request.method == "POST":
        lga = request.POST['lga']
        with open("KATSINA.csv", "r") as my_file:
            read_csv = csv.reader(my_file)
            count = 0
            for data in read_csv:
                if data[2] == lga.upper():
                    count += 1
            if count != 0:
                return JsonResponse({'success': True, 'message': f'The total number of polling units of {lga} is {count}'})
            else:
                return JsonResponse({'success': False, 'message': f'Polling units of {lga} is not available for now'})

    return render(request, "data-display.html")
