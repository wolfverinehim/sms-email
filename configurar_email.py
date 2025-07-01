import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import sys

# Configuración Gmail
GMAIL_CONFIG = {
    'host': 'smtp.gmail.com',
    'puerto': 587,
    'usuario': 'infonutribel@gmail.com',
    'password': '',
    'ssl': True
}

def probar_conexion_gmail():
    """Prueba la conexión básica con Gmail SMTP"""
    print("🔗 PROBANDO CONEXIÓN CON GMAIL...")
    print("-" * 50)
    
    try:
        # Crear conexión SMTP
        print(f"📡 Conectando a {GMAIL_CONFIG['host']}:{GMAIL_CONFIG['puerto']}")
        servidor = smtplib.SMTP(GMAIL_CONFIG['host'], GMAIL_CONFIG['puerto'])
        
        # Habilitar debug para ver el intercambio completo
        servidor.set_debuglevel(1)
        
        print("🔐 Iniciando TLS...")
        servidor.starttls()
        
        print("👤 Intentando login...")
        servidor.login(GMAIL_CONFIG['usuario'], GMAIL_CONFIG['password'])
        
        print("✅ ¡CONEXIÓN EXITOSA!")
        servidor.quit()
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ ERROR DE AUTENTICACIÓN: {e}")
        print("\n💡 POSIBLES SOLUCIONES:")
        print("1. Verifica usuario y contraseña")
        print("2. Activa 'Verificación en 2 pasos' en Gmail")
        print("3. Genera una 'Contraseña de aplicación'")
        print("4. Permite 'Acceso de apps menos seguras' (no recomendado)")
        return False
        
    except smtplib.SMTPException as e:
        print(f"❌ ERROR SMTP: {e}")
        return False
        
    except Exception as e:
        print(f"❌ ERROR GENERAL: {e}")
        return False

def enviar_email_prueba(destino):
    """Envía un email de prueba"""
    print(f"\n📧 ENVIANDO EMAIL DE PRUEBA A: {destino}")
    print("-" * 50)
    
    try:
        # Crear mensaje
        mensaje = MIMEMultipart('alternative')
        mensaje['From'] = formataddr(('Sistema SMS/Email', GMAIL_CONFIG['usuario']))
        mensaje['To'] = destino
        mensaje['Subject'] = "✅ Prueba de configuración - Sistema SMS/Email"
        
        # Contenido del email (texto plano y HTML)
        texto_plano = """
¡Hola!

Este es un email de prueba del sistema de envío de SMS y Email.

✅ La configuración de Gmail está funcionando correctamente.

Detalles de la prueba:
- Servidor SMTP: smtp.gmail.com
- Puerto: 587
- Seguridad: TLS
- Usuario: infonutribel@gmail.com

¡El sistema está listo para enviar emails!

Saludos,
Sistema Automatizado
        """
        
        html = """
        <html>
            <head></head>
            <body>
                <h2 style="color: #4CAF50;">✅ Prueba de Configuración Exitosa</h2>
                
                <p>¡Hola!</p>
                
                <p>Este es un email de prueba del <strong>sistema de envío de SMS y Email</strong>.</p>
                
                <div style="background-color: #f0f8ff; padding: 15px; border-left: 4px solid #4CAF50; margin: 20px 0;">
                    <h3>✅ La configuración de Gmail está funcionando correctamente</h3>
                </div>
                
                <h4>📋 Detalles de la prueba:</h4>
                <ul>
                    <li><strong>Servidor SMTP:</strong> smtp.gmail.com</li>
                    <li><strong>Puerto:</strong> 587</li>
                    <li><strong>Seguridad:</strong> TLS</li>
                    <li><strong>Usuario:</strong> infonutribel@gmail.com</li>
                </ul>
                
                <div style="background-color: #e8f5e8; padding: 10px; border-radius: 5px; margin: 20px 0;">
                    🎉 <strong>¡El sistema está listo para enviar emails!</strong>
                </div>
                
                <hr>
                <p style="color: #666; font-size: 12px;">
                    <em>Sistema Automatizado - {fecha}</em>
                </p>
            </body>
        </html>
        """.format(fecha="1 de julio de 2025")
        
        # Adjuntar contenido
        parte_texto = MIMEText(texto_plano, 'plain', 'utf-8')
        parte_html = MIMEText(html, 'html', 'utf-8')
        
        mensaje.attach(parte_texto)
        mensaje.attach(parte_html)
        
        # Enviar email
        servidor = smtplib.SMTP(GMAIL_CONFIG['host'], GMAIL_CONFIG['puerto'])
        servidor.starttls()
        servidor.login(GMAIL_CONFIG['usuario'], GMAIL_CONFIG['password'])
        
        texto_mensaje = mensaje.as_string()
        servidor.sendmail(GMAIL_CONFIG['usuario'], destino, texto_mensaje)
        servidor.quit()
        
        print("✅ EMAIL ENVIADO CORRECTAMENTE")
        print(f"📨 Revisa la bandeja de entrada de: {destino}")
        return True
        
    except Exception as e:
        print(f"❌ ERROR AL ENVIAR EMAIL: {e}")
        return False

