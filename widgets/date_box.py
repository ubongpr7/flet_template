from datetime import datetime
from flet import * 
import calendar

date_class:dict[int,str]={
    0:"Mon",
    1:"Tue",
    2:"Wed",
    3:"Thu",
    4:"Fri",
    5:"Sat",
    6:"Sun",
}
month_class:dict[int,str]={
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"Septemer",
    10:"October",
    11:"November",
    12:"December",
}

class DateSettings:
    year:int=datetime.now().year
    month:int=datetime.now().month

    @staticmethod
    def get_year():
        return  DateSettings.year
    @staticmethod
    def get_month():
        return  DateSettings.month
    
    @staticmethod
    def get_date(delta:int):
        if  delta==1:
            if delta+DateSettings.month>12:
                DateSettings.month=1
                DateSettings.year+=1
                
            else:
                DateSettings.month+=1
        elif delta==-1:
            if delta+DateSettings.month+delta<1:
                DateSettings.year-=1
                DateSettings.month=12
            else:
                DateSettings.month-=1


            
        return  ''''''

class DateBox(Container):
    def __init__(
            self,
            day,
            date=None,
            date_instance:Column=None,
            task_instance:Column=None,
            opacity_:float|int=None
        ):
        super(DateBox,self).__init__(
            data=date,
            opacity=opacity_
        )
        self.width=33
        self.height=30
        self.task_instance:Column=task_instance
        self.date_instance:Column=date_instance
        self.bgcolor=colors.with_opacity(0.75,colors.PRIMARY_CONTAINER)
        self.border_radius=5
        self.animate=Animation(400,'ease')
        self.shadow=BoxShadow('rectangle')
        self.alignment=alignment.center
        self.day:int=day
        self.on_click=self.select_date
        self.content=Text(value=self.day,text_align='center',color=colors.PRIMARY)
    def select_date(self,e):
        if self.date_instance:
            for row in self.date_instance.controls[1:]:
                for date in row.controls:
                    date.bgcolor='#20303e' if date  ==e.control else None
                    date.border=(
                        border.all(0.5,'#4fadf9') if date==e.control else None
                    )
                    if date==e.control:
                        print(e.control.data)
                        self.task_instance.date.value=e.control.data
                        self.task_instance.date.update()
                        print('done')
                        print(self.date_instance.date.value)
            self.date_instance.update()
class DateGrid(Column):
    
    def __init__(
            self,
        task_instance:object,
            year:int,
            month:int,
        ):
        super(DateGrid,self).__init__(

        )
        self.year=year
        self.month=month
        self.task_manager:object=task_instance
        self.date=Text(value=f'{month_class[self.month]} {self.year}',color=colors.PRIMARY)
        self.year_and_month=Container(
            bgcolor='#20303e',
            border_radius=border_radius.only(top_left=10),
            content=Row(
                alignment='center',
                controls=[
                    IconButton(
                        'chevron_left',
                        icon_color=colors.PRIMARY,
                        on_click=lambda e: self.update_grid(e,-1)
                    ),
                    
                    Container(
                        width=150,
                        content=self.date,
                        alignment=alignment.center
                    ),
                    IconButton(
                        'chevron_right',
                        icon_color=colors.PRIMARY,
                        on_click=lambda e: self.update_grid(e,1)


                    ),
                    
                ]
            )
        )
        self.week_days=Row(
            alignment='spaceEvenly',
            controls=[
                DateBox(
                    day=date_class[index],
                    opacity_=0.81
                    
                )for index in range(7)

            ]
        )
        
        self.controls=[
            self.year_and_month,
            self.week_days
        ]
        self.cal=calendar.Calendar()
        self.populate_grid_date(self.year,self.month)
    def populate_grid_date(self,year:int,month:int):
        del self.controls[2:]
        for week in self.cal.monthdayscalendar(year,month):
            row=Row(
                alignment='spaceEvenly',

            )
            for day in week:
                if  day!=0:
                    row.controls.append(DateBox(
                        day=day,date=self.format_date(day),date_instance=self,task_instance=self.task_manager
                    ))

                else:
                    row.controls.append(DateBox(''))
            self.controls.append(row)
    def format_date(self,day):
        return f'{month_class[self.month]} {day}, {self.year}'

    def update_grid(self,e:TapEvent,delta:int):
        DateSettings.get_date(delta)
        self.update_y_m(DateSettings.get_year(),DateSettings.get_month())
        self.populate_grid_date(DateSettings.get_year(),DateSettings.get_month())
        
    def update_y_m(self,year:int,month:int):
        self.year=year
        self.month=month
        self.date.value=value=f'{month_class[self.month]} {self.year}'
        self.update()
        
        
class TaskManager(Column):
    
    def __init__(
            self,
        
        ):
        super(TaskManager,self).__init__(

        )
        self.date=TextField(value='',read_only=True,label='Date',color=colors.PRIMARY)
        self.controls=[self.date]