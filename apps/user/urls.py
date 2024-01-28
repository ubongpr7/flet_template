from .views import *

urlpatterns=[
    Profile(routed='profile',auth_=True,page=Page),
    ProfileSettings(routed='profile-settings',page=Page,auth_=True),

]

    