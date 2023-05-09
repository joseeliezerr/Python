import os
import datetime
import shutil
import locale

# establecer configuración regional en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# ruta de origen y destino
nombre_usuario = os.getlogin()
ruta_origen = f"C:/Users/{nombre_usuario}/BTT-Writer/automatic_backups"


ruta_destino_raiz = os.path.join(os.path.expanduser('~'), 'Desktop', 'WA', nombre_usuario)

# crea la carpeta de destino si no existe
if not os.path.exists(ruta_destino_raiz):
    os.makedirs(ruta_destino_raiz)

# copia los archivos de origen a destino y los agrupa por fecha
for carpeta_raiz, carpetas, archivos in os.walk(ruta_origen):
    for archivo in archivos:
        ruta_archivo_origen = os.path.join(carpeta_raiz, archivo)
        fecha_creacion = datetime.datetime.fromtimestamp(os.path.getctime(ruta_archivo_origen))
        fecha_creacion_str = fecha_creacion.strftime('%d de %B de %Y')
        ruta_destino_fecha = os.path.join(ruta_destino_raiz, fecha_creacion_str)
        if not os.path.exists(ruta_destino_fecha):
            os.makedirs(ruta_destino_fecha)
        ruta_archivo_destino = os.path.join(ruta_destino_fecha, archivo)
        shutil.copy2(ruta_archivo_origen, ruta_archivo_destino)

# cambia los permisos de la carpeta de destino
os.chmod(ruta_destino_raiz, 0o777)
