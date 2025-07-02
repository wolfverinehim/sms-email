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

### **� PYTHON (Modo Desarrollo)**

**�📧 Envío de Email:**
```bash
python envio_sms_email.py EMAIL "destino@email.com" "<h1>Mi mensaje</h1>" "587" "usuario@gmail.com" "contraseña_app" "smtp.gmail.com" "True"
```

**📱 Envío de SMS:**
```bash
python envio_sms_email.py SMS "+34612345678" "Mensaje de prueba" "COM3"
```

**📊 Visor de Logs:**
```bash
python visor_logs.py
```

### **🔐 GESTIÓN DE CREDENCIALES**

El sistema soporta **2 métodos** para manejar credenciales:

**Método 1: Parámetros de línea de comandos**
- ✅ Automatización completa
- ⚠️ Credenciales visibles temporalmente

**Método 2: Archivo de configuración (RECOMENDADO)**
- ✅ Máxima seguridad
- ✅ Credenciales nunca expuestas
- ✅ Configuración centralizada en `config.ini`

**Para usar config.ini:** Simplemente omite las credenciales en los comandos

## 🖥️ **EJECUTABLES**

Los ejecutables permiten usar el sistema sin tener Python instalado y ofrecen **dos modos de operación**:

### **Generación de Ejecutables**
```bash
python crear_ejecutable.py
```

### **📋 MODO 1: Con Parámetros (Línea de Comandos)**

**✅ VENTAJAS:**
- 🚀 **Ejecución inmediata** sin interacción del usuario
- 🔄 **Automatización completa** desde otras aplicaciones
- 📝 **Logging automático** de todos los parámetros
- ⚡ **Ideal para integración** con sistemas externos

**⚠️ CONSIDERACIONES DE SEGURIDAD:**
- 🔒 **Las credenciales son visibles** en la línea de comandos
- 👁️ **Pueden aparecer en historial** de comandos del sistema
- 📊 **Se registran en logs del sistema** (enmascaradas en nuestros logs)

**Ejemplos:**
```bash
# Envío de Email con parámetros
dist\AjpdSoftEnvioSMS.exe EMAIL "test@email.com" "Mensaje HTML" "587" "user@gmail.com" "password_app" "smtp.gmail.com" "True"

# Envío de SMS con parámetros  
dist\AjpdSoftEnvioSMS.exe SMS "+34612345678" "Mensaje de prueba" "COM3"
```

### **🔐 MODO 2: Sin Parámetros (Modo Seguro)**

**✅ VENTAJAS:**
- 🛡️ **Máxima seguridad** - credenciales desde config.ini
- 🔒 **No exposición** de credenciales en línea de comandos
- 💻 **Interfaz interactiva** paso a paso
- 📝 **Validación previa** de configuración

**⚠️ CONSIDERACIONES:**
- 🕐 **Requiere interacción** del usuario
- ⚙️ **Necesita config.ini** configurado previamente
- 🔄 **Menos automatizable** para procesos batch

**Ejemplos:**
```bash
# Modo interactivo seguro (SIN parámetros)
dist\AjpdSoftEnvioSMS.exe

# El programa solicitará:
# 1. Tipo de operación (EMAIL/SMS)
# 2. Datos específicos según el tipo
# 3. Las credenciales se leen automáticamente de config.ini
```

### **🎯 RECOMENDACIONES DE USO**

| Escenario | Modo Recomendado | Razón |
|-----------|------------------|--------|
| **Integración con ERP/CRM** | Con parámetros | Automatización completa |
| **Scripts automatizados** | Con parámetros | No requiere interacción |
| **Uso manual esporádico** | Sin parámetros | Mayor seguridad |
| **Entornos compartidos** | Sin parámetros | Evita exposición de credenciales |
| **Producción crítica** | Sin parámetros | Máximo control y seguridad |

### **🔍 MONITOREO Y LOGS**

**Ambos modos generan logs completos:**
```bash
# Ver logs en tiempo real
dist\AjpdSoftVisorLogs.exe

# Logs se guardan en: logs/envio_sms_email_YYYYMMDD.log
```

