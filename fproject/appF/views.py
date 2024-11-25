# mi_aplicacion/views.py
from django.http import HttpResponse
from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from .models import Reserv
from email import encoders
import os
from django.http import JsonResponse
from django.conf import settings
def inicio(request):
    return render(request,'PPrinci.html')

def about(request):
    return render(request, 'menu.html')

def contactos(request):
    return render(request, 'Contact.html')

def index(request):
    return render(request,  'index.html')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        numero_personas = request.POST.get('numero_personas')
        mesa = request.POST.get('mesa')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('Hora')
        tipo_reserva = request.POST.get('tipo_reserva')
        notas = request.POST.get('notas')
        acceso = request.POST.get('acceso')
    
        reservasExis = Reserv.objects.filter(fecha=fecha, hora=hora, mesa=mesa)
        if reservasExis.exists():
            return render(request, 'error.html')
        else:context = {
        'mostrar_modal': True  # Aquí decides si mostrar el modal o no
        }
        
        # Llama a la función para enviar el correo
        enviar_correo(nombre, correo, telefono, numero_personas, fecha, hora, tipo_reserva, notas, acceso,mesa)

        #llama la base
        Reserva(nombre, correo, telefono, numero_personas, fecha, hora, tipo_reserva, notas, acceso,mesa)

        return render(request, 'index.html', context)
    return render(request, 'index.html')


def enviar_correo(nombre, correo, telefono, numero_personas, fecha, hora, tipo_reserva, notas, acceso,mesa):
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
    ¡Hola {nombre}!

    ¡Gracias por elegir BerlFood para tu próxima experiencia gastronómica! Nos complace confirmar tu reservación y estamos emocionados de ofrecerte una experiencia única en nuestro restaurante.

    Aquí están los detalles de tu reservación:

    🌟 **Nombre del Cliente**: {nombre}

    📧 **Correo Electrónico**: {correo} 

    📞 **Teléfono**: {telefono}  

    🍽️ **Número de Personas**: {numero_personas} 

    📅 **Fecha de la Reserva**: {fecha} 
    
    ⏰ **Hora de la Reserva**: {hora}

    🪑 **Mesa reservada**: {mesa}
     
    🍷 **Tipo de Reserva**: {tipo_reserva}  

    📝 **Notas**: {notas}

    🔑 **Acceso Especial**: {acceso}

    En BerlFood, nos enorgullece ofrecer una atmósfera cálida y acogedora, donde cada plato es una obra maestra. Ya sea que vengas a disfrutar de una deliciosa cena en nuestra exclusiva área de mesas o en el salón reservado, nuestro equipo se asegurará de que tu visita sea memorable.

    Para facilitar tu llegada, hemos asignado un código QR con información importante sobre tu reservación y nuestro restaurante. ¡No olvides mostrarlo al llegar!
    
    ¡Tambien hemos colocado el menú de nuestro restaurante!

    Si tienes alguna petición especial o necesitas ajustar tu reserva, no dudes en contactarnos. Estamos aquí para hacer de tu experiencia algo inolvidable.

    ¡Nos vemos pronto en BerlFood, donde cada comida es una celebración!
    
    Con cariño,  
    El equipo de BerlFood 

    📍 **Dirección**: Calle de la Gastronomía, 123, Zona Gastronómica, Ciudad Gourmet

    📞 **Teléfono**: +5037418-2650  

    ---
    Por favor, guarda este código QR en tu dispositivo para acceder fácilmente a la información relacionada con tu reservación.
    """

    mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

    # Abrimos el archivo que vamos a adjuntar
    ruta_adjunto = os.path.join(settings.MEDIA_ROOT, 'Verificador.png')
    ruta_adjunto2 = os.path.join(settings.MEDIA_ROOT, 'menu.png')

    qr = open(ruta_adjunto, 'rb')
    menu = open(ruta_adjunto2, 'rb')


    parte = MIMEBase('application', 'octet-stream')
    parte.set_payload(qr.read())
    encoders.encode_base64(parte)
    parte.add_header(
        'Content-Disposition',
        f'attachment; filename={os.path.basename(ruta_adjunto)}'
    )
    mensaje.attach(parte)

    parte2 = MIMEBase('application', 'octet-stream')
    parte2.set_payload(menu.read())
    encoders.encode_base64(parte2)
    parte2.add_header(
        'Content-Disposition',
        f'attachment; filename={os.path.basename(ruta_adjunto2)}'
    )
    mensaje.attach(parte2)

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




def Reserva(nombre, correo, telefono, numero_personas, fecha, hora, tipo_reserva, notas, acceso,mesa):
     nueva_reserva = Reserv(
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            numPersonas=numero_personas,
            fecha=fecha,
            hora=hora,
            tipo=tipo_reserva,
            nota=notas,
            acceso=acceso,
            mesa=mesa,
        )
     #guarda en la base  de datos

     nueva_reserva.save()

