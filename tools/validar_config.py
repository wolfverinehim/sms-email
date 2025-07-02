#!/usr/bin/env python3
"""
Validador de configuración para IBA-Soft Envío SMS/Email
Verifica que el archivo config.ini esté bien configurado
"""

import os
import configparser
import smtplib

def validar_archivo_config():
    """Valida que existe el archivo de configuración"""
    if not os.path.exists("config.ini"):
        print("❌ ERROR: No se encuentra config.ini")
        print("\n🔧 SOLUCIÓN:")
        print("1. Copia config.ini.ejemplo como config.ini")
        print("2. Edita config.ini con tus credenciales reales")
        return False
    
    print("✅ Archivo config.ini encontrado")
    return True

def validar_estructura_config():
    """Valida la estructura del archivo de configuración"""
    try:
        config = configparser.ConfigParser()
        config.read("config.ini", encoding='utf-8')
        
        # Verificar secciones requeridas
        secciones_requeridas = ['gmail', 'sms', 'sistema']
        for seccion in secciones_requeridas:
            if not config.has_section(seccion):
                print(f"❌ ERROR: Falta la sección [{seccion}] en config.ini")
                return False
        
        # Verificar campos de Gmail
        campos_gmail = ['usuario', 'password', 'host', 'puerto', 'ssl']
        for campo in campos_gmail:
            if not config.has_option('gmail', campo):
                print(f"❌ ERROR: Falta el campo '{campo}' en la sección [gmail]")
                return False
        
        print("✅ Estructura de config.ini válida")
        return True, config
        
    except Exception as e:
        print(f"❌ ERROR leyendo config.ini: {e}")
        return False

def validar_credenciales_gmail(config):
    """Valida que las credenciales de Gmail sean válidas"""
    try:
        usuario = config.get('gmail', 'usuario')
        password = config.get('gmail', 'password')
        host = config.get('gmail', 'host')
        puerto = config.getint('gmail', 'puerto')
        
        # Verificar que no sean valores de ejemplo
        if usuario == 'tu_email@gmail.com':
            print("❌ ERROR: Debes cambiar 'tu_email@gmail.com' por tu email real")
            return False
        
        if 'tu_contraseña' in password:
            print("❌ ERROR: Debes cambiar la contraseña de ejemplo por tu contraseña de aplicación")
            return False
        
        # Verificar formato de email
        if '@' not in usuario or '.' not in usuario:
            print(f"❌ ERROR: '{usuario}' no parece un email válido")
            return False
        
        # Verificar longitud de contraseña de aplicación (suelen ser 16 caracteres)
        if len(password.replace(' ', '')) != 16:
            print(f"⚠️  ADVERTENCIA: La contraseña de aplicación suele tener 16 caracteres")
            print(f"   Tu contraseña tiene {len(password.replace(' ', ''))} caracteres")
        
        print("✅ Credenciales Gmail parecen válidas")
        return True
        
    except Exception as e:
        print(f"❌ ERROR validando credenciales: {e}")
        return False

def probar_conexion_gmail(config):
    """Prueba la conexión real con Gmail"""
    try:
        print("\n🔄 Probando conexión con Gmail...")
        
        usuario = config.get('gmail', 'usuario')
        password = config.get('gmail', 'password')
        host = config.get('gmail', 'host')
        puerto = config.getint('gmail', 'puerto')
        
        # Crear conexión SMTP
        servidor = smtplib.SMTP(host, puerto)
        servidor.starttls()
        servidor.login(usuario, password)
        servidor.quit()
        
        print("✅ ¡Conexión con Gmail EXITOSA!")
        return True
        
    except Exception as e:
        print(f"❌ ERROR de conexión Gmail: {e}")
        print("\n💡 POSIBLES SOLUCIONES:")
        print("1. Verifica que la contraseña sea una 'contraseña de aplicación'")
        print("2. Asegúrate de tener activada la verificación en 2 pasos")
        print("3. Genera una nueva contraseña de aplicación")
        return False

def validar_configuracion_sms(config):
    """Valida la configuración SMS"""
    try:
        puerto = config.get('sms', 'puerto_default')
        baudrate = config.getint('sms', 'baudrate')
        timeout = config.getint('sms', 'timeout')
        
        print(f"✅ Configuración SMS: Puerto {puerto}, Baudrate {baudrate}, Timeout {timeout}s")
        return True
        
    except Exception as e:
        print(f"❌ ERROR en configuración SMS: {e}")
        return False

def main():
    print("🔍 VALIDADOR DE CONFIGURACIÓN - IBA-Soft")
    print("=" * 60)
    
    # Paso 1: Verificar archivo
    if not validar_archivo_config():
        return
    
    # Paso 2: Verificar estructura
    resultado = validar_estructura_config()
    if isinstance(resultado, tuple):
        valido, config = resultado
        if not valido:
            return
    else:
        return
    
    # Paso 3: Validar credenciales
    if not validar_credenciales_gmail(config):
        return
    
    # Paso 4: Validar configuración SMS
    validar_configuracion_sms(config)
    
    # Paso 5: Probar conexión (opcional)
    print(f"\n¿Quieres probar la conexión con Gmail? (s/n): ", end="")
    respuesta = input().strip().lower()
    
    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
        if probar_conexion_gmail(config):
            print(f"\n🎉 ¡CONFIGURACIÓN COMPLETAMENTE VÁLIDA!")
            print(f"✅ Tu sistema está listo para enviar emails")
        else:
            print(f"\n⚠️  Configuración válida pero hay problemas de conexión")
    else:
        print(f"\n✅ Validación de estructura completada")
    
    print(f"\n📄 Para usar el sistema:")
    print(f"   python envio_sms_email.py EMAIL destino@ejemplo.com \"Mensaje\" 587 {config.get('gmail', 'usuario')}")

if __name__ == "__main__":
    main()
