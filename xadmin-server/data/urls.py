# 文件位置 demo/urls.py
from django.urls import re_path, path
from rest_framework.routers import SimpleRouter

from data.views import BookView

router = SimpleRouter(False)  # 设置为 False ,为了去掉url后面的斜线

# router.register('book', BookView, basename='book')
no_auth_url = [

]


urlpatterns = [
    path('book', BookView.as_view(), name='BookView'),
]
urlpatterns += router.urls