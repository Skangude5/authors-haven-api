from .base import *
from .base import env

DEBUG = True



SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default="^3!0xrE3D1y$8W%NK1pRVxDUUwVyBTBvgH%O@zz5U!0wZwUCU1"
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]