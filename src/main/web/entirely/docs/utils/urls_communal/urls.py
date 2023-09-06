from django.urls import re_path

from docs.utils.views import VueHome

ADD_TOOL_URL = [
    # http://0.0.0.0:8000/Chunnel/Tool
    re_path(r'$', VueHome.as_view()),
    # # http://0.0.0.0:8000/Chunnel/Tool/LeftSidebar/2aPaPHbvhpgibCmV9VF2szUKUD4oBNVE
    # re_path(r'^LeftSidebar/(?P<sidebar>\w{32})$', LeftSidebar.as_view()),
    # # http://0.0.0.0:8000/Chunnel/Tool/LeftSidebarSon/2aPaPHbvhpgibCmV9VF2szUKUD4oBNVE
    # re_path(r'^LeftSidebarSon/(?P<sidebar>\w{32})$', LeftSidebarSon.as_view()),
    # # http://0.0.0.0:8000/Chunnel/Tool/LeftSidebarSonContent/e4c3267869244e90b4a54361a8b9c045
    # re_path(r'^LeftSidebarSonContent/(?P<sidebar>\w{32})$', LeftSidebarSonContent.as_view()),
]
