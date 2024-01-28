from flet import *


class DropDownWidget(Dropdown):
    def __init__(self,options, title):

        super().__init__()
        self.width=180
        self.height=40
        self.options=options
        self.border_width=0
        self.label=title

                
            