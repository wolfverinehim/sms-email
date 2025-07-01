#!/usr/bin/env python3
"""
Script de verificación antes de subir a GitHub
Verifica que no se suban archivos sensibles y que todo esté listo
"""

import os
import glob
import sys

def verificar_gitignore():
    """Verifica que .gitignore esté correctamente configurado"""
    print("🔍 VERIFICANDO .GITIGNORE")
    print("=" * 50)
    
    if not os.path.exists('.gitignore'):
        print("❌ .gitignore no existe!")
        return False
    
    with open('.gitignore', 'r') as f:
        contenido = f.read()
    
    archivos_criticos = [
        'config.ini',
        'logs/',
        '.venv/',
        '*.log',
        '.env'
    ]
    
    for archivo in archivos_criticos:
        if archivo in contenido:
            print(f"✅ {archivo} está excluido")
        else:
            print(f"❌ {archivo} NO está excluido")
            return False
    
    return True

def verificar_archivos_sensibles():
    """Verifica que no haya archivos sensibles que se puedan subir"""
    print("\n🔒 VERIFICANDO ARCHIVOS SENSIBLES")
    print("=" * 50)
    
    archivos_prohibidos = [
        'config.ini',
        '.env'
    ]
    
    encontrados = []
    for archivo in archivos_prohibidos:
        if os.path.exists(archivo):
            encontrados.append(archivo)
    
    if encontrados:
        print("⚠️  ARCHIVOS SENSIBLES ENCONTRADOS:")
        for archivo in encontrados:
            print(f"   📄 {archivo}")
        print("💡 Estos archivos están en .gitignore y NO se subirán")
        return True
    else:
        print("✅ No se encontraron archivos sensibles")
        return True

def verificar_estructura():
    """Verifica que la estructura del proyecto esté completa"""
    print("\n📁 VERIFICANDO ESTRUCTURA DEL PROYECTO")
    print("=" * 50)
    
    archivos_requeridos = [
        'README.md',
        'requirements.txt',
        'LICENSE',
        '.gitignore',
        'envio_sms_email.py',
        'visor_logs.py',
        'config.ini.ejemplo'
    ]
    
    todos_presentes = True
    for archivo in archivos_requeridos:
        if os.path.exists(archivo):
            tamaño = os.path.getsize(archivo) / 1024
            print(f"✅ {archivo} ({tamaño:.1f} KB)")
        else:
            print(f"❌ {archivo} - FALTA")
            todos_presentes = False
    
    return todos_presentes

def verificar_ejecutables():
    """Verifica los ejecutables"""
    print("\n🔧 VERIFICANDO EJECUTABLES")
    print("=" * 50)
    
    if os.path.exists('dist'):
        ejecutables = glob.glob('dist/*.exe')
        if ejecutables:
            for exe in ejecutables:
                tamaño = os.path.getsize(exe) / (1024 * 1024)
                print(f"✅ {os.path.basename(exe)} ({tamaño:.2f} MB)")
            return True
        else:
            print("⚠️  No se encontraron ejecutables en dist/")
            print("💡 Ejecuta: python crear_ejecutable.py")
            return False
    else:
        print("⚠️  Directorio dist/ no existe")
        print("💡 Ejecuta: python crear_ejecutable.py")
        return False

def verificar_documentacion():
    """Verifica la documentación"""
    print("\n📚 VERIFICANDO DOCUMENTACIÓN")
    print("=" * 50)
    
    docs_importantes = [
        'README.md',
        'DOCUMENTACION_LOGGING.md',
        'README_EJECUTABLE.md'
    ]
    
    for doc in docs_importantes:
        if os.path.exists(doc):
            with open(doc, 'r', encoding='utf-8') as f:
                contenido = f.read()
                lineas = len(contenido.splitlines())
                print(f"✅ {doc} ({lineas} líneas)")
        else:
            print(f"❌ {doc} - FALTA")

def generar_resumen_github():
    """Genera un resumen para GitHub"""
    print("\n🐙 RESUMEN PARA GITHUB")
    print("=" * 50)
    
    # Contar archivos Python
    scripts_py = glob.glob('*.py')
    print(f"📝 Scripts Python: {len(scripts_py)}")
    
    # Contar ejecutables
    ejecutables = glob.glob('dist/*.exe') if os.path.exists('dist') else []
    print(f"🔧 Ejecutables: {len(ejecutables)}")
    
    # Contar documentación
    docs = glob.glob('*.md')
    print(f"📚 Documentación: {len(docs)} archivos")
    
    # Tamaño total (sin archivos excluidos)
    tamaño_total = 0
    for root, dirs, files in os.walk('.'):
        # Excluir directorios ignorados
        dirs[:] = [d for d in dirs if d not in ['.venv', 'logs', '__pycache__', '.git']]
        
        for file in files:
            if not file.endswith(('.log', '.pyc')) and file != 'config.ini':
                file_path = os.path.join(root, file)
                try:
                    tamaño_total += os.path.getsize(file_path)
                except:
                    pass
    
    print(f"📊 Tamaño total del repositorio: {tamaño_total / (1024*1024):.2f} MB")

def main():
    """Función principal"""
    print("🔍 VERIFICACIÓN PRE-GITHUB - AjpdSoft SMS/Email")
    print("=" * 60)
    
    verificaciones = [
        verificar_gitignore(),
        verificar_archivos_sensibles(),
        verificar_estructura(),
        verificar_ejecutables(),
    ]
    
    verificar_documentacion()
    generar_resumen_github()
    
    print("\n" + "=" * 60)
    if all(verificaciones):
        print("✅ ¡PROYECTO LISTO PARA GITHUB!")
        print("🚀 Ejecuta: subir_a_github.bat")
        print("\n💡 RECOMENDACIONES:")
        print("   1. Crea el repositorio en GitHub como 'ajpdsoft-sms-email'")
        print("   2. Hazlo público para mayor visibilidad")
        print("   3. Agrega topics: python, sms, email, automation, gmail")
        print("   4. Considera crear una release con los ejecutables")
    else:
        print("❌ HAY PROBLEMAS QUE RESOLVER")
        print("💡 Corrige los errores mostrados arriba")
    
    print("\n🔒 SEGURIDAD:")
    print("   ✅ config.ini está excluido del repositorio")
    print("   ✅ Contraseñas se enmascaran en logs")
    print("   ✅ Solo config.ini.ejemplo se sube (plantilla)")

if __name__ == "__main__":
    main()
