from math import pi
import os
from flet import *
import requests

from settings.utils import *
from base.app_bar_widget import  *
from widgets.auth_widgets import *
from base.base_ import *
from widgets.buttons_widget import column_set, image_address1
from widgets.page_widget import sections_container
from widgets.post_widget import * 
from widgets.text_widget import *


class  EventPage(View):
    def __init__(self,page:Page,routed,auth_=None,routed_='event-home'):
        super().__init__()
        self.page=page
        self.route=f'/'
        self.routed_=routed_
        self.routed=routed
        self.auth_=auth_
        self.navigation_bar=NavBottom(selfed=self)
        self.bgcolor=colors.PRIMARY_CONTAINER
        self.appbar=LernOnAppBar(selfed=self)
        self.drawer=LeftSideBar(selfed=self)
        self.scroll='always'
        self.end_drawer=RightSideBar(selfed=self)
        self.controls_=[
            PostContainer(
                names='Ubong Prosper',
            profile_pic='images/img2/school1.jpg',
            posted='19h',
            selfed=self,
            location='Odogunyan Deeper Life Ministry',
            _likes=200,
            _comments=400,
            _shares=2338,
            title='TechAware Youth Program 2024',
            description='During the research to prove the validity & necessity of this program, I spoke with students from different academic levels, some undergraduates, ex-students, secondary school & some who could not pursue tertiary education. They all expressed interest & desire to get involved, some sited some challenges which can all be mapped to one universal set ignorance. Many of the things we see as  challenges persist & becomes a problem when we are ignorant of the means to overcome them. ',
            src='images/img2/school1.jpg',
            ),
            Divider(color=colors.with_opacity(color=colors.PRIMARY_CONTAINER,opacity=0.45),thickness=10),
            PostContainer(
                names='Ubong Prosper',
            profile_pic='images/img2/school1.jpg',
            posted='19h',
            selfed=self,
            location='Odogunyan Deeper Life Ministry',
            _likes=200,
            _comments=400,
            _shares=2338,
            title='TechAware Youth Program 2024',
            description='During the research to prove the validity & necessity of this program, I spoke with students from different academic levels, some undergraduates, ex-students, secondary school & some who could not pursue tertiary education. They all expressed interest & desire to get involved, some sited some challenges which can all be mapped to one universal set ignorance. Many of the things we see as  challenges persist & becomes a problem when we are ignorant of the means to overcome them. ',
            src='images/img2/school1.jpg',
            ),
            Divider(color=colors.with_opacity(color=colors.PRIMARY_CONTAINER,opacity=0.45),thickness=10),
            
            PostContainer(
                names='Ubong Prosper',
            profile_pic='images/img2/school1.jpg',
            posted='19h',
            selfed=self,
            location='Odogunyan Deeper Life Ministry',
            _likes=200,
            _comments=400,
            _shares=2338,
            title='TechAware Youth Program 2024',
            description='During the research to prove the validity & necessity of this program, I spoke with students from different academic levels, some undergraduates, ex-students, secondary school & some who could not pursue tertiary education. They all expressed interest & desire to get involved, some sited some challenges which can all be mapped to one universal set ignorance. Many of the things we see as  challenges persist & becomes a problem when we are ignorant of the means to overcome them. ',
            src='images/img2/school1.jpg',
            ),
            Divider(color=colors.with_opacity(color=colors.PRIMARY_CONTAINER,opacity=0.45),thickness=10),

            PostContainer(
                names='Ubong Prosper',
            profile_pic='images/img2/school1.jpg',
            posted='19h',
            selfed=self,
            location='Odogunyan Deeper Life Ministry',
            _likes=200,
            _comments=400,
            _shares=2338,
            title='TechAware Youth Program 2024',
            description='During the research to prove the validity & necessity of this program, I spoke with students from different academic levels, some undergraduates, ex-students, secondary school & some who could not pursue tertiary education. They all expressed interest & desire to get involved, some sited some challenges which can all be mapped to one universal set ignorance. Many of the things we see as  challenges persist & becomes a problem when we are ignorant of the means to overcome them. ',
            src='images/img2/school1.jpg',
            ),
            Divider(color=colors.with_opacity(color=colors.PRIMARY_CONTAINER,opacity=0.45),thickness=10),
            
        ]
        
        self.post_container=sections_container(
            self,
            controls=[
                
                Row(
        
                    col=column_set(small_phone=12,tablet=2,land_scape_phone=3,land_scape_tablet=2.5,desktop=2.5)
                ),
                
                AllPostContainer(controls=self.controls_),
                
                
                Row(
        
                    col=column_set(small_phone=12,tablet=2,land_scape_phone=3,land_scape_tablet=2.5,desktop=2.5)
                ),
                
                ]
        )
        self.group_container=sections_container(
            self,
            controls=[
                Groups()])
        self.controls=[self.post_container,self.group_container]


