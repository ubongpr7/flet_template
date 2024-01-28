from flet import *
import datetime
from flet import *
import requests
from math import pi
from http import cookies
import asyncio

from base.app_bar_widget import *
from widgets.auth_widgets import *
from base.base_ import  *
from widgets.buttons_widget import column_set
from widgets.cards_ import *
from widgets.images import *
from widgets.page_widget import sections_container
from widgets.text_input_widget import NumberInput
from widgets.text_widget import  * 
from settings.utils import *
from .utils import *
from widgets.countdown import CountDown

class  ProfileSettings(View):
    def __init__(self,page:Page,routed,auth_=None,routed_='profile-settings'):
        super().__init__()
        self.divider=Divider(
            height=2, color='transparent',
            
        )
        self.routed=routed

        self.routed_=routed_
        self.page=page
        self.appbar=LernOnAppBar(selfed=self)
        self.end_drawer=RightSideBar(selfed=self)

        self.route=f'/{project_}/{app_name_}/{routed}'

        self.email= AuthInputField(field_hint='First name',focus_input=True,type='name')              
        self.password= AuthInputField(field_hint='Last Name',focus_input=False,type='name')              
        self.password_verifier=Text(color=colors.RED_300,height=0)
        self.verify=Text(color=colors.RED_300,height=0)
        self.auth_=auth_
        self.account_type=RadioGroup(
            content=ResponsiveRow(
                controls=[

                    Radio(
                        value='is_student',
                        label='Student'
                    ),
                    Radio(
                        value='is_teacher',
                        label='Teacher'
                    ),
                    Radio(
                        value='is_lecturer',
                        label='Lecturer'
                    ),
                ]
            )
        )        
        self.account_type_verifier=Text()

        self.heading=PageHeading_2(main_title='Initial Profile Settings',bg_color=None,main_size=22,sub_title='Fill in your details correctly and as applicable to you', text_color=colors.PRIMARY, sub_size=13)
        self.view_container=Container(
            content=Column(
                controls=[

                        # self.stack,
                          
                        self.divider,
                        self.heading,
                        self.divider,
                        AuthInputContainer(icon_name=icons.EMAIL_ROUNDED,input_field=self.email),

                        self.verify,
                        AuthInputContainer(icon_name=icons.LOCK_PERSON_ROUNDED,input_field=self.password),

                        self.password_verifier,
                        Text('Account Type'),

                        self.account_type,
                        self.account_type_verifier,

                        ElevatedButton('Next',width=300, color=colors.PRIMARY,bgcolor=colors.BLUE,on_click=self.fill_validation),
                        ],
                horizontal_alignment='center',
                alignment='center'),
            bgcolor=colors.SECONDARY_CONTAINER,
            border_radius=12,

        )
        
        self.register_card=Card(
            elevation=15,
            content=self.view_container,

            )
        self.controls=[self.register_card]
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.vertical_alignment='center'
        self.horizontal_alignment='center'
        

        
    def fill_validation(self,e):
        if  self.email.value=='' :
            self.verify.value='First Name field is required'
            self.verify.height=20
            
            self.verify.update()
        else:    
            self.verify.value=''
            self.verify.height=0
            
            self.verify.update()
        
        if  self.password.value=='' :
            self.password_verifier.value='Last name field is required'
            self.password_verifier.height=20

            self.password_verifier.update()
        else:
            self.password_verifier.value=''
            self.password_verifier.height=0
            self.password_verifier.update()
            
            res=make_authenticated_put_request(
                self=self,
                url=f'account_api/user/{User(selfed=self).id}',
                data={
                    'first_name':str(self.email.value),
                    'last_name':str(self.password.value),
                    
                      },
                      cookie=None,
                      key=None

                )
            if res.status_code==200:
                go_to_page(self=self, app_name=app_name_, route='profile')
             

    def did_mount(self):
        self.running=True
        
    def will_unmount(self):
        self.running=False
             


