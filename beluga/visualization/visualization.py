from beluga.visualization import renderers
from beluga.visualization.renderers import MatplotlibRenderer, BokehRenderer, ToyplotRenderer
from beluga.utils import load
import inspect
import warnings, logging


class Visualizer:
    def __init__(self, renderer='matplotlib'):

        self.renderer = None
        self.load_renderer(renderer)

    def load_renderer(self, name, **kwargs):
        """
        Helper method to load renderer by name.

        :param name: The name of the bvp algorithm
        :keywords: Additional keyword arguments passed into the renderer.
        :return: An instance of the renderer.
        """

        # Load algorithm from the package
        for renderer_name, renderer in inspect.getmembers(renderers):
            if inspect.isclass(renderer):
                if renderer_name.lower() == (name.lower() + 'renderer'):
                    self.renderer = renderer(**kwargs)
                    return self.renderer
        else:
            logging.warning('Renderer ''{}'' not found so defaulting to Matplotlib'.format(name))

            from beluga.visualization.renderers import MatplotlibRenderer
            self.renderer = MatplotlibRenderer(**kwargs)
            return self.renderer




