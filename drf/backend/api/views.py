from django.http import JsonResponse
# The "JsonResponse" class takes a Python dictionary or list and converts it to a JSON object before returning it to the client.

# Here we are going to design our very first API endpoint view.

def api_home(request, *args, **kwargs):
    return JsonResponse({"messaege": "Hi there. This is your Django API response!!"})