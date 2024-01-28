from flet import *

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
            
    def validators(self,e):
        pass
