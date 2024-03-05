# Importar las librerías necesarias
import pydicom
import plistlib
import tarfile

# Definir el nombre del archivo .inv3 local
filename = "proyecto.inv3"

# Crear un objeto de archivo tar con tarfile
tar = tarfile.open(filename)

# Extraer el contenido del archivo tar en una carpeta temporal
tar.extractall(path="temp")

# Cerrar el objeto de archivo tar
tar.close()

# Obtener el nombre de la carpeta que contiene el archivo main.plist
folder = tar.getnames()[0]

# Leer el archivo main.plist con plistlib
with open(f"temp/{folder}/main.plist", "rb") as f:
    plist = plistlib.load(f)

# Obtener el primer diccionario de la lista del archivo main.plist
dicom_dict = plist[0]

# Obtener el nombre del archivo DICOM que corresponde al primer diccionario
dicom_file = dicom_dict["file"]

# Leer el archivo DICOM con pydicom
dataset = pydicom.dcmread(f"temp/{folder}/{dicom_file}")

# Mostrar algunos atributos del dataset
print("Nombre del paciente:", dataset.PatientName)
print("Modalidad:", dataset.Modality)
print("Dimensiones:", dataset.Rows, "x", dataset.Columns, "x", dataset.SamplesPerPixel)

