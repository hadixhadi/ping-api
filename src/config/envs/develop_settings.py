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
}
#DRF sepctacular settings
SPECTACULAR_SETTINGS = {
"TITLE": "Blog API Project",
"DESCRIPTION": "A sample blog to learn about DRF",
"VERSION": "1.0.0",
# OTHER SETTINGS
}