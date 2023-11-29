from pyrevit import revit, DB
from pyrevit import script
from pyrevit import forms
import os

def export_dwg():

    doc = revit.doc

    options = DB.DWGExportOptions()
    
    dwg_file_path = forms.save_file(title="Save DWG File", filename="exported_model.dwg", file_filter="DWG Files (*.dwg)|*.dwg")

    if dwg_file_path:
        doc.Export(dwg_file_path, "DWG", options)

        forms.alert("Exportação feita!", exitscript=True)

    try:
        import shutil

        download_folder = os.path.expanduser("~/Downloads")
        shutil.move(dwg_file_path, os.path.join(download_folder, "Arquivo.dwg"))
        script.get_output().print_stdout("Arquivo movido para a área de download.")
    except Exception as e:
        script.get_output().print_stderr("Erro ao mover o arquivo: {}".format(str(e)))


button = forms.CommandButton(label="Export DWG", command=export_dwg)

forms.toolbar("pyRevit Tools", items=[button])
