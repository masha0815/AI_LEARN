from django.db import models

# Create your models here.
# home/models.py

class TopicModel(models.Model) :
    topic_idx = models.AutoField(primary_key=True)
    topic_name = models.TextField(null=False)

# CASCADE : 상위 클래스에서 값을 지우면 그 값을 참조하고 있는 모든 클래스의 값들이 자동으로 지워지게 해준다.
class ContentModel(models.Model) :
    content_idx = models.AutoField(primary_key=True)
    content_topic_idx = models.ForeignKey(TopicModel, null=False, on_delete=models.CASCADE)
    content_text = models.TextField(null=False)






