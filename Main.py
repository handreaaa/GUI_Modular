from WindowMaster import *
from COMsClass import *
from MasterData import DataMaster
_RootMain = RootGUI()
_DataMaster = DataMaster()
_SerialInit = SerialCtrl()
Comunication = ComGui(_RootMain.root,_SerialInit,_DataMaster)
_RootMain.root.mainloop()