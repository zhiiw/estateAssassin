from django.db.models import QuerySet
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import random
from .models import User, House, HouseOfCase, Intermediary, LocationOfHouse


@csrf_exempt
def get_id(request, id):
    dic = {}
    if request.method != 'POST':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        house = House.objects.get(house_id=id)
        dic['house_id'] = house.house_id
        dic['toward'] = house.toward
        dic['unit_price'] = house.unit_price
        dic['building_area'] = house.building_area
        dic['total_price'] = house.total_price
        dic['decoration'] = house.decoration
        dic['floor'] = house.floor
        dic['unit_type'] = house.unit_type
    except House.DoesNotExist:
        dic['status'] = "Failed"
        return HttpResponse(json.dumps(dic))
    try:
        print("ee\n")

        dic['case_type'] = 'PP'

    except HouseOfCase.DoesNotExist:
        dic['case_type'] = []

    try:
        intermediary = Intermediary.objects.get(house_id=id)
        dic['intermediary_name'] = intermediary.intermediary_name
        dic['phone'] = intermediary.phone
    except Intermediary.DoesNotExist:
        dic['intermediary_name'] = []
        dic['phone'] = []

    try:
        location = LocationOfHouse.objects.get(house_id=id)
        dic['area'] = location.area
        dic['community_name'] = location.community_name
        dic['part_area'] = location.part_area
    except LocationOfHouse.DoesNotExist:
        dic['community_name'] = []
        dic['area'] = []
        dic['part_area'] = []

    dic['status'] = "Success"
    return HttpResponse(json.dumps(dic))


@csrf_exempt
def random(request):
    dic = {}
    if request.method != 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))

    total = House.objects.all()
    house_random = House.objects.order_by('?')[0]
    dic['house_id'] = house_random.house_id
    dic['price'] = house_random.total_price
    dic['decoration'] = house_random.decoration
    dic['unit_type'] = house_random.unit_type
    return HttpResponse(json.dumps(dic))


@csrf_exempt
def login(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))

    try:
        post_content = json.loads(request.body)
        username = post_content['username']
        password = post_content['password']
        user = User.objects.get(username=username)
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    except User.DoesNotExist:
        dic['status'] = "Failed"
        dic['message'] = "Wrong Username"
        return HttpResponse(json.dumps(dic))
    if user.password != password:
        dic['message'] = "Wrong Password"
        dic['status'] = "Failed"
        return HttpResponse(json.dumps(dic))
    else:
        dic['status'] = "Success"
        dic['user_id'] = user.uid
        dic['is_admin'] = user.is_admin
        return HttpResponse(json.dumps(dic))


@csrf_exempt
def register(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        post_content = json.loads(request.body)
        username = post_content['username']
        password = post_content['password']
        user = User.objects.get(username=username)
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    except User.DoesNotExist:
        dic['status'] = "Success"
        now = datetime.datetime.now()
        newUser = User(username=username, password=password, register_time=now)
        newUser.save()
        return HttpResponse(json.dumps(dic))
    if user is not None:
        dic['status'] = "Failed"
        dic['message'] = "User exist"
        return HttpResponse(json.dumps(dic))
