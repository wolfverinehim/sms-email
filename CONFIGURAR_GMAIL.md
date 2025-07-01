# 🔧 GUÍA PARA CONFIGURAR GMAIL CON TU APLICACIÓN

## ❌ **PROBLEMA DETECTADO**
Gmail rechazó la autenticación con tu contraseña normal. Esto es **normal y esperado** por seguridad.

## ✅ **SOLUCIÓN: CONTRASEÑA DE APLICACIÓN**

### 📋 **PASO A PASO:**

#### **1. Activar Verificación en 2 Pasos**
1. Ve a: https://myaccount.google.com/security
2. En "Cómo inicias sesión en Google", busca "Verificación en 2 pasos"
3. Haz clic en "Verificación en 2 pasos"
4. Sigue las instrucciones para activarla (necesitarás tu teléfono)

#### **2. Generar Contraseña de Aplicación**
1. Una vez activada la verificación en 2 pasos
2. Ve a: https://myaccount.google.com/apppasswords
3. Selecciona "Correo" como aplicación
4. Selecciona "Otro (nombre personalizado)" como dispositivo
5. Escribe: "Sistema SMS Email Python"
6. Haz clic en "Generar"
7. **COPIA LA CONTRASEÑA GENERADA** (16 caracteres sin espacios)

#### **3. Usar la Nueva Contraseña**
- **NO uses tu contraseña normal de Gmail**
- **USA la contraseña de aplicación de 16 caracteres**

---

## 🚀 **CONFIGURACIÓN RÁPIDA**

### **Opción A: Configuración Manual**
```python
# En configurar_email.py, cambia:
'password': 'tu_contraseña_de_aplicacion_de_16_caracteres'
```

### **Opción B: Variables de Entorno (Recomendado)**
```bash
# Crear archivo .env
GMAIL_USER=infonutribel@gmail.com
GMAIL_APP_PASSWORD=tu_contraseña_de_aplicacion
```

---

## 🧪 **DESPUÉS DE CONFIGURAR**

Ejecuta nuevamente:
```bash
python configurar_email.py
```

---

## 🔐 **SEGURIDAD**

✅ **Ventajas de Contraseña de Aplicación:**
- Más seguro que la contraseña normal
- Se puede revocar en cualquier momento
- Específica para esta aplicación
- No compromete tu cuenta principal

❌ **NUNCA hagas esto:**
- Usar "Acceso de apps menos seguras" 
- Compartir tu contraseña principal
- Dejar credenciales en código público

---

## 📞 **¿PROBLEMAS?**

Si tienes problemas:
1. Verifica que la verificación en 2 pasos esté activa
2. Asegúrate de usar la contraseña de aplicación (no la normal)
3. Verifica que el email sea exactamente: infonutribel@gmail.com
4. Intenta generar una nueva contraseña de aplicación

---

## 🎯 **PRÓXIMO PASO**

1. **Genera tu contraseña de aplicación**
2. **Actualiza el configurador**
3. **Ejecuta la prueba otra vez**

¿Ya tienes la contraseña de aplicación?
