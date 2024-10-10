from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from common.core.response import ApiResponse
from sgp.controller.add_score import read_excel, add_data_sql

@permission_classes([AllowAny])
class AddScore(GenericAPIView):
    def get(self, request, *args, **kwargs):
        dic = read_excel()
        add_data_sql(dic=dic)
        return ApiResponse(data={})