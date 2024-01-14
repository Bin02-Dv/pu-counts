from django.shortcuts import render
from django.http import HttpResponse
import csv

# Create your views here.

def datas_load(request):
    if request.method == "POST":
        with open("KATSINA.csv", "r") as my_file:
            read_csv = csv.reader(my_file)
            for data in read_csv:
                print(data[1])

    return render(request, "data-display.html")
