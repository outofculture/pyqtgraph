import warnings
import weakref
from math import ceil, floor, isfinite, log, log10

import numpy as np

from .. import debug as debug
from .. import functions as fn
from .. import getConfigOption
from ..Point import Point
from ..Qt import QtCore, QtGui, QtWidgets
from .GraphicsWidget import GraphicsWidget

__all__ = ['AxisItem']
class AxisItem(GraphicsWidget):
    """
    GraphicsItem showing a single plot axis with ticks, values, and label.
    Can be configured to fit on any side of a plot, 
    Can automatically synchronize its displayed scale with ViewBox items.
    Ticks can be extended to draw a grid.
    If maxTickLength is negative, ticks point into the plot.
    """

    def __init__(self, orientation, pen=None, textPen=None, linkView=None, parent=None, maxTickLength=-5, showValues=True, text='', units='', unitPrefix='', **args):
        """
        =============== ===============================================================
        **Arguments:**
        orientation     one of 'left', 'right', 'top', or 'bottom'
        maxTickLength   (px) maximum length of ticks to draw. Negative values draw
                        into the plot, positive values draw outward.
        linkView        (ViewBox) causes the range of values displayed in the axis
                        to be linked to the visible range of a ViewBox.
        showValues      (bool) Whether to display values adjacent to ticks
        pen             (QPen) Pen used when drawing ticks.
        textPen         (QPen) Pen used when drawing tick labels.
        text            The text (excluding units) to display on the label for this
                        axis.
        units           The units for this axis. Units should generally be given
                        without any scaling prefix (eg, 'V' instead of 'mV'). The
                        scaling prefix will be automatically prepended based on the
                        range of data displayed.
        args            All extra keyword arguments become CSS style options for
                        the <span> tag which will surround the axis label and units.
        =============== ===============================================================
        """

        GraphicsWidget.__init__(self, parent)
        self.label = QtWidgets.QGraphicsTextItem(self)
        self.picture = None
        self.orientation = orientation
        if orientation not in ['left', 'right', 'top', 'bottom']:
            raise Exception("Orientation argument must be one of 'left', 'right', 'top', or 'bottom'.")
        if orientation in ['left', 'right']:
            self.label.setRotation(-90)

        self.style = {
            'tickTextOffset': [5, 2],  ## (horizontal, vertical) spacing between text and axis
            'tickTextWidth': 30,  ## space reserved for tick text
            'tickTextHeight': 18,
            'autoExpandTextSpace': True,  ## automatically expand text space if needed
            'autoReduceTextSpace': True,
            'tickFont': None,
            'stopAxisAtTick': (False, False),  ## whether axis is drawn to edge of box or to last tick
            'textFillLimits': [  ## how much of the axis to fill up with tick text, maximally.
                (0, 0.8),    ## never fill more than 80% of the axis
                (2, 0.6),    ## If we already have 2 ticks with text, fill no more than 60% of the axis
                (4, 0.4),    ## If we already have 4 ticks with text, fill no more than 40% of the axis
                (6, 0.2),    ## If we already have 6 ticks with text, fill no more than 20% of the axis
                ],
            'showValues': showValues,
            'tickLength': maxTickLength,
            'maxTickLevel': 2,
            'maxTextLevel': 2,
            'tickAlpha': None,  ## If not none, use this alpha for all ticks.
            'labelMargin': [5, 0],  # label margin : [between label and axis ticks, between label and axis external edge]
        }

        self.textWidth = 30  ## Keeps track of maximum width / height of tick text
        self.textHeight = 18

        # If the user specifies a width / height, remember that setting
        # indefinitely.
        self.fixedWidth = None
        self.fixedHeight = None

        self.labelText = text
        self.labelUnits = units
        self.labelUnitPrefix = unitPrefix
        self.labelStyle = args
        self.logMode = False

        self._tickLevels = None  ## used to override the automatic ticking system with explicit ticks
        self._tickSpacing = None  # used to override default tickSpacing method
        self.scale = 1.0
        self.autoSIPrefix = True
        self.autoSIPrefixScale = 1.0

        self.showLabel(False)

        self.setRange(0, 1)

        if pen is None:
            self.setPen()
        else:
            self.setPen(pen)

        if textPen is None:
            self.setTextPen()
        else:
            self.setTextPen(pen)

        self._linkedView = None
        if linkView is not None:
            self._linkToView_internal(linkView)

        self.grid = False
        
        #self.setCacheMode(self.DeviceCoordinateCache)

    def setStyle(self, **kwds):
        """
        Set various style options.

        =================== =======================================================
        Keyword Arguments:
        tickLength          (int) The maximum length of ticks in pixels.
                            Positive values point toward the text; negative
                            values point away.
        tickTextOffset      (int) reserved spacing between text and axis in px
        tickTextWidth       (int) Horizontal space reserved for tick text in px
        tickTextHeight      (int) Vertical space reserved for tick text in px
        autoExpandTextSpace (bool) Automatically expand text space if the tick
                            strings become too long.
        autoReduceTextSpace (bool) Automatically shrink the axis if necessary 
        tickFont            (QFont or None) Determines the font used for tick
                            values. Use None for the default font.
        stopAxisAtTick      (tuple: (bool min, bool max)) If True, the axis
                            line is drawn only as far as the last tick.
                            Otherwise, the line is drawn to the edge of the
                            AxisItem boundary.
        textFillLimits      (list of (tick #, % fill) tuples). This structure
                            determines how the AxisItem decides how many ticks
                            should have text appear next to them. Each tuple in
                            the list specifies what fraction of the axis length
                            may be occupied by text, given the number of ticks
                            that already have text displayed. For example::

                                [(0, 0.8), # Never fill more than 80% of the axis
                                 (2, 0.6), # If we already have 2 ticks with text,
                                           # fill no more than 60% of the axis
                                 (4, 0.4), # If we already have 4 ticks with text,
                                           # fill no more than 40% of the axis
                                 (6, 0.2)] # If we already have 6 ticks with text,
                                           # fill no more than 20% of the axis

        showValues          (bool) indicates whether text is displayed adjacent
                            to ticks.
        tickAlpha           (float or int or None) If None, pyqtgraph will draw the
                            ticks with the alpha it deems appropriate.  Otherwise, 
                            the alpha will be fixed at the value passed.  With int, 
                            accepted values are [0..255].  With value of type
                            float, accepted values are from [0..1].
        =================== =======================================================

        Added in version 0.9.9
        """
        for kwd,value in kwds.items():
            if kwd not in self.style:
                raise NameError("%s is not a valid style argument." % kwd)

            if kwd in ('tickLength', 'tickTextOffset', 'tickTextWidth', 'tickTextHeight'):
                if not isinstance(value, int):
                    raise ValueError("Argument '%s' must be int" % kwd)

            if kwd == 'tickTextOffset':
                if self.orientation in ('left', 'right'):
                    self.style['tickTextOffset'][0] = value
                else:
                    self.style['tickTextOffset'][1] = value
            elif kwd == 'stopAxisAtTick':
                try:
                    assert len(value) == 2 and isinstance(value[0], bool) and isinstance(value[1], bool)
                except:
                    raise ValueError("Argument 'stopAxisAtTick' must have type (bool, bool)")
                self.style[kwd] = value
            else:
                self.style[kwd] = value

        self.picture = None
        self._adjustSize()
        self.update()

    def close(self):
        self.scene().removeItem(self.label)
        self.label = None
        self.scene().removeItem(self)

    def setGrid(self, grid):
        """Set the alpha value (0-255) for the grid, or False to disable.

        When grid lines are enabled, the axis tick lines are extended to cover
        the extent of the linked ViewBox, if any.
        """
        self.grid = grid
        self.picture = None
        self.prepareGeometryChange()
        self.update()

    def setLogMode(self, *args, **kwargs):
        """
        Set log scaling for x and/or y axes.

        If two positional arguments are provided, the first will set log scaling
        for the x axis and the second for the y axis. If a single positional
        argument is provided, it will set the log scaling along the direction of
        the AxisItem. Alternatively, x and y can be passed as keyword arguments.

        If an axis is set to log scale, ticks are displayed on a logarithmic scale
        and values are adjusted accordingly. (This is usually accessed by changing
        the log mode of a :func:`PlotItem <pyqtgraph.PlotItem.setLogMode>`.) The 
        linked ViewBox will be informed of the change.
        """
        if len(args) == 1:
            self.logMode = args[0]
        else:
            if len(args) == 2:
                x, y = args
            else:
                x = kwargs.get('x')
                y = kwargs.get('y')

            if x is not None and self.orientation in ('top', 'bottom'):
                self.logMode = x
            if y is not None and self.orientation in ('left', 'right'):
                self.logMode = y
        
        if self._linkedView is not None:
            if self.orientation in ('top', 'bottom'):           
                self._linkedView().setLogMode('x', self.logMode)    
            elif self.orientation in ('left', 'right'):
                self._linkedView().setLogMode('y', self.logMode)    

        self.picture = None

        self.update()

    def setTickFont(self, font):
        """
        (QFont or None) Determines the font used for tick values. 
        Use None for the default font.
        """
        self.style['tickFont'] = font
        self.picture = None
        self.prepareGeometryChange()
        ## Need to re-allocate space depending on font size?

        self.update()

    def resizeEvent(self, ev=None):
        #s = self.size()

        ## Set the position of the label
        if self.label is None: # self.label is set to None on close, but resize events can still occur.
            self.picture = None
            return
            
        br = self.label.boundingRect()
        p = QtCore.QPointF(0, 0)
        if self.orientation == 'left':
            p.setY(int(self.size().height() / 2 + br.width() / 2))
            p.setX(-self.style['labelMargin'][0] + self.style['labelMargin'][1])
        elif self.orientation == 'right':
            p.setY(int(self.size().height() / 2 + br.width() / 2))
            p.setX(int(self.size().width() - br.height() + self.style['labelMargin'][0] - self.style['labelMargin'][1]))
        elif self.orientation == 'top':
            p.setY(-self.style['labelMargin'][0] + self.style['labelMargin'][1])
            p.setX(int(self.size().width() / 2. - br.width() / 2.))
        elif self.orientation == 'bottom':
            p.setX(int(self.size().width() / 2. - br.width() / 2.))
            p.setY(int(self.size().height() - br.height() + self.style['labelMargin'][0] - self.style['labelMargin'][1]))
        self.label.setPos(p)
        self.picture = None

    def showLabel(self, show=True):
        """Show/hide the label text for this axis."""
        #self.drawLabel = show
        self.label.setVisible(show)
        if self.orientation in ['left', 'right']:
            self._updateWidth()
        else:
            self._updateHeight()
        if self.autoSIPrefix:
            self.updateAutoSIPrefix()

    def setLabel(self, text=None, units=None, unitPrefix=None, **args):
        """Set the text displayed adjacent to the axis.

        ==============  =============================================================
        **Arguments:**
        text            The text (excluding units) to display on the label for this
                        axis.
        units           The units for this axis. Units should generally be given
                        without any scaling prefix (eg, 'V' instead of 'mV'). The
                        scaling prefix will be automatically prepended based on the
                        range of data displayed.
        args            All extra keyword arguments become CSS style options for
                        the <span> tag which will surround the axis label and units.
        ==============  =============================================================

        The final text generated for the label will look like::

            <span style="...options...">{text} (prefix{units})</span>

        Each extra keyword argument will become a CSS option in the above template.
        For example, you can set the font size and color of the label::

            labelStyle = {'color': '#FFF', 'font-size': '14pt'}
            axis.setLabel('label text', units='V', **labelStyle)

        """
        # `None` input is kept for backward compatibility!
        self.labelText = text or ""
        self.labelUnits = units or ""
        self.labelUnitPrefix = unitPrefix or ""
        if len(args) > 0:
            self.labelStyle = args
        # Account empty string and `None` for units and text
        visible = True if (text or units) else False
        self.showLabel(visible)
        self._updateLabel()

    def _updateLabel(self):
        """Internal method to update the label according to the text"""
        self.label.setHtml(self.labelString())
        self._adjustSize()
        self.picture = None
        self.update()

    def labelString(self):
        if self.labelUnits == '':
            if not self.autoSIPrefix or self.autoSIPrefixScale == 1.0:
                units = ''
            else:
                units = '(x%g)' % (1.0/self.autoSIPrefixScale)
        else:
            units = '(%s%s)' % (self.labelUnitPrefix, self.labelUnits)

        s = '%s %s' % (self.labelText, units)

        style = ';'.join(['%s: %s' % (k, self.labelStyle[k]) for k in self.labelStyle])

        return "<span style='%s'>%s</span>" % (style, s)

    def _updateMaxTextSize(self, x):
        ## Informs that the maximum tick size orthogonal to the axis has
        ## changed; we use this to decide whether the item needs to be resized
        ## to accomodate.
        if self.orientation in ['left', 'right']:
            if self.style["autoReduceTextSpace"]:
                if x > self.textWidth or x < self.textWidth - 10:
                    self.textWidth = x
            else:
                mx = max(self.textWidth, x)
                if mx > self.textWidth or mx < self.textWidth - 10:
                    self.textWidth = mx
            if self.style['autoExpandTextSpace']:
                self._updateWidth()
        
        else:
            if self.style['autoReduceTextSpace']:
                if x > self.textHeight or x < self.textHeight - 10:
                    self.textHeight = x
            else:
                mx = max(self.textHeight, x)
                if mx > self.textHeight or mx < self.textHeight - 10:
                    self.textHeight = mx
            if self.style['autoExpandTextSpace']:
                self._updateHeight()

    def _adjustSize(self):
        if self.orientation in ['left', 'right']:
            self._updateWidth()
        else:
            self._updateHeight()

    def setHeight(self, h=None):
        """Set the height of this axis reserved for ticks and tick labels.
        The height of the axis label is automatically added.

        If *height* is None, then the value will be determined automatically
        based on the size of the tick text."""
        self.fixedHeight = h
        self._updateHeight()

    def _updateHeight(self):
        if not self.isVisible():
            h = 0
        else:
            if self.fixedHeight is None:
                if not self.style['showValues']:
                    h = 0
                elif self.style['autoExpandTextSpace']:
                    h = self.textHeight
                else:
                    h = self.style['tickTextHeight']
                h += self.style['tickTextOffset'][1] if self.style['showValues'] else 0
                h += max(0, self.style['tickLength'])
                if self.label.isVisible():
                    # bounding rect is usually an overestimate
                    h += self.label.boundingRect().height() * 0.8 + sum(self.style['labelMargin'])
            else:
                h = self.fixedHeight

        self.setMaximumHeight(h)
        self.setMinimumHeight(h)
        self.picture = None

    def setWidth(self, w=None):
        """Set the width of this axis reserved for ticks and tick labels.
        The width of the axis label is automatically added.

        If *width* is None, then the value will be determined automatically
        based on the size of the tick text."""
        self.fixedWidth = w
        self._updateWidth()

    def _updateWidth(self):
        if not self.isVisible():
            w = 0
        else:
            if self.fixedWidth is None:
                if not self.style['showValues']:
                    w = 0
                elif self.style['autoExpandTextSpace']:
                    w = self.textWidth
                else:
                    w = self.style['tickTextWidth']
                w += self.style['tickTextOffset'][0] if self.style['showValues'] else 0
                w += max(0, self.style['tickLength'])
                if self.label.isVisible():
                    # bounding rect is usually an overestimate
                    w += self.label.boundingRect().height() * 0.8 + sum(self.style['labelMargin'])
            else:
                w = self.fixedWidth

        self.setMaximumWidth(w)
        self.setMinimumWidth(w)
        self.picture = None

    def pen(self):
        if self._pen is None:
            return fn.mkPen(getConfigOption('foreground'))
        return fn.mkPen(self._pen)

    def setPen(self, *args, **kwargs):
        """
        Set the pen used for drawing text, axes, ticks, and grid lines.
        If no arguments are given, the default foreground color will be used
        (see :func:`setConfigOption <pyqtgraph.setConfigOption>`).
        """
        self.picture = None
        if args or kwargs:
            self._pen = fn.mkPen(*args, **kwargs)
        else:
            self._pen = fn.mkPen(getConfigOption('foreground'))
        self.labelStyle['color'] = self._pen.color().name() #   #RRGGBB
        self._updateLabel()

    def textPen(self):
        if self._textPen is None:
            return fn.mkPen(getConfigOption('foreground'))
        return fn.mkPen(self._textPen)

    def setTextPen(self, *args, **kwargs):
        """
        Set the pen used for drawing text.
        If no arguments are given, the default foreground color will be used.
        """
        self.picture = None
        if args or kwargs:
            self._textPen = fn.mkPen(*args, **kwargs)
        else:
            self._textPen = fn.mkPen(getConfigOption('foreground'))
        self.labelStyle['color'] = self._textPen.color().name() #   #RRGGBB
        self._updateLabel()

    def setScale(self, scale=None):
        """
        Set the value scaling for this axis.

        Setting this value causes the axis to draw ticks and tick labels as if
        the view coordinate system were scaled. By default, the axis scaling is
        1.0.
        """
        # Deprecated usage, kept for backward compatibility
        if scale is None:
            warnings.warn(
                'AxisItem.setScale(None) is deprecated, will be removed in 0.13.0'
                'instead use AxisItem.enableAutoSIPrefix(bool) to enable/disable'
                'SI prefix scaling',                
                DeprecationWarning, stacklevel=2
            )
            scale = 1.0
            self.enableAutoSIPrefix(True)

        if scale != self.scale:
            self.scale = scale
            self._updateLabel()

    def enableAutoSIPrefix(self, enable=True):
        """
        Enable (or disable) automatic SI prefix scaling on this axis.

        When enabled, this feature automatically determines the best SI prefix
        to prepend to the label units, while ensuring that axis values are scaled
        accordingly.

        For example, if the axis spans values from -0.1 to 0.1 and has units set
        to 'V' then the axis would display values -100 to 100
        and the units would appear as 'mV'

        This feature is enabled by default, and is only available when a suffix
        (unit string) is provided to display on the label.
        """
        self.autoSIPrefix = enable
        self.updateAutoSIPrefix()

    def updateAutoSIPrefix(self):
        if self.label.isVisible():
            if self.logMode:
                _range = 10**np.array(self.range)
            else:
                _range = self.range
            (scale, prefix) = fn.siScale(max(abs(_range[0]*self.scale), abs(_range[1]*self.scale)))
            if self.labelUnits == '' and prefix in ['k', 'm']:  ## If we are not showing units, wait until 1e6 before scaling.
                scale = 1.0
                prefix = ''
            self.autoSIPrefixScale = scale
            self.labelUnitPrefix = prefix
        else:
            self.autoSIPrefixScale = 1.0

        self._updateLabel()

    def setRange(self, mn, mx):
        """Set the range of values displayed by the axis.
        Usually this is handled automatically by linking the axis to a ViewBox with :func:`linkToView <pyqtgraph.AxisItem.linkToView>`"""
        if not isfinite(mn) or not isfinite(mx):
            raise Exception("Not setting range to [%s, %s]" % (str(mn), str(mx)))
        self.range = [mn, mx]
        if self.autoSIPrefix:
            # XXX: Will already update once!
            self.updateAutoSIPrefix()
        else:
            self.picture = None
            self.update()

    def linkedView(self):
        """Return the ViewBox this axis is linked to"""
        if self._linkedView is None:
            return None
        else:
            return self._linkedView()

    def _linkToView_internal(self, view):
        # We need this code to be available without override,
        # even though DateAxisItem overrides the user-side linkToView method
        self.unlinkFromView()

        self._linkedView = weakref.ref(view)
        if self.orientation in ['right', 'left']:
            view.sigYRangeChanged.connect(self.linkedViewChanged)
        else:
            view.sigXRangeChanged.connect(self.linkedViewChanged)
        view.sigResized.connect(self.linkedViewChanged)

    def linkToView(self, view):
        """Link this axis to a ViewBox, causing its displayed range to match the visible range of the view."""
        self._linkToView_internal(view)
        
    def unlinkFromView(self):
        """Unlink this axis from a ViewBox."""
        oldView = self.linkedView()
        self._linkedView = None
        if self.orientation in ['right', 'left']:
            if oldView is not None:
                oldView.sigYRangeChanged.disconnect(self.linkedViewChanged)
        else:
            if oldView is not None:
                oldView.sigXRangeChanged.disconnect(self.linkedViewChanged)

        if oldView is not None:
            oldView.sigResized.disconnect(self.linkedViewChanged)

    def linkedViewChanged(self, view, newRange=None):
        if self.orientation in ['right', 'left']:
            if newRange is None:
                newRange = view.viewRange()[1]
            if view.yInverted():
                self.setRange(*newRange[::-1])
            else:
                self.setRange(*newRange)
        else:
            if newRange is None:
                newRange = view.viewRange()[0]
            if view.xInverted():
                self.setRange(*newRange[::-1])
            else:
                self.setRange(*newRange)

    def boundingRect(self):
        linkedView = self.linkedView()
        if linkedView is None or self.grid is False:
            rect = self.mapRectFromParent(self.geometry())
            ## extend rect if ticks go in negative direction
            ## also extend to account for text that flows past the edges
            tl = self.style['tickLength']
            if self.orientation == 'left':
                rect = rect.adjusted(0, -15, -min(0,tl), 15)
            elif self.orientation == 'right':
                rect = rect.adjusted(min(0,tl), -15, 0, 15)
            elif self.orientation == 'top':
                rect = rect.adjusted(-15, 0, 15, -min(0,tl))
            elif self.orientation == 'bottom':
                rect = rect.adjusted(-15, min(0,tl), 15, 0)
            return rect
        else:
            return self.mapRectFromParent(self.geometry()) | linkedView.mapRectToItem(self, linkedView.boundingRect())

    def paint(self, p, opt, widget):
        profiler = debug.Profiler()
        if self.picture is None:
            try:
                picture = QtGui.QPicture()
                painter = QtGui.QPainter(picture)
                if self.style["tickFont"]:
                    painter.setFont(self.style["tickFont"])
                specs = self.generateDrawSpecs(painter)
                profiler('generate specs')
                if specs is not None:
                    self.drawPicture(painter, *specs)
                    profiler('draw picture')
            finally:
                painter.end()
            self.picture = picture
        #p.setRenderHint(p.RenderHint.Antialiasing, False)   ## Sometimes we get a segfault here ???
        #p.setRenderHint(p.RenderHint.TextAntialiasing, True)
        self.picture.play(p)

    def setTicks(self, ticks):
        """Explicitly determine which ticks to display.
        This overrides the behavior specified by tickSpacing(), tickValues(), and tickStrings()
        The format for *ticks* looks like::

            [
                [ (majorTickValue1, majorTickString1), (majorTickValue2, majorTickString2), ... ],
                [ (minorTickValue1, minorTickString1), (minorTickValue2, minorTickString2), ... ],
                ...
            ]

        If *ticks* is None, then the default tick system will be used instead.
        """
        self._tickLevels = ticks
        self.picture = None
        self.update()

    def setTickSpacing(self, major=None, minor=None, levels=None):
        """
        Explicitly determine the spacing of major and minor ticks. This
        overrides the default behavior of the tickSpacing method, and disables
        the effect of setTicks(). Arguments may be either *major* and *minor*,
        or *levels* which is a list of (spacing, offset) tuples for each
        tick level desired.

        If no arguments are given, then the default behavior of tickSpacing
        is enabled.

        Examples::

            # two levels, all offsets = 0
            axis.setTickSpacing(5, 1)
            # three levels, all offsets = 0
            axis.setTickSpacing([(3, 0), (1, 0), (0.25, 0)])
            # reset to default
            axis.setTickSpacing()
        """

        if levels is None:
            if major is None:
                levels = None
            else:
                levels = [(major, 0), (minor, 0)]
        self._tickSpacing = levels
        self.picture = None
        self.update()

    def tickSpacing(self, minVal, maxVal, size):
        """Return values describing the desired spacing and offset of ticks.

        This method is called whenever the axis needs to be redrawn and is a
        good method to override in subclasses that require control over tick locations.

        The return value must be a list of tuples, one for each set of ticks::

            [
                (major tick spacing, offset),
                (minor tick spacing, offset),
                (sub-minor tick spacing, offset),
                ...
            ]
        """
        # First check for override tick spacing
        if self._tickSpacing is not None:
            return self._tickSpacing

        dif = abs(maxVal - minVal)
        if dif == 0:
            return []

        ## decide optimal minor tick spacing in pixels (this is just aesthetics)
        optimalTickCount = max(2., log(size))

        ## optimal minor tick spacing
        optimalSpacing = dif / optimalTickCount

        ## the largest power-of-10 spacing which is smaller than optimal
        p10unit = 10 ** floor(log10(optimalSpacing))

        ## Determine major/minor tick spacings which flank the optimal spacing.
        intervals = np.array([1., 2., 10., 20., 100.]) * p10unit
        minorIndex = 0
        while intervals[minorIndex+1] <= optimalSpacing:
            minorIndex += 1

        levels = [
            (intervals[minorIndex+2], 0),
            (intervals[minorIndex+1], 0),
            #(intervals[minorIndex], 0)    ## Pretty, but eats up CPU
        ]

        if self.style['maxTickLevel'] >= 2:
            ## decide whether to include the last level of ticks
            minSpacing = min(size / 20., 30.)
            maxTickCount = size / minSpacing
            if dif / intervals[minorIndex] <= maxTickCount:
                levels.append((intervals[minorIndex], 0))
         
        return levels
        
        ##### This does not work -- switching between 2/5 confuses the automatic text-level-selection
        ### Determine major/minor tick spacings which flank the optimal spacing.
        #intervals = np.array([1., 2., 5., 10., 20., 50., 100.]) * p10unit
        #minorIndex = 0
        #while intervals[minorIndex+1] <= optimalSpacing:
            #minorIndex += 1

        ### make sure we never see 5 and 2 at the same time
        #intIndexes = [
            #[0,1,3],
            #[0,2,3],
            #[2,3,4],
            #[3,4,6],
            #[3,5,6],
        #][minorIndex]

        #return [
            #(intervals[intIndexes[2]], 0),
            #(intervals[intIndexes[1]], 0),
            #(intervals[intIndexes[0]], 0)
        #]

    def tickValues(self, minVal, maxVal, size):
        """
        Return the values and spacing of ticks to draw::

            [
                (spacing, [major ticks]),
                (spacing, [minor ticks]),
                ...
            ]

        By default, this method calls tickSpacing to determine the correct tick locations.
        This is a good method to override in subclasses.
        """
        minVal, maxVal = sorted((minVal, maxVal))


        minVal *= self.scale
        maxVal *= self.scale
        #size *= self.scale

        ticks = []
        tickLevels = self.tickSpacing(minVal, maxVal, size)
        allValues = np.array([])
        for i in range(len(tickLevels)):
            spacing, offset = tickLevels[i]

            ## determine starting tick
            start = (ceil((minVal-offset) / spacing) * spacing) + offset

            ## determine number of ticks
            num = int((maxVal-start) / spacing) + 1
            values = (np.arange(num) * spacing + start) / self.scale
            ## remove any ticks that were present in higher levels
            ## we assume here that if the difference between a tick value and a previously seen tick value
            ## is less than spacing/100, then they are 'equal' and we can ignore the new tick.
            values = list(filter(lambda x: np.all(np.abs(allValues-x) > spacing/self.scale*0.01), values))
            allValues = np.concatenate([allValues, values])
            ticks.append((spacing/self.scale, values))

        if self.logMode:
            return self.logTickValues(minVal, maxVal, size, ticks)


        #nticks = []
        #for t in ticks:
            #nvals = []
            #for v in t[1]:
                #nvals.append(v/self.scale)
            #nticks.append((t[0]/self.scale,nvals))
        #ticks = nticks

        return ticks

    def logTickValues(self, minVal, maxVal, size, stdTicks):

        ## start with the tick spacing given by tickValues().
        ## Any level whose spacing is < 1 needs to be converted to log scale

        ticks = []
        for (spacing, t) in stdTicks:
            if spacing >= 1.0:
                ticks.append((spacing, t))

        if len(ticks) < 3:
            v1 = int(floor(minVal))
            v2 = int(ceil(maxVal))
            #major = list(range(v1+1, v2))

            minor = []
            for v in range(v1, v2):
                minor.extend(v + np.log10(np.arange(1, 10)))
            minor = [x for x in minor if x>minVal and x<maxVal]
            ticks.append((None, minor))
        return ticks

    def tickStrings(self, values, scale, spacing):
        """Return the strings that should be placed next to ticks. This method is called
        when redrawing the axis and is a good method to override in subclasses.
        The method is called with a list of tick values, a scaling factor (see below), and the
        spacing between ticks (this is required since, in some instances, there may be only
        one tick and thus no other way to determine the tick spacing)

        The scale argument is used when the axis label is displaying units which may have an SI scaling prefix.
        When determining the text to display, use value*scale to correctly account for this prefix.
        For example, if the axis label's units are set to 'V', then a tick value of 0.001 might
        be accompanied by a scale value of 1000. This indicates that the label is displaying 'mV', and
        thus the tick should display 0.001 * 1000 = 1.
        """
        if self.logMode:
            return self.logTickStrings(values, scale, spacing)

        places = max(0, ceil(-log10(spacing*scale)))
        strings = []
        for v in values:
            vs = v * scale
            if abs(vs) < .001 or abs(vs) >= 10000:
                vstr = "%g" % vs
            else:
                vstr = ("%%0.%df" % places) % vs
            strings.append(vstr)
        return strings

    def logTickStrings(self, values, scale, spacing):
        estrings = ["%0.1g"%x for x in 10 ** np.array(values).astype(float) * np.array(scale)]
        convdict = {"0": "⁰",
                    "1": "¹",
                    "2": "²",
                    "3": "³",
                    "4": "⁴",
                    "5": "⁵",
                    "6": "⁶",
                    "7": "⁷",
                    "8": "⁸",
                    "9": "⁹",
                    }
        dstrings = []
        for e in estrings:
            if e.count("e"):
                v, p = e.split("e")
                sign = "⁻" if p[0] == "-" else ""
                pot = "".join([convdict[pp] for pp in p[1:].lstrip("0")])
                if v == "1":
                    v = ""
                else:
                    v = v + "·"
                dstrings.append(v + "10" + sign + pot)
            else:
                dstrings.append(e)
        return dstrings

    def generateDrawSpecs(self, p):
        """
        Calls tickValues() and tickStrings() to determine where and how ticks should
        be drawn, then generates from this a set of drawing commands to be
        interpreted by drawPicture().
        """
        profiler = debug.Profiler()
        if self.style['tickFont'] is not None:
            p.setFont(self.style['tickFont'])
        bounds = self.mapRectFromParent(self.geometry())

        linkedView = self.linkedView()
        if linkedView is None or self.grid is False:
            tickBounds = bounds
        else:
            tickBounds = linkedView.mapRectToItem(self, linkedView.boundingRect())

        if self.orientation == 'left':
            span = (bounds.topRight(), bounds.bottomRight())
            tickStart = tickBounds.right()
            tickStop = bounds.right()
            tickDir = -1
            axis = 0
        elif self.orientation == 'right':
            span = (bounds.topLeft(), bounds.bottomLeft())
            tickStart = tickBounds.left()
            tickStop = bounds.left()
            tickDir = 1
            axis = 0
        elif self.orientation == 'top':
            span = (bounds.bottomLeft(), bounds.bottomRight())
            tickStart = tickBounds.bottom()
            tickStop = bounds.bottom()
            tickDir = -1
            axis = 1
        elif self.orientation == 'bottom':
            span = (bounds.topLeft(), bounds.topRight())
            tickStart = tickBounds.top()
            tickStop = bounds.top()
            tickDir = 1
            axis = 1
        else:
            raise ValueError("self.orientation must be in ('left', 'right', 'top', 'bottom')")
        #print tickStart, tickStop, span

        ## determine size of this item in pixels
        points = list(map(self.mapToDevice, span))
        if None in points:
            return
        lengthInPixels = Point(points[1] - points[0]).length()
        if lengthInPixels == 0:
            return

        # Determine major / minor / subminor axis ticks
        if self._tickLevels is None:
            tickLevels = self.tickValues(self.range[0], self.range[1], lengthInPixels)
            tickStrings = None
        else:
            ## parse self.tickLevels into the formats returned by tickLevels() and tickStrings()
            tickLevels = []
            tickStrings = []
            for level in self._tickLevels:
                values = []
                strings = []
                tickLevels.append((None, values))
                tickStrings.append(strings)
                for val, strn in level:
                    values.append(val)
                    strings.append(strn)

        ## determine mapping between tick values and local coordinates
        dif = self.range[1] - self.range[0]
        if dif == 0:
            xScale = 1
            offset = 0
        else:
            if axis == 0:
                xScale = -bounds.height() / dif
                offset = self.range[0] * xScale - bounds.height()
            else:
                xScale = bounds.width() / dif
                offset = self.range[0] * xScale

        xRange = [x * xScale - offset for x in self.range]
        xMin = min(xRange)
        xMax = max(xRange)

        profiler('init')

        tickPositions = [] # remembers positions of previously drawn ticks

        ## compute coordinates to draw ticks
        ## draw three different intervals, long ticks first
        tickSpecs = []
        for i in range(len(tickLevels)):
            tickPositions.append([])
            ticks = tickLevels[i][1]

            ## length of tick
            tickLength = self.style['tickLength'] / ((i*0.5)+1.0)
                
            lineAlpha = self.style["tickAlpha"]
            if lineAlpha is None:
                lineAlpha = 255 / (i+1)
                if self.grid is not False:
                    lineAlpha *= self.grid/255. * fn.clip_scalar((0.05  * lengthInPixels / (len(ticks)+1)), 0., 1.)
            elif isinstance(lineAlpha, float):
                lineAlpha *= 255
                lineAlpha = max(0, int(round(lineAlpha)))
                lineAlpha = min(255, int(round(lineAlpha)))
            elif isinstance(lineAlpha, int):
                if (lineAlpha > 255) or (lineAlpha < 0):
                    raise ValueError("lineAlpha should be [0..255]")
            else:
                raise TypeError("Line Alpha should be of type None, float or int")

            for v in ticks:
                ## determine actual position to draw this tick
                x = (v * xScale) - offset
                if x < xMin or x > xMax:  ## last check to make sure no out-of-bounds ticks are drawn
                    tickPositions[i].append(None)
                    continue
                tickPositions[i].append(x)

                p1 = [x, x]
                p2 = [x, x]
                p1[axis] = tickStart
                p2[axis] = tickStop
                if self.grid is False:
                    p2[axis] += tickLength*tickDir
                tickPen = self.pen()
                color = tickPen.color()
                color.setAlpha(int(lineAlpha))
                tickPen.setColor(color)
                tickSpecs.append((tickPen, Point(p1), Point(p2)))
        profiler('compute ticks')


        if self.style['stopAxisAtTick'][0] is True:
            minTickPosition = min(map(min, tickPositions))
            if axis == 0:
                stop = max(span[0].y(), minTickPosition)
                span[0].setY(stop)
            else:
                stop = max(span[0].x(), minTickPosition)
                span[0].setX(stop)
        if self.style['stopAxisAtTick'][1] is True:
            maxTickPosition = max(map(max, tickPositions))
            if axis == 0:
                stop = min(span[1].y(), maxTickPosition)
                span[1].setY(stop)
            else:
                stop = min(span[1].x(), maxTickPosition)
                span[1].setX(stop)
        axisSpec = (self.pen(), span[0], span[1])


        textOffset = self.style['tickTextOffset'][axis]  ## spacing between axis and text
        #if self.style['autoExpandTextSpace'] is True:
            #textWidth = self.textWidth
            #textHeight = self.textHeight
        #else:
            #textWidth = self.style['tickTextWidth'] ## space allocated for horizontal text
            #textHeight = self.style['tickTextHeight'] ## space allocated for horizontal text

        textSize2 = 0
        lastTextSize2 = 0
        textRects = []
        textSpecs = []  ## list of draw

        # If values are hidden, return early
        if not self.style['showValues']:
            return (axisSpec, tickSpecs, textSpecs)

        for i in range(min(len(tickLevels), self.style['maxTextLevel']+1)):
            ## Get the list of strings to display for this level
            if tickStrings is None:
                spacing, values = tickLevels[i]
                strings = self.tickStrings(values, self.autoSIPrefixScale * self.scale, spacing)
            else:
                strings = tickStrings[i]

            if len(strings) == 0:
                continue

            ## ignore strings belonging to ticks that were previously ignored
            for j in range(len(strings)):
                if tickPositions[i][j] is None:
                    strings[j] = None

            ## Measure density of text; decide whether to draw this level
            rects = []
            for s in strings:
                if s is None:
                    rects.append(None)
                else:
                    br = p.boundingRect(QtCore.QRectF(0, 0, 100, 100), QtCore.Qt.AlignmentFlag.AlignCenter, s)
                    ## boundingRect is usually just a bit too large
                    ## (but this probably depends on per-font metrics?)
                    br.setHeight(br.height() * 0.8)

                    rects.append(br)
                    textRects.append(rects[-1])

            if len(textRects) > 0:
                ## measure all text, make sure there's enough room
                if axis == 0:
                    textSize = np.sum([r.height() for r in textRects])
                    textSize2 = np.max([r.width() for r in textRects])
                else:
                    textSize = np.sum([r.width() for r in textRects])
                    textSize2 = np.max([r.height() for r in textRects])
            else:
                textSize = 0
                textSize2 = 0

            if i > 0:  ## always draw top level
                ## If the strings are too crowded, stop drawing text now.
                ## We use three different crowding limits based on the number
                ## of texts drawn so far.
                textFillRatio = float(textSize) / lengthInPixels
                finished = False
                for nTexts, limit in self.style['textFillLimits']:
                    if len(textSpecs) >= nTexts and textFillRatio >= limit:
                        finished = True
                        break
                if finished:
                    break
            
            lastTextSize2 = textSize2

            #spacing, values = tickLevels[best]
            #strings = self.tickStrings(values, self.scale, spacing)
            # Determine exactly where tick text should be drawn
            for j in range(len(strings)):
                vstr = strings[j]
                if vstr is None: ## this tick was ignored because it is out of bounds
                    continue
                x = tickPositions[i][j]
                #textRect = p.boundingRect(QtCore.QRectF(0, 0, 100, 100), QtCore.Qt.AlignmentFlag.AlignCenter, vstr)
                textRect = rects[j]
                height = textRect.height()
                width = textRect.width()
                #self.textHeight = height
                offset = max(0,self.style['tickLength']) + textOffset

                if self.orientation == 'left':
                    alignFlags = QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignVCenter
                    rect = QtCore.QRectF(tickStop-offset-width, x-(height/2), width, height)
                elif self.orientation == 'right':
                    alignFlags = QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter
                    rect = QtCore.QRectF(tickStop+offset, x-(height/2), width, height)
                elif self.orientation == 'top':
                    alignFlags = QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignBottom
                    rect = QtCore.QRectF(x-width/2., tickStop-offset-height, width, height)
                elif self.orientation == 'bottom':
                    alignFlags = QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop
                    rect = QtCore.QRectF(x-width/2., tickStop+offset, width, height)

                textFlags = alignFlags | QtCore.Qt.TextFlag.TextDontClip    
                #p.setPen(self.pen())
                #p.drawText(rect, textFlags, vstr)
                textSpecs.append((rect, textFlags, vstr))
        profiler('compute text')

        ## update max text size if needed.
        self._updateMaxTextSize(lastTextSize2)

        return (axisSpec, tickSpecs, textSpecs)

    def drawPicture(self, p, axisSpec, tickSpecs, textSpecs):
        profiler = debug.Profiler()

        p.setRenderHint(p.RenderHint.Antialiasing, False)
        p.setRenderHint(p.RenderHint.TextAntialiasing, True)

        ## draw long line along axis
        pen, p1, p2 = axisSpec
        p.setPen(pen)
        p.drawLine(p1, p2)
        # p.translate(0.5,0)  ## resolves some damn pixel ambiguity

        ## draw ticks
        for pen, p1, p2 in tickSpecs:
            p.setPen(pen)
            p.drawLine(p1, p2)
        profiler('draw ticks')

        # Draw all text
        if self.style['tickFont'] is not None:
            p.setFont(self.style['tickFont'])
        p.setPen(self.textPen())
        bounding = self.boundingRect().toAlignedRect()
        p.setClipRect(bounding)
        for rect, flags, text in textSpecs:
            p.drawText(rect, int(flags), text)

        profiler('draw text')

    def show(self):
        GraphicsWidget.show(self)
        if self.orientation in ['left', 'right']:
            self._updateWidth()
        else:
            self._updateHeight()

    def hide(self):
        GraphicsWidget.hide(self)
        if self.orientation in ['left', 'right']:
            self._updateWidth()
        else:
            self._updateHeight()

    def wheelEvent(self, event):
        lv = self.linkedView()
        if lv is None:
            return
        # Did the event occur inside the linked ViewBox (and not over the axis iteself)?
        if lv.sceneBoundingRect().contains(event.scenePos()):
            event.ignore()
            return
        else:
            # pass event to linked viewbox with appropriate single axis zoom parameter
            if self.orientation in ['left', 'right']:
                lv.wheelEvent(event, axis=1)
            else:
                lv.wheelEvent(event, axis=0)
        event.accept()

    def mouseDragEvent(self, event):
        lv = self.linkedView()
        if lv is None:
            return
        # Did the mouse down event occur inside the linked ViewBox (and not the axis)?
        if lv.sceneBoundingRect().contains(event.buttonDownScenePos()):
            event.ignore()
            return
        # otherwise pass event to linked viewbox with appropriate single axis parameter
        if self.orientation in ['left', 'right']:
            return lv.mouseDragEvent(event, axis=1)
        else:
            return lv.mouseDragEvent(event, axis=0)

    def mouseClickEvent(self, event):
        lv = self.linkedView()
        if lv is None:
            return
        return lv.mouseClickEvent(event)
