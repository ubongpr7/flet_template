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


class  Registration(View):
    def __init__(self,page:Page,routed,auth_=None):
        super().__init__()

        self.page=page
        self.routed=routed

        self.appbar=LernOnAppBarAuth(selfed=self,center_title_=False)
        self.route=f'/{project_}/{app_name_}/{routed}'
        self.divider=Divider(
            height=2, color='transparent',
            
        )
        self.auth_=auth_
        
        self.email= AuthInputField(field_hint='Email',focus_input=True,type='email')              
        self.password= AuthInputField(field_hint='Password',focus_input=True,type='password')              
        self.confirm_email= AuthInputField(field_hint='Confirm Email ',focus_input=False,type='email') 

        self.confirm_password= AuthInputField(field_hint='Confirm password',focus_input=True,type='password')
        

        self.password_verifier=Text(color=colors.RED_300,height=0)
        self.overall_verifier=Text(color=colors.RED_300,height=0)
        self.email_verifier=Text(color=colors.RED_300,height=0)

        
        self.register_card=AuthCard(
            auth_purpose="Sign Up",
            auth_message="Already have an account?",
            linking="Log in",
            link_to= self.login_f,
            form_fields=[
                Text(value='Email address',font_family='subheading',color=colors.PRIMARY),
                self.email,
                self.confirm_email,
                self.email_verifier,
                Text(value='Password',font_family='subheading',color=colors.PRIMARY),

                self.password,
                self.confirm_password,
                self.password_verifier,
                self.overall_verifier,
            ],
            submit_fuction=self.fill_validation,
        )
        
        self.controls=[self.register_card,]
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.vertical_alignment='center'
        self.horizontal_alignment='center'
        self.auto_scroll=True
        self.scroll='always'
        self.verification_code=NumberInput(field_hint='Enter verification code',type='num')              

        self.text_info='Code expires after'
        self.timer=CountDown(seconds=90,text_info='')
        self.resend_btn=TextButton(content=Text(value=f"Resend Code",size=10,),style=ButtonStyle(color=colors.PRIMARY,bgcolor=''), on_click=self.verify_regenerate,)
        
        self.v_head=Text(color=colors.PRIMARY,col=11)
        self.count=0
        self.v_btn=ElevatedButton(text="Verify",bgcolor=colors.ON_PRIMARY,color=colors.SECONDARY_CONTAINER, on_click=self.verify_user)


        self.resends=Row(
                            alignment='center',
                            controls=[

                            self.resend_btn,

                            self.timer
                            ])
                        
        self.verify_dialog = AlertDialog(
            title=Text("Verification",size=14,weight='bold'),
            content=Container(
                
                bgcolor=colors.SECONDARY_CONTAINER,
                content=ResponsiveRow(
                    alignment='center',
                    expand=1,
                    controls=[
                        ResponsiveRow([Row(width=1,col=0.5),self.v_head],Row(width=1,col=0.5)),
                        ResponsiveRow(col=12,controls=[Row(col=1),self.verification_code,Row(col=1),]),
                        self.v_btn,
                        self.resends,
                        
                    
                ],
            ),),
            actions=[
                PageHeading_2(main_size=0,main_title='',sub_title='Back to',sub_size=12,bg_color=None,text_color=colors.PRIMARY,link_color='#809CFF',linking='Login',link_to=self.return_to_self)

                    ],
           
            actions_alignment="center",
        )
    async def fill_validation(self,e):
    
            if  (self.email.error_text=='' or self.confirm_email.error_text=='' or self.password.error_text=='' or self.confirm_password.error_text==''):

                if  self.email.value=='' or self.confirm_email.value=='':
                    self.email_verifier.value='The two email fields are required'
                    self.email_verifier.height=20
                    
                    await self.email_verifier.update_async()
                else:
                    if self.email.value!= self.confirm_email.value:
                        self.email_verifier.value='The two emails do not match'
                        self.email_verifier.height=20
                        await self.email_verifier.update_async()

                    else: 
                        self.email_verifier.value=''
                        self.email_verifier.height=0
                        await self.email_verifier.update_async()
                        
                    
                if  self.password.value=='' or self.confirm_password.value=='':
                    self.password_verifier.value='The two password fields are required '
                    self.password_verifier.height=20
                    await self.password_verifier.update_async()
                else:
                    if self.password.value!= self.confirm_password.value:
                        self.password_verifier.value='The two passwords do not match'
                        self.password_verifier.height=20
                        await self.password_verifier.update_async()

                    else: 
                        self.password_verifier.value=''
                        self.password_verifier.height=0
                        await self.password_verifier.update_async()

                if self.confirm_email.value!='' and self.confirm_password.value!='':        
                    if self.password.value==self.confirm_password.value and self.email.value == self.confirm_email.value:
                        cookies={'email':str(self.email.value)}

                        r=requests.post(
                            f'{base_url}account_api/register/',
                            data={
                                'email':str(self.confirm_email.value),
                                'username':str(self.confirm_email.value),
                                'password':str(self.password.value),
                                },
                                cookies=cookies,

                            ) 
                        if r.status_code==201 or r.status_code==200:
                            print(r.text)
                            cookies={'email':str(self.email.value)}
                            response=requests.get(
                            f'{base_url}account_api/verify/',
                            data={},
                            cookies=cookies,
                            
                            )
                            if response.status_code==200:
                                self.page.dialog=self.verify_dialog
                                self.verify_dialog.modal=True
                                self.verify_dialog.open=True
                                self.verification_code.value=''
                                self.v_head.value=f'A verification code has been sent to {self.email.value.split("@")[0][:3]}...@{self.email.value.split("@")[1]}'
                                await self.page.update_async()
                            else :
                                return go_to_page(self=self, app_name=app_name_, route='register')    

            else:
                self.password_verifier.value='Correct the errors above'     
                self.password_verifier.height=20
                await self.password_verifier.update_async()

        

    async def login_f(self,e):
        await self.page.go_async(f'/{project_}/{app_name_}/login')
    
    async def return_to_self(self,e):
        self.verify_dialog.open=False
        await self.verify_dialog.update_async()

             
    async def verify_regenerate(self,e):
        await regenerate(self=self)
        
    async def enable(self):
        await enable_resend(self=self)  
            
    async def verify_user(self,e):
       await verify_finale(self=self,redirect_url='profile')
    

