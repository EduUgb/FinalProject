# mi_aplicacion/views.py
from django.http import HttpResponse
from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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

        return HttpResponse("Reservación enviada con éxito")

    return render(request, 'index.html')


def enviar_correo(nombre, correo, telefono, numero_personas, fecha, hora, tipo_reserva, notas, acceso):
    # Configura el servidor SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'carloseduardog310@gmail.com'  # Cambia esto por tu correo real
    smtp_password = 'pnfx ptkv qwir omvq '      # Cambia esto por tu contraseña real

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

    Saludos,
    Tu Restaurante
    """
    mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

    # Envía el correo
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Activa la encriptación
            server.login(smtp_user, smtp_password)  # Inicia sesión
            server.sendmail(mensaje['From'], mensaje['To'], mensaje.as_string())  # Envía el correo
        print("Correo enviado con éxito")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")