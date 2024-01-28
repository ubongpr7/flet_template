from flet import *
from widgets.buttons_widget import column_set

from widgets.images import *
from widgets.text_widget import SmallBodyText


class PostAvartar(Row):
     def __init__(self,selfed:object,names:str='Ubong Prosper',profile_pic:str=None,posted:str='',location='',):
        super().__init__()
                
        self.user_names=Text(value=f'{names}',font_family='heading',color=colors.BLACK,size=15)
        self.posted=Text(value=f'{posted}',font_family='subheading',color=colors.BLACK,size=10)
        self.location=Container(content=Row([Text(value=f'{location}',font_family='subheading',color=colors.BLACK,size=10)]))
        self.profile_pic=profile_pic
        
        self.controls=[
            Container(
                on_click=None,
                   content= Stack(
                        height=30,
                        width=30,
                        controls=[CircleAvatar(
                            
                            foreground_image_url=self.profile_pic,
                            radius=15,
                            
                        ),
                        Container(
                        content=CircleAvatar(bgcolor=colors.GREEN, radius=2),
                        alignment=alignment.bottom_right,
                ),
                    ]
                    ),
                    
        ),
                    
                    # profile_avartar(self=selfed,user_pk=1),
                    self.user_names,
                    self.posted
                ]
            
class ReactionComponent(Container):
    def __init__(self,icon_):
        super().__init__()
        self.padding=10
        self.icon_=icon_
        self.content=Column(
            
            [
                Icon(self.icon_,color=colors.PRIMARY,),
            ],
        alignment='center',
        horizontal_alignment='center',
        spacing=0
        



        )
        self.on_hover=self.on_hover_


    async def on_hover_(self,e):
        self.bgcolor=colors.PRIMARY_CONTAINER if  e.data=='true'    else None
        await self.update_async()

class ReactionComponentGesture(GestureDetector):
    def __init__(self,icon_):
        super().__init__()
        self.content=ReactionComponent(icon_)
        self.on_hover=self.on_hover_
        

    async def on_hover_(self,e):
        self.content.bgcolor=colors.RED
        await self.update_async()

class PostReactions(Row) :
    def __init__(self,_likes:int,_comments:int,_shares:int):
        super().__init__()

        self.alignment='spaceEvenly'
        self.likes=Row()
        self.comments=Row()
        self.register_btn=ReactionComponent(icon_=icons.REPORT_GMAILERRORRED)
        
        self.share_btn=ReactionComponent(icon_=icons.SHARE)
        self.comment_btn=ReactionComponent(icon_=icons.COMMENT_OUTLINED)
        self.like_btn=ReactionComponent(icon_=icons.HEART_BROKEN_SHARP)
        self.controls=[
            Column(
                [
                    self.like_btn,
                ]
            ),
        
            Column(
                [
                    self.comment_btn,
                ]
            ),
        
            Column(
                [
                    self.register_btn,
                ]
            ),
        
            Column(
                [
                    self.share_btn,
                ]
            ),
        
        ]

class CommentSection(Container):
    def __init__(self):
        super().__init__()
        self.bgcolor=colors.SECONDARY_CONTAINER
        self.content=Column(
            [

                Text(value='Be the first to comment',text_align='center',color=colors.TERTIARY,font_family='heading'),
                TextField(label='Add comment'),
                Container(height=2)
            ],
            alignment='center'
        )


