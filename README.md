# Ball-screensaver-using-tkinter
This is a screensaver made with python using the tkinter library. It contains balls moving around the screen.
Para guardar como protector de pantalla ejecutable (sólo para Windows):
1) Guardar el script con extensión .py
2) Abrir la consola, terminal de comandos o cmd
3) Instalar la librería pyinstaller con el comando: pip install pyinstaller
4) Moverse al directorio donde se encuentra el script con el comando: cd \aquí la ruta o path
5) Ejecutar el siguiente comando: pyinstaller --windowed --onefile script.py
6) Moverse al directorio dist con el siguiente comando: cd dist
7) Crear una copia del archivo con extensión .exe pero que tenga extensión .scr: copy script.exe script.scr
8) Ahora ya trabajando nuevamente con el explorador de archivos copiar o mover el archivo script.scr al directorio C:\windows\system32\
9) Abrir la configuración de pantalla de la computadora y colocar el nuevo protector de pantalla como protector actual
