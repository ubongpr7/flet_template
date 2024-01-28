from flet import *
from functools import partial
import flet as fl
import asyncio
from settings.utils import *
from user_controlled_widget import BackgroundControl
from widgets.auth_widgets import logout_user
from widgets.drawer_item import NavDrawerItem
from widgets.images import AppLogo, image_container
from widgets.text_widget import *

class NavDestination(NavigationDestination,):
    def __init__(self,routed,icon_content,label='',data=None):
        super().__init__()
        self.routed=routed
        self.icon_content=icon_content
        self.label=label
        self.data=data

    


class NavBottom(NavigationBar):
    def __init__(self,selfed):

        super().__init__()
        self.selfed=selfed
        self.indicator_color=colors.with_opacity(opacity=0.8,color=colors.ON_TERTIARY)
        self.indicator_shape=None
        self.height=48
        self.elevation=2
        self.label_behavior=NavigationBarLabelBehavior.ALWAYS_HIDE
        self.bgcolor=colors.with_opacity(opacity=0.09,color=colors.PRIMARY_CONTAINER)
        self.destinations=[
            NavDestination(routed='event-home',data='home', icon_content=IconButton(icon_color=colors.PRIMARY,icon_size=20,icon=icons.HOME, on_click=self.go_to_another_page,tooltip='Home',data='home')),
            NavDestination(routed='event-forms',icon_content=IconButton(icon_color=colors.PRIMARY,icon_size=20,icon=icons.ADD, on_click=self.go_to_another_page,tooltip='Create new event',data='add-event')),
            NavDestination(routed='post-forms',icon_content=IconButton(icon_color=colors.PRIMARY,icon_size=20,icon=icons.POST_ADD, on_click=self.go_to_another_page,tooltip='Add post',data='add-post')),
            
            NavDestination(
                routed='bells',
                icon_content=TextButton(
                data='add-post',
                    style=ButtonStyle(bgcolor=None,overlay_color={"":"transparent"},),

                    tooltip='Profile',
                    on_click=self.go_to_another_page,
                    content=Stack(
            

                [
                    Container(
                        content=Icon(icons.MESSAGE,color=colors.PRIMARY,size=15, ),
                        alignment=alignment.center,
                        padding=15

                    ),

                    Container(content=Text(value='45',),alignment=alignment.top_right)
                ],
                width=60,
                ),
                )
    
        
            ),
           
            NavDestination(
                routed='bells',
                icon_content=TextButton(
                data='add-post',
                    style=ButtonStyle(bgcolor=None,overlay_color={"":"transparent"},),

                    tooltip='Profile',
                    on_click=self.go_to_another_page,
                    content=Stack(
            

                [
                    Container(
                        content=Icon(icons.PEOPLE,color=colors.PRIMARY,size=15, ),
                        alignment=alignment.center,
                        padding=15
                    ),

                    Container(content=Text(value='450',),alignment=alignment.top_right)
                ],
                width=60,
                ),
                )
    
        
            ),
           
            NavDestination(
                routed='bells',
                icon_content=TextButton(
                data='add-post',
                    style=ButtonStyle(bgcolor=None,overlay_color={"":"transparent"},),

                    tooltip='Profile',
                    on_click=self.go_to_another_page,
                    content=Stack(
            

                [
                    Container(
                        content=Icon(icons.PEOPLE,color=colors.PRIMARY,size=15, ),
                        alignment=alignment.center,
                        padding=15
                    ),

                    Container(content=Text(value='450',),alignment=alignment.top_right)
                ],
                width=60,
                ),
                )
    
        
            ),
           
        BackgroundControl(selfed=self)
        ]
    async def background_task(self):
            print('1. NavBottom task is running')
            for i in range(len(self.destinations)):
                if self.destinations[i].routed==self.selfed.routed_:
                    self.selected_index=i
                    await self.update_async()
                    break
                else:
                    self.selected_index=50
    async   def go_to_another_page(self,e):
        return await dey_go_async(self=self.selfed,event=e)
        
