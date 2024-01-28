from flet import *


async def code_verifier(code):
    password=code.value
    if len(password)!=0:
        
            try:
                
                int(password)

                code.error_text=''

                code.valid=True

                await   code.update_async()
            except:
                code.error_text=f'Numbers  only'
                code.value=""
                await code.update_async()
   
class NumberInput(TextField):
    def __init__(self,type=None,field_hint=None,prefix_=None,suffix=None,col=None):
        super().__init__()
        self.hint_text=field_hint
        self.type=type
        self.valid=False
        self.prefix_text=prefix_
        self.suffix_text=suffix        
        self.width=150     
        self.color=colors.PRIMARY
        self.border_color='transparent'
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.cursor_color=colors.PRIMARY
        self.text_size=12,
        self.col=col
        self.content_padding=5
        self.text_align=TextAlign.CENTER
        self.hint_style=TextStyle(size=12,color=colors.PRIMARY,)
        self.on_change=self.validators        
            
    async def validators(self,e):
        
        if self.type=='num':
            return await  code_verifier(code=self)
                
        
class ReadonlyTextInput(TextField):
    def __init__(self,type,value,):
        super().__init__()
        self.type=type
        self.valid=False
        self.value=value
        self.read_only=True

        
        self.width=150     
        self.color=colors.PRIMARY
        self.border_color='transparent'
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.cursor_color=colors.PRIMARY
        self.text_size=12,
        self.content_padding=5
        self.text_align=TextAlign.CENTER
        self.hint_style=TextStyle(size=12,color=colors.PRIMARY,)
        self.on_change=self.validators        
            
    def validators(self,e):
        
        if self.type=='read':
            # return code_verifier(code=self)
            pass

 
class TextInput(TextField):
    def __init__(self,field_hint,prefix_=None,suffix=None,tooltip=None,col=None):
        super().__init__()
        self.hint_text=field_hint
        self.valid=False
        self.prefix_text=prefix_
        self.suffix_text=suffix 
        self.tooltip=tooltip
        self.col=col       

        self.multiline=True
        self.width=150     
        self.color=colors.PRIMARY
        self.border_color=colors.with_opacity(0.8,colors.PRIMARY_CONTAINER)
        self.bgcolor=None
        self.cursor_color=colors.PRIMARY
        self.text_size=12
        self.content_padding=10
        # self.text_align=TextAlign.CENTER
        self.hint_style=TextStyle(size=10,color=colors.TERTIARY,)
        self.on_change=self.validators        
            
    def validators(self,e):
        
        if self.type=='text':
            # return code_verifier(code=self)
            pass
                
class TransparentTextInput(TextField):
    def __init__(self,field_hint,prefix_=None,suffix=None,tooltip=None,col=None):
        super().__init__()
        self.hint_text=field_hint
        self.valid=False
        self.prefix_text=prefix_
        self.suffix_text=suffix 
        self.tooltip=tooltip
        self.col=col       
        self.border=InputBorder.NONE
        self.multiline=False
        self.width=150     
        self.color=colors.PRIMARY
        self.border_color=None
        self.bgcolor=None
        self.cursor_color=colors.PRIMARY
        self.text_style=TextStyle(font_family='heading')
        self.content_padding=10
        # self.text_align=TextAlign.CENTER
        self.hint_style=TextStyle(size=12,color=colors.TERTIARY,)
            
        

class TransparentInputContainer(Container):
    def __init__(self,field_hint):
        super().__init__()
        self.col=12
        self.content=TransparentTextInput(field_hint=field_hint)
        self.border=border.only(bottom=border.BorderSide(0.5,colors.PRIMARY,))
        
    
                   
        