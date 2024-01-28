import asyncio
from flet import *
from settings.utils import *

from widgets.buttons_widget import image_address1
from widgets.text_widget import PageHeading_3

class AppLogo(UserControl):
    def __init__(self,selfed):
        super().__init__()
        self.selfed=selfed
        
    
    # async def bg_task(self):
    #         print('src is coming')
    #         if await self.selfed.page.client_storage.get_async(f'{project_}.logo'):

    #             self.image.src= await self.selfed.page.client_storage.get_async(f'{project_}.logo')
    #             await self.update_async()
    #         else:
    #             self.image.src='images/logos/logo-blue.svg'
    #             await self.update_async()
    # async def did_mount_async(self):
    #      self.running=True
    #      asyncio.create_task(self.bg_task())
    # async  def will_unmount_async(self):
    #      self.running=False


    def build(self):
        self.image=Image(src='images/logos/logo-blue.svg',fit=ImageFit.CONTAIN,tooltip='home') 
        return   self.image


def width_fitted_image(src):
    return Image(
            src=src,
            fit=ImageFit.FIT_WIDTH,
        )
def height_fitted_image(src):
    return Image(
            src=src,
            fit=ImageFit.FIT_HEIGHT,
        )
def container_fitted_image(src):
    return Image(
            src=src,
            fit=ImageFit.CONTAIN,
        )
def affm_logo(selfed):
    if selfed.page.client_storage.get('logo'):
        return selfed.page.client_storage.get('logo')
    else:
        return  'images/logos/lernon_logowl.svg'

def profile_avartar(self,user_pk:int,on_click_=None,width=30,height=30,radius=15):
    res=make_authenticated_get_request(self=self,url=f'account_api/user/{user_pk}',cookie=get_access_email(self=self),key='email')
    if res.status_code==200:
        profile_pic=f'{str(res.json()["picture"])}'
        tooltip=f'{str(res.json()["first_name"])} {str(res.json()["last_name"])}'          

        return Container(
                on_click=on_click_,
                tooltip=tooltip,
                content= Stack(
                height=height,
                width=width,
                controls=[CircleAvatar(
                    
                    foreground_image_url=profile_pic,
                    radius=radius,
                    
                ),
                Container(
                content=CircleAvatar(bgcolor=colors.GREEN, radius=2),
                alignment=alignment.bottom_right,
            ),
                ]
                ),
                
        )
                    

def image_container(self,title , image_name,sub_title,slides=1):
        
        return Container(
            height=300,
            image_src=image_address1(name=image_name),
            image_fit=ImageFit.FIT_WIDTH,
            border=border.all(0.8,colors.PRIMARY_CONTAINER),
            border_radius=20,
            padding=20,
            content=ResponsiveRow(
                vertical_alignment='center',
                controls=[
                    Row(height=50),
                   Container(
                       padding=20,
                       height=150,

                        bgcolor=colors.with_opacity(opacity=0.0,color=colors.PRIMARY_CONTAINER),
                       
                   ),
                    Row(height=1.5),
                   
                    PageHeading_3(main_title=title,main_size=20,sub_size=12,sub_title='',bg_color=colors.SECONDARY_CONTAINER,text_color=colors.PRIMARY),
                   
                    
                ],
            )
        )   
    

