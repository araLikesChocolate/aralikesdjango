"""
Django settings for notebook project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'www_dir', 'secret_key.txt')) as f :
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
# 개발 환경
DEBUG = True
# 실행 환경
#DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    # pip install django-rest-auth
    'rest_auth',
    'app1_ara',
    'registration',
    'api',
]

# 임시로 보안사항을 열어줌
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'notebook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'notebook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #    'NAME': os.path.join(BASE_DIR, 'db', 'db.sqlite3'),
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'notebook_db',  #mysql
    #    'USER': 'root', #root
    #    'PASSWORD': '1234', #1234
    #    'HOST': '192.168.22.126', #공백으로 냅두면 default localhost
    #    'PORT': '3307' #공백으로 냅두면 default 3306
   }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# static 파일에 접근하기위한 url을 작성하는 곳
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "registration", "static"),
)

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'registration/login/'
LOGIN_URL = 'registration/login/'

# STATIC_ROOT collectstatic 명령어를 통해서 수집되는 static 파일들이 위치하는 곳
# 운영 모드에서는 static 파일들의 위치를 지정해주어야한다. 
# python manage.py collectstatic을 실행하면 BASE_DIR/www_dir/static에 정적 파일들이 모아진다.
STATIC_ROOT = os.path.join(BASE_DIR, 'www_dir', 'static')

# 장고의 디폴트 설정을 유지하면서 로깅 설정함
# LOGGING = {
#     'version' : 1,
#     'disable_exitsting_loggers' : False,
#     'formatters' : {
#         'verbose' : {
#             'format' : '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
#             'datefmt' : '%d/%b/%Y %H:%M:%S',
#         },
#     },
#     'handlers' : {
#         'app1_ara' : {
#             'level' :'DEBUG',
#             'class' : 'logging.FileHandler',
#             'filename' : os.path.join(BASE_DIR, 'logs', 'app1_ara.log'),
#             'formatter' : 'verbose',
#         },
#     },
#     'loggers' : {
#         'app1_ara' : {
#             'handlers' : ['app1_ara'],
#             'level' : 'DEBUG',
#         },
#     },
# }