def probar_configuracion_original(destino):
    """Prueba usando la función original del script"""
    print(f"\n🧪 PROBANDO FUNCIÓN ORIGINAL...")
    print("-" * 50)
    
    # Importar la función original
    sys.path.append('.')
    try:
        from envio_sms_email import enviar_email
        
        mensaje_html = """
        <h2>🧪 Prueba con función original</h2>
        <p>Este email fue enviado usando la función <code>enviar_email</code> original.</p>
        <p>✅ Todo funciona correctamente!</p>
        """
        
        enviar_email(
            destino=destino,
            mensaje=mensaje_html,
            puerto=587,
            usuario=GMAIL_CONFIG['usuario'],
            password=GMAIL_CONFIG['password'],
            host=GMAIL_CONFIG['host'],
            ssl="True"
        )
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR CON FUNCIÓN ORIGINAL: {e}")
        return False

def main():
    print("🔧 CONFIGURADOR Y PROBADOR DE EMAIL GMAIL")
    print("=" * 60)
    
    # Mostrar configuración
    print("📋 CONFIGURACIÓN ACTUAL:")
    print(f"   Usuario: {GMAIL_CONFIG['usuario']}")
    print(f"   Servidor: {GMAIL_CONFIG['host']}:{GMAIL_CONFIG['puerto']}")
    print(f"   Seguridad: TLS")
    
    # Paso 1: Probar conexión
    if not probar_conexion_gmail():
        print("\n❌ No se pudo establecer conexión con Gmail")
        print("\n🔧 GUÍA DE SOLUCIÓN:")
        print("1. Ve a: https://myaccount.google.com/security")
        print("2. Activa 'Verificación en 2 pasos'")
        print("3. Genera una 'Contraseña de aplicación'")
        print("4. Usa esa contraseña en lugar de tu contraseña normal")
        return
    
    # Paso 2: Pedir email de destino
    print(f"\n📧 ¿A qué email quieres enviar la prueba?")
    destino = input("Email destino (o ENTER para usar el mismo): ").strip()
    
    if not destino:
        destino = GMAIL_CONFIG['usuario']
    
    # Paso 3: Enviar email de prueba mejorado
    if enviar_email_prueba(destino):
        print("\n✅ PRUEBA MEJORADA EXITOSA")
    
    # Paso 4: Probar función original
    if probar_configuracion_original(destino):
        print("\n✅ FUNCIÓN ORIGINAL FUNCIONA")
    
    # Paso 5: Mostrar comando para usar
    print(f"\n🎯 COMANDO PARA USAR EN TU SCRIPT:")
    print(f'python envio_sms_email.py EMAIL "{destino}" "<h1>Tu mensaje</h1>" "587" "{GMAIL_CONFIG["usuario"]}" "{GMAIL_CONFIG["password"]}" "{GMAIL_CONFIG["host"]}" "True"')
    
    print(f"\n✅ ¡CONFIGURACIÓN COMPLETA!")

if __name__ == "__main__":
    main()
