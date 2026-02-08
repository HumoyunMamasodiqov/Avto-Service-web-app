from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

# ==============================
# Base directory
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# Security
# ==============================
SECRET_KEY = 'django-insecure-gpjw0cvjd$8njpmbk)epbme@w95=e4uw%%lu#5@c+vw7!bywm5'
DEBUG = True
ALLOWED_HOSTS = ['*']  # Developmentda hammasi ishlashi uchun

# ==============================
# Installed apps
# ==============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Avto',
    'Auth',
]

# ==============================
# Middleware
# ==============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static fayllar uchun
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==============================
# Root URL and WSGI
# ==============================
ROOT_URLCONF = 'Main.urls'
WSGI_APPLICATION = 'Main.wsgi.application'

# ==============================
# Database
# ==============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================
# Password validation
# ==============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ==============================
# Internationalization
# ==============================
LANGUAGE_CODE = 'uz'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('uz', 'Uzbek'),
    ('ru', 'Russian'),
    ('en', 'English'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# ==============================
# Static files (CSS, JS, Images)
# ==============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Development uchun
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Production uchun
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ==============================
# Media files
# ==============================
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ==============================
# Templates
# ==============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Agar siz qo‘shimcha template papkasi ishlatmoqchi bo‘lsangiz shu yerga qo‘shing
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ==============================
# Default primary key field
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
