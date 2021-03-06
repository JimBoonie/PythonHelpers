from .numpy_utils import subsample
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def scatter_3d(X, sample_size=None, fig=None, subplot=None, title='X', xlabel='X', 
               ylabel='Y', zlabel='Z'):
    """
    Create 3d scatterplot of N-by-3 array.

    Inputs:
        x - The N-by-3 array to visualize.
        sample_size - The number of samples to select from x. If None, the whole 
            array X is used. Useful if N of X is very large. (Default: None)
        fig - The Matplotlib figure to display the plot. If None, a new figure is
            created. (Default: None)
        subplot - The subplot positions consumed by Figure.add_subplot. If None, no
            subplot is created. (Default: None)
        title - The plot title.
        xlabel - The label applied to the x-axis.
        ylabel - The label applied to the y-axis.
        zlabel - The label applied to the z-axis.
    Outputs:
        x - The subsampled array.
    """

    if not X.ndim == 2:
        raise ValueError('Shape of X must be two dimensions. (shape: {})'.format(X.shape))

    if not X.shape[1] == 3:
        raise ValueError('Number of columns of X must be equal to 3. (shape: {})'.format(
            X.shape))

    if fig is None and subplot is not None:
        raise ValueError('If subplot is set, then fig must be provided.')
    
    if fig is None and subplot is None:
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1], projection='3d')
    elif subplot is None:
        ax = fig.add_axes([0, 0, 1, 1], projection='3d')
    else:
        if isinstance(subplot, list):
            ax = fig.add_subplot(*subplot, projection='3d')
        else:
            ax = fig.add_subplot(subplot, projection='3d')
           
    if sample_size is not None:
        X = subsample(X, sample_size)
        
    ax.scatter(X[:, 0], X[:, 1], X[:, 2])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    
    return ax

def grid_imshow(grid, imgs_list, imgs2_list):
    """
    Plot a grid of subplots with paired images.

    Inputs:
        grid - The list of dimensions of the grid.
        imgs_list - The list of images to plot.
        imgs2_list - The second list of images to plot. Must be the same length as
            imgs_list.
    Outputs:
        None
    """

    for r in range(grid[0]):
        for c in range(grid[1]):
            img = imgs_list[grid[1] * r + c]
            img2 = imgs2_list[grid[1] * r + c]

            plt.subplot(2 * grid[0], grid[1], 2 * r * grid[1] + c + 1)
            plt.imshow(img)
            plt.subplot(2 * grid[0], grid[1], (2 * r + 1) * grid[1] + c + 1)
            plt.imshow(img2)
