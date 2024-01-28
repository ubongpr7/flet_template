import asyncio
from flet import *
from settings.utils import *

from widgets.notifications import NotificationItem
from widgets.text_widget import *




class BackgroundControl(UserControl):
    def __init__(self,selfed):
        super().__init__()
        self.selfed=selfed
    
    
    async def did_mount_async(self):
        self.running=True
        asyncio.create_task(self.selfed.background_task())
   
    
    async def will_unmount_async(self):
        self.running=False
    def build(self):

        return Container(content=Text(value=''))



