import subprocess
import re
import serial
import time

def obtener_puertos_windows():
    """Obtiene los puertos COM usando comandos de Windows"""
    try:
        print("=== BUSCANDO PUERTOS COM CON WMIC ===")
        # Usar WMIC para obtener información de puertos serie
        resultado = subprocess.run(['wmic', 'path', 'Win32_SerialPort', 'get', 'DeviceID,Description,PNPDeviceID'], 
                                 capture_output=True, text=True, shell=True)
        
        if resultado.returncode == 0:
            lines = resultado.stdout.strip().split('\n')
            puertos = []
            
            for line in lines[1:]:  # Saltar encabezado
                if line.strip():
                    parts = line.strip().split()
                    if len(parts) >= 1 and 'COM' in line:
                        # Extraer puerto COM
                        com_match = re.search(r'COM\d+', line)
                        if com_match:
                            puerto = com_match.group()
                            descripcion = line.replace(puerto, '').strip()
                            puertos.append((puerto, descripcion))
                            print(f"Encontrado: {puerto} - {descripcion}")
            
            return [puerto[0] for puerto in puertos]
        else:
            print("Error ejecutando WMIC")
            return []
            
    except Exception as e:
        print(f"Error con WMIC: {e}")
        return []

def obtener_puertos_powershell():
    """Obtiene puertos COM usando PowerShell"""
    try:
        print("\n=== BUSCANDO PUERTOS COM CON POWERSHELL ===")
        cmd = 'Get-WmiObject -Class Win32_SerialPort | Select-Object DeviceID, Description, PNPDeviceID | Format-Table -AutoSize'
        resultado = subprocess.run(['powershell', '-Command', cmd], 
                                 capture_output=True, text=True, shell=True)
        
        if resultado.returncode == 0:
            print("Resultado PowerShell:")
            print(resultado.stdout)
            
            # Extraer puertos COM
            puertos = re.findall(r'COM\d+', resultado.stdout)
            return list(set(puertos))  # Eliminar duplicados
        else:
            print("Error ejecutando PowerShell")
            return []
            
    except Exception as e:
        print(f"Error con PowerShell: {e}")
        return []

def obtener_puertos_device_manager():
    """Intenta obtener información desde el administrador de dispositivos"""
    try:
        print("\n=== BUSCANDO DISPOSITIVOS USB/SERIE ===")
        cmd = 'Get-WmiObject -Class Win32_PnPEntity | Where-Object {$_.Name -like "*COM*" -or $_.Name -like "*Serial*" -or $_.Name -like "*Modem*" -or $_.Name -like "*USB*"} | Select-Object Name, DeviceID | Format-Table -AutoSize'
        resultado = subprocess.run(['powershell', '-Command', cmd], 
                                 capture_output=True, text=True, shell=True)
        
        if resultado.returncode == 0:
            print("Dispositivos relacionados:")
            print(resultado.stdout)
            
            # Extraer puertos COM
            puertos = re.findall(r'COM\d+', resultado.stdout)
            return list(set(puertos))
        else:
            return []
            
    except Exception as e:
        print(f"Error buscando dispositivos: {e}")
        return []

def probar_puertos_comunes():
    """Prueba puertos COM comunes aunque no aparezcan en la lista"""
    print("\n=== PROBANDO PUERTOS COM COMUNES ===")
    puertos_comunes = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8']
    puertos_disponibles = []
    
    for puerto in puertos_comunes:
        try:
            print(f"Probando {puerto}...", end=' ')
            ser = serial.Serial(puerto, 9600, timeout=1)
            ser.close()
            print("✅ Disponible")
            puertos_disponibles.append(puerto)
        except serial.SerialException:
            print("❌ No disponible")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    return puertos_disponibles

def main():
    print("DETECTOR AVANZADO DE MÓDEM GSM")
    print("=" * 50)
    
    todos_los_puertos = []
    
    # Método 1: WMIC
    puertos_wmic = obtener_puertos_windows()
    todos_los_puertos.extend(puertos_wmic)
    
    # Método 2: PowerShell
    puertos_ps = obtener_puertos_powershell()
    todos_los_puertos.extend(puertos_ps)
    
    # Método 3: Dispositivos relacionados
    puertos_dev = obtener_puertos_device_manager()
    todos_los_puertos.extend(puertos_dev)
    
    # Método 4: Probar puertos comunes
    puertos_comunes = probar_puertos_comunes()
    todos_los_puertos.extend(puertos_comunes)
    
    # Eliminar duplicados
    puertos_unicos = list(set(todos_los_puertos))
    
    if puertos_unicos:
        print(f"\n=== PUERTOS ENCONTRADOS: {puertos_unicos} ===")
        
        # Probar cada puerto
        for puerto in puertos_unicos:
            probar_modem_gsm(puerto)
    else:
        print("\n❌ NO SE ENCONTRARON PUERTOS COM")
        print("\n💡 POSIBLES SOLUCIONES:")
        print("1. Conecta el módem USB")
        print("2. Instala los drivers del módem")
        print("3. Verifica en el Administrador de Dispositivos")
        print("4. Prueba con otro cable USB")

def probar_modem_gsm(puerto):
    """Prueba específicamente si hay un módem GSM"""
    try:
        print(f"\n🔍 Probando módem GSM en {puerto}...")
        ser = serial.Serial(puerto, 9600, timeout=3)
        time.sleep(1)
        
        # Comando AT básico
        ser.write(b'AT\r\n')
        time.sleep(1)
        respuesta = ser.read_all().decode('utf-8', errors='ignore')
        
        if 'OK' in respuesta:
            print(f"✅ MÓDEM ENCONTRADO EN {puerto}")
            
            # Información adicional
            comandos = [
                ('ATI', 'Información del módem'),
                ('AT+CGMI', 'Fabricante'),
                ('AT+CGMM', 'Modelo'),
                ('AT+CGSN', 'IMEI'),
                ('AT+CREG?', 'Estado de red'),
                ('AT+CSQ', 'Calidad de señal')
            ]
            
            for cmd, desc in comandos:
                ser.write(f'{cmd}\r\n'.encode())
                time.sleep(1)
                resp = ser.read_all().decode('utf-8', errors='ignore')
                print(f"  {desc}: {resp.strip()}")
            
            print(f"\n🎯 USA ESTE PUERTO: {puerto}")
            print(f"Comando de ejemplo:")
            print(f'python envio_sms_email.py SMS "+1234567890" "Prueba" "{puerto}"')
            
        else:
            print(f"❌ No es un módem GSM válido en {puerto}")
        
        ser.close()
        
    except Exception as e:
        print(f"❌ Error probando {puerto}: {e}")

if __name__ == "__main__":
    main()
