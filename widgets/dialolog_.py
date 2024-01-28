from flet import  *

from widgets.cards_ import AuthResetCard

class AuthAlert(AlertDialog):
    def __init__(self,alert_content=[]):
        self.title=Text(f"Verification",size=14,weight='bold')
        self.alert_content=alert_content
        self.content=AuthResetCard(
            auth_purpose="Verification ",
            auth_message='Verify',
            form_fields=[
                
                Container(
                
                bgcolor=colors.SECONDARY_CONTAINER,
                content=ResponsiveRow(
                    alignment='center',
                    controls=self.alert_content
            ),),
            ],
            # extra=[PageHeading_2(
            #     main_title=f'',
            #     link_to=lambda _:self.page.go(f'/{project_}/accounts/login'),
            #     link_color='#809CFF',
            #     linking='Login',
            #     bg_color=None,
            #     main_size=18,
            #     sub_title=f'Back to',
            #     text_color=colors.PRIMARY,
            #     sub_size=13),
            #     ],
            
            submit_fuction=None,
        )
        
            
        self.actions=[

                ]
    

