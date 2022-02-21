from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse
from .permissions import Check_API_KEY_Auth


@api_view(['POST'])
@permission_classes((Check_API_KEY_Auth,))
def webhook(request):
    print("Data received from Webhook is: ", request.body)
    return HttpResponse(request.body)
