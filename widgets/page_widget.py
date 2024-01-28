from flet import *

def sections_container(self:object,controls:list,bgcolor:str=None,col=12,border=None,border_radius=20,padding=1):
        return Container(
            bgcolor=bgcolor,
            border=border,
            padding=padding,
            
            border_radius=border_radius,
            col=col,
            content=ResponsiveRow(
                controls=controls
            )
        )      
