# Use_OpenCV
OpenCV + Technologies Smart


[English]

The OpenCV library must be installed.
For Windows https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html.
For MacOs https://docs.opencv.org/master/d0/db2/tutorial_macos_install.html.

To use the main camera of the mobile phone, you must use the free app DroidCam (available on Google Play).
This App provides IP access for the camera, example of this route http://192.168.1.92:4747 (do not forget that it must end with: 4747).

When starting the Phone_Cam.py program, the DroidCam app must be initialized, then it can be closed and the Python or Spyder display screen will continue to output the video in real time with RGB color scale.

The .py has 2 options to view the video in real time, through the main camera of the phone or through the computer camera. This differs in access, which is:
(1) cam=cv.VideoCapture ("http://192.168.1.92:4747") with access from the main camera of the mobile phone.
(2) cam=cv.VideoCapture (0) for the computer camera. Note: the number 0 may vary if you have external cameras connected via USB or network.



[Spanish]

Se debe instalar la librería OpenCV. 
Para Windows https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html.
Para MacOs https://docs.opencv.org/master/d0/db2/tutorial_macos_install.html.

Para el uso de la cámara principal del télefono móvil, se debe hacer uso de la app gratuita DroidCam (disponible en Google Play). 
Esta App proporciona un acceso IP para la cámara, ejemplo de esta ruta http://192.168.1.92:4747 (no olvidar que debe ir finalizado con :4747).

Al iniciar el programa Phone_Cam.py, la app DroidCam debe estar inicializada, luego puede ser cerrado y la pantalla de visualización de Python o Spyder seguirá emitiendo el video en tiempo real con escala de colores RGB.

El .py tiene 2 opciones para visualizar el video en tiempo real, por medio de la cámara principal del teléfono o por la cámara del computador. Esto se diferencia en el acceso, que es:
(1) cam=cv.VideoCapture("http://192.168.1.92:4747") con el acceso de la cámara principal del teléfono móvil.
(2) cam=cv.VideoCapture(0) para la cámara del computador. Nota: el número 0 puede variar en caso de tener cámaras externas conectadas por medio de USB o por red.
