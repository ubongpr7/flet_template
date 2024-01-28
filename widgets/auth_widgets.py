
from flet import *
import re
import requests
from settings.utils import *
from apps.account.utils import *
from widgets.countdown import CountDown
from widgets.text_widget import PageHeading_2


async def email_validator(email_field):
        email= email_field.value
        d,j,k=0,0,0
        if len(email)!=0:
            if email[0].isalpha():
                if email.count("@")==1:
                    
                    if (email[-4]==".")|(email[-3]=="."):
                        for part in email.split("@"):
                            for i in part:
                                if not i.isspace():
                                    if i=="_"or i=="-" or i.isalnum():

                                        email_field.error_text=''
                                        # email_field.focus()
                                        email_field.valid=True


                                        await email_field.update_async()

                                    else:
                                        email_field.error_text="Invalid characters present in your email "
                                        # email_field.focus()
                                        await email_field.update_async()

                                else:
                                    email_field.error_text="Email cannot contain spaces"
                                    # email_field.focus()
                                    await email_field.update_async()

                                    
                        
                    else:
                        email_field.error_text="Email is invalid with no domain extension"
                else:
                    email_field.error_text="Invalid email format"
                    await email_field.update_async()

                        
            else:
                email_field.error_text="Email must start with alphabet"
                await email_field.update_async()

        
async def password_validator(password_field):
    password=password_field.value
    if len(password)!=0:
        if len(password)>=8:
            if  re.search(r'[a-z]',password):   
                if re.search(r'[A-Z]',password):
                    if  re.search(r'[0-9]',password):
                        if  re.search(r'[!@$%&*()_+-=<>:"?|/\\]',password):

                            password_field.error_text=''
                            password_field.valid=True
                            await password_field.update_async()

                        else:    
                            password_field.error_text='At least one !@$%&*()_+-=<>:"?|/\\ special character is required '
                            await password_field.update_async()

                    else:        
                        password_field.error_text=' At least 1 number is requied'
                        await password_field.update_async()

                else:
                    password_field.error_text='Capital letters are required '
                    await password_field.update_async()

            else:
                password_field.error_text='lowercase letters are required'
                await password_field.update_async()


        else:
            password_field.error_text='At least 8 characters are required '

            await password_field.update_async()

            
async def code_verifier(code):
    password=code.value
    if len(password)!=0:
        
            if len(password)==5+1:


                code.error_text=''
                code.valid=True
                code.update()
            else:
                code.error_text=f'Exactly {8-2} characters are required '
                code.update()
                
async def name_verifier(name):
    password=name.value
    if len(password)!=0:
       
            if password.isalpha():


                name.error_text=''
                name.valid=True
                await name.update_async()

            else:
                name.error_text=f'Name can only alphabetic character'
                await name.update_async()



async def regenerate(self):
    print('regenerating')
    if self.timer.seconds<=0:

        if self.count>=2:
                
            self.verify_dialog.open=False
            self.password.value=''
            self.email.value=''
            self.count=0
            await self.verify_dialog.update_async()
            await self.update_async()

        else:        

        
            cookies={'email':str(self.email.value)}
            response=requests.get(
                    f'{base_url}account_api/verify/',
                    data={},
                    cookies=cookies,
                    
                    )
            if response.status_code==200:
                self.v_head.sub_title=f'A new code has been sent to {self.email.value.split("@")[0][:3]}...@{self.email.value.split("@")[1]}'
                await self.v_head.update_async()
                self.count+=1
                self.timer=CountDown(seconds=150)
                self.resends.controls.pop()
                self.resends.controls.append(self.timer)

                await self.verify_dialog.update_async()
                self.v_btn.disabled=False

                self.verify_dialog.open=True
                await self.update_async()

                await self.verify_dialog.update_async()
                await self.page.update_async()
    else:
        self.page.snack_bar=SnackBar(
            content=Text('Wait until countdown reaches 0',color=colors.RED_400),
            bgcolor=colors.ON_ERROR,
            behavior=SnackBarBehavior.FLOATING,
            close_icon_color=True,
            dismiss_direction=DismissDirection.START_TO_END,
            elevation=190
        )
        self.page.snack_bar.open=True
        await self.update_async()
        await self.page.update_async()
        await self.verify_dialog.update_async()
        
