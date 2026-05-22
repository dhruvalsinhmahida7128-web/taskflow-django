# middleware for additional request processing
class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code executed before view
        response = self.get_response(request)
        # Code executed after view
        return response