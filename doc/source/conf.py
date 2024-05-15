#
# pyqtgraph documentation build configuration file, created by
# sphinx-quickstart on Fri Nov 18 19:33:12 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
import time
from datetime import datetime

from sphinx.application import Sphinx

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(path, '..', '..'))
sys.path.insert(0, os.path.join(path, '..', 'extensions'))
import pyqtgraph

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_qt_documentation",
    "sphinx_design",
    "sphinx_favicon",
    "sphinxext.rediraffe",
    "sphinxcontrib.images",
    "sphinx_autodoc_typehints"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# Set Qt Documentation Variable
qt_documentation = "Qt6"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None)
}

nitpick_ignore_regex = [
    ("py:class", r"re\.Pattern"),  # doesn't seem to be a good ref in python docs
]

napoleon_preprocess_types = True
napoleon_type_aliases = {
    "callable": ":class:`collections.abc.Callable`",
    "np.ndarray": ":class:`numpy.ndarray`",
    'array_like': ':term:`array_like`',
    'color_like': ':func:`pyqtgraph.mkColor`',
    # 'ColorMapSpecifier': ':class:`str`, (:class:`str`, :class:`str`), or :class:`~pyqtgraph.ColorMap`',
}

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'pyqtgraph'
now = datetime.utcfromtimestamp(
    int(os.environ.get('SOURCE_DATE_EPOCH', time.time()))
)
copyright = '2011 - {}, PyQtGraph developers'.format(now.year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = pyqtgraph.__version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

autodoc_inherit_docstrings = False
autodoc_mock_imports = [
    "scipy",
    "h5py",
    "matplotlib",
]


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pydata_sphinx_theme'

# favicons
favicons = [
    "docset-icon.png",
    "docset-icon@2x.png",
    "peegee_03_square_no_bg_32_cleaned.ico"
]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "github_url": "https://github.com/pyqtgraph/pyqtgraph",
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "twitter_url": "https://twitter.com/pyqtgraph",
    "use_edit_page_button": False,
    "secondary_sidebar_items": ["page-toc"],
    "navigation_with_keys": False
}


if os.getenv("BUILD_DASH_DOCSET"):
    html_theme_options |= {
        'secondary_sidebar_items': [],
        "show_prev_next": False,
        "collapse_navigation": True,
    }


# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = os.path.join("images", "peegee_02.svg")

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# add the theme customizations
html_css_files = [
    "custom.css",
]

if os.getenv("BUILD_DASH_DOCSET"):
    html_css_files.append("dash.css")

