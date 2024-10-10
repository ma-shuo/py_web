from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from common.core.response import ApiResponse
from sgp.controller.add_sgp_score import read_sgp_excel, add_sgp_sql


@permission_classes([AllowAny])
class AddSgpScore(GenericAPIView):
    def get(self, request, *args, **kwargs):
        dic = read_sgp_excel()
        add_sgp_sql(dic=dic)
        return ApiResponse(data={})