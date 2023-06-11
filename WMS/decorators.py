from django.shortcuts import render


def group_required(groups):
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated and user.groups.filter(name__in=groups).exists():
                return view_func(request, *args, **kwargs)
            else:
                return render(request, "core/access_denied.html")

        return wrapped_view

    return decorator
