from django.utils.deprecation import MiddlewareMixin
from . models import Visitors


class VisitorsMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)

        if not request.session.session_key:
            request.session.create()
    
        ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
        user_agent = request.META.get('HTTP_USER_AGENT', '')

        Visitors.objects.create(
            session_id = request.session.session_key,
            ip_addres_of_visitor  = str(ip),
            user_agent = user_agent,
            path = request.path,
        )

        return response


    # def process_request(self, request):
    #     ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
    #     user_agent = request.META.get('HTTP_USER_AGENT', '')

    #     Visitors.objects.create(
    #         ip_addres_of_visitor  = str(ip),
    #         user_agent = user_agent,
    #         path = request.path,
    #     )