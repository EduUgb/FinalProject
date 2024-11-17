# mi_aplicacion/views.py
from django.http import HttpResponse
from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from .models import Reserv
from email import encoders
import uuid
import os
from django.conf import settings
def inicio(request):
    return HttpResponse("<h1>Bienvenido a mi sitio web en Django</h1>")

def index(request):
    return render(request,  'index.html')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        numero_personas = request.POST.get('numero_personas')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        tipo_reserva = request.POST.get('tipo_reserva')
        notas = request.POST.get('notas')
        acceso = request.POST.get('acceso')


        # Llama a la función para enviar el correo
        enviar_correo(nombre, correo, telefono, numero_personas, fecha, hora, tipo_reserva, notas, acceso)

        #llama la base
        Reserva(nombre, correo, telefono, numero_personas, fecha, hora, tipo_reserva, notas, acceso)

        return HttpResponse("Reservación enviada con éxito")
    return render(request, 'index.html')


def enviar_correo(nombre, correo, telefono, numero_personas, fecha, hora, tipo_reserva, notas, acceso):
    # Configura el servidor SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'carloseduardog310@gmail.com'  #correo principal
    smtp_password = 'pnfx ptkv qwir omvq'      #contraseña a utilizar (contraseña de apps)
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # Crea el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = smtp_user
    mensaje['To'] = correo  # El correo del usuario
    mensaje['Subject'] = 'Confirmación de Reservación'

    # Crea el cuerpo del mensaje
    cuerpo_mensaje = f"""
    Hola {nombre},

    Gracias por su reservación. Aquí están los detalles:

    - Nombre: {nombre}
    - Correo: {correo}
    - Teléfono: {telefono}
    - Número de Personas: {numero_personas}
    - Fecha: {fecha}
    - Hora: {hora}
    - Tipo de Reserva: {tipo_reserva}
    - Notas: {notas}
    - Acceso: {acceso}

    Saludos
    """
    mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

    # Abrimos el archivo que vamos a adjuntar
    ruta_adjunto = os.path.join(settings.MEDIA_ROOT, 'Github.png')
    qr = open(ruta_adjunto, 'rb')


    parte = MIMEBase('application', 'octet-stream')
    parte.set_payload(qr.read())
    encoders.encode_base64(parte)
    parte.add_header(
        'Content-Disposition',
        f'attachment; filename={os.path.basename(ruta_adjunto)}'
    )
    mensaje.attach(parte)


    # Envía el correo
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Activa la encriptación
            server.login(smtp_user, smtp_password)  # Inicia sesión
            server.sendmail(mensaje['From'], mensaje['To'], mensaje.as_string())  # Envía el correo
            sesion_smtp.quit()
        print("Correo enviado con éxito")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")




def Reserva(nombre, correo, telefono, numero_personas, fecha, hora, tipo_reserva, notas, acceso):
     nueva_reserva = Reserv(
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            numPersonas=numero_personas,
            fecha=fecha,
            hora=hora,
            tipo=tipo_reserva,
            nota=notas,
            acceso=acceso
        )
     #guarda en la base  de datos

     nueva_reserva.save()

