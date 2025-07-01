@echo off
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
if exist logs\*.log (
    dir logs\*.log /O-D
    echo.
    echo Contenido del log más reciente:
    for /f %%i in ('dir logs\*.log /b /O-D') do (
        type "logs\%%i" | more
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
