from .common_settings import *

#mail setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hadi.hadi.oc@gmail.com'
EMAIL_HOST_PASSWORD = 'tozyrzptsuttyydj'

# DRF settings
REST_FRAMEWORK = {
    # YOUR SETTINGS
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
],
}
#DRF sepctacular settings
SPECTACULAR_SETTINGS = {
"TITLE": "Blog API Project",
"DESCRIPTION": "A sample blog to learn about DRF",
"VERSION": "1.0.0",
# OTHER SETTINGS
}

#CSRF
CSRF_TRUSTED_ORIGINS = ["http://192.168.100.31:3000","https://192.168.100.31:3000",
                        "http://127.0.0.1:3000","https://192.168.100.31",
                        "http://192.168.100.30"
                        ]


CORS_ALLOWED_ORIGINS = [
    "http://192.168.100.31",
    "http://192.168.100.30"

]

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)