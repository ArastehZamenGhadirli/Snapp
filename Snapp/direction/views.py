from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from direction.models import UserDirection ,UserWallet
from direction.serializers import DirectionSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.http.response import HttpResponse,StreamingHttpResponse, responses
import json
from django.shortcuts import get_object_or_404
import requests
# Create your views here.



class RequestTaxi(CreateAPIView):
    
    queryset = UserDirection.objects.all()
    serializer_class = DirectionSerializer

    def post(self, request):
        # objectModel= serializer.save()
        data=json.loads(request.body)
        origin = f'{data.get("origin_x")},{data.get("origin_y")}'
        destination = f'{data.get("destination_x")},{data.get("destination_y")}'
        url = f"https://api.neshan.org/v4/direction?type=car&origin={origin}&destination={destination}"

        headers = {
        "Api-Key": "service.08e74db58f774e069a5c4272fbe457c3" 
        }
  
        response = requests.get(url, headers=headers)
        duration_time = response.json()["routes"][0]["legs"][0]["duration"]["value"]
        final_price=(duration_time//60)*80000
        print(final_price)
        request_user=request.user
        
        if final_price>request_user.wallet :
            return HttpResponse("Safar no ok ")
        else :
            return HttpResponse("Safar  ok ")
        
        
    

    
    
    
    
    
    

