from django.shortcuts import render
from rest_framework.views import status, Response, APIView
from location.models import Place
import logging
from location import messages_code
from location.serializers import PlaceSerializer
from rest_framework import generics
from django.db.models import Q
import json


logger = logging.getLogger("normal")


class PlaceViewList(generics.ListAPIView):
    
    def get(self, request):
        try:
            logger.info(f"PageNumberPagination started....")
            queryset = Place.objects.all()
            if not queryset:
                return Response(
                    data="Data list is Empty",
                    status=status.HTTP_404_NOT_FOUND
                )
            page = self.paginate_queryset(queryset=queryset)
            serializer = PlaceSerializer(page, many=True)
            return Response(
                data=serializer.data
            )
        except Exception as e:
            logger.error(f"Exception found :{e}", exc_info=True)
            return Response(
                data="Not found",
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def post(self, request):
        try:
            serializer = PlaceSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    data=serializer.errors
                )
            validated_data = serializer.validated_data
            Place.objects.create(**validated_data)
            return Response(
                data="Data Store successfully",
                status=status.HTTP_200_OK
            )
        except Exception as e:
            logger.error("Exception in data storing {e}", exc_info=True)
            return Response(
                data="Unable to store data.",
                status=status.HTTP_404_NOT_FOUND
            )
        



class DeleteLocationId(APIView):
    def delete(self, request, pk):
        try:
            logger.info(f"Deleting the location_id:{pk}")
            if not pk:
                return Response(
                    data=messages_code.LOCATION_ID_MISSING,
                    status=status.HTTP_204_NO_CONTENT
                )
            elif not Place.objects.filter(id=pk).exists():
                return Response(
                    data=messages_code.LOCATION_ID_404,
                    status=status.HTTP_404_NOT_FOUND
                )
            else:
                Place.objects.filter(id=pk).delete()
            logger.info(f"Deleted successfully location_id:{pk}")
            return Response(
                data=messages_code.DELETE_SUCCESS_200,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            logger.error(f"exception found for deleting the location_id:{id}"+
                        f"exception:{e}", exc_info=True)
            return Response(
                data=messages_code.LOCATION_ID_404,
                status=status.HTTP_400_BAD_REQUEST
            )
    

class SearchPlacesView(APIView):
    def get(self, request):
        try:
            name = request.query_params.get("name")
            description = request.query_params.get("description")
            query1, query2 = None, None
            if name:
                query1 = Q(name__iexact=name)
            if description:
                query2 = Q(description__iexact=description)
            
            if query1 and query2:
                data = Place.objects.filter(query1 | query2).values()
            elif query1:
                data = Place.objects.filter(query1).values()
            elif query2:
                data = Place.objects.filter(query2).values()
        
            return Response(
                data=data,
                status=status.HTTP_200_OK
            )

        except Exception as e:
            logger.error("Exception found in searching :{e}", exc_info=True)
            return Response(
                data="Unable to search given data.",
                status=status.HTTP_404_NOT_FOUND
            )