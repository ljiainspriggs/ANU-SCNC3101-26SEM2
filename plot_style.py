import inspect
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_rgb, to_rgba, LogNorm
from matplotlib.ticker import ScalarFormatter, NullFormatter, PercentFormatter
import seaborn as sns


def _apply_layout_defaults():
    plt.rcParams.update({
        # figure and layout
        "figure.figsize": (8, 5),
        "figure.dpi": 120,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",

        # typography and font sizes
        "font.size": 11,
        "figure.titlesize": 14,
        "figure.titleweight": "bold",
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.titlepad": 6,
        "axes.labelsize": 10,
        "axes.labelpad": 4,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 10,
        "legend.title_fontsize": 11,

        # axes, ticks, and lines
        "axes.linewidth": 1.0,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.major.size": 4.5,
        "xtick.major.width": 1.0,
        "ytick.major.size": 4.5,
        "ytick.major.width": 1.0,
        "lines.linewidth": 2.0,
        "lines.markersize": 6,
        "scatter.marker": "^",
        "lines.marker": "^",
        "grid.linewidth": 0.6,
        "grid.alpha": 0.2,
    })


def dark():

    plt.style.use("dark_background")
    _apply_layout_defaults()

    cream = "#FAF2F0"
    p1 = "#19D3C5"  # teal primary
    p2 = "#9353FF"  # purple primary
    p3 = "#FFD034"  # gold primary
    s1 = "#99F6EE"  # teal secondary
    s2 = "#CFAFFF"  # purple secondary
    s3 = "#FFECA3"  # gold secondary

    plt.rcParams.update({
        "lines.color": cream,
        "patch.edgecolor": cream,
        "text.color": cream,
        "axes.edgecolor": cream,
        "axes.labelcolor": cream,
        "xtick.color": cream,
        "ytick.color": cream,
        "grid.color": cream,
        "legend.facecolor": "black",
        "legend.edgecolor": "none",
        "legend.labelcolor": cream,
    })

    # full multi-hue sequential map (deep void to purple to teal to gold to cream)
    cmap_dark_full = LinearSegmentedColormap.from_list(
        "dark_full",
        ["#0D051A", "#3D1878", p2, p1, p3, s3, cream],
        N=256
    )

    # sequential purple
    cmap_dark_purple = LinearSegmentedColormap.from_list(
        "dark_purple",
        ["#0D051A", "#3D1878", p2, s2, cream],
        N=256
    )

    # sequential gold
    cmap_dark_gold = LinearSegmentedColormap.from_list(
        "dark_gold",
        ["#1A1100", "#6E4D00", p3, s3, cream],
        N=256
    )

    # sequential teal
    cmap_dark_teal = LinearSegmentedColormap.from_list(
        "dark_teal",
        ["#021716", "#095751", p1, s1, cream],
        N=256
    )

    # diverging purple to gold (colourblind-safe and balanced around neutral charcoal)
    cmap_dark_div = LinearSegmentedColormap.from_list(
        "dark_div",
        [s2, p2, "#46316E", "#262626", "#6E5514", p3, s3],
        N=256
    )

    # push all local variables into the notebook's namespace
    target = inspect.currentframe().f_back.f_globals
    target.update({k: v for k, v in locals().items() if k != "target"})


def light():

    plt.style.use("default")
    _apply_layout_defaults()

    cream = "#FAF2F0"
    p1 = "#006B63"  # teal primary
    p2 = "#301075"  # purple primary
    p3 = "#B57C00"  # gold primary
    s1 = "#59DED3"  # teal secondary
    s2 = "#A378FF"  # purple secondary
    s3 = "#FFF0A8"  # gold secondary

    plt.rcParams.update({
        "legend.facecolor": "white",
        "legend.edgecolor": "none",
        "legend.labelcolor": "black",
    })

    # full multi-hue sequential map (cream to gold to teal to purple to deep void)
    cmap_light_full = LinearSegmentedColormap.from_list(
        "light_full",
        [cream, s3, p3, p1, p2, "#140536"],
        N=256
    )

    # sequential purple (cream to deep purple)
    cmap_light_purple = LinearSegmentedColormap.from_list(
        "light_purple",
        [cream, s2, p2, "#140536"],
        N=256
    )

    # sequential gold (cream to deep gold)
    cmap_light_gold = LinearSegmentedColormap.from_list(
        "light_gold",
        [cream, s3, p3, "#4A3100"],
        N=256
    )

    # sequential teal (cream to deep teal)
    cmap_light_teal = LinearSegmentedColormap.from_list(
        "light_teal",
        [cream, s1, p1, "#002B28"],
        N=256
    )

    # diverging purple to gold (colourblind-safe and balanced around neutral light grey)
    cmap_light_div = LinearSegmentedColormap.from_list(
        "light_div",
        [p2, s2, "#CFC6E6", "#EAEAEA", "#EAD8A8", p3, "#5C3D00"],
        N=256
    )

    # push all local variables into the notebook's namespace
    target = inspect.currentframe().f_back.f_globals
    target.update({k: v for k, v in locals().items() if k != "target"})