class  LoginPage(View):
    def __init__(self,page:Page,routed,auth_=None):
        super().__init__()
        self.divider=Divider(
            height=2, color='transparent',
            
        )
        self.routed=routed
        
        self.page=page
        self.appbar=LernOnAppBarAuth(selfed=self,center_title_=True)

        self.route=f'/{project_}/{app_name_}/{routed}'
        self.auth_=auth_

        self.email_text=''
        self.bgcolor=colors.SECONDARY_CONTAINER

        self.verification_code=NumberInput(field_hint='Enter verification code',col=10,type='num')              
        
        # self.scroll='adaptive'
        self.email= AuthInputField(field_hint='Enter email address',focus_input=True,type='email')              
        self.password= AuthInputField(field_hint='Enter password',focus_input=False,type='password')              
        self.password_verifier=Text(color=colors.RED_300,height=0)
        self.verify=Text(color=colors.RED_300,height=0)
        
        self.register_card=AuthCard(
            auth_purpose="Sign In",
            auth_message="New user? ",
            linking="Sign Up",
            link_to=self.login_f,
            form_fields=[
                Text(value='Email address',font_family='subheading',color=colors.PRIMARY),
                self.email,
                self.verify,

                Text(value='Password',font_family='subheading',color=colors.PRIMARY),

                self.password,
                self.password_verifier,

            ],
            extra=[PageHeadingLink(
                main_title=f'',
                link_to=self.reset_f,
                link_color='#809CFF',
                linking='Reset now',
                bg_color=None,
                main_size=18,
                sub_title=f'Forgot password?',
                text_color=colors.PRIMARY,
                sub_size=13),
                ],
            submit_fuction=self.fill_validation,
        )
        
        
        self.controls=[self.register_card]
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.vertical_alignment='center'
        self.horizontal_alignment='center'
        
        self.verification_info='A verification code has been sent to'

        self.v_head=Text(color=colors.PRIMARY,col=11)

        self.count=0
        self.v_btn=ElevatedButton(text="Verify",color=colors.SECONDARY_CONTAINER,bgcolor=colors.ON_PRIMARY, on_click=self.verify_user)

        self.dir_dialog=AlertDialog(
            content=ResponsiveRow(controls=[PageHeading_2(main_title='',bg_color=colors.SECONDARY_CONTAINER,main_size=18,sub_title='Verification sucessful', text_color=colors.PRIMARY, sub_size=10),ElevatedButton(text='Continue',on_click=lambda _:  go_to_page(self=self, app_name=app_name_, route='home'))]),
            actions=[ElevatedButton(text='Continue',on_click=lambda _:  go_to_page(self=self, app_name=app_name_, route='home')),],

        )
        self.text_info='Code expires after:'
        self.timer=CountDown(seconds=60,text_info='',t_align='center')
        self.resend_btn=TextButton(content=Text(value=f"Resend Code",size=10,),style=ButtonStyle(color=colors.PRIMARY,bgcolor=''), on_click=self.verify_regenerate,)
        self.resends=Row(
                            alignment='center',
                            controls=[

                            self.resend_btn,

                            self.timer
                            ])
            
        self.verify_dialog = AlertDialog(
            title=Text("2FA Authenttication",size=14,weight='bold'),
            modal=True,

            content=Container(
                
                bgcolor=colors.SECONDARY_CONTAINER,
                content=ResponsiveRow(
                    alignment='center',
                    expand=1,
                    controls=[

                        ResponsiveRow([Row(width=1,col=0.5),self.v_head],Row(width=1,col=0.5)),

                        ResponsiveRow(col=12,controls=[Row(col=1),self.verification_code,Row(col=1),]),
                        self.v_btn,
                        self.resends,
                        
                        
                    
                ],
            ),),
            actions=[
                PageHeading_2(main_size=0,main_title='',sub_title='Back to',sub_size=12,bg_color=None,text_color=colors.PRIMARY,link_color='#809CFF',linking='Login',link_to=self.return_to_self)
                    ],
            actions_alignment="start",
        )

        
    async def fill_validation(self,e):
        if  self.email.value=='' :
            self.verify.value='Email field is required'
            self.verify.height=20
            
            await self.verify.update_async()
        else:    
            self.verify.value=''
            self.verify.height=0
            
            await self.verify.update_async()
        
        if  self.password.value=='' :
            self.password_verifier.value='Password field is required'
            self.password_verifier.height=20

            await self.password_verifier.update_async()
        else:
            self.password_verifier.value=''
            self.password_verifier.height=0
            await self.password_verifier.update_async()
            cookies={'email':str(self.email.value)}
            r=requests.post(
                f'{base_url}account_api/login/',
                data={
                    'username':str(self.email.value),
                    'password':str(self.password.value),
                    },
                    cookies=cookies
                )
             
            self.page.session.set('email',str(self.email.value))
            self.page.session.set('verified',False)

            if r.status_code==200:
                cookies={'email':str(self.email.value)}


                response=requests.get(
                        f'{base_url}account_api/verify/',
                        data={},
                        cookies=cookies,
                        
                        )
                if response.status_code==200:
                    self.page.dialog=self.verify_dialog
                    self.verify_dialog.modal=True
                    self.verify_dialog.open=True
                    self.verification_code.value=''
                    self.v_head.value=f'A verification code has been sent to {self.email.value.split("@")[0][:3]}...@{self.email.value.split("@")[1]}'

                    await self.page.update_async()
            else :

                self.page.snack_bar=SnackBar(
                    content=Text('Invalid Login credentials',color=colors.RED_400),
                    bgcolor=colors.ON_ERROR,
                    behavior=SnackBarBehavior.FLOATING,
                    close_icon_color=True,
                    dismiss_direction=DismissDirection.START_TO_END,
                    elevation=190
                )
                self.page.snack_bar.open=True
                await self.update_async()
                await self.page.update_async()
                return await go_to_page(self=self, app_name=app_name_, route='login')    
     
    async def login_f(self,e):
        await self.page.go_async(f'/{project_}/{app_name_}/register')
       
    async def reset_f(self,e):
        await self.page.go_async(f'/{project_}/{app_name_}/reset-email')
       

    async def return_to_self(self,e):
        self.verify_dialog.open=False
        await self.verify_dialog.update_async()

             
    async def verify_regenerate(self,e):
        await regenerate(self=self)
        
    async def enable(self):
        await enable_resend(self=self)  
            
   
    async def verify_user(self,e):
       await verify_finale(self=self,redirect_url='profile')
    

