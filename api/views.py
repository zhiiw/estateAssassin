from django.db.models import QuerySet
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import random
from .models import User, House, HouseCase, Intermediary, LocationOfHouse, Case


@csrf_exempt
def get_list(request):
    array = []
    if request.method != 'GET':
        dic = {}
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    for i in House.objects.all():
        house_id = i.house_id
        dic = {}
        dic['house_id'] = i.house_id
        dic['toward'] = i.toward
        dic['unit_price'] = i.unit_price
        dic['building_area'] = i.building_area
        dic['total_price'] = i.total_price
        dic['decoration'] = i.decoration
        dic['floors'] = i.floor
        dic['unit_type'] = i.unit_type
        array.append(dic)

    return HttpResponse(json.dumps(array))


@csrf_exempt
def create(request):
    dict = {}
    try:
        if request.method == 'GET':
            dict['status'] = "Failed"
            dict['message'] = "Wrong Method"
            return HttpResponse(json.dumps(dict))
        print("ee\n")

        content = json.loads(request.body)
        print("ee\n")
        user_id = int(content['uid'])
        user = User.objects.get(uid=user_id)
        print("ee\n")

        if user.is_admin != 1:
            dict['status'] = "Failed"
            dict['message'] = "You are not admin"
            return HttpResponse(json.dumps(dict))
        toward = content['toward']
        unit_price = int(content['unit_price'])
        building_area = int(content['building_area'])
        total_price = int(content['total_price'])
        print("ee\n")

        decoration = content['decoration']
        floors = content['floors']
        unit_type = content['unit_type']
        print("ee\n")

        house = House(
            toward=toward,
            unit_price=unit_price,
            building_area=building_area,
            total_price=total_price,
            decoration=decoration,
            floor=floors,
            unit_type=unit_type,
            admin_id=1
        )
        house.save()
        print("ee\n")

        id = house.house_id
        print(id)
        print("\n")
        intermediary_name = content['intermediary_name']
        phone = int(content['phone'])
        print("ee\n")

        intermediary = Intermediary(
            house_id=id, intermediary_name=intermediary_name, phone=phone
        )
        intermediary.save()
        area = content['area']
        print("ee\n")

        community_name = content['community_name']
        part_area = content['part_area']
        location = LocationOfHouse(
            house_id=id, area=area, community_name=community_name, part_area=part_area
        )
        location.save()
    except (KeyError, json.decoder.JSONDecodeError):
        dict['status'] = "Failed"
        dict['message'] = "No Input"

    dict['status'] = "Success"
    dict['message'] = "Create Success"
    return HttpResponse(json.dumps(dict))


@csrf_exempt
def delete(request):
    dic = {}
    try:
        content = json.loads(request.body)
        user_id = int(content['uid'])
        id = int(content['house_id'])
        user = User.objects.get(uid=user_id)
        if user.is_admin != 1:
            dic['status'] = "Failed"
            dic['message'] = "You are not admin"
            return HttpResponse(json.dumps(dic))

        house = House.objects.get(house_id=id)
        cases = HouseCase.objects.filter(house=house)
        i = 0
        for case in cases:
            i += 1
            temp = Case.objects.get(case_id=case.case_id)
            temp.delete()
            case.delete()
        house.delete()
        inter = Intermediary.objects.get(house_id=id)
        inter.delete()
        location = LocationOfHouse.objects.get(house_id=id)
        location.delete()

    except House.DoesNotExist:
        dic['status'] = "Failed"
        dic['message'] = "id doesn't exist"
        return HttpResponse(json.dumps(dic))

    dic['status'] = "Success"
    return HttpResponse(json.dumps(dic))


@csrf_exempt
def get_id(request, id):
    dic = {}
    try:
        house = House.objects.get(house_id=id)
        dic['house_id'] = house.house_id
        dic['toward'] = house.toward
        dic['unit_price'] = house.unit_price
        dic['building_area'] = house.building_area
        dic['total_price'] = house.total_price
        dic['decoration'] = house.decoration
        dic['floors'] = house.floor
        dic['unit_type'] = house.unit_type
    except House.DoesNotExist:
        dic['status'] = "Failed"
        return HttpResponse(json.dumps(dic))

    try:
        cases = HouseCase.objects.filter(house=house)
        i = 0
        for case in cases:
            i += 1
            temp = Case.objects.get(case_id=case.case_id)
            dic['case_type'] = temp.case_type
            dic['case_times'] = i
        if 'case_times' in dic:
            print('ee')
        else:
            dic['case_type'] = ""
            dic['case_times'] = 0
    except HouseCase.DoesNotExist:
        dic['case_type'] = ""
        dic['case_times'] = 0

    try:
        intermediary = Intermediary.objects.get(house_id=id)
        dic['intermediary_name'] = intermediary.intermediary_name
        dic['phone'] = int(intermediary.phone)
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
def get_all(request, id):
    array = []

    if request.method != 'GET':
        dic = {}
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    j = 0
    h = 0
    for i in House.objects.all():
        if (h < id):
            h += 1
            continue
        house_id = i.house_id
        dic = {}

        dic['house_id'] = i.house_id
        dic['toward'] = i.toward
        dic['unit_price'] = i.unit_price
        dic['building_area'] = i.building_area
        dic['total_price'] = i.total_price
        dic['decoration'] = i.decoration
        dic['floors'] = i.floor
        dic['unit_type'] = i.unit_type

        try:
            cases = HouseCase.objects.filter(house=i)
            i = 0
            for case in cases:
                i += 1
                temp = Case.objects.filter(case_id=case.case_id)
                for e in temp:
                    dic['case_s_type'] = e.case_type
                    dic['case_times'] = i

        except HouseCase.DoesNotExist:
            dic['case_type'] = []
            dic['categories_times'] = 0
        try:
            intermediary = Intermediary.objects.get(house_id=house_id)
            dic['intermediary_name'] = intermediary.intermediary_name
            dic['phone'] = intermediary.phone
        except Intermediary.DoesNotExist:
            dic['intermediary_name'] = []
            dic['phone'] = []

        try:
            location = LocationOfHouse.objects.get(house_id=house_id)
            dic['area'] = location.area
            dic['community_name'] = location.community_name
            dic['part_area'] = location.part_area
        except LocationOfHouse.DoesNotExist:
            dic['community_name'] = []
            dic['area'] = []
            dic['part_area'] = []
        j += 1
        array.append(dic)
        if j == 50:
            break

    return HttpResponse(json.dumps(array))


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
