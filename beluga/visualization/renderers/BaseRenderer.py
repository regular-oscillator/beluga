from abc import ABC


class BaseRenderer(ABC):
    def __init__(self):
        super(BaseRenderer, self).__init__()

    def create_fig(self, num=None):
        pass

