# 📊 Sistema de Logging - IBA-Soft Envío SMS/Email

## 📋 **CARACTERÍSTICAS DEL LOGGING**

### ✅ **Lo que se registra:**
- **Parámetros recibidos** (con contraseñas enmascaradas por seguridad)
- **Inicio y fin de cada operación** (SMS/Email)
- **Pasos detallados** del proceso de envío
- **Resultados** (éxito o error)
- **Timestamps** precisos de cada evento
- **Información de conexión** (puertos, hosts, etc.)

### 🔒 **Seguridad del Logging:**
- ✅ Contraseñas automáticamente enmascaradas como `***MASKED***`
- ✅ Solo información necesaria para debugging
- ✅ Logs con encoding UTF-8 para caracteres especiales

## 📁 **Ubicación de los Logs**

### **Directorio:** `logs/`
- Se crea automáticamente si no existe
- Un archivo por día: `envio_sms_email_YYYYMMDD.log`
- Ejemplo: `envio_sms_email_20250702.log`

### **Formato de cada línea:**
```
2025-07-02 00:25:04,167 | INFO | INICIO APLICACIÓN | IBA-Soft Envío SMS/Email
```
- **Timestamp:** Fecha y hora exacta
- **Nivel:** INFO, WARNING, ERROR
- **Mensaje:** Descripción del evento

## 📧 **Ejemplo de Log - Envío de Email**

```log
2025-07-02 10:15:30,123 | INFO | ================================================================================
2025-07-02 10:15:30,124 | INFO | INICIO APLICACIÓN | IBA-Soft Envío SMS/Email
2025-07-02 10:15:30,124 | INFO | INICIO EJECUCIÓN | Parámetros: IBA-SoftEnvioSMS.exe EMAIL usuario@test.com Mensaje 587 sender@gmail.com ***MASKED*** smtp.gmail.com True
2025-07-02 10:15:30,124 | INFO | Total parámetros recibidos: 9
2025-07-02 10:15:30,125 | INFO | Modo seleccionado: EMAIL
2025-07-02 10:15:30,125 | INFO | EMAIL | Iniciando envío a usuario@test.com via smtp.gmail.com
2025-07-02 10:15:30,125 | INFO | INICIO EMAIL | Destino: usuario@test.com | Host: smtp.gmail.com:587 | SSL: True
2025-07-02 10:15:30,126 | INFO | EMAIL | Usuario: sender@gmail.com | Longitud mensaje: 25
2025-07-02 10:15:30,127 | INFO | EMAIL | Mensaje MIME creado
2025-07-02 10:15:30,127 | INFO | EMAIL | Contenido HTML adjuntado
2025-07-02 10:15:31,234 | INFO | EMAIL | Conexión SMTP establecida con smtp.gmail.com:587
2025-07-02 10:15:31,456 | INFO | EMAIL | TLS iniciado
2025-07-02 10:15:32,123 | INFO | EMAIL | Autenticación exitosa para sender@gmail.com
2025-07-02 10:15:32,789 | INFO | EMAIL | Mensaje enviado a usuario@test.com
2025-07-02 10:15:32,790 | INFO | EMAIL | Conexión SMTP cerrada
2025-07-02 10:15:32,791 | INFO | FIN EMAIL | Estado: ÉXITO | Detalles: Enviado a usuario@test.com
2025-07-02 10:15:32,792 | INFO | FIN APLICACIÓN | IBA-Soft Envío SMS/Email
2025-07-02 10:15:32,792 | INFO | ================================================================================
```

## 📱 **Ejemplo de Log - Envío de SMS**

```log
2025-07-02 10:20:15,456 | INFO | ================================================================================
2025-07-02 10:20:15,457 | INFO | INICIO APLICACIÓN | IBA-Soft Envío SMS/Email
2025-07-02 10:20:15,457 | INFO | INICIO EJECUCIÓN | Parámetros: IBA-SoftEnvioSMS.exe SMS +34612345678 Mensaje_de_prueba COM3
2025-07-02 10:20:15,458 | INFO | Total parámetros recibidos: 5
2025-07-02 10:20:15,458 | INFO | Modo seleccionado: SMS
2025-07-02 10:20:15,459 | INFO | SMS | Iniciando envío a +34612345678 por puerto COM3
2025-07-02 10:20:15,459 | INFO | INICIO SMS | Número: +34612345678 | Puerto: COM3 | Longitud mensaje: 17
2025-07-02 10:20:15,567 | INFO | SMS | Puerto serie COM3 abierto correctamente
2025-07-02 10:20:16,123 | INFO | SMS | Modo texto configurado
2025-07-02 10:20:16,234 | INFO | SMS | Número destinatario configurado: +34612345678
2025-07-02 10:20:19,567 | INFO | SMS | Mensaje enviado
2025-07-02 10:20:19,568 | INFO | SMS | Puerto serie cerrado
2025-07-02 10:20:19,569 | INFO | FIN SMS | Estado: ÉXITO | Detalles: Enviado a +34612345678
2025-07-02 10:20:19,570 | INFO | FIN APLICACIÓN | IBA-Soft Envío SMS/Email
2025-07-02 10:20:19,570 | INFO | ================================================================================
```

