import wx, os, shutil, datetime


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
        listForDate = []
        today = datetime.date.today()
        listForDate.append(today)
        print('This is a new day : ' + str(listForDate[0])) 
         
        self.window.SetInsertionPointEnd()
        self.window.updateText("\n%d file(s) dropped at %d,%d:\n" %
                              (len(filenames), x, y))
        

        directoryName = input('Input part number:')
        print('Directory for ' + directoryName + ' is being created')

        count = 0
        fileExtension = '.xls' ###Insert extension that your file will need
        for filepath in filenames:
            #filepath is auto-detecting. Shows where file came from, ending with individual filename
            self.window.updateText(filepath + '\n')  

            #storing variable for new directory 
            newDirectory = '' + directoryName ### Insert your custom path here
            
            #if new folder does not exist 
            if not os.path.exists(newDirectory):
                #make folder called newDirectory
                os.makedirs(newDirectory) 
                fileName = str(directoryName) + ' Meeting ' + str(listForDate[0]) ###Format your file name
                shutil.copy(filepath, os.path.dirname(newDirectory) + "\\" + directoryName + "\\" + fileName + fileExtension)
                
                os.rename(filepath, str(fileName) + fileExtension)
                os.rename(os.path.dirname(newDirectory) + "\\" + fileName + fileExtension, fileName)
            #else:
                #shutil.copy(filenames[0], newDirectory)#+ '-' + str(count) + '.pdf'
 
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
        wx.Frame.__init__(self, parent=None, title="Drag and Drop Your Files")
        panel = DnDPanel(self)
        self.Show()
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = DnDFrame()
    app.MainLoop()