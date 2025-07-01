@echo off
echo ===============================================
echo    INSTALADOR AJPD SOFT ENVIO SMS/EMAIL
echo ===============================================

REM Crear directorio de instalación
set INSTALL_DIR=C:\AjpdSoft\EnvioSMS
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

REM Copiar ejecutables
echo 📁 Copiando archivos...
copy "dist\AjpdSoftEnvioSMS.exe" "%INSTALL_DIR%\"
copy "dist\AjpdSoftVisorLogs.exe" "%INSTALL_DIR%\"
copy "usar_AjpdSoft.bat" "%INSTALL_DIR%\"
copy "README.md" "%INSTALL_DIR%\"
copy "DOCUMENTACION_LOGGING.md" "%INSTALL_DIR%\"

REM Crear directorio de logs
if not exist "%INSTALL_DIR%\logs" mkdir "%INSTALL_DIR%\logs"

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
echo 🚀 Ejecuta: %INSTALL_DIR%\usar_AjpdSoft.bat
echo 📧 Envío SMS/Email: %INSTALL_DIR%\AjpdSoftEnvioSMS.exe
echo 📊 Visor de logs: %INSTALL_DIR%\AjpdSoftVisorLogs.exe
echo.
pause
