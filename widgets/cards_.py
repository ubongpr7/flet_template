from flet import *
from widgets.images import *

from widgets.text_widget import *

class AuthResetCard(Card):

    def __init__(self,auth_purpose,auth_message,linking=None,form_fields=[],data_='',link_to=None,submit_fuction=None,extra=None):
        super().__init__()
        self.width=325
        self.elevation=2
        self.form_fields=form_fields

        self.heading=PageHeading_2(main_title=f'{auth_purpose} ',link_to=link_to,link_color='#809CFF',linking=linking,bg_color=None,main_size=18,sub_title=f'', text_color=colors.PRIMARY, sub_size=13)
        self.submit_fuction=submit_fuction
        self.content=Container(
            padding=20,
            border_radius=10,
            bgcolor=colors.SECONDARY_CONTAINER,
            content=Column(

                controls=[
                    self.heading,
                    Column(
                        controls=self.form_fields
                        
                    ),    
                    ElevatedButton(
                        content=Row(
                            alignment='center',

                            controls=[
                                
                                Text(value=f'{auth_message}',font_family='subheading',color=colors.SECONDARY_CONTAINER)
                            ],
                        ),
                        on_click=self.submit_fuction,
                        data=data_,
                        bgcolor=colors.PRIMARY
                        ),
                   Column(
                       controls=extra
                   )
                ]
            ),
            
        )
class AuthCard(Card):

    def __init__(self,auth_purpose,auth_message,linking=None,form_fields=[],link_to=None,submit_fuction=None,extra=None):
        super().__init__()
        self.width=325
        self.elevation=5
        self.form_fields=form_fields

        self.heading=PageHeadingCenter(main_title=f'{auth_purpose} ',link_to=link_to,link_color='#809CFF',linking='',bg_color=None,main_size=18,sub_title=f'', text_color=colors.PRIMARY, sub_size=13)
        self.redirect_=PageHeadingLink(main_title=f'',link_to=link_to,link_color='#809CFF',linking=linking,bg_color=None,main_size=18,sub_title=f'{auth_message}', text_color=colors.PRIMARY, sub_size=13)
        self.submit_fuction=submit_fuction
        self.content=Container(
            padding=20,
            border_radius=10,
            bgcolor=colors.SECONDARY_CONTAINER,
            content=Column(

                controls=[
                    self.heading,
                    
                   
                    Column(
                        controls=self.form_fields
                        
                    ),    
                    ElevatedButton(
                        content=Row(
                            alignment='center',

                            controls=[
                                
                                Text(value=f'{auth_purpose}',font_family='subheading',color=colors.SECONDARY_CONTAINER)
                            ],
                        ),
                        on_click=self.submit_fuction,
                        bgcolor=colors.PRIMARY
                        ),
                   Column(
                       controls=extra
                   ),
                   ElevatedButton(
                        content=Row(
                            alignment='center',
                            height=30,

                            controls=[
                                height_fitted_image(
                                    src='images/logos/google3.png'
                                ),
                                Text(value='Continue with Google',font_family='subheading',color=colors.SECONDARY_CONTAINER)
                            ],
                        ),
                        on_click=None,
                        bgcolor=colors.ON_TERTIARY
                        ),
                   
                self.redirect_,
                ]
            ),
            
        )
