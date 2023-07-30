from django.shortcuts import render
from rest_framework.views import status, Response, APIView
from location.models import Place
import logging
from location import messages_code


logger = logging.getLogger("normal")


class UserLocation(APIView):
    def get(self, request):
        return Response(data={})
    def post(self, request):
        return Response(data={})


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
                Place.objects.delete(id=pk)
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
    
