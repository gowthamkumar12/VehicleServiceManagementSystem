from django import template
from vehicle.models import *
from vehicle.models import ServiceRequest
register = template.Library()




@register.simple_tag()
def notificationnumber(*args, **kwargs):
    servicecount = ServiceRequest.objects.filter(adminstatus=None).count()

    return servicecount