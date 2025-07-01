import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import getpass
import sys
import os

def obtener_credenciales():
    """Obtiene las credenciales de forma segura"""
    print("🔐 CONFIGURACIÓN DE CREDENCIALES GMAIL")
    print("-" * 50)
    
    # Usuario
    usuario = input(f"📧 Usuario Gmail [infonutribel@gmail.com]: ").strip()
    if not usuario:
        usuario = "infonutribel@gmail.com"
    
    print("\n💡 IMPORTANTE:")
    print("   - NO uses tu contraseña normal de Gmail")
    print("   - USA una 'Contraseña de aplicación' de 16 caracteres")
    print("   - Genera una en: https://myaccount.google.com/apppasswords")
    
    # Contraseña de aplicación
    password = getpass.getpass("\n🔑 Contraseña de aplicación (16 caracteres): ")
    
    return usuario, password

def probar_conexion_gmail(usuario, password):
    """Prueba la conexión básica con Gmail SMTP"""
    print("\n🔗 PROBANDO CONEXIÓN CON GMAIL...")
    print("-" * 50)
    
    config = {
        'host': 'smtp.gmail.com',
        'puerto': 587,
        'usuario': usuario,
        'password': password
    }
    
    try:
        print(f"📡 Conectando a {config['host']}:{config['puerto']}")
        servidor = smtplib.SMTP(config['host'], config['puerto'])
        
        print("🔐 Iniciando TLS...")
        servidor.starttls()
        
        print("👤 Intentando login...")
        servidor.login(config['usuario'], config['password'])
        
        print("✅ ¡CONEXIÓN EXITOSA!")
        servidor.quit()
        return True, config
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ ERROR DE AUTENTICACIÓN: {e}")
        print("\n💡 VERIFICA:")
        print("1. ¿Activaste la verificación en 2 pasos?")
        print("2. ¿Generaste una contraseña de aplicación?")
        print("3. ¿Usaste la contraseña de aplicación (no la normal)?")
        print("4. ¿La contraseña tiene exactamente 16 caracteres?")
        return False, None
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False, None

