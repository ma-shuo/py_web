from django.db.models import Avg, Count

from data.models.sgp import SgpScore

def sgp_score_demo():
    result = (
        SgpScore.objects
        .values('sgp考试科目')
        .annotate(sgp=Avg('sgp成绩'), num=Count('sgp人员'))
    )
    return list(result)