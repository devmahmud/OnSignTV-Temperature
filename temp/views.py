from django.shortcuts import render
import requests
from django.views.decorators.cache import cache_page # import the cache_page decorator

# Cache the view for 2 hours
@cache_page(60 * 60 *2)
def home(request):
    # key of the api
    key = 'enter your darksky api key'
    url = 'https://api.darksky.net/forecast/{}/{},{}'
    
    # check if the form is submitted
    if request.method == "POST":
        # get latitude from form
        latitude = request.POST['latitude']
        # get longitude from the form
        longitude = request.POST['longitude']

        # call the api and convert the result in json format
        result = requests.get(url.format(key, latitude,longitude)).json()

        # extract the temperature value from the api result and convert it into celsious
        temp = round((int(result['currently']['temperature'])-32)*(5/9))

        # pass the data in the context
        context ={
            "latitude": latitude,
            "longitude": longitude,
            "temp": temp
        }
    else:
        # no data will be passed when the GET request
        context = {}
    return render(request,'temp/home.html',context)