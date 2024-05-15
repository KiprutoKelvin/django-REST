from django.http import JsonReponse
from .models import Kinywa
from .serializers import KinywaSerializer

def kinywa_list(request):
    kinywas = Kinywa.objects.all()
    serializer = KinywaSerializer(kinywas, many=True)
    return JsonReponse(serializer.data, safe=False)