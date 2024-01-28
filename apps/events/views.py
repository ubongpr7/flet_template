from flet import *
import calendar
from base.app_bar_widget import LernOnAppBar

from base.base_ import *
from widgets.date_box import *
from widgets.forms import  *
from widgets.page_widget import sections_container
from widgets.pickers import DatePicker_
from widgets.post_widget import PostAvartar
from widgets.text_input_widget import TextInput, TransparentInputContainer
from .utils import app_name_
from settings.utils import project_

class PostAddView(View):

    def __init__(self,page:Page,routed='add-post',routed_='post-forms',auth_=True):
        super().__init__() 
        self.page=page
        self.routed_=routed_
        self.route=f'/{project_}/{app_name_}/{routed}'
        self.navigation_bar=NavBottom(selfed=self)
        self.auth_=auth_
        self.routed=routed

        self.scroll='always'
        self.appbar=LernOnAppBar(selfed=self)
        self.end_drawer=RightSideBar(selfed=self)
        self.bgcolor=colors.PRIMARY_CONTAINER        
        self.drawer=LeftSideBar(selfed=self)
        self.file_picker=FilePicker()
        self.event_description=TextInput(
            field_hint='Briefly describe this event',

            col=12
        )
        self.main_container=sections_container(self=self,controls=[
            PostAvartar(selfed=self),
            Forms(controls=[
                Text(value='Title',font_family='heading'),

                TransparentInputContainer(field_hint='Post Title'),
            
                Divider(height=0.3,color=colors.with_opacity(0.8,colors.PRIMARY_CONTAINER)),
                Text(value='Post Content',font_family='heading'),
                self.event_description,
                Container(
                    content=ElevatedButton(
                        text='Submit post',
                        bgcolor=colors.ON_PRIMARY,
                        color=colors.SECONDARY_CONTAINER
                    ),
                    width=100,
                    alignment=alignment.center
                )
                ]),
            
        ])
        
        self.controls=[
           self.main_container
        ]

class EventAddView(View):

    def __init__(self,page:Page,routed,routed_='event-forms',auth_=True):
        super().__init__() 
        self.page=page
        self.routed_=routed_
        self.routed=routed

        self.route=f'/{project_}/{app_name_}/{routed}'
        self.navigation_bar=NavBottom(selfed=self)
        self.auth_=auth_
        self.scroll='always'
        self.appbar=LernOnAppBar(selfed=self)
        self.end_drawer=RightSideBar(selfed=self)
        self.auth_links=ElevatedButton()
        self.bgcolor=colors.PRIMARY_CONTAINER        
        self.drawer=LeftSideBar(selfed=self)
        self.file_picker=FilePicker()
        self.event_description=TextInput(
            field_hint='Briefly describe this event',

            col=12
        )
        self.main_container=sections_container(self=self,controls=[
            PostAvartar(selfed=self),
            Forms(controls=[
                TransparentInputContainer(field_hint='Event Title'),
                PickerColumn(selfed=self,label='Upload Media files',picker_type='file'),
                Text(value='Date and time settings',font_family='heading'),
                PickerColumn(selfed=self,label='Start date',picker_type='date'),
                PickerColumn(selfed=self,label='End date',picker_type='date'),
                PickerColumn(selfed=self,label='Start time',picker_type='time'),
                PickerColumn(selfed=self,label='End time',picker_type='time'),
                
                Divider(height=0.3,color=colors.with_opacity(0.8,colors.PRIMARY_CONTAINER)),
                Text(value='Description',font_family='heading'),
                self.event_description,
                Container(
                    content=ElevatedButton(
                        text='Submit event',
                        bgcolor=colors.ON_PRIMARY,
                        color=colors.SECONDARY_CONTAINER
                    ),
                    width=100,
                    alignment=alignment.center
                )
                ]),
            
        ])
        
        self.controls=[
           self.main_container
        ]

    
