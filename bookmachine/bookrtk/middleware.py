from django.utils.deprecation import MiddlewareMixin
from . models import Visitors


class VisitorsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        Visitors.objects.create(
            ip_addres_of_visitor  = str(ip),
            user_agent = user_agent,
            path = request.path,
        )