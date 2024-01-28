from flet import *

from widgets.text_widget import SmallBodyText

class NotificationItem(PopupMenuItem):

    def __init__(self,image,notification):
        super().__init__()
        
        self.content=Container(
           on_click=None ,
           height=40,
           border_radius=10,
           padding=5,
           bgcolor=colors.with_opacity(0.95,color='#FFFFFF'),
            content=Row(
                controls=[
                    Stack(
                        height=30,
                        width=30,
                        controls=[CircleAvatar(
                            foreground_image_url=image,
                            radius=15
                        ),
                        Container(
                        content=CircleAvatar(bgcolor=colors.GREEN, radius=2),
                        alignment=alignment.bottom_right,
                ),
                    ]
                    ),
                    
                    Text(value=f'{notification[:45]}...',weight='bold',color=colors.BLACK,size=9)
                ]
            )
        
        )







