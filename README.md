# youth_database
## resourses
### Django_Allauth
Find the documentation [here](http://django-allauth.readthedocs.io/en/latest/installation.html)
    pip install django-allauth
### settings.py (Important - Please note ‘django.contrib.sites’ is required as INSTALLED_APPS):
    'context_processors': [
                # Already defined Django-related contexts here

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
    AUTHENTICATION_BACKENDS = (
    ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
)
### The following apps are required for Django allauth:
    'django.contrib.auth',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
### ... include the providers you want to enable:
    #'allauth.socialaccount.providers.amazon',
    #'allauth.socialaccount.providers.angellist',
    
    accounts/ login/ [name='login']
    accounts/ logout/ [name='logout']
    accounts/ password_change/ [name='password_change']
    accounts/ password_change/done/ [name='password_change_done']
    accounts/ password_reset/ [name='password_reset']
    accounts/ password_reset/done/ [name='password_reset_done']
    accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    accounts/ reset/done/ [name='password_reset_complete']
