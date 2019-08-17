import wx,pygame, pygame.locals as pl
from speech import speak
def dialog(text):
 speak(text)
 while 1:
  for event in pygame.event.get():
   if event.type == pygame.KEYDOWN:
    if event.key == pl.K_RETURN: return
    elif event.key == pl.K_UP or event.key == pl.K_RIGHT or event.key == pl.K_DOWN or event.key == pl.K_LEFT: speak(text)

def text_dialog(title, text):
 wx.MessageBox(text, title, wx.OK)

def question(title, text, parent=None):
 dlg = wx.MessageDialog(parent, text, title, wx.YES_NO | wx.ICON_QUESTION)
 result = dlg.ShowModal()
 dlg.Destroy()
 if result == wx.ID_YES: return 0
 else: return -1

def input_box(parent=None, message='', caption='', default_value=''):
 dlg = wx.TextEntryDialog(parent, caption, message, value=default_value)
 dlg.ShowModal()
 result = dlg.GetValue()
 dlg.Destroy()
 return result

app = wx.App()