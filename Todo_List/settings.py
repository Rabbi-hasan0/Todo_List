import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SECURITY
# =========================
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG=True


CSRF_TRUSTED_ORIGINS = ['https://todo-list-x5kr.onrender.com']
ALLOWED_HOSTS = ['todo-list-x5kr.onrender.com', 'localhost', '127.0.0.1']



# =========================
# APPLICATIONS
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tasks',
    'widget_tweaks',
]


# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",   # static serve for Railway
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = 'Todo_List.urls'


# =========================
# TEMPLATES
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'Todo_List.wsgi.application'


# =========================
# DATABASE (Postgres)
# =========================
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + str(BASE_DIR / "db.sqlite3"),
        conn_max_age=600,
        # শুধুমাত্র যদি DATABASE_URL থাকে (মানে যখন Render-এ থাকবে) তখনই SSL চাইবে
        ssl_require=True if os.getenv("DATABASE_URL") else False,
    )
}



# =========================
# PASSWORD VALIDATION
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 4,
        }
    },
]


# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# =========================
# STATIC FILES
# =========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# প্রোডাকশনে স্ট্যাটিক ফাইল হ্যান্ডেল করার জন্য
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# মিডিয়া ফাইল সেটিংস
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# =========================
# LOGIN / LOGOUT
# =========================
LOGIN_REDIRECT_URL = '/tasklist/'
LOGOUT_REDIRECT_URL = '/login/'
LOGOUT_ON_GET = True

# =========================
# EMAIL (SMTP Gmail secure)
# =========================
# এটি ইমেইল না পাঠিয়ে সরাসরি লগের মধ্যে ইমেইল লিঙ্কটি লিখে দিবে
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASS")
EMAIL_TIMEOUT = 20  # এটি ১০ সেকেন্ড পর কানেকশন ছেড়ে দিবে


# =========================
# DEFAULT PK
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
