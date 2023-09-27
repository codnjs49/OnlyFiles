"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--k7ej+vgw=goxnxt9o+%!l^yl1z1*zw2(om=%6%a8sl$x33(^i"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    #added
    "rest_framework",
    "corsheaders",
    "app"
]

#added
CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASE_ROUTERS = ['app.dbrouter.server1Router', 'app.dbrouter.server2Router', 'app.dbrouter.server3Router', 
                    'app.dbrouter.server4Router', 'app.dbrouter.server5Router', 'app.dbrouter.server6Router', 'app.dbrouter.server7Router']
DATABASE_APPS_MAPPING = {'FileServer1': 'server1',
                         'FileServer2': 'server2',
                         'FileServer3': 'server3',
                         'FileServer4': 'server4',
                         'FileServer5': 'server5',
                         'FileServer6': 'server6',
                         'FileServer7': 'server7',}

DATABASES = {
    "default": {
       "ENGINE": "django.db.backends.postgresql",
        "NAME": "metadatadb",
        "USER": "postgres",
        "PASSWORD": "passcanliao",
        "HOST": "testdb.c9ybbr2jzshu.ap-southeast-1.rds.amazonaws.com",
        "PORT": "5432",
    },

    "server1": {
       "ENGINE": "django.db.backends.postgresql",
        "NAME": "FileServer1",
        "USER": "postgres",
        "PASSWORD": "passcanliao",
        "HOST": "testdb.c9ybbr2jzshu.ap-southeast-1.rds.amazonaws.com",
        "PORT": "5432",
    },

    "server2": {
       "ENGINE": "django.db.backends.postgresql",
        "NAME": "FileServer2",
        "USER": "postgres",
        "PASSWORD": "passcanliao",
        "HOST": "testdb.c9ybbr2jzshu.ap-southeast-1.rds.amazonaws.com",
        "PORT": "5432",
    },

    "server3": {
       "ENGINE": "django.db.backends.postgresql",
        "NAME": "FileServer3",
        "USER": "postgres",
        "PASSWORD": "passcanliao",
        "HOST": "testdb.c9ybbr2jzshu.ap-southeast-1.rds.amazonaws.com",
        "PORT": "5432",
    },

    "server4": {
       "ENGINE": "django.db.backends.postgresql",
        "NAME": "FileServer4",
        "USER": "postgres",
        "PASSWORD": "passcanliao",
        "HOST": "testdb.c9ybbr2jzshu.ap-southeast-1.rds.amazonaws.com",
        "PORT": "5432",
    },
    "server5": {
       "ENGINE": "django.db.backends.postgresql",
        "NAME": "FileServer5",
        "USER": "postgres",
        "PASSWORD": "passcanliao",
        "HOST": "testdb.c9ybbr2jzshu.ap-southeast-1.rds.amazonaws.com",
        "PORT": "5432",
    },
    "server6":{ ## azure?
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "FileServer6",
        "USER": "myadmin",
        "PASSWORD": "Passcanliao1",
        "HOST": "myfypserver.postgres.database.azure.com",
        "PORT": "5432",
    },
    "server7":{ ## azure?
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "FileServer7",
        "USER": "myadmin",
        "PASSWORD": "Passcanliao1",
        "HOST": "myfypserver.postgres.database.azure.com",
        "PORT": "5432",
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Singapore"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
