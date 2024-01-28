from flet import *


class DropDownWidget(Container):
    def __init__(self,visible):
        super().__init__()
        self.bgcolor=colors.SECONDARY_CONTAINER
        self.visible=visible
        self.border_radius=15
        self.columns=Column(
                    controls=[]
                ),
           
        self.main_content=ResponsiveRow(
            controls=[
                self.columns
            ]
        )