# 文件位置 demo/urls.py
from django.urls import re_path, path
from rest_framework.routers import SimpleRouter


router = SimpleRouter(False)  # 设置为 False ,为了去掉url后面的斜线

# router.register('book', BookView, basename='book')
no_auth_url = [

]


urlpatterns = [

]
urlpatterns += router.urls