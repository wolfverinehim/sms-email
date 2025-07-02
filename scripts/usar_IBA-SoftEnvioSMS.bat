@echo off
chcp 65001 >nul
REM Script interactivo para usar IBA-SoftEnvioSMS
REM Permite enviar SMS y emails de forma facil e interactiva

echo ===============================================
echo    IBA-SOFT - SISTEMA DE ENVIO SMS/EMAIL
echo ===============================================

echo.
echo Que quieres hacer?
echo 1. Enviar Email (con credenciales)
echo 2. Enviar Email (modo seguro - usa config.ini)
echo 3. Enviar SMS
echo 4. Detectar modem GSM
echo 5. Ver logs
echo 6. Configurar Gmail
echo 7. Salir
echo.
set /p opcion="Elige una opcion (1-7): "

if "%opcion%"=="1" goto email
if "%opcion%"=="2" goto email_seguro
if "%opcion%"=="3" goto sms
if "%opcion%"=="4" goto detectar_modem
if "%opcion%"=="5" goto ver_logs
if "%opcion%"=="6" goto configurar_gmail
if "%opcion%"=="7" goto salir
goto salir

:email
echo.
echo =====================================
echo    CONFIGURACION DE EMAIL
echo =====================================
echo.
echo Consejos para Gmail:
echo    - Usa tu email completo (@gmail.com)
echo    - Usa contrasena de aplicacion (16 caracteres)
echo    - Activa verificacion en 2 pasos antes
echo.
set /p EMAIL_DESTINO="Email destino: "
echo.
echo Puedes usar HTML: ^<h1^>Titulo^</h1^>^<p^>Texto^</p^>
set /p EMAIL_MENSAJE="Mensaje: "
echo.
set /p EMAIL_USUARIO="Tu usuario Gmail: "
set /p EMAIL_PASSWORD="Contrasena de aplicacion: "

echo.
echo Enviando email...
echo    De: %EMAIL_USUARIO%
echo    Para: %EMAIL_DESTINO%
echo.
..\dist\IBA-SoftEnvioSMS.exe EMAIL "%EMAIL_DESTINO%" "%EMAIL_MENSAJE%" "587" "%EMAIL_USUARIO%" "%EMAIL_PASSWORD%" "smtp.gmail.com" "True"
pause
goto salir

:sms
echo.
echo =====================================
echo    CONFIGURACION DE SMS
echo =====================================
echo.
echo Requisitos para SMS:
echo    - Modem GSM conectado y configurado
echo    - SIM card activa con saldo
echo    - Drivers del modem instalados
echo.
set /p SMS_NUMERO="Numero destino (+34612345678): "
set /p SMS_MENSAJE="Mensaje SMS (max 160 caracteres): "
echo.
echo Puertos comunes: COM3, COM4, COM5
set /p SMS_PUERTO="Puerto COM del modem: "

echo.
echo Enviando SMS...
echo    Para: %SMS_NUMERO%
echo    Puerto: %SMS_PUERTO%
echo.
..\dist\IBA-SoftEnvioSMS.exe SMS "%SMS_NUMERO%" "%SMS_MENSAJE%" "%SMS_PUERTO%"
pause
goto salir

:email_seguro
echo.
echo =====================================
echo    EMAIL MODO SEGURO
echo =====================================
echo.
echo Este modo usa las credenciales de config.ini
echo    - Mas seguro (no expone credenciales)
echo    - Requiere config.ini configurado
echo.
set /p EMAIL_DESTINO="Email destino: "
echo.
echo Puedes usar HTML: ^<h1^>Titulo^</h1^>^<p^>Texto^</p^>
set /p EMAIL_MENSAJE="Mensaje: "

echo.
echo Enviando email de forma segura...
echo    Para: %EMAIL_DESTINO%
echo    Credenciales: Desde config.ini
echo.
..\dist\IBA-SoftEnvioSMS.exe EMAIL "%EMAIL_DESTINO%" "%EMAIL_MENSAJE%"
pause
goto salir

:configurar_gmail
echo.
echo =====================================
echo    CONFIGURADOR DE GMAIL
echo =====================================
echo.
echo Ejecutando configurador seguro de Gmail...
echo Este proceso te ayudara a configurar las credenciales
echo.
python ..\tools\configurar_gmail_seguro.py
pause
goto salir

:detectar_modem
echo.
echo =====================================
echo    DETECTOR DE MODEM GSM
echo =====================================
echo.
echo Detectando modems GSM conectados...
python ..\tools\detectar_modem.py
pause
goto salir

:ver_logs
echo.
echo =====================================
echo    VISOR DE LOGS
echo =====================================
echo.
echo Abriendo visor de logs...
..\dist\IBA-SoftVisorLogs.exe
goto salir

:salir
echo.
echo Hasta luego!
pause
