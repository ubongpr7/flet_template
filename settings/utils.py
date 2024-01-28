import asyncio
from flet import *
import requests
import flet as fl

base_url='http://3.132.196.131/'


project_='web.dev'       

project_name='Simply Bells'


urlpatterns_={

    'home':f'/',
    'login':f'/{project_}/auth/login',
    'add-event':f'/{project_}/events/event',
    'add-post':f'/{project_}/events/add-post',
    'profile':f'/{project_}/user/profile',
    'register':f'/{project_}/auth/register',
    'profile-settings':f'/{project_}/auth/profile-settings',
    'reset-email':f'/{project_}/auth/reset-email',
    'reset-password':f'/{project_}/auth/reset-password',

}


async def get_user_id(self):
    return await self.page.client_storage.get_async(f'{project_}.pk')
def get_refresh_token_page(self):
    try :
            return  self.client_storage.get(f'{project_}.refresh_token')
    except :
        return False
async def get_access_token(self):
    try :
        if self.page:
            return await self.page.client_storage.get_async(f'{project_}.access_token')
    except :
        return False
async def get_access_email(self):
    try:
        if self.page:

            return await self.page.client_storage.get_async(f'{project_}.email')
    except :
        return False
async def is_authenticated(self):
    try:
        if self.page:

            return await self.page.client_storage.get_async(f'{project_}.authenticated')
    except :
        return False

class User():
    def __init__(self, selfed ):
        self.selfed=selfed
    
    def  user_id(self):
        return self.selfed.page.client_storage.get(f'{project_}.pk')
    async def  user_email(self):
        return await str(self.selfed.page.client_storage.get_async(f'{project_}.email'))
    async def  user_token(self):
        return await str(self.selfed.page.client_storage.get_async(f'{project_}.token'))
    async def  user_is_logged_in(self):
        return await str(self.selfed.page.client_storage.get_async(f'{project_}.authenticated'))

class UserPage():
    def __init__(self, selfed):
        self.selfed=selfed
    
    async def  user_id(self):
        return await str(self.selfed.client_storage.get_async(f'{project_}.pk'))
    async def  user_email(self):
        return await str(self.selfed.client_storage.get_async(f'{project_}.email'))
    def  refresh_token(self):
        return self.client_storage.get(f'{project_}.refresh_token')
    async def  user_token(self):
        return await str(self.selfed.client_storage.get_async(f'{project_}.token'))
    async def  user_is_logged_in(self):
        return await str(self.selfed.client_storage.get_async(f'{project_}.authenticated'))


def make_authenticated_request_async(self,url,cookie=None,key=None,method='get',request_type='data',data=None):
    cookies={str(key):str(cookie)}
    token= self.page.session.get(f'{project_}.access_token')
    headers={
        "Authorization":f"Bearer {token}"
    }
    if request_type !='files':
        if method=='get':

            response=requests.get(url=f'{base_url}{url}/',headers=headers,cookies=cookies)
            return   response
        elif  method=='post':
            response=requests.post(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
            return   response

        elif method=='put':
            response=requests.put(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
            return   response
        
        elif method=='patch':
            response=requests.patch(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
            return  response
            
        elif method=='delete':
            response=requests.delete(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
            return   response
            
    else:
        response=requests.post(url=f'{base_url}{url}/',headers=headers ,files=data,cookies=cookies)
        return   response
def make_authenticated_request(self,url,cookie=None,key=None,method='get',request_type='data',data=None):
    cookies={str(key):str(cookie)}
    token=get_access_token(self=self)
    headers={
        "Authorization":f"Bearer {token}"
    }
    if request_type !='files':
        if method=='get':

            response=requests.get(url=f'{base_url}{url}/',headers=headers,cookies=cookies)
            return response
        elif  method=='post':
            response=requests.post(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
            return 
        elif method=='put':
            response=requests.put(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
            return response
        elif method=='patch':
            response=requests.patch(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
            return response
        elif method=='delete':
            response=requests.delete(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
            return response
    else:
        response=requests.post(url=f'{base_url}{url}/',headers=headers ,files=data,cookies=cookies)
        return response
def make_authenticated_get_request(self,url,cookie,key):
    cookies={str(key):str(cookie)}
    token=get_access_token(self=self)
    headers={
        "Authorization":f"Bearer {token}"
    }
    response=requests.get(url=f'{base_url}{url}/',headers=headers,cookies=cookies)
    return response
def make_authenticated_post_request(self,url,data,cookie,key):
    cookies={str(key):str(cookie)}

    token=get_access_token(self=self)
    headers={
        "Authorization":f"Bearer {token}"
    }
    response=requests.post(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
    return response
def make_authenticated_put_request(self,url,data,cookie,key):
    cookies={str(key):str(cookie)}

    token=get_access_token(self=self)
    headers={
        "Authorization":f"Bearer {token}"
    }
    response=requests.put(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
    return response
def make_authenticated_patch_request(self,url,data,cookie,key):
    cookies={str(key):str(cookie)}

    token=get_access_token(self=self)
    headers={
        "Authorization":f"Bearer {token}"
    }
    response=requests.patch(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
    return response
def make_authenticated_delete_request(self,url,data,cookie,key):
    cookies={str(key):str(cookie)}

    token=get_access_token(self=self)
    headers={
        "Authorization":f"Bearer {token}"
    }
    response=requests.delete(url=f'{base_url}{url}/',headers=headers ,data=data,cookies=cookies)
    return response
async def go_to_page(self, route,app_name):
    if app_name:
        return await self.page.go(route=f'/{project_}/{app_name}/{route}')
    else:
        return await self.page.go(route=f'/{project_}/{route}')

def go_to_paged(self, route):
    return self.selfed.page.go(route=f'/{project_}/{route}')

async def dey_go_async(self, event):
    for route in urlpatterns_:
            if event.control.data.lower()==route:
                print(urlpatterns_[route])
                await self.page.go_async(urlpatterns_[route])
