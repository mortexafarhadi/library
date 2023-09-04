from utils.session_service import get_session_key, set_session_key


def check_theme(request):
    theme = get_session_key(request, 'theme')
    res = 'light'
    if theme is not None:
        if theme == 'dark':
            res = 'dark'
            return res
        else:
            return res
    else:
        set_session_key(request, 'theme', 'light')
        return res