## ❌ **Ejemplo de Log - Error**

```log
2025-07-02 10:25:00,123 | INFO | ================================================================================
2025-07-02 10:25:00,124 | INFO | INICIO APLICACIÓN | IBA-Soft Envío SMS/Email
2025-07-02 10:25:00,124 | INFO | INICIO EJECUCIÓN | Parámetros: IBA-SoftEnvioSMS.exe EMAIL usuario@test.com Mensaje 587 sender@gmail.com wrong_password smtp.gmail.com True
2025-07-02 10:25:00,125 | INFO | Total parámetros recibidos: 9
2025-07-02 10:25:00,125 | INFO | Modo seleccionado: EMAIL
2025-07-02 10:25:00,126 | INFO | EMAIL | Iniciando envío a usuario@test.com via smtp.gmail.com
2025-07-02 10:25:00,126 | INFO | INICIO EMAIL | Destino: usuario@test.com | Host: smtp.gmail.com:587 | SSL: True
2025-07-02 10:25:00,127 | INFO | EMAIL | Usuario: sender@gmail.com | Longitud mensaje: 7
2025-07-02 10:25:00,128 | INFO | EMAIL | Mensaje MIME creado
2025-07-02 10:25:00,128 | INFO | EMAIL | Contenido HTML adjuntado
2025-07-02 10:25:01,234 | INFO | EMAIL | Conexión SMTP establecida con smtp.gmail.com:587
2025-07-02 10:25:01,456 | INFO | EMAIL | TLS iniciado
2025-07-02 10:25:02,789 | ERROR | FIN EMAIL | Estado: ERROR | Detalles: (535, '5.7.8 Username and Password not accepted')
2025-07-02 10:25:02,790 | INFO | FIN APLICACIÓN | IBA-Soft Envío SMS/Email
2025-07-02 10:25:02,790 | INFO | ================================================================================
```

## 🔍 **Visor de Logs - visor_logs.py**

### **Funcionalidades:**
1. **📋 Ver logs recientes** - Últimas 24 horas o periodo personalizado
2. **📈 Estadísticas** - Contadores de SMS, emails, éxitos y errores
3. **🔍 Buscar** - Encontrar términos específicos en todos los logs
4. **📅 Ver fecha específica** - Logs de un día concreto
5. **🧹 Limpiar logs antiguos** - Eliminar logs anteriores a X días
6. **📁 Listar archivos** - Ver todos los logs disponibles

### **Uso del Visor:**
```bash
python visor_logs.py
```

### **Ejemplos de búsqueda:**
- Buscar "ERROR" para ver todos los errores
- Buscar "gmail.com" para ver envíos por Gmail
- Buscar "+34612" para ver SMS a un número específico

## 📊 **Análisis de Logs**

### **Métricas importantes:**
- **Tasa de éxito:** % de operaciones exitosas
- **Tiempos de respuesta:** Duración de cada operación
- **Errores frecuentes:** Problemas recurrentes
- **Uso por día/hora:** Patrones de actividad

### **Comandos útiles:**
```bash
# Ver logs de hoy
python visor_logs.py → opción 4 → ENTER

# Ver estadísticas generales
python visor_logs.py → opción 2

# Buscar errores de autenticación
python visor_logs.py → opción 3 → "Password not accepted"

# Limpiar logs antiguos (30 días)
python visor_logs.py → opción 5 → 30
```

## 🚀 **Integración con Ejecutable**

El ejecutable `IBA-SoftEnvioSMS.exe` incluye automáticamente:
- ✅ Logging completo activado
- ✅ Creación automática del directorio `logs/`
- ✅ Rotación diaria de archivos de log
- ✅ Formato consistente y legible

## 🔧 **Personalización**

### **Cambiar nivel de logging:**
Editar en `envio_sms_email.py`:
```python
logging.basicConfig(
    level=logging.DEBUG,  # Cambiar a DEBUG para más detalle
    # level=logging.WARNING,  # Solo warnings y errores
)
```

### **Cambiar ubicación de logs:**
```python
log_dir = "mi_directorio_logs"  # Cambiar directorio
```

### **Formato personalizado:**
```python
format='%(asctime)s [%(levelname)s] %(message)s'  # Formato más simple
```

## 📞 **Solución de Problemas de Logs**

### **No se crean logs:**
- ✅ Verificar permisos de escritura
- ✅ Verificar espacio en disco
- ✅ Ejecutar desde directorio correcto

### **Logs muy grandes:**
- 🧹 Usar la opción de limpiar logs antiguos
- 📊 Rotar logs manualmente
- ⚙️ Cambiar nivel de logging a WARNING

### **Errores al abrir logs:**
- 📝 Verificar encoding UTF-8
- 🔒 Cerrar aplicaciones que usen el archivo
- 👤 Verificar permisos de usuario

---

**📝 Con este sistema de logging tendrás visibilidad completa de todas las operaciones del sistema IBA-Soft Envío SMS/Email.**