def enviar_email_prueba(config, destino):
    """Envía un email de prueba"""
    print(f"\n📧 ENVIANDO EMAIL DE PRUEBA A: {destino}")
    print("-" * 50)
    
    try:
        # Crear mensaje
        mensaje = MIMEMultipart('alternative')
        mensaje['From'] = formataddr(('Sistema SMS/Email ✅', config['usuario']))
        mensaje['To'] = destino
        mensaje['Subject'] = "✅ Configuración Gmail Exitosa - Sistema SMS/Email"
        
        # Contenido HTML mejorado
        html = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                    .header {{ background: linear-gradient(135deg, #4CAF50, #45a049); color: white; padding: 20px; text-align: center; border-radius: 10px 10px 0 0; }}
                    .content {{ padding: 20px; background: #f9f9f9; }}
                    .success-box {{ background: #d4edda; border: 1px solid #c3e6cb; padding: 15px; border-radius: 5px; margin: 15px 0; }}
                    .config-box {{ background: #e2e3e5; border: 1px solid #d6d8db; padding: 15px; border-radius: 5px; margin: 15px 0; }}
                    .footer {{ background: #6c757d; color: white; padding: 10px; text-align: center; border-radius: 0 0 10px 10px; font-size: 12px; }}
                    .command {{ background: #f8f9fa; border: 1px solid #dee2e6; padding: 10px; border-radius: 3px; font-family: monospace; word-break: break-all; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>🎉 ¡Configuración Exitosa!</h1>
                    <p>Tu sistema de envío de emails está funcionando correctamente</p>
                </div>
                
                <div class="content">
                    <div class="success-box">
                        <h3>✅ Conexión Gmail Establecida</h3>
                        <p>La autenticación con Gmail fue exitosa usando contraseña de aplicación.</p>
                    </div>
                    
                    <h3>📋 Configuración Utilizada:</h3>
                    <div class="config-box">
                        <strong>Servidor SMTP:</strong> {config['host']}<br>
                        <strong>Puerto:</strong> {config['puerto']}<br>
                        <strong>Seguridad:</strong> TLS<br>
                        <strong>Usuario:</strong> {config['usuario']}<br>
                        <strong>Autenticación:</strong> Contraseña de aplicación ✅
                    </div>
                    
                    <h3>🚀 Comando para usar en tu script:</h3>
                    <div class="command">
python envio_sms_email.py EMAIL "{destino}" "&lt;h1&gt;Tu mensaje&lt;/h1&gt;" "587" "{config['usuario']}" "tu_contraseña_app" "smtp.gmail.com" "True"
                    </div>
                    
                    <div style="margin-top: 20px; padding: 15px; background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 5px;">
                        <strong>🔐 Recuerda:</strong> Guarda tu contraseña de aplicación de forma segura. No la compartas y úsala solo para esta aplicación.
                    </div>
                </div>
                
                <div class="footer">
                    Sistema automatizado de SMS/Email - Configurado exitosamente el 1 de julio de 2025
                </div>
            </body>
        </html>
        """
        
        # Adjuntar contenido
        parte_html = MIMEText(html, 'html', 'utf-8')
        mensaje.attach(parte_html)
        
        # Enviar email
        servidor = smtplib.SMTP(config['host'], config['puerto'])
        servidor.starttls()
        servidor.login(config['usuario'], config['password'])
        
        servidor.sendmail(config['usuario'], destino, mensaje.as_string())
        servidor.quit()
        
        print("✅ EMAIL ENVIADO CORRECTAMENTE")
        print(f"📨 Revisa la bandeja de entrada de: {destino}")
        return True
        
    except Exception as e:
        print(f"❌ ERROR AL ENVIAR EMAIL: {e}")
        return False

def guardar_configuracion(config):
    """Guarda la configuración en config.ini"""
    try:
        config_content = f"""# Archivo de configuración para AjpdSoft Envío SMS/Email
# IMPORTANTE: Este archivo contiene credenciales sensibles
# NO subir este archivo a repositorios públicos

[gmail]
usuario = {config['usuario']}
password = {config['password']}
host = {config['host']}
puerto = {config['puerto']}
ssl = True

[sms]
puerto_default = COM3
baudrate = 9600
timeout = 5

[sistema]
directorio_logs = logs
nivel_log = INFO
rotacion_logs_dias = 30
"""
        
        with open('config.ini', 'w', encoding='utf-8') as f:
            f.write(config_content)
        
        print(f"\n💾 Configuración guardada en config.ini")
        print(f"🔐 IMPORTANTE: Este archivo contiene credenciales sensibles")
        print(f"⚠️  NO subir config.ini a repositorios públicos")
        
    except Exception as e:
        print(f"❌ Error guardando configuración: {e}")

def main():
    print("🔧 CONFIGURADOR SEGURO DE EMAIL GMAIL")
    print("=" * 60)
    
    # Obtener credenciales
    usuario, password = obtener_credenciales()
    
    # Probar conexión
    exito, config = probar_conexion_gmail(usuario, password)
    
    if not exito:
        print("\n❌ No se pudo establecer conexión.")
        print("\n📖 Lee la guía: CONFIGURAR_GMAIL.md")
        return
    
    # Pedir email de destino
    print(f"\n📧 ¿A qué email enviar la prueba?")
    destino = input("Email destino (ENTER para usar el mismo): ").strip()
    
    if not destino:
        destino = usuario
    
    # Enviar email de prueba
    if enviar_email_prueba(config, destino):
        print("\n🎉 ¡CONFIGURACIÓN COMPLETA Y EXITOSA!")
        
        # Guardar configuración
        guardar_configuracion(config)
        
        # Mostrar comandos de ejemplo
        print(f"\n🎯 COMANDOS DE EJEMPLO:")
        print(f"\n📧 Email simple:")
        print(f'python envio_sms_email.py EMAIL "{destino}" "Mensaje de prueba" "587" "{usuario}" "tu_contraseña_app" "smtp.gmail.com" "True"')
        
        print(f"\n📧 Email HTML:")
        print(f'python envio_sms_email.py EMAIL "{destino}" "<h1>Título</h1><p>Contenido HTML</p>" "587" "{usuario}" "tu_contraseña_app" "smtp.gmail.com" "True"')
        
        print(f"\n✅ ¡Tu sistema está listo para usar!")
    
    else:
        print(f"\n❌ Error enviando email de prueba")

if __name__ == "__main__":
    main()
