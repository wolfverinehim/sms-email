@echo off
REM Script de ejemplo para usar AjpdSoftEnvioSMS.exe
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
echo ¿Qué quieres enviar?
echo 1. Email de prueba
echo 2. SMS de prueba
echo 3. Salir
echo.
set /p opcion="Elige una opción (1-3): "

if "%opcion%"=="1" goto email
if "%opcion%"=="2" goto sms
if "%opcion%"=="3" goto salir
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

:salir
echo.
echo ¡Hasta luego!
pause
