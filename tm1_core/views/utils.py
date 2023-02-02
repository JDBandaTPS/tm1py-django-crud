from django.http.response import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from TM1py.Services import TM1Service
from django.contrib import messages

class HomeView(View):
    template_name = 'pages/home.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        with TM1Service(address='10.1.1.2', port=59997, user='admin', password='apple', ssl=False) as tm1:
            year_ti_dimension = tm1.dimensions.get('Year_TI')
            #Only elements
            context['yearti_24retail'] = [y for x in year_ti_dimension.hierarchies for y in x]
        with TM1Service(address='10.1.1.2', port=50045, user='admin', password='apple', ssl=False) as tm1:
            year_ti_dimension = tm1.dimensions.get('Year_TI')
            #Only elements
            context['yearti_carsales'] = [y for x in year_ti_dimension.hierarchies for y in x]
        with TM1Service(address='10.1.1.2', port=50053, user='admin', password='apple', ssl=False) as tm1:
            year_ti_dimension = tm1.dimensions.get('Year_TI')
            #Only elements
            context['yearti_demo'] = [y for x in year_ti_dimension.hierarchies for y in x]
        with TM1Service(address='10.1.1.2', port=53294, user='admin', password='apple', ssl=False) as tm1:
            year_ti_dimension = tm1.dimensions.get('Year_TI')
            #Only elements
            context['yearti_coffee'] = [y for x in year_ti_dimension.hierarchies for y in x]
        with TM1Service(address='10.1.1.2', port=50061, user='admin', password='apple', ssl=False) as tm1:
            year_ti_dimension = tm1.dimensions.get('Year_TI')
            #Only elements
            context['yearti_go'] = [y for x in year_ti_dimension.hierarchies for y in x]
        
        return render(request, self.template_name, context)

class YearsView(View):
    def post(self, request, *args, **kwargs):
        pAnio = request.POST.get('year')
        ti_statements = [
            "IF(DimensionElementExists('Year_TI','"+pAnio+"')=0);",
            "\tDimensionElementInsertDirect( 'Year_TI', '', '"+pAnio+"', 'n' );",
            "ENDIF;"
        ]
        server_list = request.POST.getlist('server')
        try:
            if '1' in server_list:
                #24Retail - 59997
                with TM1Service(address='10.1.1.2', port=59997, user='admin', password='apple', ssl=False) as tm1:
                    tm1.processes.execute_ti_code(lines_prolog=ti_statements, lines_epilog=[])
            if '2' in server_list:
                #CarSales - 50045
                with TM1Service(address='10.1.1.2', port=50045, user='admin', password='apple', ssl=False) as tm1:
                    tm1.processes.execute_ti_code(lines_prolog=ti_statements, lines_epilog=[])
            if '3' in server_list:
                #DemoGuide - 50053
                with TM1Service(address='10.1.1.2', port=50053, user='admin', password='apple', ssl=False) as tm1:
                    tm1.processes.execute_ti_code(lines_prolog=ti_statements, lines_epilog=[])
            if '4' in server_list:
                #Coffe - 53294
                with TM1Service(address='10.1.1.2', port=53294, user='admin', password='apple', ssl=False) as tm1:
                    tm1.processes.execute_ti_code(lines_prolog=ti_statements, lines_epilog=[])
            if '5' in server_list:
                #GO_scorecards - 50061
                with TM1Service(address='10.1.1.2', port=50061, user='admin', password='apple', ssl=False) as tm1:
                    tm1.processes.execute_ti_code(lines_prolog=ti_statements, lines_epilog=[])
            return JsonResponse(data={}, status=200)
        except:
            return JsonResponse(data={}, status=500)

class YearsDeleteView(View):
    def post(self, request, *args, **kwargs):
        pAnio = self.kwargs['year']
        server = self.kwargs['server']
        ti_statements = [
            "DimensionElementDeleteDirect( 'Year_TI', '"+pAnio+"' );",
        ]
        try:
            if server == '1':
                #24Retail - 59997
                with TM1Service(address='10.1.1.2', port=59997, user='admin', password='apple', ssl=False) as tm1:
                    tm1.processes.execute_ti_code(lines_prolog=ti_statements, lines_epilog=[])
            if server == '2':
                #CarSales - 50045
                with TM1Service(address='10.1.1.2', port=50045, user='admin', password='apple', ssl=False) as tm1:
                    tm1.processes.execute_ti_code(lines_prolog=ti_statements, lines_epilog=[])
            if server == '3':
                #DemoGuide - 50053
                with TM1Service(address='10.1.1.2', port=50053, user='admin', password='apple', ssl=False) as tm1:
                    tm1.processes.execute_ti_code(lines_prolog=ti_statements, lines_epilog=[])
            if server == '4':
                #Coffe - 53294
                with TM1Service(address='10.1.1.2', port=53294, user='admin', password='apple', ssl=False) as tm1:
                    tm1.processes.execute_ti_code(lines_prolog=ti_statements, lines_epilog=[])
            if server == '5':
                #GO_scorecards - 50061
                with TM1Service(address='10.1.1.2', port=50061, user='admin', password='apple', ssl=False) as tm1:
                    tm1.processes.execute_ti_code(lines_prolog=ti_statements, lines_epilog=[])
            return JsonResponse(data={}, status=200)
        except:
            return JsonResponse(data={}, status=500)
