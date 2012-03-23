from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def update_cities(request):
	param = request.POST
	country = param['country']
	options = {'Spain': ['Madrid','Barcelona','Vitoria','Burgos'],
			'France' : ['Paris','Evreux','Le Havre','Reims'],
			'England':['London','Birmingham','Bristol','Cardiff']}
	
	return HttpResponse(json.dumps(options[country]))