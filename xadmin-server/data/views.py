from django.shortcuts import render

# Create your views here.
import logging

from django_filters import rest_framework as filters
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from common.core.filter import BaseFilterSet
from common.core.modelset import BaseModelSet, ImportExportDataAction
from common.core.pagination import DynamicPageNumber
from common.core.response import ApiResponse
from data.controller.sgpscore import sgp_score_demo
from data.models.sgp import SgpScore
from data.serializers.sgpscore import BookSerializer

logger = logging.getLogger(__name__)

class BookFilter(BaseFilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    author = filters.CharFilter(field_name='author', lookup_expr='icontains')
    publisher = filters.CharFilter(field_name='publisher', lookup_expr='icontains')

    class Meta:
        model = SgpScore
        fields = []  # fields用于前端自动生成的搜索表单

class BookView(GenericAPIView):
    """
    书籍管理
    """
    # permission_classes = (AllowAny,)
    # queryset = SgpScore.objects.all()
    # serializer_class = BookSerializer
    # filterset_class = BookFilter
    # pagination_class = DynamicPageNumber(1000)
    def get(self, request, *args, **kwargs):
        # demo()
        data = sgp_score_demo()
        return ApiResponse(data=data)