from profiles.classes import CLASS_NAMES
from django import template

register = template.Library()


@register.filter
def get_class_name(class_code):
    for code, name in CLASS_NAMES:
        if code == class_code:
            return name
    return 'NO_CLASS'
