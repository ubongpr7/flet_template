from .views import *

from flet import View,Page
from apps.account import urls as account_urls    
from apps.events import urls as event_urls    
from apps.user import urls as user_urls    

urlpatterns=[
 
    EventPage(page=Page,routed='home',)

]

urlpatterns.extend(account_urls.urlpatterns)
urlpatterns.extend(event_urls.urlpatterns)
urlpatterns.extend(user_urls.urlpatterns)




