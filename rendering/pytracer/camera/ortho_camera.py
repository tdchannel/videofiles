from .core import PtCommon
from .core import PtCamera

class ortho_camera(PtCamera.PtCamera):
    def __init__(self,name=None):
        PtCamera.PtCamera.__init__(self,name=name)
