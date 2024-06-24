from django.http import JsonResponse
from django.shortcuts import render
from .models import Personalapplication
from metro.models import Stationtime, Transfertime
from personal.models import Personal
from applications.models import Application

def index(request):
    return render(request, 'main/index.html')

def distribute_tasks(request):
    station_times = Stationtime.objects.all().values('id_st1', 'id_st2', 'time')
    transfer_times = Transfertime.objects.all().values('id1', 'id2', 'time')
    
    vertexes = []
    for record in station_times:
        vertexes.append({
            'id_st1': record['id_st1'],
            'id_st2': record['id_st2'],
            'time': str(record['time'])
        })
    for record in transfer_times:
        vertexes.append({
            'id1': record['id1'],
            'id2': record['id2'],
            'time': str(record['time'])
        })
        
    distance = None
    shortest_path = None
    
    # for record in vertexes:
    #     if 'id_st1' in record and 'id_st2' in record:
    #         distance = routes_instance.CalcDistance(int(record['id_st1']), int(record['id_st2']))
    #     elif 'id1' in record and 'id2' in record:
    #         shortest_path = routes_instance.CreateShortestPath(int(record['id1']), int(record['id2']))
    
    response_data = {
        'distance': distance,
        'shortest_path': shortest_path
    }
    return JsonResponse(response_data)
