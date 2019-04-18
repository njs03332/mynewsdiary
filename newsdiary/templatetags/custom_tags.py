from django import template
register = template.Library()

@register.filter
def index(List, i):
    return List[int(i)]

# @register.inclusion_tag('../newsdiary/article/article1.html')
# def render_content():
#     return
