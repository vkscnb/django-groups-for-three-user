from rest_framework.response import Response

def permission_decorator(allowed_roles=[]):
    def decorator(views_fucn):
        def wrapper_func(request, *args, **kwargs):
            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return views_fucn(request, *args, **kwargs)

            else:
                return Response({ "detail": "You are not authorised"})

        return wrapper_func
    return decorator
