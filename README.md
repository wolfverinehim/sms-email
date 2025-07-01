# 📱📧 AjpdSoft - Sistema de Envío SMS y Email

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)

Sistema completo para envío de mensajes SMS (vía módem GSM) y emails (vía SMTP) con logging avanzado y ejecutables independientes.

## 🚀 **CARACTERÍSTICAS PRINCIPALES**

- ✅ **Envío de SMS** via módem GSM con comandos AT
- ✅ **Envío de emails** con soporte HTML completo
- ✅ **Sistema de logging** detallado con timestamps
- ✅ **Ejecutables independientes** sin dependencias externas
- ✅ **Visor de logs** interactivo y análisis de estadísticas
- ✅ **Seguridad** - credenciales protegidas y enmascaradas
- ✅ **Compatibilidad Gmail** con contraseñas de aplicación
- ✅ **Configuración externa** sin hardcodear credenciales

## 📦 **ESTRUCTURA DEL PROYECTO**

```
smspy/
├── 📄 envio_sms_email.py          # Script principal
├── 📊 visor_logs.py               # Visualizador de logs
├── 🔧 configurar_gmail_seguro.py  # Configurador de Gmail
├── 🔍 detectar_modem.py           # Detector de módem GSM
├── 🏗️ crear_ejecutable.py         # Generador de ejecutables
├── 📋 validar_config.py           # Validador de configuración
├── 📁 dist/                       # Ejecutables generados
│   ├── AjpdSoftEnvioSMS.exe      # Ejecutable principal (7.45 MB)
│   └── AjpdSoftVisorLogs.exe     # Ejecutable visor (6.85 MB)
├── 📁 logs/                       # Logs del sistema (ignorado en Git)
├── ⚙️ config.ini.ejemplo         # Plantilla de configuración
├── 🔒 .gitignore                 # Archivos excluidos de Git
└── 📚 docs/                      # Documentación completa
```

## 🛠️ **INSTALACIÓN Y CONFIGURACIÓN**

### **1. Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/ajpdsoft-sms-email.git
cd ajpdsoft-sms-email
```

### **2. Crear entorno virtual**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

### **3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

### **4. Configurar credenciales**
```bash
# Copiar archivo de configuración
copy config.ini.ejemplo config.ini

# Editar config.ini con tus credenciales reales
notepad config.ini
```

**Configuración Gmail:**
1. Activa verificación en 2 pasos: https://myaccount.google.com/security
2. Genera contraseña de aplicación: https://myaccount.google.com/apppasswords
3. Usa la contraseña de 16 caracteres en `config.ini`

## 🎯 **USO**

### **📧 Envío de Email**
```bash
python envio_sms_email.py EMAIL "destino@email.com" "<h1>Mi mensaje</h1>" "587" "usuario@gmail.com" "contraseña_app" "smtp.gmail.com" "True"
```

### **📱 Envío de SMS**
```bash
python envio_sms_email.py SMS "+34612345678" "Mensaje de prueba" "COM3"
```

### **📊 Ver Logs**
```bash
python visor_logs.py
```

## 🖥️ **EJECUTABLES**

Los ejecutables permiten usar el sistema sin tener Python instalado:

```bash
# Generar ejecutables
python crear_ejecutable.py

# Usar ejecutables
dist\AjpdSoftEnvioSMS.exe EMAIL "test@email.com" "Mensaje" "587" "user@gmail.com" "pass" "smtp.gmail.com" "True"
dist\AjpdSoftVisorLogs.exe
```

## 📊 **SISTEMA DE LOGGING**

### **Características:**
- 📁 Logs diarios: `logs/envio_sms_email_YYYYMMDD.log`
- 🔒 Contraseñas automáticamente enmascaradas
- ⏰ Timestamps precisos de cada operación
- 📈 Registro detallado de éxitos y errores
- 🔍 Búsqueda y análisis avanzado

### **Ejemplo de Log:**
```log
2025-07-02 10:15:30,123 | INFO | INICIO EMAIL | Destino: user@test.com | Host: smtp.gmail.com:587
2025-07-02 10:15:31,456 | INFO | EMAIL | Autenticación exitosa para sender@gmail.com
2025-07-02 10:15:32,789 | INFO | FIN EMAIL | Estado: ÉXITO | Enviado a user@test.com
```

## 🔧 **CONFIGURACIÓN**

El archivo `config.ini` permite centralizar todas las configuraciones:

```ini
[gmail]
usuario = tu_email@gmail.com
password = tu_contraseña_de_aplicacion_de_16_caracteres
host = smtp.gmail.com
puerto = 587
ssl = True

[sms]
puerto_default = COM3
baudrate = 9600
timeout = 5

