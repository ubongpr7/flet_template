from math import pi
import requests
import time

from flet import *
import flet as fl

from base.app_bar_widget import LernOnAppBar 
from .urls import urlpatterns
from .utils import *
import  asyncio



async def main(page:fl.Page):
        
    async def route_change(route):
        page.views.clear()
        seen =False
        
        for url in urlpatterns:

            if page.route == url.route:
                if url.auth_:
                    if await page.client_storage.get_async(f'{project_}.authenticated'):
                        url.page=page
                
                        page.views.append(url) 
                        seen=True         
                        await page.update_async()
                    else:
                        page.session.set('desired_url',page.route)
                        print(f"Desired url: {page.session.get('desired_url')}")
                        for urled in urlpatterns:
                            if urled.route==f"/{project_}/auth/login":
                        
                                urled.page=page
                                page.route=urled.route
                                page.views.append(urled) 
                                seen=True 
                                print(f"Login first @ {page.route}")        
                                await page.update_async()




                else:
                    url.page=page
                
                    page.views.append(url) 
                    seen=True         
                    await page.update_async()
                    
        

        if not  seen :
            # you can add your custom 404
            page.session.set('wrong_route',page.route)
            print(f"wrong_route  {page.session.get('wrong_route')}")
            if len(page.views)>1: 
                page.views.pop()

                top_view=page.views[-1] 
                await page.go_async(top_view.route)
            else :   
                await page.go_async('/')
                await page.update_async()

    

    async def view_pop(views):
        page.views.pop()
        top_view=page.views[-1] 
        await page.go_async(top_view.route)
        await page.update_async()

    async def refresh_user_token():
        print('start refreshing')
        trial=0
        token=await page.client_storage.get_async(f'{project_}.refresh_token')
        
        while await page.client_storage.get_async(f'{project_}.refresh_token'):
            res= requests.post(
                f'{base_url}api/token/refresh/',
                data={
                    "refresh":token
                    },
                )
            print(res.status_code)
            if res.status_code==200:
                page.session.set(f'{project_}.access_token',str(res.json()["access"] ))
                await page.client_storage.set_async(f'{project_}.refresh_token',str(res.json()["refresh"] ))
                await page.client_storage.set_async(f'{project_}.authenticated',True)
                print('user is logged in')
                
                await asyncio.sleep(1.5*1200)
            else :
                trial+=1
                print(trial)
                if trial==12:
                    await page.client_storage.remove_async(f'{project_}.email')
                    await page.client_storage.remove_async(f'{project_}.access_token')
                    await page.client_storage.remove_async(f'{project_}.refresh_token')
                    await page.client_storage.set_async(f'{project_}.authenticated',False)
                    print(f'user is logged out after {trial} trials')

    
    async def tasks_():
        print('tasks started')
        asyncio.create_task(refresh_user_token())
    await asyncio.create_task(tasks_())              
    page.window_bgcolor=colors.PRIMARY_CONTAINER
    page.fonts={
    'heading': 'fonts/Roboto/Roboto-Bold.ttf',
    'body': 'fonts/Roboto/Roboto-Medium.ttf',
    'subheading': 'fonts/Roboto/Roboto-Regular.ttf',
    'sanserifl': 'fonts/sanserif/OpenSans-Light.ttf',
    'styled': 'fonts/Lobster/Lobster-Regular.ttf',
    

    }
    page.title=project_name
    page.theme_mode='light'
    
    if page.theme_mode=='light':
        page.theme= fl.Theme(
            color_scheme=fl.ColorScheme(
                #mostly Text
                primary ='#000000',
                secondary ='#757575',
                # on_tertiary_container='#809CFF',
                tertiary ="#CBCBCB",

                #mostly buttons 
                on_primary ="#000000",
                on_secondary='#BB74CD',
                on_tertiary="#1980E6",
                
                #mostly Container
                primary_container ='#F5F7F9',
                secondary_container ='#FFFFFF',
                tertiary_container="#F5F5F5",
                
                

            ),
        )
        await page.client_storage.set_async(f'{project_}.logo','images/logos/logo-white.svg')

    else:    
        page.theme= fl.Theme(
            color_scheme=fl.ColorScheme(
               #mostly Text
                primary ='#c8e6c9',
                # primary ='#000154',
                secondary ='#f5fdc',
                tertiary ="#CBCBCB",

                #mostly buttons 
                on_primary ="#4caf50",
                on_secondary='#795548',
                # primary_container ='#1f262f',


                
                #mostly Container
                primary_container ='#2D292D',
                secondary_container ='#000000',

                tertiary_container="#F5F5F5",

            )
        )
        await page.client_storage.set_async(f'{project_}.logo','images/logos/logo-blue.svg')

        

    page.on_view_pop=view_pop
    page.auto_scroll=True
    page.on_route_change=route_change
    await page.go_async(page.route)
    
    await page.update_async()
