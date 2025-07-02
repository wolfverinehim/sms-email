# IBA-SoftEnvioSMS.exe - Sistema de Envío SMS y Email

## 📋 **DESCRIPCIÓN**
IBA-SoftEnvioSMS.exe es un ejecutable que permite enviar mensajes SMS y emails desde línea de comandos sin necesidad de tener Python instalado.

## 📦 **CONTENIDO DEL PAQUETE**
- `IBA-SoftEnvioSMS.exe` - Ejecutable principal (7.45 MB)
- `usar_IBA-SoftEnvioSMS.bat` - Script de ejemplo interactivo
- `instalar_IBA-Soft.bat` - Instalador automático
- `README_EJECUTABLE.md` - Esta documentación

## 🚀 **INSTALACIÓN**

### Opción A: Instalación Automática (Recomendada)
1. Ejecuta `instalar_IBA-Soft.bat` como **Administrador**
2. Sigue las instrucciones en pantalla
3. El ejecutable se instalará en `C:\IBA-Soft\EnvioSMS\`

### Opción B: Instalación Manual
1. Copia `IBA-SoftEnvioSMS.exe` a cualquier carpeta
2. Agrega la carpeta al PATH de Windows (opcional)

## 💻 **USO**

### 📧 **Enviar Email:**
```cmd
IBA-SoftEnvioSMS.exe EMAIL "destino@ejemplo.com" "<h1>Mi mensaje</h1>" "587" "usuario@gmail.com" "contraseña_app" "smtp.gmail.com" "True"
```

**Parámetros:**
- `EMAIL` - Modo de envío
- `destino@ejemplo.com` - Email destinatario
- `<h1>Mi mensaje</h1>` - Mensaje (soporta HTML)
- `587` - Puerto SMTP
- `usuario@gmail.com` - Tu email Gmail
- `contraseña_app` - Contraseña de aplicación de Gmail (16 caracteres)
- `smtp.gmail.com` - Servidor SMTP
- `True` - Usar SSL/TLS

### 📱 **Enviar SMS:**
```cmd
IBA-SoftEnvioSMS.exe SMS "+1234567890" "Mensaje de prueba" "COM3"
```

**Parámetros:**
- `SMS` - Modo de envío
- `+1234567890` - Número de teléfono
- `Mensaje de prueba` - Texto del SMS
- `COM3` - Puerto COM del módem GSM

### 💡 **Ver Ayuda:**
```cmd
IBA-SoftEnvioSMS.exe
```

## 🔧 **CONFIGURACIÓN GMAIL**

Para usar Gmail necesitas una **contraseña de aplicación**:

1. Ve a: https://myaccount.google.com/security
2. Activa "Verificación en 2 pasos"
3. Ve a: https://myaccount.google.com/apppasswords
4. Genera una contraseña para "Correo" → "Otro"
5. Usa esa contraseña de 16 caracteres (no tu contraseña normal)

## 📱 **CONFIGURACIÓN SMS**

Para SMS necesitas:
- Un módem GSM USB conectado
- Una SIM card activa
- Drivers del módem instalados
- Conocer el puerto COM (ej: COM3, COM4)

## 🎯 **EJEMPLOS PRÁCTICOS**

### Email de Recordatorio:
```cmd
IBA-SoftEnvioSMS.exe EMAIL "cliente@empresa.com" "<h2>Recordatorio de Cita</h2><p>Su cita es mañana a las 10:00 AM.</p>" "587" "infonutribel@gmail.com" "abcd1234efgh5678" "smtp.gmail.com" "True"
```

### SMS de Confirmación:
```cmd
IBA-SoftEnvioSMS.exe SMS "+34612345678" "Su pedido ha sido confirmado. Gracias." "COM3"
```

### Email HTML Complejo:
```cmd
IBA-SoftEnvioSMS.exe EMAIL "usuario@test.com" "<div style='background:#f0f8ff;padding:20px;'><h1 style='color:#4CAF50;'>¡Bienvenido!</h1><p>Su cuenta ha sido activada correctamente.</p></div>" "587" "admin@miempresa.com" "passwordapp123" "smtp.gmail.com" "True"
```

## 🔒 **SEGURIDAD**

- ✅ **Usa contraseñas de aplicación** para Gmail
- ✅ **No compartas** tus credenciales
- ✅ **Revisa los logs** de envío
- ❌ **No uses** contraseñas normales en scripts
- ❌ **No hardcodees** credenciales en batch files

## 🛠️ **SOLUCIÓN DE PROBLEMAS**

### Error: "No se puede conectar al servidor SMTP"
- Verifica la conexión a internet
- Confirma los datos del servidor SMTP
- Revisa la configuración del firewall

### Error: "Autenticación fallida"
- Verifica que uses contraseña de aplicación (no la normal)
- Confirma que la verificación en 2 pasos esté activa
- Regenera la contraseña de aplicación si es necesario

### Error: "Puerto COM no encontrado"
- Verifica que el módem esté conectado
- Instala los drivers del módem
- Usa el Administrador de Dispositivos para verificar el puerto

### Error: "Comando no reconocido"
- Verifica que el ejecutable esté en el PATH
- Usa la ruta completa al ejecutable
- Ejecuta desde la carpeta donde está el .exe

## 📞 **SOPORTE**

Para soporte técnico:
1. Revisa esta documentación
2. Verifica los ejemplos de uso
3. Consulta los logs de error

## 📄 **INFORMACIÓN TÉCNICA**

- **Desarrollado en:** Python 3.13
- **Compilado con:** PyInstaller 6.10.0
- **Dependencias incluidas:** pyserial, smtplib, email
- **Tamaño:** 7.45 MB
- **Compatible con:** Windows 10/11
- **Arquitectura:** x64

## 📝 **CHANGELOG**

### v1.0 (Julio 2025)
- ✅ Envío de emails HTML via SMTP
- ✅ Envío de SMS via módem GSM
- ✅ Soporte para Gmail con contraseñas de aplicación
- ✅ Ejecutable independiente sin dependencias
- ✅ Scripts de instalación incluidos

---

**© 2025 IBA-Soft - Sistema de Envío SMS y Email**
