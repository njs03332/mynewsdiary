from django.contrib import admin
from .models import Profile, Issue, Event, Journalist, Article, Memo

# Register your models here.
admin.site.register(Profile)
admin.site.register(Issue)
admin.site.register(Event)
admin.site.register(Journalist)
admin.site.register(Article)
admin.site.register(Memo)
# admin.site.register(Noti)
# admin.site.register(NonregularNoti)

