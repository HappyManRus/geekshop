from xml.etree import ElementTree as ET

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="mail_to")
def mail_to(input_str):
    """
    Create link `mailto:`
    """
    link_mailto = ET.Element("a", {"href": f"mailto:{input_str}"})
    link_mailto.text = input_str
    return mark_safe(ET.tostring(link_mailto, encoding="unicode"))


@register.filter(name="tel")
def tel(input_str):
    """
    Create link `tel:`
    """
    link_tel = ET.Element("a", {"href": f"tel:{input_str}"})
    link_tel.text = input_str
    return mark_safe(ET.tostring(link_tel, encoding="unicode"))


# Or you can register tag like this
# register.filter("mail_to", mail_to)
