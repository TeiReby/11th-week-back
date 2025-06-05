from django.http import JsonResponse

def test_deploy(request):
    return JsonResponse({"status": "deployed", "message": "New version works!"})
