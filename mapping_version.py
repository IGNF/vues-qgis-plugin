from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QSizePolicy,QFrame,QFileDialog,QDialog

# QT6
try :
    # Dialog = Qt.WindowType.Dialog
    # WindowCloseButtonHint = Qt.WindowType.WindowCloseButtonHint
    # WindowTitleHint = Qt.WindowType.WindowTitleHint
    # WindowStaysOnTopHint = Qt.WindowType.WindowStaysOnTopHint
    Checked = Qt.CheckState.Checked
    Unchecked = Qt.CheckState.Unchecked
    # ItemIsEnabled = Qt.ItemFlag.ItemIsEnabled
    # ItemIsUserCheckable = Qt.ItemFlag.ItemIsUserCheckable
    # MatchExactly = Qt.MatchFlag.MatchExactly
    # RightSide = QTabBar.ButtonPosition.RightSide
    # LeftSide = QTabBar.ButtonPosition.LeftSide
    # Warning = QMessageBox.Icon.Warning
    # YesRole = QMessageBox.ButtonRole.YesRole
    # AcceptRole = QMessageBox.ButtonRole.AcceptRole
    ScrollBarAlwaysOff = Qt.ScrollBarPolicy.ScrollBarAlwaysOff
    ScrollBarAsNeeded = Qt.ScrollBarPolicy.ScrollBarAsNeeded
    CustomContextMenu = Qt.ContextMenuPolicy.CustomContextMenu
    Expanding = QSizePolicy.Policy.Expanding
    Fixed = QSizePolicy.Policy.Fixed
    MinimumExpanding = QSizePolicy.Policy.MinimumExpanding
    VLine = QFrame.Shape.VLine
    Directory = QFileDialog.FileMode.Directory
    ShowDirsOnly = QFileDialog.Option.ShowDirsOnly
    DontResolveSymlinks = QFileDialog.Option.DontResolveSymlinks
    Accept = QFileDialog.DialogLabel.Accept
    Accepted = QFileDialog.DialogCode.Accepted

# QT5
except :
    # Dialog = Qt.Dialog
    # WindowCloseButtonHint = Qt.WindowCloseButtonHint
    # WindowTitleHint = Qt.WindowTitleHint
    # WindowStaysOnTopHint = Qt.WindowStaysOnTopHint
    Checked = Qt.Checked
    Unchecked = Qt.Unchecked
    # ItemIsEnabled = Qt.ItemIsEnabled
    # ItemIsUserCheckable = Qt.ItemIsUserCheckable
    # MatchExactly = Qt.MatchFlag.MatchExactly
    # RightSide = QTabBar.RightSide
    # LeftSide = QTabBar.LeftSide
    # Warning = QMessageBox.Warning
    # YesRole = QMessageBox.YesRole
    # AcceptRole = QMessageBox.AcceptRole
    ScrollBarAlwaysOff = Qt.ScrollBarAlwaysOff
    ScrollBarAsNeeded = Qt.ScrollBarAsNeeded
    CustomContextMenu = Qt.CustomContextMenu
    Expanding = Qt.Expanding
    Fixed = Qt.Fixed
    MinimumExpanding = Qt.MinimumExpanding
    VLine = Qt.VLine
    Directory = Qt.Directory
    ShowDirsOnly = Qt.ShowDirsOnly
    DontResolveSymlinks = Qt.DontResolveSymlinks
    Accept = QFileDialog.Accept
    Accepted = QDialog.Accepted