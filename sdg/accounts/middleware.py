from django.http import HttpResponseForbidden

class AccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = request.user

        if request.path == '/create_goal/' and not user.groups.filter(name='Normal User').exists():
            return HttpResponseForbidden("Permission Denied")

        if request.path == '/create_challenge/' and not user.groups.filter(name='Company').exists():
            return HttpResponseForbidden("Permission Denied")

        return response
