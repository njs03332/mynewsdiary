from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from enum import Enum
from polymorphic.models import PolymorphicModel
from django.urls import reverse



# 필수 아닌 것들 한 번 더 체크하기
# 캘린더 API
# seeding

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(validators=[MaxValueValidator(200), MinValueValidator(1)], blank=True, null=True)
    noti_time = models.TimeField(default=datetime.time(hour=10)) #, tzinfo=pytz.timezone(settings.TIME_ZONE)))

    def __str__(self):
        return 'user: %d, name: %s' % (self.user.id, self.name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Category(Enum):
    POL = "정치"
    SOC = "사회"
    ECON = "경제"

class Issue(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    explanation = models.TextField(blank=True)  #markdown?
    categories = ArrayField(models.CharField(max_length=20, choices=[(tag, tag.value) for tag in Category]), default=list)
    # related_dates = ArrayField(models.DateField())  # 캘린더 상에 
    followers = models.ManyToManyField(User, related_name='following_issues', blank=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    datetime = models.DateTimeField()
    title = models.CharField(max_length=50)
    concept = models.TextField(blank=True)
    background = models.TextField(blank=True)
    importance = models.TextField(blank=True)
    explanation = models.TextField(blank=True)  #markdown?
    category = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in Category])
    issue = models.ForeignKey(Issue, on_delete=models.SET_NULL, related_name='events', blank=True, null=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    # author = models.CharField(max_length=20)
    press = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    url = models.URLField(default="https://www.naver.com")
    issue = models.ForeignKey(Issue, on_delete=models.SET_NULL, related_name='articles', blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, related_name='articles', blank=True, null=True)
    parent_event = models.ForeignKey(Event, on_delete=models.SET_NULL, related_name='top_article', blank=True, null=True)  # 어떤 event의 대표기사일 경우

    def __str__(self):
        return self.title

    def update_date(self):  # 자동으로 수정일이 반영되게 하는 방법이 있을까.. 크롤링..? 어렵다
        self.updated_at = timezone.now()
        self.save()

class Journalist(models.Model):  # 그냥 매번 새로 생성. 이름만 들어가므로.. 기자의 기사들 모아보기 같은건 없다..
    name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='authors')

class Memo(models.Model):
    title = models.CharField(max_length=20, default="새로운 메모")
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memos', default=1)
    issue = models.ForeignKey(Issue, on_delete=models.SET_NULL, related_name='memos', null=True)  # 유저가 생성할 때 없는 건 불가능, 나중에 이슈가 삭제되어 표류하는 메모가 생겼을 때는 이 column이 null으로 존재 가능
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, related_name='memos', null=True)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Noti(PolymorphicModel):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)

class NonregularNoti(Noti):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
