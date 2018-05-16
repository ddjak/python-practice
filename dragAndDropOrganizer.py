import wx, os, shutil
 
########################################################################
class MyFileDropTarget(wx.FileDropTarget):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, window):
        """Constructor"""
        wx.FileDropTarget.__init__(self)
        self.window = window
 
    #----------------------------------------------------------------------
    def OnDropFiles(self, x, y, filenames):
        """
        When files are dropped, write where they were dropped and then
        the file paths themselves
        """

        self.window.SetInsertionPointEnd()
        self.window.updateText("\n%d file(s) dropped at %d,%d:\n" %
                              (len(filenames), x, y))
        directoryName = input('Input part number:')
        print(directoryName)
        for filepath in filenames:
            count = 0
            self.window.updateText(filepath + '\n')  
            '''print('-+-')
            print(os.path.exists('T:\\TEST\\' + os.path.basename(filepath)[:-4]))
            print('-+-')'''
            newDirectory = '' + directoryName ### Insert your custom path here
            #print(os.path.exists(newDirectory))
            if not os.path.exists(newDirectory):
                os.makedirs(newDirectory)
                #print(str(filenames) + '------------')
                #print(str(filepath) + '++++++++++++')
                shutil.copy(filenames[0], newDirectory)
            else:
                shutil.copy(filenames[0], newDirectory)#+ '-' + str(count) + '.pdf'
 
########################################################################
class DnDPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
 
        file_drop_target = MyFileDropTarget(self)
        lbl = wx.StaticText(self, label="Drag some files here:")
        self.fileTextCtrl = wx.TextCtrl(self,
                                        style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY)
        self.fileTextCtrl.SetDropTarget(file_drop_target)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(self.fileTextCtrl, 1, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def SetInsertionPointEnd(self):
        """
        Put insertion point at end of text control to prevent overwriting
        """
        self.fileTextCtrl.SetInsertionPointEnd()
 
    #----------------------------------------------------------------------
    def updateText(self, text):
        """
        Write text to the text control
        """
        self.fileTextCtrl.WriteText(text)
 
########################################################################
class DnDFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Drag and Drop File Organizer")
        panel = DnDPanel(self)
        self.Show()
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = DnDFrame()
    app.MainLoop()