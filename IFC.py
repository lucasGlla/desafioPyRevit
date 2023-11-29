from pyrevit import revit, DB
from pyrevit import script
from pyrevit import forms
import os

def export_ifc():

    doc = revit.doc

    options = DB.IFCExportOptions()
    
    ifc_file_path = forms.save_file(title="Save IFC File", filename="exported_model.ifc", file_filter="IFC Files (*.ifc)|*.ifc")

    if ifc_file_path:
    
        doc.Export(ifc_file_path, "IFC", options)

        forms.alert("Exportação feita!", exitscript=True)
    
    try:
        import shutil

        download_folder = os.path.expanduser("~/Downloads")
        shutil.move(ifc_file_path, os.path.join(download_folder, "Arquivo.ifc"))
        script.get_output().print_stdout("Arquivo movido para a área de download.")
    except Exception as e:
        script.get_output().print_stderr("Erro ao mover o arquivo: {}".format(str(e)))

button = forms.CommandButton(label="Export IFC", command=export_ifc)

forms.toolbar("pyRevit Tools", items=[button])
