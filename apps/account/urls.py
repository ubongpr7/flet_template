from .views import *
from flet import Page
urlpatterns=[
    LoginPage(routed='login',page=Page),
    Registration(routed='register',page=Page),
    PasswordResetEmail(routed='reset-email',page=Page),
    PasswordReset(routed='reset-password',page=Page),
    
]

    