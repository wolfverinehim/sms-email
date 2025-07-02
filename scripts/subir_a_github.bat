@echo off
echo ===============================================
echo    PREPARANDO PROYECTO PARA GITHUB
echo ===============================================

echo.
echo 🔧 Paso 1: Inicializando repositorio Git...
git init

echo.
echo 📝 Paso 2: Configurando usuario Git (si es necesario)...
set /p git_name="Introduce tu nombre de usuario Git: "
set /p git_email="Introduce tu email Git: "
git config user.name "%git_name%"
git config user.email "%git_email%"

echo.
echo 📁 Paso 3: Verificando archivos a excluir...
if exist config.ini (
    echo ✅ config.ini existe y será excluido por .gitignore
) else (
    echo ⚠️  config.ini no existe - recuerda no subirlo nunca
)

if exist logs (
    echo ✅ Directorio logs/ será excluido por .gitignore
)

if exist .venv (
    echo ✅ Entorno virtual .venv/ será excluido por .gitignore
)

echo.
echo 📦 Paso 4: Agregando archivos al repositorio...
git add .
git status

echo.
echo 💬 Paso 5: Realizando commit inicial...
git commit -m "Initial commit: IBA-Soft SMS/Email System

✅ Features:
- SMS sending via GSM modem
- Email sending with HTML support  
- Advanced logging system
- Independent executables
- Interactive log viewer
- Secure configuration management
- Gmail integration with app passwords

📦 Structure:
- Main script: envio_sms_email.py
- Log viewer: visor_logs.py
- Executables: dist/IBA-Soft*.exe
- Configuration: config.ini.ejemplo
- Documentation: README.md and docs/

🔒 Security:
- Credentials in external config
- Passwords masked in logs
- Sensitive files excluded from Git"

echo.
echo 🌐 Paso 6: Configurando repositorio remoto...
echo.
echo "Ve a GitHub y crea un nuevo repositorio llamado 'IBA-Soft-sms-email'"
echo "Luego ejecuta estos comandos:"
echo.
echo "git branch -M main"
echo "git remote add origin https://github.com/TU_USUARIO/IBA-Soft-sms-email.git"
echo "git push -u origin main"
echo.

set /p repo_url="Introduce la URL completa de tu repositorio GitHub: "
if not "%repo_url%"=="" (
    echo.
    echo 🔗 Configurando repositorio remoto...
    git branch -M main
    git remote add origin "%repo_url%"
    
    echo.
    echo 🚀 Subiendo a GitHub...
    git push -u origin main
    
    if %ERRORLEVEL% EQU 0 (
        echo.
        echo ✅ ¡PROYECTO SUBIDO EXITOSAMENTE A GITHUB!
        echo 🌐 Tu repositorio: %repo_url%
        echo.
        echo 📋 PRÓXIMOS PASOS:
        echo 1. Ve a tu repositorio en GitHub
        echo 2. Verifica que config.ini NO aparezca (debe estar excluido)
        echo 3. Verifica que la documentación se vea correctamente
        echo 4. Considera hacer el repositorio público
        echo 5. Agrega topics/tags relevantes (python, sms, email, automation)
        echo.
    ) else (
        echo.
        echo ❌ Error al subir a GitHub
        echo 💡 Verifica la URL del repositorio y tus credenciales
    )
) else (
    echo.
    echo ⏸️  Configuración manual pendiente
    echo 💡 Ejecuta los comandos mostrados arriba cuando tengas el repositorio creado
)

echo.
echo 📊 RESUMEN DEL PROYECTO:
echo - Archivos Python: %cd%\*.py
echo - Ejecutables: %cd%\dist\*.exe  
echo - Documentación: README.md, docs\*.md
echo - Configuración: config.ini.ejemplo (template)
echo - Exclusiones: config.ini, logs/, .venv/ (en .gitignore)
echo.
pause
