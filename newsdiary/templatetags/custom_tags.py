from django import template
register = template.Library()

@register.filter
def index(List, i):
    return List[int(i)]

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
