from django.urls import path


from rest_framework.response import Response
from cloud.functions.instance import *


from rest_framework.views import APIView
from rest_framework import status

app_name = 'cloud'

class CreateInstanceView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            instance_name = data.get('name', '')
            external_ip, internal_ip,zone,subnet, sourceimage,machinetype,disksize, key = create_instance(instance_name)
            
            return Response({'external_ip': external_ip, 'internal_ip': internal_ip,'zone':zone,'subnet':subnet, 'sourceimage':sourceimage,'machinetype':machinetype,'disksize':disksize, 'key':key})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteInstanceView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            instance_name = data.get('name', '')
            if delete_instance(instance_name):
                return Response("Deleted instance")
            else:
                return Response("Failed to delete instance", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StopInstanceView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            instance_name = data.get('name', '')
            if stop_instance(instance_name):
                return Response("Stopped instance")
            else:
                return Response("Failed to stop instance", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StartInstanceView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            instance_name = data.get('name', '')
            external_ip = start_instance(instance_name)
            if external_ip:
                return Response({'external_ip': external_ip})
            else:
                return Response("Failed to start instance", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PublishInstanceView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            instance_name = data.get('name', '')
            external_ip, internal_ip = publish_to_vuln(instance_name)
            if external_ip:
                return Response({'external_ip': external_ip, 'internal_ip': internal_ip})
            else:
                return Response("Failed to start instance", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


urlpatterns = [
    path('create-instance', CreateInstanceView.as_view()),
    path('delete-instance', DeleteInstanceView.as_view()),
    path('stop-instance', StopInstanceView.as_view()),
    path('start-instance', StartInstanceView.as_view()),
    path('publish-instance', PublishInstanceView.as_view()),
]
