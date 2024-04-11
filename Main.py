from WindowMaster import *
from COMsClass import *
from MasterData import DataMaster

_DataMaster = DataMaster()
_SerialInit = SerialCtrl()
_RootMain = RootGUI(_SerialInit,_DataMaster)
Comunication = ComGui(_RootMain.root,_SerialInit,_DataMaster)
_RootMain.root.mainloop()