class  PasswordResetEmail(View):

    def __init__(self,page:Page,routed,auth_=None):
        super().__init__()
        self.divider=Divider(
            height=2, color='transparent',
            
        )
        self.routed=routed

        self.page=page

        self.appbar=LernOnAppBarAuth(selfed=self,center_title_=True)


        self.auth_=auth_

        self.route=f'/{project_}/{app_name_}/{routed}'

        self.email= AuthInputField(field_hint='Enter email address',focus_input=True,type='email')              
        self.verify=Text(color=colors.RED_300,height=0)
        

        self.heading=PageHeading_2(main_title='Password Reset Request',bg_color=None,main_size=22,sub_title='Enter registered email address', text_color=colors.PRIMARY, sub_size=13)
        
        self.register_card=AuthResetCard(
            auth_purpose="Password reset email",
            auth_message='Request password reset',
            form_fields=[
                Text(value='Registered email address',font_family='subheading',color=colors.PRIMARY),
                self.email,

                self.verify

            ],
            extra=[PageHeadingLink(
                main_title=f'',
                link_to=lambda _:self.page.go(f'/{project_}/accounts/login'),
                link_color='#809CFF',
                linking='Login',
                bg_color=None,
                main_size=18,
                sub_title=f'Back to',
                text_color=colors.PRIMARY,
                sub_size=13),
                ],
            submit_fuction=self.fill_validation,
        )
        

        self.controls=[self.register_card]
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.vertical_alignment='center'
        self.horizontal_alignment='center'
    async  def fill_validation(self,e):
        if  self.email.value=='' :
            self.verify.value='Email field is required'
            self.verify.height=20
            
            await   self.page.update_async()
        else:    
            self.verify.value=''
            self.verify.height=0
            await   go_to_page(self=self, app_name=app_name_, route='reset-password')
            await   self.page.update_async()
    # 

