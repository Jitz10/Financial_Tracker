import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render,redirect
from django.conf import settings
from service.models import service,dta,incoming_data,Transaction  # Assuming your model is named Service
from django.http import JsonResponse
from django.db.models import Sum
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed

def homepage(request):
    cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
    data = [23, 17, 35, 29, 12, 41]
    explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0)
    colors = ("orange", "cyan", "brown", "grey", "indigo", "beige")
    wp = {'linewidth': 1, 'edgecolor': "green"}
    
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data), explode=explode, labels=cars,
                                      shadow=True, colors=colors, startangle=90, wedgeprops=wp,
                                      textprops=dict(color="magenta"))
 
    # Adding legend
    ax.legend(wedges, cars, title="Cars", loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("Customizing pie chart")
    
    # Save the plot
    plot_path = os.path.join(settings.MEDIA_ROOT, 'plot.png')
    fig.savefig(plot_path)
    plt.close()  # Close the figure to release resources
    
    # Pass the plot path to the template
    context = {'plot_path': plot_path}

    return render(request, "homepage.html", context)
    
    
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)

def tp(request):
    service_data = incoming_data.objects.all()#order_by('-service_title')  # Update model name
    data = {
        "s_data": service_data,
    }
    return render(request, "tp.html", data)


@csrf_exempt

def da(request):
    if request.method == 'POST':
        form_data = json.loads(request.body)
        json_data = json.loads(form_data['jsonString'])
        print(json_data)
        print(json_data.get('category'))
        transaction = Transaction(
            type=json_data.get('type'),
            name=json_data.get('name',' '),
            category=json_data.get('category'),
            description=json_data.get('description'),
            amount=json_data.get('amount'),
            recurring=json_data.get('recurring'),
            term=json_data.get('term'),
            end_date=json_data.get('endDate')
        )
        transaction.save()
        return HttpResponse('Data saved successfully')
    else:
        return HttpResponseNotAllowed(['POST'])
    
def dav2(request):
    if request.method == 'POST':
        jsonString = request.POST.get('jsonString')
        print("Received JSON string:", jsonString)
        
        try:
            # Parse the JSON string into a Python dictionary
            data = json.loads(jsonString)

            # Access individual fields
            transaction_type = data['type']
            name = data['name']
            category = data['category']
            description = data['description']
            amount = data['amount']
            recurring = data['recurring']
            term = data['term']
            end_date = data['endDate']

            # Print the extracted data
            print(f"Type: {transaction_type}")
            print(f"Name: {name}")
            print(f"Category: {category}")
            print(f"Description: {description}")
            print(f"Amount: {amount}")
            print(f"Recurring: {recurring}")
            print(f"Term: {term}")
            print(f"End Date: {end_date}")

            # Return a success response
            return JsonResponse({'message': 'Data received successfully'})
        except Exception as e:
            # Return an error response if there is an issue parsing the JSON string
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
