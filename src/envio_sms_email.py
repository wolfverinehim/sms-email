import sys
import serial
import time
import smtplib
import logging
import os
import configparser
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def cargar_configuracion():
    """Carga la configuración desde config.ini"""
    config = configparser.ConfigParser()
    config_file = "config.ini"
    
    if not os.path.exists(config_file):
        print(f"❌ Error: No se encuentra el archivo {config_file}")
        print(f"💡 Copia {config_file}.ejemplo como {config_file} y configura tus credenciales")
        return None
    
    try:
        config.read(config_file, encoding='utf-8')
        return config
    except Exception as e:
        print(f"❌ Error leyendo configuración: {e}")
        return None

def obtener_credenciales_gmail():
    """Obtiene las credenciales de Gmail desde la configuración"""
    config = cargar_configuracion()
    if not config:
        return None
    
    try:
        gmail_config = {
            'usuario': config.get('gmail', 'usuario'),
            'password': config.get('gmail', 'password'),
            'host': config.get('gmail', 'host'),
            'puerto': config.getint('gmail', 'puerto'),
            'ssl': config.getboolean('gmail', 'ssl')
        }
        
        # Validar que no estén vacías las credenciales críticas
        if gmail_config['usuario'] == 'tu_email@gmail.com' or 'tu_contraseña' in gmail_config['password']:
            print("❌ Error: Debes configurar tus credenciales reales en config.ini")
            print("💡 Edita config.ini con tu email y contraseña de aplicación de Gmail")
            return None
            
        return gmail_config
    except Exception as e:
        print(f"❌ Error obteniendo credenciales de Gmail: {e}")
        return None

def configurar_logging():
    """Configura el sistema de logging"""
    # Crear directorio de logs si no existe
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Nombre del archivo de log con fecha
    fecha_actual = datetime.now().strftime("%Y%m%d")
    log_file = os.path.join(log_dir, f"envio_sms_email_{fecha_actual}.log")
    
    # Configurar logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()  # También mostrar en consola
        ]
    )
    
    return logging.getLogger(__name__)

def log_parametros_recibidos(args):
    """Registra los parámetros recibidos en la llamada"""
    logger = logging.getLogger(__name__)
    
    # Enmascarar contraseñas por seguridad
    args_safe = []
    for i, arg in enumerate(args):
        if i == 6 and len(args) >= 8:  # Posición de password en EMAIL
            args_safe.append("***MASKED***")
        else:
            args_safe.append(arg)
    
    logger.info(f"INICIO EJECUCIÓN | Parámetros: {' '.join(args_safe)}")
    logger.info(f"Total parámetros recibidos: {len(args)}")

def log_resultado(operacion, exito, detalles=""):
    """Registra el resultado de la operación"""
    logger = logging.getLogger(__name__)
    
    estado = "ÉXITO" if exito else "ERROR"
    mensaje = f"FIN {operacion} | Estado: {estado}"
    
    if detalles:
        mensaje += f" | Detalles: {detalles}"
    
    if exito:
        logger.info(mensaje)
    else:
        logger.error(mensaje)

def quitar_saltos_linea(texto, reemplazo=' '):
    return texto.replace('\n', reemplazo).replace('\r', reemplazo)

def enviar_sms(numero, mensaje, puerto):
    logger = logging.getLogger(__name__)
    logger.info(f"INICIO SMS | Número: {numero} | Puerto: {puerto} | Longitud mensaje: {len(mensaje)}")
    
    try:
        ser = serial.Serial(puerto, 9600, timeout=5)
        logger.info(f"SMS | Puerto serie {puerto} abierto correctamente")
        time.sleep(1)
        
        # Comando AT básico
        ser.write(b'AT\r')
        time.sleep(0.5)
        
        # Configurar modo texto
        ser.write(b'AT+CMGF=1\r')
        time.sleep(0.5)
        logger.info(f"SMS | Modo texto configurado")
        
        # Especificar número
        ser.write(f'AT+CMGS="{numero}"\r'.encode())
        time.sleep(0.5)
        logger.info(f"SMS | Número destinatario configurado: {numero}")
        
        # Enviar mensaje
        ser.write(f'{mensaje}{chr(26)}'.encode())
        time.sleep(3)
        logger.info(f"SMS | Mensaje enviado")
        
        ser.close()
        logger.info(f"SMS | Puerto serie cerrado")
        print("SMS enviado correctamente")
        log_resultado("SMS", True, f"Enviado a {numero}")
        
    except Exception as e:
        error_msg = f"Error al enviar SMS: {e}"
        print(error_msg)
        log_resultado("SMS", False, str(e))