class Profile(View):

    def __init__(self,page:Page,routed,auth_=None,routed_='profile'):
        super().__init__()
        
        self.page=page
        self.route=f'/{project_}/{app_name_}/{routed}'
        self.routed_=routed_
        self.routed=routed

        self.navigation_bar=NavBottom(selfed=self)
        self.auth_=auth_
        self.scroll='always'
        self.auth_links=ElevatedButton()
        self.bgcolor=colors.PRIMARY_CONTAINER        
        self.updateables=[]  
        self.drawer=LeftSideBar(selfed=self)
        self.appbar=LernOnAppBar(selfed=self)
        self.end_drawer=RightSideBar(selfed=self)



        
        """
        ################################################### section 1 content: Basic info ##########################################################
        """
        self.user_img=width_fitted_image(src='/images/logos/logodl3.png')
        
        self.first_name=MediumTitleText(text='Full Name', text_align='start',font_family='heading')
        self.house_address=SmallBodyText(text='Address',text_align='start')

        self.phone=SmallBodyText(text='Phone',text_align='start')
        
        self.institution= SmallTitleText(text='Organisation',text_align='start',font_family='heading')
        self.status=SmallBodyText(text='Status',text_align='start')
        self.duration=SmallBodyText(text='Date joined-',text_align='start')
        self.email=SmallBodyText(text='Email-',text_align='start')
        self.profile_pic=CircleAvatar(radius=100,tooltip='View profile picture',)

        self.basic_info=ResponsiveRow(

            controls=[
                Row(

                    col=column_set(small_phone=12,land_scape_phone=4),
                    controls=[

        Container(
            padding=10,
            content=Stack(
                
            controls=[
                self.profile_pic,
                Container(
                    content=CircleAvatar(
                    bgcolor=colors.PRIMARY_CONTAINER,
                        
                        content=Icon(icons.EDIT,size=13,color=colors.PRIMARY,tooltip='Edit profile picture')),
                    alignment=alignment.bottom_right,

                    left=70,
                    bottom=5,

                    
                ),
            ],
            width=100,
            height=100,
        )
        
        ),
        #    Divider(color='transparent'),
                
                ResponsiveRow(
                    expand=1,
                    spacing=0,
                    controls=[

                        self.first_name,
                        self.email,
                        self.phone,
                        self.house_address,


                    
                              ]
                    ),
                 
                 
                 
                    ]
                ),
                
                
                ResponsiveRow(
                    expand=1,
                    col=column_set(small_phone=5+1,land_scape_phone=4),
                    spacing=0,
                    controls=[

                        self.institution,
                        Row(controls=[self.status ,self.duration,]),

                    
                              ]
                    ),
                Divider(height=2),

                 ResponsiveRow(
                    expand=1,
                    col=column_set(small_phone=12,tablet=5+1, land_scape_phone=4),
                    spacing=0,
                    controls=[

                        SmallTitleText(text=f'Bio',text_align='start',font_family='heading'),
                        SmallBodyText(boldness='bold',text='I am a full stack web and mobile app developer. I develop web apps with Django, a python framework for web development. I build flutter apps with flet for cross platform applications  ',text_align='start'),

                    
                              ]
                    ),
               
                 ResponsiveRow(
                    expand=1,
                    col=column_set(small_phone=12,tablet=5+1, land_scape_phone=4),
                    spacing=0,
                    controls=[

                        SmallTitleText(text=f'About',text_align='start',font_family='heading'),
                        SmallBodyText(boldness='bold',text='I am a full stack web and mobile app developer. I develop web apps with Django, a python framework for web development. I build flutter apps with flet for cross platform applications  ',text_align='start'),

                    
                              ]
                    ),
               
                Divider(height=2),

                
                
            ]
        )
        """
        ################################################### section 2 content: Courses ##########################################################
        """
        self.course_type_status=ResponsiveRow(
            controls=[
                Container(
                    col=3,
                    content=SmallBodyText(text='All Courses',font_family='heading'),
                ),
                Container(
                    col=3,
                    content=SmallBodyText(text='FUTA Courses' ,font_family='heading'),
                ),
                Container(
                    col=3,
                    content=SmallBodyText(text='LernOn Courses' ,font_family='heading'),
                ),
                Container(
                    col=3,
                    content=SmallBodyText(text='Other Courses' ,font_family='heading'),
                ),
            ]
        )
        self.courses=ResponsiveRow(
            controls=[

                self.course_type_status,
                Divider(height=1,color=colors.PRIMARY)
            ],
        )


        """
        ################################################### sections definitions ##########################################################
        """

        self.secion_1=sections_container(
            self=self,
            padding=10,
            border_radius=20,
            border=border.all(1,colors.PRIMARY),

            controls=[
                self.basic_info,
            ],
        )
        
        self.secion_2=sections_container(
            self=self,
            padding=10,
            border_radius=0,
            border=border.all(1,colors.PRIMARY),

            controls=[
                self.courses,
            ],
        )
        
        self.main_controls=[self.secion_1,self.secion_2]
        self.main_container=ResponsiveRow(controls=self.main_controls)
        
        self.controls=[
            self.main_container
        ]
        
    async def profile(self):
        # while self.running:
            if get_access_token(self=self) and User(selfed=self).is_logged_in :
                # 
                get_user_status(self=self)
                res=make_authenticated_get_request(self=self,url=f'account_api/user/{User(selfed=self).id}',cookie=get_access_email(self=self),key='email')
                if res.status_code==200:

                    for item in res.json():
                        if item=='picture':
                            if res.json()[item]:
                                self.profile_pic.foreground_image_url=f'{str(res.json()[item])}'
                            
                        if item=='username':
                            if res.json()[item]:
                                self.email.value=f'{str(res.json()[item])}'
                            
                        if item=='phone':
                            if res.json()[item]:
                                self.phone.value=f'{str(res.json()[item])}'
                            
                            
                        if item=='first_name':
                            if res.json()[item]:
                                self.first_name.value=f'{str(res.json()[item])}'
                            
                        if item=='last_name':
                            if res.json()[item]:
                                self.first_name.value +=f' {str(res.json()[item])}'
                            
                        
                                self.status.update()
                            
                        if item=='date_joined':
                            if res.json()[item]:
                                self.duration.value=f'{str(res.json()[item])}'
                            
                        
                            
                        if item=='address':
                            if res.json()[item]:
                                self.house_address.value=f'{str(res.json()[item])}'
                        self.main_controls.append(sections_container(
                            self=self,
                            controls=[Text(value=f'{str(item)}: {str(res.json()[item])}',size=14)],
                            bgcolor='blue',
                            )
                        )
                    self.update()
            

                   
    def logout_user(self,e):
        logout_user(self=self)  
    
     