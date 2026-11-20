
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_rgb, to_rgba, LogNorm
from matplotlib.ticker import ScalarFormatter, NullFormatter, PercentFormatter
import seaborn as sns

plt.style.use("dark_background")

light = "#FAF2F0"
c1 = "#F9C87C"
c2 = "#822B8B"
c3 = "#EC5B4E"
c4 = "#F38A67"
c5 = "#DD355B"
c6 = "#B96AC9"

plt.rcParams.update({
    "legend.facecolor": "black",
    "legend.edgecolor": "none",
    "legend.labelcolor": "white",
})

cmap_film_full = LinearSegmentedColormap.from_list(
    "film_burn_full",
    [light, c1, c4, c3, c5, c2, "#14071A"],
    N=256
)

cmap_film_purple = LinearSegmentedColormap.from_list(
    "film_burn_purple",
    ["#14071A", "#4A1554", c2, c6, "#E5B8F0", light],
    N=256
)

cmap_film_orange = LinearSegmentedColormap.from_list(
    "film_burn_orange",
    ["#1A080C", "#8C1D38", c3, "#F76D3C", c1, light],
    N=256
)

cmap_film_div = LinearSegmentedColormap.from_list(
    "film_burn_div",
    ["#E5B8F0", "#9D4EDD", "#5D3D62", "#383838", "#66322C", c3, c1],
    N=256
)

for cm in [cmap_film_full, cmap_film_purple, cmap_film_orange, cmap_film_div]:
    plt.colormaps.register(cm, force=True)
