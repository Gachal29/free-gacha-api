from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)
env.read_env(BASE_DIR / ".env.local")

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
    },
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = "gacha_api.urls"
WSGI_APPLICATION = "gacha_api.wsgi.application"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = False
USE_L10N = False
USE_TZ = False

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"

ADMINS = [("Gacha", "taisuke0129t@gmail.com")]
SERVER_EMAIL = "gacha-api@localhost"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": ("%(levelname)s [%(asctime)s] %(name)s %(message)s"),
        },
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(name)s %(process)d %(thread)d %(message)s"
        },
    },
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
        "require_debug_true": {"()": "django.utils.log.RequireDebugTrue"},
    },
    "handlers": {
        "debug-console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],  # settings.DEBUG=Falseなら全て破棄
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "prod-console": {
            "level": "INFO",
            "filters": ["require_debug_false"],  # settings.DEBUG=Trueなら全て破棄
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {  # 'root' の代わり。全てキャッチする
            "handlers": ["prod-console", "debug-console"],
            "level": "NOTSET",
            "propagate": False,
        },
        "django": {
            "handlers": ["prod-console", "debug-console"],
            "level": "ERROR",  # Djangoモジュール由来のログをERROR以上のみに制限
            "propagate": False,
        },
        "django.request": {
            "handlers": ["prod-console", "debug-console"],
            "level": "ERROR",  # Djangoモジュール由来のログをERROR以上のみに制限
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["prod-console", "debug-console"],
            "level": "DEBUG",  # DBに発行するSQLログを出力（実際の出力はhandlerの方で制御する）
            "propagate": False,
        },
    },
}
