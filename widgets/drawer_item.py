from flet import *

from widgets.text_widget import SmallBodyText

class NavDrawerItem(NavigationDrawerDestination):
    def __init__(self,tooltip_1,text_1,icon_1,icon_2,text_2,tooltip_2='',on_click_=None,routed=None,):
            super().__init__()
            self.tooltip_2=tooltip_2
            self.tooltip_1=tooltip_1
            self.on_click_=on_click_
            self.text_1=text_1
            self.text_2=text_2
            self.icon_2=icon_2
            self.icon_1=icon_1
            self.routed=routed
            self.icon_content=Container(
                    tooltip=self.tooltip_1,
                    on_click=self.on_click_,
                    content=Row(
                        controls=[
                            Icon(self.icon_2,color=colors.PRIMARY),
                            SmallBodyText(text=self.text_1,)
                        ]
                    ,),
                )
            self.selected_icon_content=Container(
                    on_click=self.on_click_,
                    tooltip=self.tooltip_2,
                    
                    content=Row(
                        controls=[
                            Icon(self.icon_2,color=colors.ON_PRIMARY),
                            SmallBodyText(text=self.text_2,color=colors.ON_PRIMARY)
                        ]
                    ,),
                )
    
           