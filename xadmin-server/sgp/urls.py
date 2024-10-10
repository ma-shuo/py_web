# 文件位置 demo/urls.py
from django.urls import re_path, path
from rest_framework.routers import SimpleRouter

from sgp.views.import_add_score import AddScore

router = SimpleRouter(False)  # 设置为 False ,为了去掉url后面的斜线

# router.register('book', BookView, basename='book')
no_auth_url = [
    path('addscore', AddScore.as_view(), name='AddScore'),
]
# router.register('add-score', AddScore, basename='AddScore')

urlpatterns = [

]
urlpatterns = urlpatterns + router.urls + no_auth_url