@echo off
echo ===============================================
echo   PRUEBA DE PARAMETROS CON ESPACIOS
echo ===============================================

echo.
echo 🧪 Caso 1: Contraseña con espacios (entrecomillada)
IBA-SoftEnvioSMS.exe EMAIL "test@ejemplo.com" "Mensaje de prueba" "587" "usuario@gmail.com" "zzns wtrh utjd epux" "smtp.gmail.com" "True"

echo.
echo 🧪 Caso 2: Sin entrecomillar (problema simulado)
IBA-SoftEnvioSMS.exe EMAIL test@ejemplo.com Mensaje_sin_espacios 587 usuario@gmail.com zzns wtrh utjd epux smtp.gmail.com True

echo.
echo 🧪 Caso 3: Mensaje y contraseña con espacios
IBA-SoftEnvioSMS.exe EMAIL "ivan.becerro@gmail.com" "Le recordamos su cita para el miercoles" "587" "infonutribel@gmail.com" "zzns wtrh utjd epux" "smtp.gmail.com" "True"

echo.
echo ✅ Pruebas completadas. Revisa los logs en la carpeta logs/
pause
