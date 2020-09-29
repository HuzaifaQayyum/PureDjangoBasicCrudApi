import json
from django.http import HttpResponse

class BaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

class JSONMiddleware(BaseMiddleware):
    def __call__(self, request):
            
        if request.method != "GET" and (request.META['CONTENT_TYPE'] and 'application/json' in request.META['CONTENT_TYPE']):
            try:
                request._body = json.loads(request.body)
            except:
                return HttpResponse("{ \"errorMsg\": \"Invalid json recieved\" }", content_type="application/json", status=400)
        return super().__call__(request)