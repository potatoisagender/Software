from pyqtgraph.opengl import *

from software.thunderscope.constants import Colors, DepthValues
from software.thunderscope.thread_safe_buffer import ThreadSafeBuffer
from software.thunderscope.gl.layers.gl_layer import GLLayer
from software.thunderscope.gl.graphics.gl_circle import GLCircle
from software.thunderscope.gl.graphics.gl_polygon import GLPolygon
from software.thunderscope.gl.graphics.gl_stadium import GLStadium


from software.thunderscope.gl.helpers.observable_list import ObservableList

class GLMaxDribbleLayer(GLLayer):
    """GLLayer"""

    def __init__(self, name: str, buffer_size:int = 5) -> None:
        """Initialize the GLMaxDribbleLayer

        :param name: The displayed name of the layer
        :param buffer_size: The buffer size, set higher for smoother plots.
                            Set lower for more realtime plots. Default is arbitrary
                            """
        super().__init__(name)
        self.setDepthValue(DepthValues.BACKGROUND_DEPTH)

        self.dribble_radius_graphics = ObservableList(self._graphics_changed)
        self.dribble_circle_graphics = ObservableList(self._graphics_changed)