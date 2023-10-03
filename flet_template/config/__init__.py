from flet import *
import flet as fl 
from .urls import urlpatterns

    
def main(page:fl.Page):
    page.theme_mode='light'
    def route_change(route):
        page.views.clear()
        seen =False
        for url in urlpatterns:
            # if66666 pa
            if page.route == url.route:

                page.views.append(url) 
                seen=True         
                print(url.route)
                page.update()         


        if not  seen :
            # you can add your custom 404
            page.session.set('wrong_route',page.route)
            if len(page.views)>1: 
                page.views.pop()

                top_view=page.views[-1] 
                page.go(top_view.route)
            else :   
                page.go('/')
                # print(url.route)
                # page.update()         
                     
    def view_pop(views):
        page.views.pop()
        top_view=page.views[-1] 
        page.go(top_view.route)
        page.update()

    def store_route(e):
        page.route='/store' 
        page.update()
    
    # define fonts family for the app
    page.fonts={
    'heading': 'fonts/Roboto/Roboto-Bold.ttf',
    'body': 'fonts/Roboto/Roboto-Medium.ttf',
    'subheading': 'fonts/Roboto/Roboto-Regular.ttf',
    'styled': 'fonts/Lobster/Lobster-Regular.ttf',
    

    }
    if page.theme_mode=='dark':
        page.theme= fl.Theme(
            color_scheme=fl.ColorScheme(
                primary ='white',
                secondary ='#3FD0B6',
                tertiary ='#E35588',
                primary_container ='#33313F',
                secondary_container ='#202E57',
                

            )
        )
    else:    
        page.theme= fl.Theme(
            color_scheme=fl.ColorScheme(
                primary ='#000154',
                secondary ='#3FD0B6',
                tertiary ='#E35588',
                primary_container ='#33313F',
                secondary_container ='#202E57',
                

            )
        )
        
    page.on_view_pop=view_pop

    page.on_route_change=route_change
    page.go(page.route)
    
    page.update()
# color_mode =main.   
    