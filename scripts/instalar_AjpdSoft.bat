@echo off
echo ===============================================
echo    INSTALADOR AJPD SOFT ENVIO SMS/EMAIL
echo ===============================================

REM Crear directorio de instalación
set INSTALL_DIR=C:\IBA-Soft\EnvioSMS
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

REM Copiar ejecutables
echo 📁 Copiando archivos...
copy "dist\IBA-SoftEnvioSMS.exe" "%INSTALL_DIR%\"
copy "dist\IBA-SoftVisorLogs.exe" "%INSTALL_DIR%\"
copy "usar_IBA-Soft.bat" "%INSTALL_DIR%\"
copy "README.md" "%INSTALL_DIR%\"
copy "DOCUMENTACION_LOGGING.md" "%INSTALL_DIR%\"

REM Crear directorio de logs
if not exist "%INSTALL_DIR%\logs" mkdir "%INSTALL_DIR%\logs"

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
echo 🚀 Ejecuta: %INSTALL_DIR%\usar_IBA-Soft.bat
echo 📧 Envío SMS/Email: %INSTALL_DIR%\IBA-SoftEnvioSMS.exe
echo 📊 Visor de logs: %INSTALL_DIR%\IBA-SoftVisorLogs.exe
echo.
pause
