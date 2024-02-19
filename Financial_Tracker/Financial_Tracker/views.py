import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.conf import settings
from service.models import Service  # Assuming your model is named Service
from django.http import JsonResponse
from django.db.models import Sum

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
    service_data = Service.objects.all().order_by('-service_title')  # Update model name
    data = {
        "s_data": service_data,
    }
    return render(request, "tp.html", data)

def calculate_income_expense(request):
    # Querying income and expense data from the database
    income_query = Service.objects.aggregate(total_income=Sum('income'))
    expense_query = Service.objects.aggregate(total_expense=Sum('expense'))
    
    # Extracting values from the query result
    income = income_query['total_income'] if income_query['total_income'] is not None else 0
    expense = expense_query['total_expense'] if expense_query['total_expense'] is not None else 0
    
    # Calculating the balance
    balance = income - expense
    
    # Constructing the response data
    data = {
        'income': income,
        'expense': expense,
        'balance': balance
    }
    
    return JsonResponse(data)
