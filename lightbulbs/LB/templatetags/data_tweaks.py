from django import template

register = template.Library()


@register.simple_tag
def get_list(ds_values):
    try:
        return ds_values.value().split("~")[:-1]
    except:
        return ds_values.split("~")[:-1]