# Redirects for pages that were moved to new locations
rediraffe_redirects = {
    "3dgraphics/glaxisitem.rst": "api_reference/3dgraphics/glaxisitem.rst",
    "3dgraphics/glgraphicsitem.rst": "api_reference/3dgraphics/glgraphicsitem.rst",
    "3dgraphics/glgraphitem.rst": "api_reference/3dgraphics/glgraphitem.rst",
    "3dgraphics/glgriditem.rst": "api_reference/3dgraphics/glgriditem.rst",
    "3dgraphics/glimageitem.rst": "api_reference/3dgraphics/glimageitem.rst",
    "3dgraphics/gllineplotitem.rst": "api_reference/3dgraphics/gllineplotitem.rst",
    "3dgraphics/glmeshitem.rst": "api_reference/3dgraphics/glmeshitem.rst",
    "3dgraphics/glscatterplotitem.rst": "api_reference/3dgraphics/glscatterplotitem.rst",
    "3dgraphics/glsurfaceplotitem.rst": "api_reference/3dgraphics/glsurfaceplotitem.rst",
    "3dgraphics/gltextitem.rst": "api_reference/3dgraphics/gltextitem.rst",
    "3dgraphics/glviewwidget.rst": "api_reference/3dgraphics/glviewwidget.rst",
    "3dgraphics/glvolumeitem.rst": "api_reference/3dgraphics/glvolumeitem.rst",
    "3dgraphics/index.rst": "api_reference/3dgraphics/index.rst",
    "3dgraphics/meshdata.rst": "api_reference/3dgraphics/meshdata.rst",
    "colormap.rst": "api_reference/colormap.rst",
    "config_options.rst": "api_reference/config_options.rst",
    "dockarea.rst": "api_reference/dockarea.rst",
    "flowchart/flowchart.rst": "api_reference/flowchart/flowchart.rst",
    "flowchart/index.rst": "api_reference/flowchart/index.rst",
    "flowchart/node.rst": "api_reference/flowchart/node.rst",
    "flowchart/terminal.rst": "api_reference/flowchart/terminal.rst",
    "functions.rst": "api_reference/functions.rst",
    "graphicsItems/arrowitem.rst": "api_reference/graphicsItems/arrowitem.rst",
    "graphicsItems/axisitem.rst": "api_reference/graphicsItems/axisitem.rst",
    "graphicsItems/bargraphitem.rst": "api_reference/graphicsItems/bargraphitem.rst",
    "graphicsItems/buttonitem.rst": "api_reference/graphicsItems/buttonitem.rst",
    "graphicsItems/colorbaritem.rst": "api_reference/graphicsItems/colorbaritem.rst",
    "graphicsItems/curvearrow.rst": "api_reference/graphicsItems/curvearrow.rst",
    "graphicsItems/curvepoint.rst": "api_reference/graphicsItems/curvepoint.rst",
    "graphicsItems/dateaxisitem.rst": "api_reference/graphicsItems/dateaxisitem.rst",
    "graphicsItems/errorbaritem.rst": "api_reference/graphicsItems/errorbaritem.rst",
    "graphicsItems/fillbetweenitem.rst": "api_reference/graphicsItems/fillbetweenitem.rst",
    "graphicsItems/gradienteditoritem.rst": "api_reference/graphicsItems/gradienteditoritem.rst",
    "graphicsItems/gradientlegend.rst": "api_reference/graphicsItems/gradientlegend.rst",
    "graphicsItems/graphicsitem.rst": "api_reference/graphicsItems/graphicsitem.rst",
    "graphicsItems/graphicslayout.rst": "api_reference/graphicsItems/graphicslayout.rst",
    "graphicsItems/graphicsobject.rst": "api_reference/graphicsItems/graphicsobject.rst",
    "graphicsItems/graphicswidget.rst": "api_reference/graphicsItems/graphicswidget.rst",
    "graphicsItems/graphicswidgetanchor.rst": "api_reference/graphicsItems/graphicswidgetanchor.rst",
    "graphicsItems/graphitem.rst": "api_reference/graphicsItems/graphitem.rst",
    "graphicsItems/griditem.rst": "api_reference/graphicsItems/griditem.rst",
    "graphicsItems/histogramlutitem.rst": "api_reference/graphicsItems/histogramlutitem.rst",
    "graphicsItems/imageitem.rst": "api_reference/graphicsItems/imageitem.rst",
    "graphicsItems/index.rst": "api_reference/graphicsItems/index.rst",
    "graphicsItems/infiniteline.rst": "api_reference/graphicsItems/infiniteline.rst",
    "graphicsItems/isocurveitem.rst": "api_reference/graphicsItems/isocurveitem.rst",
    "graphicsItems/labelitem.rst": "api_reference/graphicsItems/labelitem.rst",
    "graphicsItems/legenditem.rst": "api_reference/graphicsItems/legenditem.rst",
    "graphicsItems/linearregionitem.rst": "api_reference/graphicsItems/linearregionitem.rst",
    "graphicsItems/multiplotitem.rst": "api_reference/graphicsItems/multiplotitem.rst",
    "graphicsItems/pcolormeshitem.rst": "api_reference/graphicsItems/pcolormeshitem.rst",
    "graphicsItems/plotcurveitem.rst": "api_reference/graphicsItems/plotcurveitem.rst",
    "graphicsItems/plotdataitem.rst": "api_reference/graphicsItems/plotdataitem.rst",
    "graphicsItems/plotitem.rst": "api_reference/graphicsItems/plotitem.rst",
    "graphicsItems/roi.rst": "api_reference/graphicsItems/roi.rst",
    "graphicsItems/scalebar.rst": "api_reference/graphicsItems/scalebar.rst",
    "graphicsItems/scatterplotitem.rst": "api_reference/graphicsItems/scatterplotitem.rst",
    "graphicsItems/targetitem.rst": "api_reference/graphicsItems/targetitem.rst",
    "graphicsItems/textitem.rst": "api_reference/graphicsItems/textitem.rst",
    "graphicsItems/uigraphicsitem.rst": "api_reference/graphicsItems/uigraphicsitem.rst",
    "graphicsItems/viewbox.rst": "api_reference/graphicsItems/viewbox.rst",
    "graphicsItems/vtickgroup.rst": "api_reference/graphicsItems/vtickgroup.rst",
    "graphicsscene/graphicsscene.rst": "api_reference/graphicsscene/graphicsscene.rst",
    "graphicsscene/hoverevent.rst": "api_reference/graphicsscene/hoverevent.rst",
    "graphicsscene/index.rst": "api_reference/graphicsscene/index.rst",
    "graphicsscene/mouseclickevent.rst": "api_reference/graphicsscene/mouseclickevent.rst",
    "graphicsscene/mousedragevent.rst": "api_reference/graphicsscene/mousedragevent.rst",
    "apireference.rst": "api_reference/index.rst",
    "parametertree/apiref.rst": "api_reference/parametertree/apiref.rst",
    "parametertree/index.rst": "api_reference/parametertree/index.rst",
    "parametertree/interactiveparameters.rst": "api_reference/parametertree/interactiveparameters.rst",
    "parametertree/parameter.rst": "api_reference/parametertree/parameter.rst",
    "parametertree/parameteritem.rst": "api_reference/parametertree/parameteritem.rst",
    "parametertree/parametertree.rst": "api_reference/parametertree/parametertree.rst",
    "parametertree/parametertypes.rst": "api_reference/parametertree/parametertypes.rst",
    "point.rst": "api_reference/point.rst",
    "transform3d.rst": "api_reference/transform3d.rst",
    "uml_overview.rst": "api_reference/uml_overview.rst",
    "widgets/busycursor.rst": "api_reference/widgets/busycursor.rst",
    "widgets/checktable.rst": "api_reference/widgets/checktable.rst",
    "widgets/colorbutton.rst": "api_reference/widgets/colorbutton.rst",
    "widgets/colormapwidget.rst": "api_reference/widgets/colormapwidget.rst",
    "widgets/combobox.rst": "api_reference/widgets/combobox.rst",
    "widgets/consolewidget.rst": "api_reference/widgets/consolewidget.rst",
    "widgets/datatreewidget.rst": "api_reference/widgets/datatreewidget.rst",
    "widgets/feedbackbutton.rst": "api_reference/widgets/feedbackbutton.rst",
    "widgets/filedialog.rst": "api_reference/widgets/filedialog.rst",
    "widgets/gradientwidget.rst": "api_reference/widgets/gradientwidget.rst",
    "widgets/graphicslayoutwidget.rst": "api_reference/widgets/graphicslayoutwidget.rst",
    "widgets/graphicsview.rst": "api_reference/widgets/graphicsview.rst",
    "widgets/histogramlutwidget.rst": "api_reference/widgets/histogramlutwidget.rst",
    "widgets/imageview.rst": "api_reference/widgets/imageview.rst",
    "widgets/index.rst": "api_reference/widgets/index.rst",
    "widgets/joystickbutton.rst": "api_reference/widgets/joystickbutton.rst",
    "widgets/layoutwidget.rst": "api_reference/widgets/layoutwidget.rst",
    "widgets/matplotlibwidget.rst": "api_reference/widgets/matplotlibwidget.rst",
    "widgets/multiplotwidget.rst": "api_reference/widgets/multiplotwidget.rst",
    "widgets/pathbutton.rst": "api_reference/widgets/pathbutton.rst",
    "widgets/plotwidget.rst": "api_reference/widgets/plotwidget.rst",
    "widgets/progressdialog.rst": "api_reference/widgets/progressdialog.rst",
    "widgets/rawimagewidget.rst": "api_reference/widgets/rawimagewidget.rst",
    "widgets/remotegraphicsview.rst": "api_reference/widgets/remotegraphicsview.rst",
    "widgets/scatterplotwidget.rst": "api_reference/widgets/scatterplotwidget.rst",
    "widgets/spinbox.rst": "api_reference/widgets/spinbox.rst",
    "widgets/tablewidget.rst": "api_reference/widgets/tablewidget.rst",
    "widgets/treewidget.rst": "api_reference/widgets/treewidget.rst",
    "widgets/valuelabel.rst": "api_reference/widgets/valuelabel.rst",
    "widgets/verticallabel.rst": "api_reference/widgets/verticallabel.rst",
    "internals.rst": "developer_guide/internals.rst",
    "3dgraphics.rst": "getting_started/3dgraphics.rst",
    "how_to_use.rst": "getting_started/how_to_use.rst",
    "images.rst": "getting_started/images.rst",
    "installation.rst": "getting_started/installation.rst",
    "introduction.rst": "getting_started/introduction.rst",
    "plotting.rst": "getting_started/plotting.rst",
    "prototyping.rst": "getting_started/prototyping.rst",
    "qtcrashcourse.rst": "getting_started/qtcrashcourse.rst",
    "exporting.rst": "user_guide/exporting.rst",
    "mouse_interaction.rst": "user_guide/mouse_interaction.rst",
    "region_of_interest.rst": "user_guide/region_of_interest.rst",
    "style.rst": "user_guide/style.rst"
}

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
if os.getenv("BUILD_DASH_DOCSET"):  # used for building dash docsets
    html_sidebars = {
        "**": []
    }
else:
    html_sidebars = {
        "**": ["sidebar-nav-bs.html"],
        'index': []  # don't show sidebar on main landing page
    }

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyqtgraphdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'pyqtgraph.tex', 'pyqtgraph Documentation',
   'Luke Campagnola', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'pyqtgraph', 'pyqtgraph Documentation',
     ['Luke Campagnola'], 1)
]


def html_page_context(app, pagename, templatename, context, doctree):
    # Disable edit button for docstring generated pages
    if "generated" in pagename:
        context["theme_use_edit_page_button"] = False

def setup(app: Sphinx):
    app.connect("html-page-context", html_page_context)
