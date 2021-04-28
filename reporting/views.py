from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
import json
from .models import cityweather
from datetime import datetime
from django.http import JsonResponse
from difflib import SequenceMatcher

def getreport(request):
    cities_list = [{"name":"Mumbai","state":"Maharashtra","lat":"18.975","lon":"72.825833"},
    {"name":"Delhi","state":"Delhi","lat":"28.666667","lon":"77.216667"},
    {"name":"Bangalore","state":"Karnataka","lat":"12.983333","lon":"77.583333"},
    {"name":"Hyderabad","state":"Telangana","lat":"17.375278","lon":"78.474444"},
    {"name":"Ahmedabad","state":"Gujarat","lat":"23.033333","lon":"72.616667"},
    {"name":"Chennai","state":"Tamil Nadu","lat":"13.083333","lon":"80.283333"},
    {"name":"Kolkata","state":"West Bengal","lat":"22.569722","lon":"88.369722"},
    {"name":"Surat","state":"Gujarat","lat":"20.966667","lon":"72.9"},
    {"name":"Pune","state":"Maharashtra","lat":"18.533333","lon":"73.866667"},
    {"name":"Jaipur","state":"Rajasthan","lat":"24.583333","lon":"86.85"},]
    api_key = "766af6bca720e0af3d9ab1942d82bfb1"
    saved_citys = []
    unsaved_citys = [] 
    for city in cities_list:
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s" % (city["lat"], city["lon"], api_key)
        response = requests.get(url)
        data = json.loads(response.text)
        # current
        current = data["current"]
        print("\n City", city["name"], "current", current['weather'][0]['description'])
        # sample data looks like
        #{'dt': 1619610779, 'sunrise': 1619566568, 'sunset': 1619613100, 'temp': 307.15, 'feels_like': 316.18, 'pressure': 1005, 
        #'humidity': 62, 'dew_point': 298.83, 'uvi': 0.17, 'clouds': 20, 'visibility': 3500, 
        #'wind_speed': 5.14, 'wind_deg': 180, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}]}
        
        
        date_obj = datetime.fromtimestamp(current['dt'] // 1000)
        sunrise =datetime.fromtimestamp(current['sunrise'] // 1000)
        sunset =datetime.fromtimestamp(current['sunset'] // 1000)
    
        cityobj = cityweather(name=city["name"], fetch_date=date_obj, sunrise=sunrise, sunset=sunset,
                                temp=current['temp'],feels=current['feels_like'],pressure=current['pressure'],humidity=current['humidity'],
                                dew_point=current['dew_point'],uvi=current['uvi'],clouds=current['clouds'],wind_speed=current['wind_speed'],
                                wind_deg=current['wind_deg'],description=current['weather'][0]['description'],type=current['weather'][0]['main'])

        try:
            cityobj.save()
            saved_citys.append(city["name"])
        except Exception as e:
            unsaved_citys.append(city['name'])
            print("exception ", e)
        print("="*30)
    final_data = {"captured_cities": saved_citys, "missed_citys": unsaved_citys}
    return JsonResponse(final_data)

def getresult(request):
    obj = cityweather.objects.all()
    latest_time_obj = cityweather.objects.order_by('-fetch_date')[:10]
    #similar_data = {"temp": None, "pressure": None, "humidity": None, "wind_speed": None}
    
    latest_city_data = [data for data in latest_time_obj]
    
    
    print("latest_city_data", latest_city_data)
    
    """
    for city_data in latest_city_data:
        print("city data", city_data)
        for rest_city_data in latest_city_data:
            print("comparin with", rest_city_data)
            if city_data.name != rest_city_data.name:
                k = list(field.name for field in cityweather._meta.get_fields())
                for key_ in k:
                    if key_ in ["temp", "pressure", "humidity", "wind_speed"]:
                        print("values in comparision ", key_)
                        if getattr(city_data, key_) == getattr(rest_city_data, key_):
                            if not similar_data[key_]:
                                similar_data[key_] = [(city_data.name, getattr(city_data, key_)), (rest_city_data.name, getattr(rest_city_data, key_))]
    """
    similarity_data = {}
    similar_data = []
    for city_data in latest_city_data:
        for rest_city_data in latest_city_data:
            if city_data.name != rest_city_data.name:
                s = SequenceMatcher(None, str(city_data), str(rest_city_data)).ratio()
                if s*100 > 50.00:
                    data = [[city_data.name, city_data.temp, city_data.pressure, city_data.humidity, city_data.feels
                    , city_data.sunrise, city_data.sunset, city_data.wind_speed, city_data.wind_deg], 
                    [rest_city_data.name, rest_city_data.temp, rest_city_data.pressure, rest_city_data.humidity, rest_city_data.feels,
                    rest_city_data.sunrise, rest_city_data.sunset, rest_city_data.wind_speed, rest_city_data.wind_deg]]
                    if data not in similar_data and [data[1], data[0]] not in similar_data:
                        similar_data.append(data)
                        similarity_data = {"perc": s*100, "data": similar_data}
    return JsonResponse(similarity_data)
   