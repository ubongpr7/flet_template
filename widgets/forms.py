import os
import shutil
from flet import *
from settings.utils import *

from widgets.buttons_widget import column_set
from widgets.pickers import DatePicker_, FilePicker_, TimePicker_


class Forms(Container):
    def __init__(self,controls=[]):
        super().__init__()
        self.col=column_set(small_phone=12,tablet=8,land_scape_phone=6,land_scape_tablet=5,desktop=4)
        
        self.bgcolor=colors.SECONDARY_CONTAINER
        self.padding=16
        self.border_radius=20
        self.content=ResponsiveRow(
            controls=controls
        )


class PickerField(TextField):
    def __init__(self,picker_type,field_hint='',on_clicked=None):
        super().__init__()
        self.col=4
        self.height=30
        
        self.content_padding=5

        if picker_type=='file':
            self.prefix=Column([
                Row(height=5,width=60),
                TextButton(
                    style=ButtonStyle(bgcolor=None,overlay_color={"":"transparent"},),

                content=Icon(icons.UPLOAD_FILE,color=colors.ON_TERTIARY,size=30,),
                on_click=on_clicked,
            ),
            Text(value='Pick here',size=9,color=colors.PRIMARY)
            
            ],
            spacing=0
            )
            self.height=60
            self.content_padding=Padding(left=15,top=20,right=15,bottom=10,)

            self.hint_text='Upload media file'

        elif picker_type=='date':
            self.suffix=TextButton(
                    style=ButtonStyle(bgcolor=None,overlay_color={"":"transparent"},),

                content=Icon(icons.CALENDAR_MONTH,color=colors.ON_TERTIARY,size=10),
                on_click=on_clicked,
            )
            self.hint_text='Pick date'
        
        elif picker_type=='time':
            self.suffix=TextButton(
                    style=ButtonStyle(bgcolor=None,overlay_color={"":"transparent"},),

                content=Icon(icons.ALARM,color=colors.ON_TERTIARY,size=10),
                on_click=on_clicked,
            )
            self.hint_text='Pick time'

        self.color=colors.PRIMARY
        self.hint_style=TextStyle(color=colors.TERTIARY,size=12)
        self.color=colors.PRIMARY
        self.enable_suggestions=True
        self.border_color='transparent'
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.cursor_color=colors.PRIMARY
        self.text_size=10
        self.read_only=True
    
class PickerColumn(Column):
    def __init__(self,selfed,label,picker_type):
        super().__init__()
        self.selfed=selfed
        self.picker_type=picker_type
        self.col=6

        self.pick_field=PickerField(on_clicked=self.open_picker,picker_type=picker_type)
        if self.picker_type=='date':

            self.to_pick=DatePicker_(date_changed=self.picker_changed,)
        elif  self.picker_type=='time':
            self.to_pick=TimePicker_(time_changed=self.picker_changed,)
            
        elif  self.picker_type=='file':
            self.col=12

            self.to_pick=FilePicker_(on_result=self.picker_changed)
            
        self.controls=[
                    Text(value=label,size=11,color=colors.PRIMARY),
                    self.pick_field,
                    self.to_pick
                ]
            
        self.spacing=0
        
        
    async def open_picker(self,e):
        if self.picker_type=='date':

            await self.to_pick.pick_date_async()
        elif self.picker_type=='time':

            await self.to_pick.pick_time_async()
        elif self.picker_type=='file':

            await self.to_pick.pick_files_async(dialog_title='Event media files',allow_multiple=False)
        await self.selfed.page.update_async()

    async def picker_changed(self,e):
        if self.picker_type !='file':
            if self.to_pick.value:
                self.pick_field.value=str(self.to_pick.value)[:11]
        else:
            print('file')
            for x in self.to_pick.result.files:
                # print(x)
                # print(x.path)
                # print(x.name)
                # file_copy=os.path.join(os.getcwd(),'uploads')
                # shutil.copy(x.path,file_copy)
                file={}
                res=make_authenticated_request(
                    self=self.selfed,
                    request_type='file',
                    url='account_api/profile_pic',
                    data={'picture':open(x.path,'rb')},
                    method='post')
                if res.status_code==200:
                    print('done')
                
        await self.update_async()








