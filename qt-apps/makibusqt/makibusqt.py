import info
from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets['master'] = 'https://github.com/Inokinoki/makibus-qt.git'

        self.defaultTarget = 'master'
        self.description = "IBus on macOS based on Qt"
        self.displayName = "Makibus"

    def setDependencies(self):
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["qt-libs/ibusqt"] = None

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