async def verify_finale(self,redirect_url,app_name=None):
    if self.count<3:
        cookies1={'email':str(self.email.value)}
        try:
            code=str(self.verification_code.value)
            r=requests.post(
                f'{base_url}account_api/verify/',
                data={
                    'code':code,
                    },
                    cookies=cookies1
                )
            if r.status_code==200:
                print('pk' ,str(r.cookies['pk'])  )
                await self.page.client_storage.set_async(f'{project_}.pk',str(r.cookies['pk']) )

                res=requests.post(
                f'{base_url}api/token/',
                data={
                   'username':str(self.email.value),
                    'password':str(self.password.value),
                    },
                )
                await self.page.client_storage.set_async(f'{project_}.email',str(self.email.value) )
                await self.page.client_storage.set_async(f'{project_}.authenticated',True)
                self.page.session.set(f'{project_}.access_token',str(res.json()["access"] ))
                await self.page.client_storage.set_async(f'{project_}.refresh_token',str(res.json()["refresh"] ))

                print('done')
                self.verify_dialog.open=False
                if self.page.session.get('desired_url'):

                    await self.page.go_async(self.page.session.get('desired_url'))
                    self.page.session.remove('desired_url')
                    print(f"Desired url removed")
                    await self.update_async()
                else:
                    await   self.page.go_async('/')
                    print('gone')
                    await self.update_async()
                await self.update_async()



                            
            
            else:
                self.v_head.sub_title=f'That does not match the code sent to  {self.email.value.split("@")[0][:3]}...@{self.email.value.split("@")[1]}'
                
                await self.v_head.update_async()
                await self.page.update_async()
            if self.count==3:
                self.verify_dialog.open=False
                self.password.value=''
                self.email.value=''
                await self.update_async()
                await self.page.update_async()

        except Exception as ero:
            print(ero)    
                 
async def enable_resend(self):
    while True:
        print('look')
        if self.timer.seconds==0:

            self.resend_btn.content.value='Resend Code'
            self.resend_btn.disabled=False
            self.v_btn.disabled=True

           
            self.verify_dialog.actions=[
                PageHeading_2(main_size=0,main_title='',sub_title='Back to',sub_size=12,bg_color=None,text_color=colors.PRIMARY,link_color='#809CFF',linking='Login',link_to=self.return_to_self)

                    ]
            await self.verify_dialog.update_async()
            await self.update_async()
        
        
async def refresh_user_token(self):
    while await self.page.client_storage.get_async(f'{project_}.refresh_token') and self.running:
        res=requests.post(
            f'{base_url}api/token/refresh/',
            data={
                "refresh":str(self.page.client_storage.get(f'{project_}.refresh_token'))
                },
            )
        if res.status_code==200:
            await  self.page.client_storage.set_async(f'{project_}.access_token',str(res.json()["access"] ))
            await  self.page.client_storage.set_async(f'{project_}.refresh_token',str(res.json()["refresh"] ))
            await  self.page.client_storage.set_async(f'{project_}.authenticated',True)

        else :
            await self.page.go_async(f'/{project_}/{app_name_}/login')


async def logout_user(self,event):
        r=make_authenticated_request_async(self=self,url='account_api/logout',method='post',data=None,cookie=None,key=None) 
        print(f'logout={r.status_code}')
        
        if  r.status_code==200: 
            print('Logged out') 
            await self.page.client_storage.remove_async(f'{project_}.email')
            await self.page.client_storage.remove_async(f'{project_}.access_token')
            await self.page.client_storage.remove_async(f'{project_}.refresh_token',)
            await self.page.client_storage.set_async(f'{project_}.authenticated',False)
            print('cleared') 

            await self.page.go_async(f'/')
        else:
            await self.page.go_async(f'/{project_}/{app_name_}/login')
            
 
class AuthInputField(TextField):
    def __init__(self,type,field_hint,focus_input):
        super().__init__()
        self.hint_text=field_hint
        self.type=type
        self.valid=False
        self.color=colors.PRIMARY
        self.hint_style=TextStyle(color=colors.TERTIARY,size=12)

        if self.type=='password' or self.type=='code':
            self.password=True
        else:
            self.password=False  
        if self.type=='code':
            self.width=150     
        self.color=colors.PRIMARY
        self.border_color='transparent'
        self.bgcolor=colors.PRIMARY_CONTAINER
        
        self.autofocus=focus_input
        self.cursor_color=colors.PRIMARY
        self.text_size=12
        self.content_padding=10
        self.on_change=self.validators        
            
    async def validators(self,e):
        if self.type=='password':
            return await  password_validator(password_field=self) 
        elif self.type=='email':
            return await email_validator(email_field=self) 
        elif self.type=='code':
            return await code_verifier(code=self)
                
        elif self.type=='name':
            return await name_verifier(name=self)


class AuthInputContainer(Container):
    def __init__(self,icon_name,input_field:TextField):
        super().__init__()
        self.icon_name=icon_name
        # self.width=300

        self.input_field=input_field
        self.content=Row(
                spacing=20,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=self.icon_name,
                        size=14,
                        opacity=.85,
                        color=colors.PRIMARY

                    ),
                    self.input_field,
                ]

               ) 
        self.border=border.only(bottom=border.BorderSide(0.5,colors.PRIMARY,))
        self.height=43
    
    

    