def enviar_email(destino, mensaje, puerto, usuario, password, host, ssl="True"):
    logger = logging.getLogger(__name__)
    logger.info(f"INICIO EMAIL | Destino: {destino} | Host: {host}:{puerto} | SSL: {ssl}")
    logger.info(f"EMAIL | Usuario: {usuario} | Longitud mensaje: {len(mensaje)}")
    
    try:
        correo = MIMEMultipart()
        correo['From'] = usuario
        correo['To'] = destino
        correo['Subject'] = "Recordatorio de cita"
        logger.info(f"EMAIL | Mensaje MIME creado")

        correo.attach(MIMEText(mensaje, 'html'))
        logger.info(f"EMAIL | Contenido HTML adjuntado")

        servidor = smtplib.SMTP(host, int(puerto))
        logger.info(f"EMAIL | Conexión SMTP establecida con {host}:{puerto}")
        
        if ssl.lower() == "true":
            servidor.starttls()
            logger.info(f"EMAIL | TLS iniciado")
            
        servidor.login(usuario, password)
        logger.info(f"EMAIL | Autenticación exitosa para {usuario}")
        
        servidor.sendmail(usuario, destino, correo.as_string())
        logger.info(f"EMAIL | Mensaje enviado a {destino}")
        
        servidor.quit()
        logger.info(f"EMAIL | Conexión SMTP cerrada")
        
        print("Correo enviado correctamente")
        log_resultado("EMAIL", True, f"Enviado a {destino}")
        
    except Exception as e:
        error_msg = f"Error al enviar el correo: {e}"
        print(error_msg)
        log_resultado("EMAIL", False, str(e))

if __name__ == "__main__":
    # Configurar logging al inicio
    logger = configurar_logging()
    logger.info("=" * 80)
    logger.info("INICIO APLICACIÓN | IBA-Soft Envío SMS/Email")
    
    # Registrar parámetros recibidos
    log_parametros_recibidos(sys.argv)
    
    if len(sys.argv) > 1:
        modo = sys.argv[1].upper()
        logger.info(f"Modo seleccionado: {modo}")
        
        if modo == "SMS" and len(sys.argv) >= 5:
            numero = sys.argv[2]
            mensaje = sys.argv[3]
            puerto = sys.argv[4]
            logger.info(f"SMS | Iniciando envío a {numero} por puerto {puerto}")
            enviar_sms(numero, mensaje, puerto)
            
        elif modo == "EMAIL" and len(sys.argv) >= 7:  # Cambié de 8 a 7 parámetros
            destino = sys.argv[2]
            mensaje = sys.argv[3]
            puerto = sys.argv[4]
            usuario = sys.argv[5]
            
            # Intentar obtener credenciales desde config.ini
            gmail_config = obtener_credenciales_gmail()
            if gmail_config:
                password = gmail_config['password']
                host = gmail_config['host']
                ssl = str(gmail_config['ssl'])
                logger.info(f"EMAIL | Usando credenciales desde config.ini")
            else:
                # Fallback a parámetros de línea de comandos
                if len(sys.argv) >= 8:
                    password = sys.argv[6]
                    host = sys.argv[7] if len(sys.argv) > 7 else "smtp.gmail.com"
                    ssl = sys.argv[8] if len(sys.argv) > 8 else "True"
                    logger.info(f"EMAIL | Usando credenciales desde parámetros")
                else:
                    logger.error("EMAIL | No se pudieron obtener credenciales")
                    print("❌ Error: No se encontraron credenciales válidas")
                    log_resultado("EMAIL", False, "No se encontraron credenciales")
            
            logger.info(f"EMAIL | Iniciando envío a {destino} via {host}")
            enviar_email(destino, mensaje, puerto, usuario, password, host, ssl)
            
        else:
            error_msg = "Parámetros incorrectos"
            print(error_msg)
            logger.error(f"PARÁMETROS INCORRECTOS | Recibidos: {len(sys.argv)} argumentos")
            log_resultado("VALIDACIÓN", False, "Número de parámetros incorrecto")
    else:
        print("Uso:")
        print("  SMS numero mensaje puerto")
        print("  EMAIL destino mensaje puerto usuario password host [ssl]")
        logger.warning("AYUDA MOSTRADA | No se proporcionaron parámetros")
    
    logger.info("FIN APLICACIÓN | IBA-Soft Envío SMS/Email")
    logger.info("=" * 80)
