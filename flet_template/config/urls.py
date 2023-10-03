from .views import *


from flet import View,Page
from apps.account import urls as account_urls    
# 
class AppView(View):
    pass
    

        
path=AppView
urlpatterns=[
 
    path(route='/home',controls=[HomePage.text]),
    

]

urlpatterns.extend(account_urls.urlpatterns)