[sistema]
directorio_logs = logs
nivel_log = INFO
rotacion_logs_dias = 30
```

## 📱 **REQUISITOS SMS**

Para envío de SMS necesitas:
- 📟 Módem GSM/3G/4G USB
- 📞 SIM card activa
- 🔌 Puerto COM disponible
- 💾 Drivers del módem instalados

**Modelos compatibles:**
- Huawei: E3372, E8372, E3531, E173
- ZTE: MF79U, MF833V, MF190  
- Sierra Wireless: AC340U, USB 598

## 📧 **CONFIGURACIÓN EMAIL**

**Gmail (Recomendado):**
1. Activa verificación en 2 pasos
2. Genera contraseña de aplicación
3. Usa `smtp.gmail.com:587` con TLS

**Otros proveedores:**
- Outlook: `smtp-mail.outlook.com:587`
- Yahoo: `smtp.mail.yahoo.com:587`
- Custom SMTP: Configura según tu proveedor

## 🛡️ **SEGURIDAD**

### **Buenas prácticas implementadas:**
- ✅ Credenciales en archivo de configuración local
- ✅ Contraseñas enmascaradas en logs
- ✅ Archivo de configuración excluido de Git
- ✅ Validación de parámetros de entrada
- ✅ Manejo seguro de excepciones

### **IMPORTANTE:**
- ❌ **NUNCA** subas `config.ini` a repositorios públicos
- ✅ **USA** contraseñas de aplicación para Gmail
- ✅ **REVISA** logs regularmente
- ✅ **ROTA** credenciales periódicamente

## 🧪 **TESTING**

```bash
# Validar configuración
python validar_config.py

# Detectar módem GSM
python detectar_modem.py

# Configurar Gmail paso a paso
python configurar_gmail_seguro.py

# Prueba rápida
python prueba_rapida_gmail.py
```

## 📚 **DOCUMENTACIÓN**

- 📖 [`DOCUMENTACION_LOGGING.md`](DOCUMENTACION_LOGGING.md) - Sistema de logs
- 📖 [`README_EJECUTABLE.md`](README_EJECUTABLE.md) - Manual de ejecutables
- 📖 [`CONFIGURAR_GMAIL.md`](CONFIGURAR_GMAIL.md) - Configuración Gmail
- 📖 [`GUIA_INTEGRACION_EXTERNA.md`](GUIA_INTEGRACION_EXTERNA.md) - Integración con otras apps

## 🤝 **CONTRIBUIR**

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Add nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## 📄 **LICENCIA**

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👤 **AUTOR**

**AjpdSoft Development**
- 🐙 GitHub: [@tu-usuario](https://github.com/tu-usuario)
- 📧 Email: contacto@ajpdsoft.com
- 🌐 Web: https://ajpdsoft.com

## 🎉 **AGRADECIMIENTOS**

- Python Software Foundation
- PyInstaller Team
- Contribuidores de pySerial
- Comunidad de desarrolladores

## 📊 **ESTADÍSTICAS**

- 🛠️ **Lenguaje:** Python 3.13+
- 📦 **Dependencias:** pySerial, email-validator
- 🏗️ **Build:** PyInstaller 6.10.0
- 📈 **Tamaño ejecutables:** ~7-8 MB
- 🎯 **Plataforma:** Windows 10/11
- ⚡ **Performance:** <2s por operación

---

⭐ **¡Si te gusta este proyecto, dale una estrella!** ⭐

## Configuración del Entorno

### 1. Crear entorno virtual
```bash
python -m venv .venv
```

### 2. Activar el entorno virtual
En Windows:
```bash
.venv\Scripts\activate
```

En Linux/macOS:
```bash
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Uso

### Enviar SMS
```bash
python envio_sms_email.py SMS <numero> <mensaje> <puerto_serie>
```

Ejemplo:
```bash
python envio_sms_email.py SMS "+1234567890" "Hola mundo" "COM3"
```

### Enviar Email
```bash
python envio_sms_email.py EMAIL <destino> <mensaje> <puerto_smtp> <usuario> <password> <host_smtp> [ssl]
```

Ejemplo:
```bash
python envio_sms_email.py EMAIL "usuario@ejemplo.com" "<h1>Mensaje HTML</h1>" "587" "tu_email@gmail.com" "tu_password" "smtp.gmail.com" "True"
```

## Dependencias

- **pyserial**: Para comunicación con módem GSM
- **smtplib**: Incluido en Python estándar para envío de emails

## Notas

- Para SMS necesitas un módem GSM conectado al puerto serie
- Para Gmail, es recomendable usar una contraseña de aplicación en lugar de tu contraseña principal
- El parámetro SSL es opcional y por defecto es "True"
