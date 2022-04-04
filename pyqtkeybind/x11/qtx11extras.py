import ctypes
import os
from pathlib import Path

import qtpy
from qtpy.QtCore import QLibraryInfo

name_connection_func = "_ZN8QX11Info10connectionEv"
name_approotwindow_func = "_ZN8QX11Info13appRootWindowEi"


if qtpy.API_NAME in ("PyQt6", "PySide6"):
    qtpath = Path(QLibraryInfo.path(QLibraryInfo.PrefixPath)).resolve()
    lib_path = os.fspath(qtpath / "lib" / "libQt6Gui.so.6")
elif qtpy.API_NAME in ("PyQt5", "PySide2"):
    qtpath = Path(QLibraryInfo.location(QLibraryInfo.PrefixPath)).resolve()
    lib_path = os.fspath(qtpath / "lib" / "libQt5X11Extras.so.5")


qtlib = ctypes.CDLL(lib_path)

_qx11info_connection = qtlib._ZN8QX11Info10connectionEv
_qx11info_connection.restype = ctypes.c_long

_qx11info_qapprootwindow = qtlib._ZN8QX11Info13appRootWindowEi
_qx11info_qapprootwindow.restype = ctypes.c_long
_qx11info_qapprootwindow.argtypes = [ctypes.c_int]


class QX11Info:
    @staticmethod
    def connection():
        return _qx11info_connection()

    @staticmethod
    def appRootWindow(screen=-1):
        return _qx11info_qapprootwindow(screen)
