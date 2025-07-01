import serial
import serial.tools.list_ports
import time

def listar_puertos_serie():
    """Lista todos los puertos serie disponibles en el sistema"""
    puertos = serial.tools.list_ports.comports()
    print("=== PUERTOS SERIE DISPONIBLES ===")
    
    if not puertos:
        print("No se encontraron puertos serie disponibles.")
        return []
    
    for puerto in puertos:
        print(f"Puerto: {puerto.device}")
        print(f"  Descripción: {puerto.description}")
        print(f"  Hardware ID: {puerto.hwid}")
        print(f"  Fabricante: {puerto.manufacturer}")
        print("-" * 50)
    
    return [puerto.device for puerto in puertos]

def probar_modem(puerto):
    """Prueba si hay un módem GSM en el puerto especificado"""
    try:
        print(f"\nProbando puerto {puerto}...")
        ser = serial.Serial(puerto, 9600, timeout=3)
        time.sleep(1)
        
        # Enviar comando AT básico
        ser.write(b'AT\r\n')
        time.sleep(1)
        respuesta = ser.read_all().decode('utf-8', errors='ignore')
        
        if 'OK' in respuesta:
            print(f"✅ Módem respondió en {puerto}")
            
            # Obtener información del módem
            ser.write(b'ATI\r\n')  # Información del módem
            time.sleep(1)
            info_modem = ser.read_all().decode('utf-8', errors='ignore')
            
            # Verificar si es un módem GSM
            ser.write(b'AT+CGMI\r\n')  # Fabricante
            time.sleep(1)
            fabricante = ser.read_all().decode('utf-8', errors='ignore')
            
            ser.write(b'AT+CGMM\r\n')  # Modelo
            time.sleep(1)
            modelo = ser.read_all().decode('utf-8', errors='ignore')
            
            ser.write(b'AT+CGSN\r\n')  # Número de serie
            time.sleep(1)
            serie = ser.read_all().decode('utf-8', errors='ignore')
            
            print(f"  Información: {info_modem.strip()}")
            print(f"  Fabricante: {fabricante.strip()}")
            print(f"  Modelo: {modelo.strip()}")
            print(f"  Serie: {serie.strip()}")
            
            ser.close()
            return True
        else:
            print(f"❌ No hay respuesta válida en {puerto}")
            print(f"  Respuesta recibida: {repr(respuesta)}")
            ser.close()
            return False
            
    except Exception as e:
        print(f"❌ Error al probar {puerto}: {e}")
        return False

def detectar_modem_automatico():
    """Detecta automáticamente el módem GSM en todos los puertos disponibles"""
    print("DETECTOR DE MÓDEM GSM")
    print("=" * 50)
    
    puertos = listar_puertos_serie()
    
    if not puertos:
        return None
    
    print("\n=== PROBANDO MÓDEMS GSM ===")
    
    modems_encontrados = []
    
    for puerto in puertos:
        if probar_modem(puerto):
            modems_encontrados.append(puerto)
    
    print("\n=== RESULTADOS ===")
    if modems_encontrados:
        print(f"✅ Módem(s) GSM encontrado(s) en: {', '.join(modems_encontrados)}")
        return modems_encontrados[0]  # Retorna el primer módem encontrado
    else:
        print("❌ No se encontraron módems GSM en ningún puerto.")
        return None

def probar_envio_sms_test(puerto):
    """Prueba el envío de SMS (sin enviar realmente)"""
    try:
        print(f"\n=== PROBANDO FUNCIONALIDAD SMS EN {puerto} ===")
        ser = serial.Serial(puerto, 9600, timeout=5)
        time.sleep(1)
        
        # Verificar modo texto SMS
        ser.write(b'AT+CMGF=1\r\n')
        time.sleep(1)
        respuesta = ser.read_all().decode('utf-8', errors='ignore')
        
        if 'OK' in respuesta:
            print("✅ Modo texto SMS configurado correctamente")
            
            # Verificar estado de la red
            ser.write(b'AT+CREG?\r\n')
            time.sleep(1)
            red = ser.read_all().decode('utf-8', errors='ignore')
            print(f"Estado de red: {red.strip()}")
            
            # Verificar señal
            ser.write(b'AT+CSQ\r\n')
            time.sleep(1)
            signal = ser.read_all().decode('utf-8', errors='ignore')
            print(f"Calidad de señal: {signal.strip()}")
            
            print("✅ El módem está listo para enviar SMS")
        else:
            print("❌ Error al configurar modo SMS")
        
        ser.close()
        
    except Exception as e:
        print(f"❌ Error al probar SMS: {e}")

if __name__ == "__main__":
    puerto_modem = detectar_modem_automatico()
    
    if puerto_modem:
        print(f"\n🎯 PUERTO RECOMENDADO PARA TU SCRIPT: {puerto_modem}")
        
        # Preguntar si quiere probar la funcionalidad SMS
        respuesta = input("\n¿Quieres probar la funcionalidad SMS? (s/n): ")
        if respuesta.lower() in ['s', 'si', 'sí', 'y', 'yes']:
            probar_envio_sms_test(puerto_modem)
        
        print(f"\n📝 Para usar en tu script:")
        print(f'python envio_sms_email.py SMS "+1234567890" "Mensaje de prueba" "{puerto_modem}"')
    else:
        print("\n💡 SUGERENCIAS:")
        print("1. Verifica que el módem esté conectado correctamente")
        print("2. Instala los drivers del módem si es necesario")
        print("3. Verifica que el módem esté encendido")
        print("4. Prueba con diferentes velocidades de baudios")
