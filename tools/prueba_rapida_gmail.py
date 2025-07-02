#!/usr/bin/env python3
"""
Script de prueba rápida para Gmail
Úsalo cuando ya tengas tu contraseña de aplicación
"""

import sys
sys.path.append('.')

from envio_sms_email import enviar_email

def prueba_rapida():
    print("🚀 PRUEBA RÁPIDA DE EMAIL")
    print("=" * 40)
    
    # Solicitar datos
    email_destino = input("📧 Email destino: ")
    password_app = input("🔑 Contraseña de aplicación (16 chars): ")
    
    # Configuración Gmail
    usuario = "infonutribel@gmail.com"
    host = "smtp.gmail.com"
    puerto = "587"
    
    # Mensaje de prueba
    mensaje_html = """
    <div style='font-family: Arial; padding: 20px; background: #f0f8ff; border-radius: 10px;'>
        <h2 style='color: #4CAF50;'>🎉 ¡Prueba Exitosa!</h2>
        <p>Este email confirma que tu configuración Gmail está funcionando correctamente.</p>
        
        <div style='background: white; padding: 15px; border-radius: 5px; margin: 15px 0;'>
            <h3>📋 Configuración:</h3>
            <ul>
                <li><strong>Usuario:</strong> infonutribel@gmail.com</li>
                <li><strong>Servidor:</strong> smtp.gmail.com:587</li>
                <li><strong>Seguridad:</strong> TLS ✅</li>
                <li><strong>Autenticación:</strong> Contraseña de aplicación ✅</li>
            </ul>
        </div>
        
        <p style='color: #666; font-size: 12px;'>
            <em>Enviado desde el sistema automatizado de SMS/Email</em>
        </p>
    </div>
    """
    
    print(f"\n📤 Enviando email de prueba...")
    print(f"📧 Desde: {usuario}")
    print(f"📧 Para: {email_destino}")
    
    try:
        enviar_email(
            destino=email_destino,
            mensaje=mensaje_html,
            puerto=puerto,
            usuario=usuario,
            password=password_app,
            host=host,
            ssl="True"
        )
        
        print(f"\n✅ ¡EMAIL ENVIADO EXITOSAMENTE!")
        print(f"📨 Revisa la bandeja de entrada de {email_destino}")
        
        # Mostrar comando completo para referencia
        print(f"\n🎯 COMANDO COMPLETO PARA REFERENCIA:")
        print(f'python envio_sms_email.py EMAIL "{email_destino}" "Tu mensaje aquí" "{puerto}" "{usuario}" "{password_app}" "{host}" "True"')
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print(f"💡 Verifica que la contraseña de aplicación sea correcta")

if __name__ == "__main__":
    prueba_rapida()
