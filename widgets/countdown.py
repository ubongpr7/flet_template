import flet as ft
from flet import *
import asyncio


# class CountDown(UserControl):
#     def __init__(self, seconds,text_info='',t_align=None):
#         self.text_info=text_info
#         self.seconds=seconds
#         super().__init__()
#     async def count_down(self):
#         while self.seconds!=-1 and self.running:
#             print('counting down')
#             mins,secs=divmod(self.seconds,60)
#             self.text.value=f'{self.text_info}'+ '{:02d}:{:02d}'.format(mins,secs)
#             self.update()
#             await asyncio.sleep(1)
#             self.seconds-=1
#             if self.seconds==0:
#                 self.text.value=f'{self.text_info}'
#                 self.update()
        
#     def build(self):
#         self.text=Text()
#         return self.text
#     async def did_mount_async(self):
#         self.running=True
#         asyncio.create_task(self.count_down())

        


#     async def will_unmount_async(self):
#         self.running=False
     


class CountDown(ft.UserControl):
    def __init__(self, seconds,text_info='',t_align=None):
        super().__init__()
        self.seconds = seconds

    async def did_mount_async(self):
        self.running = True
        asyncio.create_task(self.update_timer())

    async def will_unmount_async(self):
        self.running = False

    async def update_timer(self):
        while self.seconds!=-1 and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value = "{:02d}:{:02d}".format(mins, secs)
            await self.update_async()
            await asyncio.sleep(1)
            self.seconds -= 1

    def build(self):
        self.countdown = ft.Text()
        return self.countdown