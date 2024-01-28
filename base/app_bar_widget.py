from flet import *
import requests
import asyncio
from settings.utils import *
from user_controlled_widget import *
from widgets.auth_widgets import logout_user
from widgets.buttons_widget import column_set
from widgets.countdown import CountDown
from widgets.images import AppLogo, affm_logo, width_fitted_image
from apps.account.utils import *
from widgets.notifications import NotificationItem
from widgets.text_widget import *
   


class LernOnAppBarAuth(AppBar):
    def __init__(self,selfed,center_title_):
        super().__init__()
        self.auth_links=Row()
        self.selfed=selfed
         
        self.title=IconButton(content=Container(
                width=60,
                height=60,
                content=Icon(icons.HOME)
                ),
                
                style=ButtonStyle(overlay_color={"":"transparent"},),
                on_click=self.go_home
                )
        self.center_title=center_title_
                
    async def go_home(self,e):
        await   self.selfed.page.go_async('/')
        
      
class LernOnAppBar(AppBar):
    def __init__(self,selfed):
        super().__init__()
        self.auth_links=Row()
        self.center_title=True
        self.selfed=selfed
        self.leading=Row(
            [

                IconButton(icon=icons.MENU,height=30,tooltip='Open Navigation menu',icon_color=colors.PRIMARY,on_click=self.show_right_drawer)
            ]
        )
        
        self.bgcolor=colors.with_opacity(opacity=0.45,color=colors.SECONDARY_CONTAINER)
        self.user_account=Row()
        self.log_btn=ElevatedButton(content=SmallBodyText(text='Login',color=colors.SECONDARY_CONTAINER),bgcolor=colors.ON_PRIMARY,height=30) 
        self.reg_btn=OutlinedButton(content=SmallBodyText(text='Join us',color=colors.PRIMARY),on_click=self.Join_link,height=30) 
        self.profile_pic=CircleAvatar(
            radius=20
                )
        self.profile_pic_cont=TextButton(
            content=self.profile_pic,
            on_click=self.show_right_drawer
            
            )
        self.account_menu=Stack(
            [

                self.profile_pic_cont,
                Container(
                    content=CircleAvatar(bgcolor=colors.GREEN, radius=5),
                    alignment=alignment.bottom_right,
            on_click=self.show_left_drawer

                ),
           
            ],
            width=40,
            height=40,
        
        )
        
        self.title=IconButton(content=Container(
                width=60,
                height=60,
                content=AppLogo(selfed=self.selfed)
                ),
                
                style=ButtonStyle(overlay_color={"":"transparent"},),
                on_click=self.go_home,
                data='home'
                )
                
      
        
        self.actions=[
            BackgroundControl(selfed=self),

                                    
            Row(
                    controls=[
                    
                    self.auth_links,
                    
                
                        
                    ]
                ),
            
            # Row(width=10),
            self.user_account,
                                
            
        Row(width=15),
        ]
    async def background_task(self):
            print('menu task')
            pk=await get_user_id(self)
            print(f'pk {pk}')
            user_email=await get_access_email(self)

            print(f'user_email {user_email}')
            if await self.selfed.page.client_storage.get_async(f'{project_}.authenticated'):
                self.log_btn.on_click=self.logout_user 
                self.log_btn.content=LargeLabelText(text='Logout',color=colors.SECONDARY) 
                self.auth_links.controls=[] 
                res=  make_authenticated_request_async(self=self.selfed,url=f'account_api/user/{pk}',cookie=user_email,key='email',method='get')
                print(res.status_code)
                self.profile_pic_cont.on_click=self.show_left_drawer
                if res.status_code==200:
                    self.profile_pic.foreground_image_url=f'{str(res.json()["picture"])}'
                    self.account_menu.controls[1].tooltip=f'{str(res.json()["first_name"])} {str(res.json()["last_name"])}'          
                    self.user_account.controls=[
                        IconButton(icon=icons.SEARCH,icon_color=colors.PRIMARY,tooltip='Search'),

                    PopupMenuButton(
                        content=Stack(
                    
                    controls=[
                        IconButton(icon=icons.NOTIFICATIONS,icon_color=colors.PRIMARY,),
                        Container(
                            tooltip='Notifications',
                    content=CircleAvatar(bgcolor=colors.PRIMARY,content=SmallBodyText(text='500',color=colors.SECONDARY_CONTAINER), radius=10),
                    alignment=alignment.top_right,
                ),
           
                        ],
                        height=40,
                        width=40
                        ),
                       
                            items=[
                                NotificationItem(image=f'{str(res.json()["picture"])}',notification='Sunny sent you a message'),
                                Divider(color='transparent'),
                                NotificationItem(image=f'{str(res.json()["picture"])}',notification='There is an outreach to the farm site'),
                                Divider(),
                                NotificationItem(image=f'{str(res.json()["picture"])}',notification='Sunny sent you a message'),
                                Divider(color='transparent'),
                                NotificationItem(image=f'{str(res.json()["picture"])}',notification='There is an outreach to the farm site'),
                                Divider(),

                                
                            ]
                    ),
                        
                        self.account_menu,
                        ] 
                    await   self.update_async()

            else: 
                self.log_btn.on_click=self.login_link
                self.log_btn.content=LargeLabelText(text='Login',color=colors.SECONDARY_CONTAINER)    
                self.auth_links.controls=[self.log_btn,self.reg_btn]
                self.user_account.controls=  []
                print('user!auth')
                await self.update_async()
   
    async  def  login_link(self,e):
        await self.selfed.page.go_async(f'/{project_}/auth/login')
    async def dey_go_async(self,e,d_route):
        return await dey_go_async(self=self.selfed,d_route=d_route)
    
    async def show_left_drawer(self,e):
        if self.selfed.end_drawer:
            self.selfed.end_drawer.open=True
            print('drawer')
            await self.selfed.update_async()
        else:
           await go_to_page(self=self.selfed,app_name='auth',route='login')
    
        
    async  def show_right_drawer(self,e):
        if self.selfed.drawer:
            self.selfed.drawer.open=True
            await self.selfed.update_async()
        else:
           await go_to_page(self=self.selfed,app_name='auth',route='login')
   
        
    async def logout_user(self,e):
        await logout_user(self=self.selfed)    
    
    async def go_home(self,e):
        await   self.selfed.page.go_async('/')
    async def Join_link(self,e):
        await   self.selfed.page.go_async(f'/{project_}/auth/register')
