import sublime, sublime_plugin, os, stat

class PreSaveCommand(sublime_plugin.EventListener):
   def on_pre_save(self, view):
      myFile = view.file_name()
      fileAtt = os.stat(view.file_name())[0]
      if view.is_dirty():
         if (not fileAtt & stat.S_IWRITE):
            if(sublime.ok_cancel_dialog('The file is Read-Only. Overwrite?', 'Overwrite!')):
               os.chmod(myFile, stat.S_IWRITE)