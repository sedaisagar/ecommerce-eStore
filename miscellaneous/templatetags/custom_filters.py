from django import template

from users.models import User

register = template.Library()

@register.filter
def get_attr(obj, attr_name):
    """
    Dynamically retrieves an attribute from an object.
    Usage: {{ object|get_attr:attribute_name_variable }}
    """
    return getattr(obj, attr_name, "") # returns an empty string if not found