class  PasswordReset(View):
    def __init__(self,page:Page,routed,auth_=None):
        super().__init__()
        self.page=page

        self.appbar=LernOnAppBarAuth(selfed=self,center_title_=True)

        self.divider=Divider(
            height=2, color='transparent',
            
        )
        self.routed=routed

        self.route=f'/{project_}/{app_name_}/{routed}'
        self.auth_=auth_
        self.password= AuthInputField(field_hint='New password',focus_input=True,type='password')              

        self.confirm_password= AuthInputField(field_hint='Confirm password',focus_input=True,type='password')

        self.password_verifier=Text(color=colors.RED_300,height=0)

        
        self.register_card=AuthResetCard(
            auth_purpose="Password reset",
            auth_message='Reset password ',
            form_fields=[
                Text(value='New password',font_family='subheading',color=colors.PRIMARY),
                self.password,
                self.confirm_password,

                self.password_verifier,


            ],
            
            submit_fuction=self.fill_validation,
        )
        


        self.controls=[self.register_card,]
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.vertical_alignment='center'
        self.horizontal_alignment='center'
        self.auto_scroll=True
        if self.password.valid==True and self.confirm_password.valid==True:
            self.btn.disabled=False
            
    async def fill_validation(self,e):
        if  self.password.value=='' or self.confirm_password.value=='':
            self.password_verifier.value='The two password fields are required '
            self.password_verifier.height=20
            await self.password_verifier.update_async()
        else:
            if self.password.value!= self.confirm_password.value:
                self.password_verifier.value='The two passwords do not match'
                self.password_verifier.height=20
                await self.password_verifier.update_async()
            else: 
                self.password_verifier.value=''
                self.password_verifier.height=0
                await self.password_verifier.update()
                await go_to_page(self=self, app_name=app_name_, route='reset-password') 
 
        
       

    


