# chart/views.py
from django.shortcuts import render
from .models import Passenger
from django.db.models import FloatField
from django.db.models import Count, Q
import json
from django.http import JsonResponse
from django.db.models.functions import Cast





def home(request):
    return render(request, 'home.html')


def covid19_korea(request):
    return render(request, 'covid19_korea.html')










def ticket_class_view_2(request):  # 방법 2
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False)),
                  rate = Cast(Count('ticket_class', filter=Q(survived=True)), FloatField())/Cast(Count('ticket_class'),FloatField())*100) \


    # 빈 리스트 3종 준비
    categories = list()             # for xAxis
    survived_series = list()        # for series named 'Survived'
    not_survived_series = list()    # for series named 'Not survived'
    rate_series = list()

    # 리스트 3종에 형식화된 값을 등록
    for entry in dataset:
        categories.append('%s Class' % entry['ticket_class'])    # for xAxis
        survived_series.append(entry['survived_count'])          # for series named 'Survived'
        not_survived_series.append(entry['not_survived_count'])  # for series named 'Not survived'
        rate_series.append(entry['rate'])



    # json.dumps() 함수로 리스트 3종을 JSON 데이터 형식으로 반환
    return render(request, 'ticket_class_2.html', {
        'categories': json.dumps(categories),
        'survived_series': json.dumps(survived_series),
        'not_survived_series': json.dumps(not_survived_series),
        'rate_series': json.dumps(rate_series)
    })










