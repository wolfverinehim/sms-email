import subprocess
import sys

def ejecutar_diagnostico_completo():
    print("🔧 DIAGNÓSTICO COMPLETO DEL SISTEMA")
    print("=" * 60)
    
    # 1. Verificar dispositivos USB
    print("\n1️⃣ DISPOSITIVOS USB CONECTADOS:")
    try:
        cmd = 'Get-WmiObject -Class Win32_PnPEntity | Where-Object {$_.DeviceID -like "USB*"} | Select-Object Name, DeviceID | Format-Table -AutoSize'
        resultado = subprocess.run(['powershell', '-Command', cmd], 
                                 capture_output=True, text=True, shell=True)
        print(resultado.stdout)
    except Exception as e:
        print(f"Error: {e}")
    
    # 2. Verificar dispositivos con problemas
    print("\n2️⃣ DISPOSITIVOS CON PROBLEMAS:")
    try:
        cmd = 'Get-WmiObject -Class Win32_PnPEntity | Where-Object {$_.ConfigManagerErrorCode -ne 0} | Select-Object Name, ConfigManagerErrorCode, DeviceID | Format-Table -AutoSize'
        resultado = subprocess.run(['powershell', '-Command', cmd], 
                                 capture_output=True, text=True, shell=True)
        if resultado.stdout.strip():
            print(resultado.stdout)
        else:
            print("✅ No hay dispositivos con problemas")
    except Exception as e:
        print(f"Error: {e}")
    
    # 3. Buscar específicamente módems
    print("\n3️⃣ BÚSQUEDA ESPECÍFICA DE MÓDEMS:")
    try:
        cmd = 'Get-WmiObject -Class Win32_PnPEntity | Where-Object {$_.Name -like "*modem*" -or $_.Name -like "*mobile*" -or $_.Name -like "*GSM*" -or $_.Name -like "*3G*" -or $_.Name -like "*4G*"} | Select-Object Name, DeviceID | Format-Table -AutoSize'
        resultado = subprocess.run(['powershell', '-Command', cmd], 
                                 capture_output=True, text=True, shell=True)
        if resultado.stdout.strip():
            print(resultado.stdout)
        else:
            print("❌ No se encontraron módems")
    except Exception as e:
        print(f"Error: {e}")
    
    # 4. Verificar puertos serie existentes
    print("\n4️⃣ PUERTOS SERIE DEL SISTEMA:")
    try:
        cmd = 'Get-WmiObject -Class Win32_SerialPort | Select-Object DeviceID, Description, PNPDeviceID | Format-Table -AutoSize'
        resultado = subprocess.run(['powershell', '-Command', cmd], 
                                 capture_output=True, text=True, shell=True)
        if resultado.stdout.strip():
            print(resultado.stdout)
        else:
            print("❌ No hay puertos serie configurados")
    except Exception as e:
        print(f"Error: {e}")
    
    # 5. Información del sistema
    print("\n5️⃣ INFORMACIÓN DEL SISTEMA:")
    try:
        # Versión de Windows
        cmd = 'Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion | Format-Table -AutoSize'
        resultado = subprocess.run(['powershell', '-Command', cmd], 
                                 capture_output=True, text=True, shell=True)
        print("Sistema operativo:")
        print(resultado.stdout)
        
        # Puertos USB disponibles
        cmd = 'Get-WmiObject -Class Win32_USBHub | Measure-Object | Select-Object Count'
        resultado = subprocess.run(['powershell', '-Command', cmd], 
                                 capture_output=True, text=True, shell=True)
        print(f"Puertos USB disponibles: {resultado.stdout}")
        
    except Exception as e:
        print(f"Error obteniendo info del sistema: {e}")
    
    # 6. Recomendaciones
    print("\n6️⃣ RECOMENDACIONES:")
    print("┌─────────────────────────────────────────────────────┐")
    print("│ 🔌 CONECTA TU MÓDEM GSM USB                         │")
    print("│ 📱 INSERTA UNA SIM CARD ACTIVA                     │")
    print("│ 💻 VERIFICA EL ADMINISTRADOR DE DISPOSITIVOS       │")
    print("│ 🔄 INSTALA LOS DRIVERS NECESARIOS                  │")
    print("│ 🔧 EJECUTA ESTE SCRIPT NUEVAMENTE                  │")
    print("└─────────────────────────────────────────────────────┘")
    
    print(f"\n📄 Diagnóstico completo guardado.")
    print(f"📧 Si necesitas ayuda, comparte este diagnóstico.")

def abrir_administrador_dispositivos():
    """Abre el administrador de dispositivos"""
    try:
        subprocess.run(['devmgmt.msc'], shell=True)
        print("✅ Administrador de dispositivos abierto")
    except Exception as e:
        print(f"❌ Error abriendo administrador de dispositivos: {e}")

def main():
    print("DIAGNÓSTICO DE MÓDEM GSM")
    print("¿Qué quieres hacer?")
    print("1. Diagnóstico completo")
    print("2. Abrir Administrador de Dispositivos")
    print("3. Salir")
    
    opcion = input("\nElige una opción (1-3): ")
    
    if opcion == "1":
        ejecutar_diagnostico_completo()
    elif opcion == "2":
        abrir_administrador_dispositivos()
    elif opcion == "3":
        print("👋 ¡Hasta luego!")
    else:
        print("❌ Opción no válida")

if __name__ == "__main__":
    main()
