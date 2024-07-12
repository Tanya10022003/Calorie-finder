from django.shortcuts import render

#IvR/qVS9xVW1aTBfFh8ufw==6IuwPcPzcUF0NQ6G
# Create your views here.
def home(request):
    import json
    import requests
    if request.method=='POST':
        query=request.POST['query']
        api_url='https://api.calorieninjas.com/v1/nutrition?query='
        api_request= requests.get(api_url+query, headers={'X-Api-Key':'IvR/qVS9xVW1aTBfFh8ufw==6IuwPcPzcUF0NQ6G'}) 
        try:
            api=json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api="OOPS!Error Occurred"
            print(e)
        return render (request,'home.html',{'api':api})

    else:
        return render (request,'home.html',{'query':'Enter a valid query '})

   