class PostContainer(Container):
    def __init__(
            self,
            selfed:object,
            names:str,
            profile_pic:str,
            posted:str,
            location:str,
            _likes:int,
            _comments:int,
            _shares:int,
            title:str,
            description:str,
            src:str):
        super().__init__()
        self.bgcolor=colors.SECONDARY_CONTAINER
        self.padding=12
        self.border_radius=20
        self.description=description
        if len(self.description)>120:
            self.description_=Text(value=f'{self.description[:120]}...',font_family='subheading',size=10,color=colors.PRIMARY)
        else:
            self.description_=Text(value=f'{self.description}',font_family='subheading',size=10,color=colors.PRIMARY)
        
        
        self.text_content=TextButton(
                    on_click=self.show_or_hide_more,
                    style=ButtonStyle(bgcolor=None,overlay_color={"":"transparent"},),
                    content=Column(

                    [
                        ResponsiveRow(
                            [
                                Text(value=title,font_family='heading',size=15,color=colors.PRIMARY),
                                self.description_,
                            ],

                        ),
                        
                    ]
                ),
                
                )
                
        self.content=Column(
            [
                Stack(
                    [PostAvartar(selfed,names,profile_pic,posted,location),
                    PopupMenuButton(
                        items=[
                            PopupMenuItem(icon=icons.POWER_INPUT, text="Check power"),
                                PopupMenuItem(content=Row(controls=[Icon(icons.LOGIN_ROUNDED,color='#0F0E15'),SmallBodyText(text='Login',color='#0F0E15'),]),on_click=lambda _: self.selfed.page.go(route=f'/{project_}/accounts/login')),
                                PopupMenuItem(content=Row(controls=[Icon(icons.LOGIN_ROUNDED,color='#0F0E15',tooltip='Login to existing account'),SmallBodyText(text='Login transparent transparent',color='#0F0E15'),]),on_click=lambda _: self.selfed.page.go(route=f'/{project_}/accounts/login')),
                                Divider(color='transparent'),
                                PopupMenuItem(content=Row(controls=[Icon(icons.LOGIN_ROUNDED,color='#0F0E15'),SmallBodyText(text='Login',color='#0F0E15'),]),on_click=lambda _: self.selfed.page.go(route=f'/{project_}/accounts/login')),
                                
                        ],
                        right=0,
                        
                        
                    )
                    
                       
                    ],
                       
                       ),
                self.text_content,
                Container(
                        container_fitted_image(src=src)
                            
                        ),
                
                PostReactions(_likes,_comments,_shares)
            ]
        )

    async def show_or_hide_more(self,e):
        if  len(self.description)>120:
            if  self.description_.value==f'{self.description[:120]}...':
                self.description_.value=f'{self.description}'
                self.content.controls.append(
                    CommentSection()
                )
                await self.update_async()
            else:
                self.description_.value=f'{self.description[:120]}...'
                self.content.controls.pop()

                await self.update_async()

class AllPostContainer(Container):
    def __init__(self,controls):
        super().__init__()
        
        self.bgcolor=colors.SECONDARY_CONTAINER
        self.padding=12
        self.border_radius=20
        self.col=column_set(small_phone=12,tablet=8,land_scape_phone=6,land_scape_tablet=5,desktop=5)
        self.content=ResponsiveRow(
            controls=controls
        )

class Group(Container):
    def __init__(self,src='/images/img2/school1.jpg',group_name='Group name'):
        super().__init__()
        
        self.content= Column(
                        [
                            height_fitted_image(src=src),
                            ResponsiveRow(
                                [

                            Text(value=group_name,font_family='heading',)
                                ]
                            ),
                        ]
                    )
        self.col=4
        self.on_click=None
    
                
class Groups(Container):
    def __init__(self):
        super().__init__()
        self.col=column_set(small_phone=12,tablet=8,land_scape_phone=6,land_scape_tablet=5,desktop=4)
        
        self.bgcolor=colors.SECONDARY_CONTAINER
        self.padding=16
        self.border_radius=20
        self.content=ResponsiveRow(
            [
               Group(),
               Group(),
               Group(),
            
                Container(
                    height=20,
                    content=Text(value='See more...',font_family='subheading',size=12,text_align='center',color=colors.ON_TERTIARY),
                    bgcolor=colors.SECONDARY_CONTAINER,
                    border=Border(top=BorderSide(1.5,color=colors.PRIMARY_CONTAINER))
                )
            ]
        )




