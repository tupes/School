import wx
from PySide import QtGui

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "hey")
frame.Show(True)

app.MainLoop()

print 'done'