**Diferencias en logging:**
- **Con parámetros:** Se registra "Parámetros recibidos desde línea de comandos"
- **Sin parámetros:** Se registra "Configuración leída desde config.ini"
- **En ambos casos:** Las contraseñas se enmascaran automáticamente

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

### **🔐 SEGURIDAD EN EJECUTABLES**

**Modo con parámetros (automatización):**
- ⚠️ **Riesgo:** Credenciales visibles en línea de comandos
- ⚠️ **Riesgo:** Pueden quedar en historial del sistema
- ✅ **Mitigación:** Usar contraseñas de aplicación específicas
- ✅ **Mitigación:** Ejecutar desde scripts que limpien historial
- ✅ **Mitigación:** Nuestros logs siempre enmascaran credenciales

**Modo sin parámetros (seguro):**
- ✅ **Seguro:** Credenciales solo en archivo local
- ✅ **Seguro:** No exposición en procesos del sistema
- ✅ **Seguro:** Config.ini con permisos restrictivos

**Ejemplo de comando seguro para limpiar historial:**
```bash
# Windows - Ejecutar y limpiar historial
dist\AjpdSoftEnvioSMS.exe EMAIL "user@test.com" "msg" "587" "admin@company.com" "pass" "smtp.gmail.com" "True" && doskey /reinstall
```

### **IMPORTANTE:**
- ❌ **NUNCA** subas `config.ini` a repositorios públicos
- ✅ **USA** contraseñas de aplicación para Gmail
- ✅ **REVISA** logs regularmente
- ✅ **ROTA** credenciales periódicamente
- ⚠️ **CONSIDERA** el modo sin parámetros en entornos compartidos

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
- 🐙 GitHub: [@wolfverinehim](https://github.com/wolfverinehim)
- 📧 Email: ivan.becerro@hotmail.com
- 🌐 Web: https://www.accuro.es

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

## 💡 **EJEMPLOS PRÁCTICOS**

### **🔧 Con Python (Desarrollo)**

**Enviar SMS:**
```bash
python envio_sms_email.py SMS "+1234567890" "Hola mundo" "COM3"
```

**Enviar Email:**
```bash
python envio_sms_email.py EMAIL "usuario@ejemplo.com" "<h1>Mensaje HTML</h1>" "587" "tu_email@gmail.com" "tu_password" "smtp.gmail.com" "True"
```

### **📦 Con Ejecutables (Producción)**

**Modo automático (con parámetros):**
```bash
# Email completo con parámetros
dist\AjpdSoftEnvioSMS.exe EMAIL "cliente@empresa.com" "<h1>Bienvenido</h1>" "587" "admin@miempresa.com" "app_password_16_chars" "smtp.gmail.com" "True"

# SMS con parámetros  
dist\AjpdSoftEnvioSMS.exe SMS "+34600123456" "Su pedido está listo" "COM3"
```

**Modo seguro (sin parámetros):**
```bash
# Ejecución interactiva segura
dist\AjpdSoftEnvioSMS.exe
# El programa te guiará paso a paso y usará config.ini para credenciales
```

### **📊 Monitoreo**
```bash
# Visor de logs interactivo
dist\AjpdSoftVisorLogs.exe
```

## ⚙️ **CONFIGURACIÓN DE CREDENCIALES**

**Para usar modo seguro (SIN parámetros):**
1. Copia `config.ini.ejemplo` como `config.ini`
2. Edita las credenciales en `config.ini`
3. Ejecuta sin parámetros para máxima seguridad

**Beneficio:** Las credenciales nunca aparecen en línea de comandos ni en historial del sistema.

## Dependencias

- **pyserial**: Para comunicación con módem GSM
- **smtplib**: Incluido en Python estándar para envío de emails

## Notas

- Para SMS necesitas un módem GSM conectado al puerto serie
- Para Gmail, es recomendable usar una contraseña de aplicación en lugar de tu contraseña principal
- El parámetro SSL es opcional y por defecto es "True"
