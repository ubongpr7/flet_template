
from .views import *
urlpatterns=[
    EventAddView(routed='event',auth_=False,page=Page),
    PostAddView(page=Page,routed='add-post'),

]

    