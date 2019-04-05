from beluga.visualization.renderers import BaseRenderer

import matplotlib
from matplotlib import pyplot as plt


class MatplotlibRenderer(BaseRenderer):
    def __init__(self):
        BaseRenderer.__init__(self)

    def create_fig(self, **kwargs):
        fig = plt.figure(**kwargs)
        return fig

