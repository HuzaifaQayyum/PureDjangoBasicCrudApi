from django.http import HttpResponse
import json

class JsonResponse(HttpResponse):
    def __init__(self, data={}, status=200, *args, **kwargs):
        is_json = isinstance(data, str)
        if (not is_json):
            if ("serialize" in dir(data)):
                data = data.serialize()
            else:
                try:
                    data = json.dumps(data)
                except:
                    raise Exception("Can not convert to json")

        super().__init__(content=data, status=status, content_type="application/json", *args, **kwargs)

class Http404(JsonResponse):
    def __init__(self):
        super().__init__(status=404, data={"error_msg": "Not found"})