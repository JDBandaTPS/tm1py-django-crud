from django.urls import path
from tm1_core.views import utils, carsales, coffee, go_scorecards, retail, demo

urlpatterns = [
    path('', utils.HomeView.as_view(), name='home'),
    path('years/create', utils.YearsView.as_view(), name='process-years'),
    path('years/<str:server>/<str:year>', utils.YearsDeleteView.as_view(), name='delete-years'),
    path('carsales/years', carsales.CarSalesView.as_view(), name='carsales-year'),
    path('coffee/years', coffee.CoffeeView.as_view(), name='coffee-year'),
    path('demo/years', demo.DemoView.as_view(), name='demo-year'),
    path('go/years', go_scorecards.GoView.as_view(), name='go-year'),
    path('retail/years', retail.RetailView.as_view(), name='retail-year'),
]