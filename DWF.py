from pyrevit import revit, DB
from pyrevit import script
from pyrevit import forms
import os

def export_dwf():

    doc = revit.doc

    options = DB.DWFExportOptions()
    
    dwf_file_path = forms.save_file(title="Save DWF File", filename="exported_model.dwf", file_filter="DWF Files (*.dwf)|*.dwf")

    if dwf_file_path:
        doc.Export(dwf_file_path, "DWF", options)

        forms.alert("Exportação feita!", exitscript=True)

    try:
        import shutil

        download_folder = os.path.expanduser("~/Downloads")
        shutil.move(dwf_file_path, os.path.join(download_folder, "Arquivo.dwf"))
        script.get_output().print_stdout("Arquivo movido para a área de download.")
    except Exception as e:
        script.get_output().print_stderr("Erro ao mover o arquivo: {}".format(str(e)))


button = forms.CommandButton(label="Export DWF", command=export_dwf)

forms.toolbar("pyRevit Tools", items=[button])
