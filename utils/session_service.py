def get_session_key(request, key):
    return request.session.get(key)


def set_session_key(request, key, value):
    request.session[key] = value
