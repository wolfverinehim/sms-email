#!/usr/bin/env python3
"""
Script para crear el ejecutable AjpdSoftEnvioSMS.exe
"""

import subprocess
import os
import sys
import shutil

def crear_ejecutable_principal():
    """Crea el ejecutable principal usando PyInstaller"""
    print("🔧 CREANDO EJECUTABLE AjpdSoftEnvioSMS.exe")
    print("=" * 60)
    
    # Verificar que el archivo principal existe
    if not os.path.exists("envio_sms_email.py"):
        print("❌ Error: No se encuentra envio_sms_email.py")
        return False
    
    print("📂 Limpiando archivos anteriores...")
    # Limpiar directorios anteriores
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("AjpdSoftEnvioSMS.spec"):
        os.remove("AjpdSoftEnvioSMS.spec")
    
    print("🏗️ Generando ejecutable...")
    
    # Comando PyInstaller con opciones optimizadas
    comando = [
        "f:/TFS/smspy/.venv/Scripts/pyinstaller.exe",
        "--onefile",                          # Un solo archivo ejecutable
        "--console",                          # Mantener ventana de consola
        "--name=AjpdSoftEnvioSMS",           # Nombre del ejecutable
        "--clean",                           # Limpiar cache
        "--noconfirm",                       # No pedir confirmación
        "--add-data=requirements.txt;.",     # Incluir requirements.txt
        "envio_sms_email.py"                 # Archivo principal
    ]
    
    try:
        print("🔄 Ejecutando PyInstaller...")
        resultado = subprocess.run(comando, capture_output=True, text=True, cwd="f:/TFS/smspy")
        
        if resultado.returncode == 0:
            print("✅ ¡EJECUTABLE CREADO EXITOSAMENTE!")
            
            # Verificar que el archivo se creó
            exe_path = "dist/AjpdSoftEnvioSMS.exe"
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
    print("\n🔧 CREANDO EJECUTABLE AjpdSoftVisorLogs.exe")
    print("=" * 60)
    
    # Verificar que el archivo del visor existe
    if not os.path.exists("visor_logs.py"):
        print("❌ Error: No se encuentra visor_logs.py")
        return False
    
    print("🏗️ Generando ejecutable del visor...")
    
    # Comando PyInstaller para el visor
    comando = [
        "f:/TFS/smspy/.venv/Scripts/pyinstaller.exe",
        "--onefile",                          # Un solo archivo ejecutable
        "--console",                          # Mantener ventana de consola
        "--name=AjpdSoftVisorLogs",          # Nombre del ejecutable
        "--clean",                           # Limpiar cache
        "--noconfirm",                       # No pedir confirmación
        "--icon=NONE",                       # Sin icono específico
        "visor_logs.py"                      # Archivo del visor
    ]
    
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, cwd="f:/TFS/smspy")
        
        if resultado.returncode == 0:
            print("✅ ¡EJECUTABLE DEL VISOR CREADO EXITOSAMENTE!")
            
            # Verificar que el archivo se creó
            exe_path = "dist/AjpdSoftVisorLogs.exe"
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
    print('AjpdSoftEnvioSMS.exe EMAIL "destino@ejemplo.com" "<h1>Mi mensaje</h1>" "587" "usuario@gmail.com" "password_app" "smtp.gmail.com" "True"')
    
    print("\n📱 ENVIAR SMS:")
    print('AjpdSoftEnvioSMS.exe SMS "+1234567890" "Mensaje de prueba" "COM3"')
    
    print("\n📊 VER LOGS:")
    print('AjpdSoftVisorLogs.exe')
    
    print("\n💡 AYUDA:")
    print('AjpdSoftEnvioSMS.exe')

