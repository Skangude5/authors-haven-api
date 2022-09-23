from .base import *
from .base import env

DEBUG = True



SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default="^3!0xrE3D1y$8W%NK1pRVxDUUwVyBTBvgH%O@zz5U!0wZwUCU1"
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

EMAIL_BACKEND="djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST=env("EMAIL_HOST", default="mailhog")
EMAIL_PORT=env("EMAIL_PORT")
DEFAULT_FROM_EMAIL="info@authors-haven.com"
DOMAIN=env("DOMAIN")
SITE_NAME="Authors Haven"