class LeftSideBar(NavigationDrawer):
    def __init__(self,selfed):
        super().__init__()
        self.elevation=40
        self.selfed=selfed
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.indicator_color=colors.ON_TERTIARY
        self.indicator_shape=StadiumBorder()
        self.shadow_color=colors.SECONDARY
        self.surface_tint_color=colors.ON_TERTIARY
        self.elevation=40
        
        self.controls=[
          BackgroundControl(selfed=self),

            Container(height=12),
            IconButton(content=Container(
                width=100,
                height=100,
                content=AppLogo(selfed=self.selfed)
                ),
                
                style=ButtonStyle(overlay_color={"":"transparent"},),
                on_click=lambda _:go_to_page(self=self,app_name=None, route='home')
                ),
            Divider(thickness=2,color=colors.PRIMARY),

            NavDrawerItem(
                 text_1=' Events',
                text_2='Events',
                tooltip_1='Register, edit and review events',
                icon_1=icons.EVENT_NOTE,
                icon_2=icons.EVENT_NOTE_ROUNDED,
                routed='event-forms',
                on_click_=None,
                
            ),

            Divider(thickness=2,color=colors.PRIMARY),
           

          IconButton(
              content=Row(
                  [
                      Icon(icons.LOGOUT),
                      Text('Logout')
                  ]
              ),
              on_click=self.logout_user
          )
        ]
    
    async def background_task(self):
        print('2. LeftSideBar task is running')

        item_list=[]
        for i in range(len(self.controls)):
            if hasattr(self.controls[i],'routed') ==True:
                    item_list.append(self.controls[i])
                    for item in range(len(item_list)):

                        if item_list[item].routed==self.selfed.routed_:
                            self.selected_index=item
                            await self.update_async()
                            break
                        else:
                            self.selected_index=50
    
    async def logout_user(self,e):
        return await logout_user(self=self.selfed,event=e)

  
        
class RightSideBar(NavigationDrawer):
    def __init__(self,selfed):
        super().__init__()
        self.elevation=40
        self.selfed=selfed
        self.bgcolor=colors.with_opacity(opacity=0.5,color=colors.PRIMARY_CONTAINER)
        self.indicator_color=colors.with_opacity(opacity=0.39,color=colors.ON_TERTIARY)
        self.indicator_shape=StadiumBorder()
        self.shadow_color=colors.with_opacity(opacity=0.59,color=colors.SECONDARY_CONTAINER)
        self.surface_tint_color=colors.with_opacity(opacity=0.69,color=colors.ON_TERTIARY)
        self.elevation=40
        
        
    
        self.status=SmallBodyText(text='')
        self.controls=[
            Container(height=12),
            IconButton(content=Container(
                width=100,
                height=100,
                content=AppLogo(selfed=self.selfed)
                ),
                
                style=ButtonStyle(overlay_color={"":"transparent"},),
                on_click=lambda _:go_to_page(self=self,app_name=None, route='home')
                ),
            Divider(thickness=2,color=colors.PRIMARY),

            NavDrawerItem(
                 text_1=' Events',
                text_2='Events',
                tooltip_1='Register, edit and review events',
                icon_1=icons.EVENT_NOTE,
                icon_2=icons.EVENT_NOTE_ROUNDED,
                routed='event-forms',
                on_click_=lambda _:self.page.go(f'/{project_}/events/event'),
            ),

            Divider(thickness=2,color=colors.PRIMARY),
           

           NavDrawerItem(
                 text_1='Evet Analytics',
                text_2='Analytics',
                tooltip_1='',
                icon_1=icons.ANALYTICS,
                icon_2=icons.ANALYTICS,
                routed='analytics',
            ),
            
          
          BackgroundControl(selfed=self)
        ]
    
    
    async def background_task(self):
        print('4. RightSideBar task is running')
        item_list=[]
        for i in range(len(self.controls)):
            if hasattr(self.controls[i],'routed') ==True:
                    item_list.append(self.controls[i])
                    for item in range(len(item_list)):

                        if item_list[item].routed==self.selfed.routed_:
                            self.selected_index=item
                            await self.update_async()
                            break
                        else:
                            self.selected_index=50
                


             
    def logout_user(self,e):
        logout_user(self=self)