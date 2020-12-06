from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from relations.models import Album
from relations.serializers import AlbumSerializer

@csrf_exempt
def relation_list(request):
    """
    List all code relations, or create a new snippet.
    """
    if request.method == 'GET':
        relations = Album.objects.all()
        serializer = AlbumSerializer(relations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AlbumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def relation_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AlbumSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AlbumSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)