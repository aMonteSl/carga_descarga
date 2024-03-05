# Importar las librerías necesarias
import pydicom
import plistlib
import tarfile
import tqdm

# Definir el nombre del archivo .inv3 local
filename = "proyecto.inv3"

# Crear una lista vacía para almacenar los diccionarios de los archivos DICOM
plist = []

# Crear una carpeta temporal para guardar los archivos DICOM
os.mkdir("temp")

# Iterar sobre los nombres de los archivos DICOM que quieres guardar
for dicom_file in ["CT_small.dcm", "MR_small.dcm", "PT_small.dcm"]:
    # Leer el archivo DICOM con pydicom
    dataset = pydicom.dcmread(dicom_file)
    # Crear un diccionario con los datos del archivo DICOM
    dicom_dict = {"file": dicom_file, "patient_name": dataset.PatientName, "modality": dataset.Modality, "rows": dataset.Rows, "columns": dataset.Columns, "samples_per_pixel": dataset.SamplesPerPixel}
    # Añadir el diccionario a la lista
    plist.append(dicom_dict)
    # Copiar el archivo DICOM a la carpeta temporal
    shutil.copy(dicom_file, f"temp/{dicom_file}")

# Crear un archivo main.plist con plistlib
with open("temp/main.plist", "wb") as f:
    plistlib.dump(plist, f)

# Crear un objeto de archivo tar con tarfile
tar = tarfile.open(filename, "w:gz")

# Añadir la carpeta temporal al archivo tar
tar.add("temp")

# Cerrar el objeto de archivo tar
tar.close()

# Eliminar la carpeta temporal
shutil.rmtree("temp")

# Obtener el tamaño del archivo .inv3 en bytes
size = os.path.getsize(filename)

# Mostrar una barra de progreso mientras se guarda el archivo
progress = tqdm.tqdm(desc="Guardando archivo .inv3", total=size, unit="B", unit_scale=True)

# Simular un proceso de guardado
for i in range(size):
    # Actualizar la barra de progreso
    progress.update(1)

# Cerrar la barra de progreso
progress.close()

