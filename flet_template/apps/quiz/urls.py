# from config.utils import AppView
# from config.urls import path
from typing import Any, List, Optional
from flet_core import Control
from flet_core.app_bar import AppBar
from flet_core.control import OptionalNumber
from flet_core.floating_action_button import FloatingActionButton
from flet_core.navigation_bar import NavigationBar
from flet_core.types import CrossAxisAlignment, MainAxisAlignment, PaddingValue, ScrollMode
from flet import View

class AppView(View):
    def __init__(self, route: str | None = None, controls: List[Control] | None = None, appbar: AppBar | None = None, floating_action_button: FloatingActionButton | None = None, navigation_bar: NavigationBar | None = None, vertical_alignment: MainAxisAlignment = MainAxisAlignment.NONE, horizontal_alignment: CrossAxisAlignment = CrossAxisAlignment.NONE, spacing: OptionalNumber = None, padding: PaddingValue = None, bgcolor: str | None = None, scroll: ScrollMode | None = None, auto_scroll: bool | None = None, fullscreen_dialog: bool | None = None, on_scroll_interval: OptionalNumber = None, on_scroll: Any = None):
        super().__init__(route, controls, appbar, floating_action_button, navigation_bar, vertical_alignment, horizontal_alignment, spacing, padding, bgcolor, scroll, auto_scroll, fullscreen_dialog, on_scroll_interval, on_scroll)

def include_url(urlpatterns:list,urls:list):
    for url in urls:
        urlpatterns.append(url)
        return urlpatterns  
path=AppView

from .views import *
urlpatterns=[
    path(route='/login',controls=[LoginPage.text]),
    path(route='/register',controls=[RegisterPage.reg_text]),

]

    