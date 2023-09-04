# from locales import language_en,language_fa
# from utils.session_service import get_session_key, set_session_key
#
#
# def get_language_dic(request):
#     language = get_session_key(request, 'language')
#     if language is not None:
#         if language == 'fa':
#             return language_fa
#         else:
#             return language_en
#     else:
#         set_session_key(request, 'language', 'en')
#         return language_en
#
#
# def get_language_status(request):
#     language = get_session_key(request, 'language')
#     if language is not None:
#         if language == 'fa':
#             return 'fa'
#         else:
#             return 'en'
#     else:
#         set_session_key(request, 'language', 'en')
#         return 'en'
#
#
# def get_language_with_status(request):
#     language = get_session_key(request, 'language')
#     if language is not None:
#         if language == 'fa':
#             return 'fa', language_fa
#         else:
#             return 'en', language_en
#     else:
#         set_session_key(request, 'language', 'en')
#         return 'en', language_en
