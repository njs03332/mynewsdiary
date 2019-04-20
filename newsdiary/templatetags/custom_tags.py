from django import template
from newsdiary.models import Issue
from datetime import datetime
register = template.Library()

@register.filter
def index(List, i):
    return List[int(i)]

@register.filter
def length(QuerySet):
    return QuerySet.count()

@register.filter
def days_left(Event):
    return (Event.datetime.date() - datetime.today().date()).days

@register.filter
def events(Issue):
    return Issue.events.all()

@register.filter
def date_only(datetime):
    arr = str(datetime.date()).split('-')
    ret = arr[1] + '/' + arr[2]
    return ret

# for calendar template range
@register.filter(name='fisttimes') 
def firstimes(number):
    if number == 6: # 첫째날이 일요일일 때
        return range(0)
    else:
        return range(number + 1)

@register.filter(name='lasttimes') 
def lasttimes(number):
    if number == 6: # 마지막 날이 일요일일 때
        return range(6);
    else:
        return range(5 - number)

@register.filter(name='times') 
def lasttimes(number):
    return range(number)




# @register.inclusion_tag('../newsdiary/article/article1.html')
# def render_content():
#     return