def crear_script_uso():
    """Crea un script de ejemplo para usar los ejecutables"""
    contenido = '''@echo off
REM Script de ejemplo para usar AjpdSoft Envío SMS/Email
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
AjpdSoftEnvioSMS.exe EMAIL "%EMAIL_DESTINO%" "<h1>Prueba</h1><p>Este es un email de prueba del sistema AjpdSoft.</p>" "587" "%EMAIL_USUARIO%" "%EMAIL_PASSWORD%" "smtp.gmail.com" "True"
pause
goto salir

:sms
echo.
echo 📱 Enviando SMS de prueba...
AjpdSoftEnvioSMS.exe SMS "%SMS_NUMERO%" "Prueba SMS desde AjpdSoft" "%SMS_PUERTO%"
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
AjpdSoftVisorLogs.exe
goto salir

:salir
echo.
echo ¡Hasta luego!
pause
'''
    
    with open("usar_AjpdSoft.bat", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print(f"\n📜 Script de ejemplo mejorado creado: usar_AjpdSoft.bat")

def crear_instalador():
    """Crea un instalador simple"""
    contenido = '''@echo off
echo ===============================================
echo    INSTALADOR AJPD SOFT ENVIO SMS/EMAIL
echo ===============================================

REM Crear directorio de instalación
set INSTALL_DIR=C:\\AjpdSoft\\EnvioSMS
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

REM Copiar ejecutables
echo 📁 Copiando archivos...
copy "dist\\AjpdSoftEnvioSMS.exe" "%INSTALL_DIR%\\"
copy "dist\\AjpdSoftVisorLogs.exe" "%INSTALL_DIR%\\"
copy "usar_AjpdSoft.bat" "%INSTALL_DIR%\\"
copy "README.md" "%INSTALL_DIR%\\"
copy "DOCUMENTACION_LOGGING.md" "%INSTALL_DIR%\\"

REM Crear directorio de logs
if not exist "%INSTALL_DIR%\\logs" mkdir "%INSTALL_DIR%\\logs"

REM Agregar al PATH (opcional)
echo.
echo ¿Quieres agregar AjpdSoft al PATH del sistema? (s/n)
set /p add_path="Esto permitirá usar los comandos desde cualquier ubicación: "

if /i "%add_path%"=="s" (
    echo 🔧 Agregando al PATH...
    setx PATH "%PATH%;%INSTALL_DIR%" /M
    echo ✅ Agregado al PATH del sistema
)

echo.
echo ✅ ¡Instalación completada!
echo 📁 Ubicación: %INSTALL_DIR%
echo 🚀 Ejecuta: %INSTALL_DIR%\\usar_AjpdSoft.bat
echo 📧 Envío SMS/Email: %INSTALL_DIR%\\AjpdSoftEnvioSMS.exe
echo 📊 Visor de logs: %INSTALL_DIR%\\AjpdSoftVisorLogs.exe
echo.
pause
'''
    
    with open("instalar_AjpdSoft.bat", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print(f"📦 Instalador mejorado creado: instalar_AjpdSoft.bat")

def main():
    """Función principal"""
    print("🏭 GENERADOR DE EJECUTABLE AJPD SOFT")
    print("=" * 60)
    
    # Verificar entorno
    if not os.path.exists(".venv"):
        print("❌ Error: No se encuentra el entorno virtual")
        print("💡 Ejecuta primero: python -m venv .venv")
        return
    
    # Crear ejecutables
    if crear_ambos_ejecutables():
        # Crear archivos adicionales
        crear_script_uso()
        crear_instalador()
        
        print("\n🎉 ¡PROCESO COMPLETADO!")
        print(f"✅ Ejecutable principal: dist/AjpdSoftEnvioSMS.exe")
        print(f"✅ Ejecutable visor logs: dist/AjpdSoftVisorLogs.exe")
        print(f"✅ Script de uso: usar_AjpdSoft.bat")
        print(f"✅ Instalador: instalar_AjpdSoft.bat")
        
        print(f"\n📦 PARA DISTRIBUIR:")
        print(f"1. Copia la carpeta 'dist' completa")
        print(f"2. Incluye usar_AjpdSoft.bat e instalar_AjpdSoft.bat")
        print(f"3. O ejecuta 'instalar_AjpdSoft.bat' como administrador")
        
    else:
        print("\n❌ Error al crear los ejecutables")
        print("💡 Revisa los errores mostrados arriba")

if __name__ == "__main__":
    main()
