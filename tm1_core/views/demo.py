from django.http.response import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from TM1py.Services import TM1Service

class DemoView(View):
    def get(self, request, *args, **kwargs):
        with TM1Service(address='10.1.1.2', port=50053, user='admin', password='apple', ssl=False) as tm1:
            year_ti_dimension = tm1.dimensions.get('Year_TI')
            return JsonResponse({'elements': [y.name for x in year_ti_dimension.hierarchies for y in x]}, status=200)
    
    def post(self, request, *args, **kwargs):
        #Se procesa la solicitud y devuelve un status
        pass