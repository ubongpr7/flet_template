import datetime
from flet import *

class DatePicker_(DatePicker):
    def __init__(self,date_changed,date_dismissed=None):
        super().__init__()
        self.confirm_text='Select'
        self.text_style=TextStyle(color=colors.BLUE,size=19)
        self.first_date=datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day)
        self.last_date=datetime.datetime(2026,12,21)
        self.date_picker_entry_mode=DatePickerEntryMode.CALENDAR
        self.on_change=date_changed
        self.date_picker_mode=DatePickerMode.DAY
        self.on_change=date_changed
        self.on_dismiss=date_dismissed
    

class TimePicker_(TimePicker):
    def __init__(self,time_changed,time_dismissed=None):
        super().__init__()
        self.confirm_text='Select'
        self.text_style=TextStyle(color=colors.BLUE,size=19)
        self.time_picker_entry_mode=TimePickerEntryMode.DIAL
        # self.hour_label_text='h'
        # self.minute_label_text='m'
        self.on_change=time_changed
        self.on_dismiss=time_dismissed
    
class FilePicker_(FilePicker):

    def __init__(self,on_result=None,on_upload=None):
        super().__init__()
        self.on_result=on_result
        self.on_upload=on_upload

