from settings.utils import *

app_name_='user'



def get_user_status(self):
    res=make_authenticated_get_request(self=self,url=f'account_api/user/{User(selfed=self).id}',cookie=get_access_email(self=self),key='email')
    if res.status_code==200:

        for item in res.json():
            if item=='is_superuser':
                if res.json()[item]:
                    self.status.value="Super User"
            elif item=='is_worker':
                if res.json()[item]:
                    self.status.value="Staff"
                    
            elif item=='is_stakeholder':
                if res.json()[item]:
                    self.status.value="Senior Staff"
            elif item=='is_dep_head':
                if res.json()[item]:
                    self.status.value="Admin"
                            
            elif item=='is_investor':
                if res.json()[item]:
                    self.status.value="Investor"
            else:
                    self.status.value="User"
# https://www.loom.com/share/11c416a644d541e9b219df270454a35f?sid=d2b18ad5-3350-450a-8cd3-1f39d14cc16c
# https://www.loom.com/share/b420ea80f1c04062aa5ecc114686058a?sid=ba746022-f3aa-4eba-9bc8-3cd504b312a8