#!/usr/bin/env python3
"""
Script para crear el ejecutable IBA-SoftEnvioSMS.exe
"""

import subprocess
import os
import sys
import shutil

def crear_ejecutable_principal():
    """Crea el ejecutable principal usando PyInstaller"""
    print("🔧 CREANDO EJECUTABLE IBA-SoftEnvioSMS.exe")
    print("=" * 60)
    
    # Verificar que el archivo principal existe
    if not os.path.exists("../src/envio_sms_email.py"):
        print("❌ Error: No se encuentra src/envio_sms_email.py")
        return False
    
    print("📂 Limpiando archivos anteriores...")
    # Limpiar directorios anteriores
    if os.path.exists("../dist"):
        shutil.rmtree("../dist")
    if os.path.exists("../build"):
        shutil.rmtree("../build")
    if os.path.exists("IBA-SoftEnvioSMS.spec"):
        os.remove("IBA-SoftEnvioSMS.spec")
    
    print("🏗️ Generando ejecutable...")
    
    # Comando PyInstaller con opciones optimizadas
    comando = [
        "../.venv/Scripts/pyinstaller.exe",
        "--onefile",                          # Un solo archivo ejecutable
        "--console",                          # Mantener ventana de consola
        "--name=IBA-SoftEnvioSMS",           # Nombre del ejecutable
        "--clean",                           # Limpiar cache
        "--noconfirm",                       # No pedir confirmación
        "--add-data=config/requirements.txt;.",     # Incluir requirements.txt
        "src/envio_sms_email.py"                 # Archivo principal
    ]
    
    try:
        print("🔄 Ejecutando PyInstaller...")
        resultado = subprocess.run(comando, capture_output=True, text=True, cwd="..")
        
        if resultado.returncode == 0:
            print("✅ ¡EJECUTABLE CREADO EXITOSAMENTE!")
            
            # Verificar que el archivo se creó
            exe_path = "../dist/IBA-SoftEnvioSMS.exe"
            if os.path.exists(exe_path):
                size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"📁 Ubicación: {os.path.abspath(exe_path)}")
                print(f"📏 Tamaño: {size_mb:.2f} MB")
                
                # Mostrar ejemplos de uso
                mostrar_ejemplos_uso()
                return True
            else:
                print("❌ Error: El ejecutable no se creó correctamente")
                return False
        else:
            print("❌ Error al crear el ejecutable:")
            print(resultado.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error ejecutando PyInstaller: {e}")
        return False

def crear_ejecutable_visor():
    """Crea el ejecutable del visor de logs"""
    print("\n🔧 CREANDO EJECUTABLE IBA-SoftVisorLogs.exe")
    print("=" * 60)
    
    # Verificar que el archivo del visor existe
    if not os.path.exists("../src/visor_logs.py"):
        print("❌ Error: No se encuentra src/visor_logs.py")
        return False
    
    print("🏗️ Generando ejecutable del visor...")
    
    # Comando PyInstaller para el visor
    comando = [
        "../.venv/Scripts/pyinstaller.exe",
        "--onefile",                          # Un solo archivo ejecutable
        "--console",                          # Mantener ventana de consola
        "--name=IBA-SoftVisorLogs",          # Nombre del ejecutable
        "--clean",                           # Limpiar cache
        "--noconfirm",                       # No pedir confirmación
        "--icon=NONE",                       # Sin icono específico
        "src/visor_logs.py"                      # Archivo del visor
    ]
    
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, cwd="..")
        
        if resultado.returncode == 0:
            print("✅ ¡EJECUTABLE DEL VISOR CREADO EXITOSAMENTE!")
            
            # Verificar que el archivo se creó
            exe_path = "../dist/IBA-SoftVisorLogs.exe"
            if os.path.exists(exe_path):
                size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"📁 Ubicación: {os.path.abspath(exe_path)}")
                print(f"📏 Tamaño: {size_mb:.2f} MB")
                return True
            else:
                print("❌ Error: El ejecutable del visor no se creó correctamente")
                return False
        else:
            print("❌ Error al crear el ejecutable del visor:")
            print(resultado.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error ejecutando PyInstaller para el visor: {e}")
        return False

def crear_ambos_ejecutables():
    """Crea ambos ejecutables: principal y visor"""
    print("🏭 GENERANDO EJECUTABLES AJPD SOFT")
    print("=" * 60)
    
    exito_principal = crear_ejecutable_principal()
    exito_visor = crear_ejecutable_visor()
    
    return exito_principal and exito_visor

def mostrar_ejemplos_uso():
    """Muestra ejemplos de cómo usar el ejecutable"""
    print("\n🎯 EJEMPLOS DE USO DE LOS EJECUTABLES:")
    print("-" * 50)
    
    print("📧 ENVIAR EMAIL:")
    print('IBA-SoftEnvioSMS.exe EMAIL "destino@ejemplo.com" "<h1>Mi mensaje</h1>" "587" "usuario@gmail.com" "password_app" "smtp.gmail.com" "True"')
    
    print("\n📱 ENVIAR SMS:")
    print('IBA-SoftEnvioSMS.exe SMS "+1234567890" "Mensaje de prueba" "COM3"')
    
    print("\n📊 VER LOGS:")
    print('IBA-SoftVisorLogs.exe')
    
    print("\n💡 AYUDA:")
    print('IBA-SoftEnvioSMS.exe')

def crear_script_uso():
    """Crea un script de ejemplo para usar los ejecutables"""
    contenido = '''@echo off
REM Script de ejemplo para usar IBA-Soft Envío SMS/Email
REM Edita las variables con tus datos reales

echo ===============================================
echo    AJPD SOFT - SISTEMA DE ENVIO SMS/EMAIL
echo ===============================================

set EMAIL_DESTINO=destino@ejemplo.com
set EMAIL_USUARIO=tu_usuario@gmail.com
set EMAIL_PASSWORD=tu_contraseña_de_aplicacion
set SMS_NUMERO=+1234567890
set SMS_PUERTO=COM3

echo.
echo ¿Qué quieres hacer?
echo 1. Email de prueba
echo 2. SMS de prueba
echo 3. Ver logs
echo 4. Visor de logs interactivo
echo 5. Salir
echo.
set /p opcion="Elige una opción (1-5): "

if "%opcion%"=="1" goto email
if "%opcion%"=="2" goto sms
if "%opcion%"=="3" goto logs
if "%opcion%"=="4" goto visor
if "%opcion%"=="5" goto salir
goto salir

:email
echo.
echo 📧 Enviando email de prueba...
IBA-SoftEnvioSMS.exe EMAIL "%EMAIL_DESTINO%" "<h1>Prueba</h1><p>Este es un email de prueba del sistema IBA-Soft.</p>" "587" "%EMAIL_USUARIO%" "%EMAIL_PASSWORD%" "smtp.gmail.com" "True"
pause
goto salir

:sms
echo.
echo 📱 Enviando SMS de prueba...
IBA-SoftEnvioSMS.exe SMS "%SMS_NUMERO%" "Prueba SMS desde IBA-Soft" "%SMS_PUERTO%"
pause
goto salir

:logs
echo.
echo 📊 Mostrando logs recientes...
if exist logs\\*.log (
    dir logs\\*.log /O-D
    echo.
    echo Contenido del log más reciente:
    for /f %%i in ('dir logs\\*.log /b /O-D') do (
        type "logs\\%%i" | more
        goto fin_logs
    )
    :fin_logs
) else (
    echo No se encontraron archivos de log.
)
pause
goto salir

:visor
echo.
echo 🔍 Abriendo visor de logs...
IBA-SoftVisorLogs.exe
goto salir

:salir
echo.
echo ¡Hasta luego!
pause
'''
    
    with open("usar_IBA-Soft.bat", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print(f"\n📜 Script de ejemplo mejorado creado: usar_IBA-Soft.bat")

def crear_instalador():
    """Crea un instalador simple"""
    contenido = '''@echo off
echo ===============================================
echo    INSTALADOR AJPD SOFT ENVIO SMS/EMAIL
echo ===============================================

REM Crear directorio de instalación
set INSTALL_DIR=C:\\IBA-Soft\\EnvioSMS
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

REM Copiar ejecutables
echo 📁 Copiando archivos...
copy "dist\\IBA-SoftEnvioSMS.exe" "%INSTALL_DIR%\\"
copy "dist\\IBA-SoftVisorLogs.exe" "%INSTALL_DIR%\\"
copy "usar_IBA-Soft.bat" "%INSTALL_DIR%\\"
copy "README.md" "%INSTALL_DIR%\\"
copy "DOCUMENTACION_LOGGING.md" "%INSTALL_DIR%\\"

REM Crear directorio de logs
if not exist "%INSTALL_DIR%\\logs" mkdir "%INSTALL_DIR%\\logs"

REM Agregar al PATH (opcional)
echo.
echo ¿Quieres agregar IBA-Soft al PATH del sistema? (s/n)
set /p add_path="Esto permitirá usar los comandos desde cualquier ubicación: "

if /i "%add_path%"=="s" (
    echo 🔧 Agregando al PATH...
    setx PATH "%PATH%;%INSTALL_DIR%" /M
    echo ✅ Agregado al PATH del sistema
)

echo.
echo ✅ ¡Instalación completada!
echo 📁 Ubicación: %INSTALL_DIR%
echo 🚀 Ejecuta: %INSTALL_DIR%\\usar_IBA-Soft.bat
echo 📧 Envío SMS/Email: %INSTALL_DIR%\\IBA-SoftEnvioSMS.exe
echo 📊 Visor de logs: %INSTALL_DIR%\\IBA-SoftVisorLogs.exe
echo.
pause
'''
    
    with open("instalar_IBA-Soft.bat", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print(f"📦 Instalador mejorado creado: instalar_IBA-Soft.bat")

def main():
    """Función principal"""
    print("🏭 GENERADOR DE EJECUTABLE AJPD SOFT")
    print("=" * 60)
    
    # Verificar entorno
    if not os.path.exists("../.venv"):
        print("❌ Error: No se encuentra el entorno virtual")
        print("💡 Ejecuta primero: python -m venv .venv")
        return
    
    # Crear ejecutables
    if crear_ambos_ejecutables():
        # Crear archivos adicionales
        crear_script_uso()
        crear_instalador()
        
        print("\n🎉 ¡PROCESO COMPLETADO!")
        print(f"✅ Ejecutable principal: ../dist/IBA-SoftEnvioSMS.exe")
        print(f"✅ Ejecutable visor logs: ../dist/IBA-SoftVisorLogs.exe")
        print(f"✅ Script de uso: usar_IBA-Soft.bat")
        print(f"✅ Instalador: instalar_IBA-Soft.bat")
        
        print(f"\n📦 PARA DISTRIBUIR:")
        print(f"1. Copia la carpeta 'dist' completa")
        print(f"2. Incluye usar_IBA-Soft.bat e instalar_IBA-Soft.bat")
        print(f"3. O ejecuta 'instalar_IBA-Soft.bat' como administrador")
        
    else:
        print("\n❌ Error al crear los ejecutables")
        print("💡 Revisa los errores mostrados arriba")

if __name__ == "__main__":
    main()
