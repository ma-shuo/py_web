from common.core.fields import LabeledChoiceField, BasePrimaryKeyRelatedField
from common.core.serializers import BaseModelSerializer
from data.models.sgp import SgpScore


class BookSerializer(BaseModelSerializer):
    class Meta:
        model = SgpScore
        ## pk 字段用于前端删除，更新等标识，如果有删除更新等，必须得加上pk 字段
        fields = ['pk', 'sgp成绩', 'sgp人员', 'sgp考试科目']
        ## 用于前端table字段展示
        table_fields = ['pk', 'sgp成绩', 'sgp人员', 'sgp考试科目']
        read_only_fields = ['pk']
        # fields_unexport = ['pk']  # 导入导出文件时，忽略该字段

    # category = LabeledChoiceField(choices=SgpScore.CategoryChoices.choices,
    #                               default=SgpScore.CategoryChoices.DIRECTORY, label='书籍类型')
    # admin = BasePrimaryKeyRelatedField(attrs=['pk', 'username'], label="管理员", queryset=SgpScore.objects,
    #                                    required=True, format="{username}({pk})")
    # covers = BasePrimaryKeyRelatedField(attrs=['pk', 'filename'],format="{filename}({pk})", label="书籍封面", queryset=models.UploadFile.objects,
    #                                    required=True,  many=True)