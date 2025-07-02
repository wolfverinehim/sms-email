@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion
echo ===============================================
echo    INSTALADOR IBA-SOFT ENVIO SMS/EMAIL
echo ===============================================

REM Cambiar al directorio del script
cd /d "%~dp0"

REM Verificar archivos requeridos
echo 🔍 Verificando archivos...
if not exist "..\dist\IBA-SoftEnvioSMS.exe" (
    echo ❌ Error: No se encuentra IBA-SoftEnvioSMS.exe
    echo 💡 Ejecuta primero: python tools\crear_ejecutable.py
    echo 📁 Buscando en: %CD%\..\dist\
    pause
    exit /b 1
)

if not exist "..\dist\IBA-SoftVisorLogs.exe" (
    echo ❌ Error: No se encuentra IBA-SoftVisorLogs.exe
    echo 💡 Ejecuta primero: python tools\crear_ejecutable.py
    echo 📁 Buscando en: %CD%\..\dist\
    pause
    exit /b 1
)

if not exist "usar_IBA-SoftEnvioSMS.bat" (
    echo ❌ Error: No se encuentra usar_IBA-SoftEnvioSMS.bat
    echo 📁 Buscando en: %CD%\
    pause
    exit /b 1
)

echo ✅ Todos los archivos necesarios están presentes

REM Crear directorio de instalación
echo.
echo 📁 Creando directorio de instalación...
set INSTALL_DIR=C:\IBA-Soft\EnvioSMS
if not exist "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%"
    echo ✅ Directorio creado: %INSTALL_DIR%
) else (
    echo ℹ️  Directorio ya existe: %INSTALL_DIR%
)

REM Copiar ejecutables
echo.
echo 📦 Copiando archivos principales...
copy "..\dist\IBA-SoftEnvioSMS.exe" "%INSTALL_DIR%\" >nul
if %ERRORLEVEL% EQU 0 (
    echo ✅ IBA-SoftEnvioSMS.exe
) else (
    echo ❌ Error copiando IBA-SoftEnvioSMS.exe
)

copy "..\dist\IBA-SoftVisorLogs.exe" "%INSTALL_DIR%\" >nul
if %ERRORLEVEL% EQU 0 (
    echo ✅ IBA-SoftVisorLogs.exe
) else (
    echo ❌ Error copiando IBA-SoftVisorLogs.exe
)

copy "usar_IBA-SoftEnvioSMS.bat" "%INSTALL_DIR%\" >nul
if %ERRORLEVEL% EQU 0 (
    echo ✅ usar_IBA-SoftEnvioSMS.bat
) else (
    echo ❌ Error copiando usar_IBA-SoftEnvioSMS.bat
)

echo.
echo 📚 Copiando documentación...
copy "..\README.md" "%INSTALL_DIR%\" >nul
if %ERRORLEVEL% EQU 0 (
    echo ✅ README.md
) else (
    echo ⚠️  README.md no copiado
)

if exist "..\docs\DOCUMENTACION_LOGGING.md" (
    copy "..\docs\DOCUMENTACION_LOGGING.md" "%INSTALL_DIR%\" >nul
    if %ERRORLEVEL% EQU 0 (
        echo ✅ DOCUMENTACION_LOGGING.md
    ) else (
        echo ⚠️  DOCUMENTACION_LOGGING.md no copiado
    )
)

echo.
echo 🔧 Copiando archivos de configuración...
if exist "..\config\config.ini.ejemplo" (
    copy "..\config\config.ini.ejemplo" "%INSTALL_DIR%\" >nul
    if %ERRORLEVEL% EQU 0 (
        echo ✅ config.ini.ejemplo
    ) else (
        echo ⚠️  config.ini.ejemplo no copiado
    )
)

REM Crear directorio de logs
echo.
echo 📊 Configurando directorios adicionales...
if not exist "%INSTALL_DIR%\logs" (
    mkdir "%INSTALL_DIR%\logs"
    echo ✅ Directorio logs/ creado
) else (
    echo ℹ️  Directorio logs/ ya existe
)

REM Verificar permisos para modificar PATH
echo.
echo 🔐 Verificando permisos administrativos...
net session >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set ADMIN_PERMS=true
    echo ✅ Permisos administrativos disponibles
) else (
    set ADMIN_PERMS=false
    echo ⚠️  Sin permisos administrativos - PATH no se puede modificar automáticamente
)

REM Agregar al PATH (opcional)
echo.
if "%ADMIN_PERMS%"=="true" (
    echo ¿Quieres agregar IBA-Soft al PATH del sistema? (s/n)
    set /p add_path="Esto permitirá usar los comandos desde cualquier ubicación: "
    
    if /i "!add_path!"=="s" (
        echo 🔧 Agregando al PATH del sistema...
        setx PATH "%PATH%;%INSTALL_DIR%" /M >nul 2>&1
        if !ERRORLEVEL! EQU 0 (
            echo ✅ Agregado al PATH del sistema correctamente
        ) else (
            echo ❌ Error agregando al PATH del sistema
        )
    )
) else (
    echo 💡 Para agregar al PATH manualmente:
    echo    1. Abre "Variables de entorno del sistema"
    echo    2. Edita la variable PATH
    echo    3. Agrega: %INSTALL_DIR%
)

REM Crear acceso directo en el escritorio (opcional)
echo.
echo 🖥️ ¿Crear acceso directo en el escritorio? (s/n)
set /p crear_acceso="Esto creará un acceso directo para fácil acceso: "

if /i "!crear_acceso!"=="s" (
    echo 🔗 Creando acceso directo...
    set DESKTOP=%USERPROFILE%\Desktop
    echo @echo off > "!DESKTOP!\IBA-Soft SMS Email.bat"
    echo cd /d "%INSTALL_DIR%" >> "!DESKTOP!\IBA-Soft SMS Email.bat"
    echo start usar_IBA-SoftEnvioSMS.bat >> "!DESKTOP!\IBA-Soft SMS Email.bat"
    echo ✅ Acceso directo creado en el escritorio
)

echo.
echo ===============================================
echo           ✅ ¡INSTALACIÓN COMPLETADA!
echo ===============================================
echo 📁 Ubicación: %INSTALL_DIR%
echo.
echo 🚀 COMANDOS DISPONIBLES:
echo    Interfaz interactiva: %INSTALL_DIR%\usar_IBA-SoftEnvioSMS.bat
echo    Envío directo SMS/Email: %INSTALL_DIR%\IBA-SoftEnvioSMS.exe
echo    Visor de logs: %INSTALL_DIR%\IBA-SoftVisorLogs.exe
echo.
echo 📋 PRÓXIMOS PASOS:
echo    1. Copia config.ini.ejemplo a config.ini
echo    2. Edita config.ini con tus credenciales
echo    3. Ejecuta usar_IBA-SoftEnvioSMS.bat para empezar
echo.
echo 💡 DOCUMENTACIÓN:
echo    - README.md: Guía completa de uso
echo    - DOCUMENTACION_LOGGING.md: Sistema de logs
echo.
if "%ADMIN_PERMS%"=="true" if /i "%add_path%"=="s" (
    echo 🌐 IBA-Soft agregado al PATH - puedes usar los comandos desde cualquier ubicación
    echo.
)
pause
