import json

import django
import requests

django.setup()

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import parsers, mixins, viewsets
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CreditScore.models import Farmer, Farm, Finance, Weather, SocialInteraction, PsychometricAssessment, \
    QuestionCategory, QuestionType, QuestionAnswer
from CreditScore.serializers import FarmerSerializer, FarmSerializer, FinanceSerializer, WeatherSerializer, \
    SocialInteractionSerializer, PsychometricAssessmentSerializer, QuestionCategorySerializer, QuestionTypeSerializer, \
    QuestionAnswerSerializer

it = []
server_url = "https://node-c-server.herokuapp.com/api/"


@csrf_exempt
def FarmApi(request):
    obj = Farm
    s = FarmSerializer
    if request.method == 'GET':
        q = (request.META['QUERY_STRING'])
        print(len(q) == 0)
        if len(q) > 0:
            tst1 = q.split("&&")
            temp = {}
            print(tst1)
            for i in tst1:
                tst = i.split("=")
                temp[tst[0]] = tst[1]
            if q:
                item = []
                item_serializer = {}

                for i in temp:
                    l = {i: temp[i]}
                    item = obj.objects.filter(**l)

                    item_serializer = s(item, many=True)

                return JsonResponse(item_serializer.data, safe=False)
        else:
            item = obj.objects.all()
            item_serializer = s(item, many=True)
            return JsonResponse(item_serializer.data, safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        res = (get_score(item_data[0], "Farm"))
        print(f"{server_url}farm")
        print("heeyyyy", requests.post(f"{server_url}farm", json=res).text)
        return JsonResponse(res, safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = obj.objects.get(id=item_data['id'])
        item_serializer = s(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)


    elif request.method == 'DELETE':
        item = Farm.objects.get()
        item.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def FaarmApi(request):
    eav.register(Farm)
    obj = Farm

    s = FarmSerializer
    if request.method == 'GET':
        eav.Attribute.objects.create(name='City', datatype=Attribute.TYPE_TEXT)
    elif request.method == 'POST':
        okay = True
        item_data = JSONParser().parse(request)

        print(item_data)
        if type(item_data) == list:
            for i in item_data:
                eav.Attribute.objects.create(name=i, datatype=eav.Attribute.TYPE_TEXT)
                # item_serializer = s(data=i)
                Farm.eav[i] = item_data[i]
                print(_Farm.save())

            if okay:
                return JsonResponse("Added successfully", safe=False)
            else:
                return JsonResponse("Failed to add", safe=False)

        else:
            item_serializer = s(data=item_data)
            print(item_serializer)
            if item_serializer.is_valid():
                item_serializer.save()
                return JsonResponse("Added successfully", safe=False)
            return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = obj.objects.get(id=item_data['id'])
        item_serializer = s(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)


    elif request.method == 'DELETE':
        item = Farmer.objects.get()
        item.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def FarmerApi(request):
    if request.method == 'GET':
        return JsonResponse("Deleted successfully", safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        res = (get_score(item_data[0], "Farmer"))
        print("heeyyyy", requests.post(f"{server_url}farmer", json=res).text)
        return JsonResponse(res, safe=False)
    elif request.method == 'PUT':
        return JsonResponse("Deleted successfully", safe=False)
    elif request.method == 'DELETE':
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def ScoreApi(request):
    if request.method == 'GET':
        return JsonResponse("Deleted successfully", safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        res = (get_farmer_score(item_data[0]["token"]))
        # print("heeyyyy", requests.post(f"{server_url}farmer", json=res).text)
        return JsonResponse(res, safe=False)
    elif request.method == 'PUT':
        return JsonResponse("Deleted successfully", safe=False)
    elif request.method == 'DELETE':
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def FinanceApi(request):
    obj = Finance
    s = FinanceSerializer
    if request.method == 'GET':
        item_data = JSONParser().parse(request)
        res = (get_score(item_data[0], "Finance"))
        return JsonResponse(res, safe=False)

    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        res = (get_score(item_data[0], "Finance"))
        print("heeyyyy", requests.post(f"{server_url}finance", json=res).text)
        return JsonResponse(res, safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = obj.objects.get(id=item_data['id'])
        item_serializer = s(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)


    elif request.method == 'DELETE':
        item = Farmer.objects.get()
        item.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def WeatherApi(request):
    obj = Weather
    s = WeatherSerializer
    if request.method == 'GET':
        q = (request.META['QUERY_STRING'])
        print(len(q) == 0)
        if len(q) > 0:
            tst1 = q.split("&&")
            temp = {}
            print(tst1)
            for i in tst1:
                tst = i.split("=")
                temp[tst[0]] = tst[1]
            if q:
                item = []
                item_serializer = {}

                for i in temp:
                    l = {i: temp[i]}
                    item = obj.objects.filter(**l)

                    item_serializer = s(item, many=True)

                return JsonResponse(item_serializer.data, safe=False)
        else:
            item = obj.objects.all()
            item_serializer = s(item, many=True)
            return JsonResponse(item_serializer.data, safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        res = (get_score(item_data[0], "Weather"))
        print("heeyyyy", requests.post(f"{server_url}weather", json=res).text)
        return JsonResponse(res, safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = obj.objects.get(id=item_data['id'])
        item_serializer = s(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)


    elif request.method == 'DELETE':
        item = Weather.objects.get()
        item.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def SocialInteractionApi(request):
    obj = SocialInteraction
    s = SocialInteractionSerializer
    if request.method == 'GET':
        q = (request.META['QUERY_STRING'])
        print(len(q) == 0)
        if len(q) > 0:
            tst1 = q.split("&&")
            temp = {}
            print(tst1)
            for i in tst1:
                tst = i.split("=")
                temp[tst[0]] = tst[1]
            if q:
                item = []
                item_serializer = {}

                for i in temp:
                    l = {i: temp[i]}
                    item = obj.objects.filter(**l)

                    item_serializer = s(item, many=True)

                return JsonResponse(item_serializer.data, safe=False)
        else:
            item = obj.objects.all()
            item_serializer = s(item, many=True)
            return JsonResponse(item_serializer.data, safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        res = (get_score(item_data[0], "Social"))
        print("heeyyyy", requests.post(f"{server_url}social", json=res).text)
        return JsonResponse(res, safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = obj.objects.get(id=item_data['id'])
        item_serializer = s(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE':
        item = SocialInteraction.objects.get()
        item.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def PsychometricAssessmentApi(request):
    obj = PsychometricAssessment
    s = PsychometricAssessmentSerializer
    if request.method == 'GET':
        q = (request.META['QUERY_STRING'])
        print(len(q) == 0)
        if len(q) > 0:
            tst1 = q.split("&&")
            temp = {}
            print(tst1)
            for i in tst1:
                tst = i.split("=")
                temp[tst[0]] = tst[1]
            if q:
                item = []
                item_serializer = {}

                for i in temp:
                    l = {i: temp[i]}
                    item = obj.objects.filter(**l)

                    item_serializer = s(item, many=True)

                return JsonResponse(item_serializer.data, safe=False)
        else:
            item = obj.objects.all()
            item_serializer = s(item, many=True)
            return JsonResponse(item_serializer.data, safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        res = (get_score(item_data[0], "Psychometric"))
        print("heeyyyy", requests.post(f"{server_url}psychometic", json=res).text)
        return JsonResponse(res, safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = obj.objects.get(id=item_data['id'])
        item_serializer = s(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)


    elif request.method == 'DELETE':
        item = PsychometricAssessment.objects.get()
        item.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def QuestionCategoryApi(request):
    obj = QuestionCategory
    s = QuestionCategorySerializer
    if request.method == 'GET':
        q = (request.META['QUERY_STRING'])
        print(len(q) == 0)
        if len(q) > 0:
            tst1 = q.split("&&")
            temp = {}
            print(tst1)
            for i in tst1:
                tst = i.split("=")
                temp[tst[0]] = tst[1]
            if q:
                item = []
                item_serializer = {}

                for i in temp:
                    l = {i: temp[i]}
                    item = obj.objects.filter(**l)

                    item_serializer = s(item, many=True)

                return JsonResponse(item_serializer.data, safe=False)
        else:
            item = obj.objects.all()
            item_serializer = s(item, many=True)
            return JsonResponse(item_serializer.data, safe=False)

    elif request.method == 'POST':
        okay = True
        item_data = JSONParser().parse(request)
        print(item_data)
        if type(item_data) == list:
            for i in item_data:
                item_serializer = s(data=i)
                if item_serializer.is_valid():
                    item_serializer.save()
                else:
                    okay = False
            if okay:
                return JsonResponse("Added successfully", safe=False)
            else:
                return JsonResponse("Failed to add", safe=False)

        else:
            item_serializer = s(data=item_data)
            print(item_serializer)
            if item_serializer.is_valid():
                item_serializer.save()
                return JsonResponse("Added successfully", safe=False)
            return JsonResponse("Failed to add", safe=False)



    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = obj.objects.get(id=item_data['id'])
        item_serializer = s(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)


    elif request.method == 'DELETE':
        item = PsychometricAssessment.objects.get()
        item.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def QuestionTypeApi(request):
    obj = QuestionType
    s = QuestionTypeSerializer
    if request.method == 'GET':
        q = (request.META['QUERY_STRING'])
        print(len(q) == 0)
        if len(q) > 0:
            tst1 = q.split("&&")
            temp = {}
            print(tst1)
            for i in tst1:
                tst = i.split("=")
                temp[tst[0]] = tst[1]
            if q:
                item = []
                item_serializer = {}

                for i in temp:
                    l = {i: temp[i]}
                    item = obj.objects.filter(**l)
                    item_serializer = s(item, many=True)

                return JsonResponse(item_serializer.data, safe=False)
        else:
            item = obj.objects.all()
            item_serializer = s(item, many=True)
            return JsonResponse(item_serializer.data, safe=False)
    elif request.method == 'POST':
        okay = True
        item_data = JSONParser().parse(request)
        print(item_data)
        if type(item_data) == list:
            for i in item_data:
                item_serializer = s(data=i)
                if item_serializer.is_valid():
                    item_serializer.save()
                else:
                    okay = False
            if okay:
                return JsonResponse("Added successfully", safe=False)
            else:
                return JsonResponse("Failed to add", safe=False)

        else:
            item_serializer = s(data=item_data)
            print(item_serializer)
            if item_serializer.is_valid():
                item_serializer.save()
                return JsonResponse("Added successfully", safe=False)
            return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = obj.objects.get(id=item_data['id'])
        item_serializer = s(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)


    elif request.method == 'DELETE':
        item = Farmer.objects.get()
        item.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def QuestionAnswerApi(request):
    obj = QuestionAnswer
    s = QuestionAnswerSerializer
    if request.method == 'GET':
        q = (request.META['QUERY_STRING'])
        if len(q) > 0:
            tst1 = q.split("&&")
            temp = {}
            for i in tst1:
                tst = i.split("=")
                temp[tst[0]] = tst[1]
            if q:
                item = []
                item_serializer = {}

                for i in temp:
                    l = {i: temp[i]}
                    print(l)
                    item = obj.objects.filter(**l)

                    item_serializer = s(item, many=True)

                return JsonResponse(item_serializer.data, safe=False)
        else:
            item = obj.objects.all()
            item_serializer = s(item, many=True)
            return JsonResponse(item_serializer.data, safe=False)

    elif request.method == 'POST':
        okay = True
        item_data = JSONParser().parse(request)
        print(item_data)
        if type(item_data) == list:
            for i in item_data:
                item_serializer = s(data=i)
                if item_serializer.is_valid():
                    item_serializer.save()
                else:
                    okay = False
            if okay:
                return JsonResponse("Added successfully", safe=False)
            else:
                return JsonResponse("Failed to add", safe=False)

        else:
            item_serializer = s(data=item_data)
            print(item_serializer)
            if item_serializer.is_valid():
                item_serializer.save()
                return JsonResponse("Added successfully", safe=False)
            print(str(s.errors))
            return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = obj.objects.get(id=item_data['id'])
        item_serializer = s(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)


    elif request.method == 'DELETE':
        item = obj.objects.get()
        item.delete()
        return JsonResponse("Deleted successfully", safe=False)


def get_score(data, table):
    obj = QuestionCategory
    obj_serializer = QuestionCategorySerializer
    obj1_serializer = QuestionTypeSerializer
    obj2_serializer = QuestionAnswerSerializer
    obj1 = QuestionType
    obj2 = QuestionAnswer

    sum = 0
    result = {}

    tbl = obj_serializer(obj.objects.get(Name=table))["Id"].value
    print(tbl)
    for item in data:
        print(item)
        try:
            ans = obj2_serializer(obj2.objects.get(Name=data[item],
                                                   TypeId=obj1_serializer(obj1.objects.get(Name=item, CategoryId=tbl))[
                                                       "Id"].value, CategoryId=tbl))
            # result[item] = ans["Score"].value
            sum, = ans["Score"].value
        except:
            # result[item] = data[item]
            print(item, "is messy")

    # data.remove("token")
    data["sum"] = sum
    return data


def _temp(tbl, token):
    tmp = json.loads(requests.get(f"{server_url}{tbl}?token={token}").text)
    return tmp["info"][0]["sum"] if len(tmp["info"]) else 0


def get_farmer_score(token):
    farmers = _temp("farmer", token)
    farm = _temp("farm", token)
    social = _temp("social", token)
    finance = _temp("finance", token)
    psychometric = _temp("psychometric", token)
    weather = _temp("weather", token)
    obj = {"farmers": farmers, "farm": farm, "social": social, "finance": finance, "psychometric": psychometric, "weather": weather}
    return obj

    # farmers = _temp("farmer", token)
    # farm = _temp("farm", token)
    # social = _temp("social", token)
    # finance = _temp("finance", token)
    # psychometric = _temp("psychometric", token)
    # weather = _temp("weather", token)
    # return [farmers, farm, social, finance, psychometric, weather]
