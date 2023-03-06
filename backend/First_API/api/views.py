import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_view(request, *args, **kwargs):
    #resquest => instance du http 
    
    #Comprendre le mot request
    print(request.body) #bit string
    dataFront = json.loads(request.body) #conveertie les donnée en dictiionaires 
    pre_dataFront = json.dumps(dataFront)
    print(dataFront)
    
    #Utilison les headers et les contents types 
    dataFront['headers'] = dict(request.headers)
    print(request.headers)
    dataFront['contents_ type'] = request.content_type
    dataFront['params'] = dict(request.GET)
    dataFront['post-data'] = dict(request.POST) 
    
    dataBac = {
        'name' : 'borel',
        'Language' : 'python'
    }
    return JsonResponse(dataFront)