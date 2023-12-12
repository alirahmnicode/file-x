from rest_framework.views import APIView
from rest_framework.response import Response
from apps.multimedia.models import File
from apps.folders.models import Folder


class SearchAPIView(APIView):

    def get(self, request):
        q = request.GET.get("q")
        result = []

        files = File.objects.filter(file_name__icontains=q)
        folders = Folder.objects.filter(title__icontains=q)

        for file in files:
            item = {}
            item["id"] = file.pk
            item["title"] = file.file_name
            item["type"] = "file"
            result.append(item)

        for file in folders:
            item = {}
            item["id"] = file.pk
            item["title"] = file.title
            item["type"] = "folder"
            result.append(item)
        
        return Response(data=result)
        