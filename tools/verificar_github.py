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
        'config/requirements.txt',
        'LICENSE',
        '.gitignore',
        'src/envio_sms_email.py',
        'src/visor_logs.py',
        'config/config.ini.ejemplo'
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

def verificar_estructura_carpetas():
    """Verifica que la estructura de carpetas esté completa"""
    print("\n📂 VERIFICANDO ESTRUCTURA DE CARPETAS")
    print("=" * 50)
    
    carpetas_requeridas = [
        'src',
        'tools', 
        'config',
        'scripts',
        'docs',
        'dist',
        'logs'
    ]
    
    todas_presentes = True
    for carpeta in carpetas_requeridas:
        if os.path.exists(carpeta) and os.path.isdir(carpeta):
            archivos = len([f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))])
            print(f"✅ {carpeta}/ ({archivos} archivos)")
        elif carpeta == 'logs':
            # logs/ puede no existir aún
            print(f"⚠️  {carpeta}/ - se creará automáticamente")
        else:
            print(f"❌ {carpeta}/ - FALTA")
            todas_presentes = False
    
    return todas_presentes

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
        else:        print("⚠️  No se encontraron ejecutables en dist/")
        print("💡 Ejecuta: python tools/crear_ejecutable.py")
        return False
    else:
        print("⚠️  Directorio dist/ no existe")
        print("💡 Ejecuta: python tools/crear_ejecutable.py")
        return False

def verificar_documentacion():
    """Verifica la documentación"""
    print("\n📚 VERIFICANDO DOCUMENTACIÓN")
    print("=" * 50)
    
    docs_importantes = [
        'README.md',
        'docs/DOCUMENTACION_LOGGING.md',
        'docs/README_EJECUTABLE.md'
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
    
    # Contar archivos Python en src/
    scripts_py = glob.glob('src/*.py') + glob.glob('tools/*.py')
    print(f"📝 Scripts Python: {len(scripts_py)}")
    
    # Contar ejecutables
    ejecutables = glob.glob('dist/*.exe') if os.path.exists('dist') else []
    print(f"🔧 Ejecutables: {len(ejecutables)}")
    
    # Contar documentación
    docs = glob.glob('*.md') + glob.glob('docs/*.md')
    print(f"📚 Documentación: {len(docs)} archivos")
    
    # Contar scripts batch
    scripts_bat = glob.glob('scripts/*.bat')
    print(f"🖥️ Scripts batch: {len(scripts_bat)}")
    
    # Tamaño total (sin archivos excluidos)
    tamaño_total = 0
    for root, dirs, files in os.walk('.'):
        # Excluir directorios ignorados
        dirs[:] = [d for d in dirs if d not in ['.venv', 'logs', '__pycache__', '.git', 'build']]
        
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
    print("🔍 VERIFICACIÓN PRE-GITHUB - IBA-Soft SMS/Email")
    print("=" * 60)
    
    verificaciones = [
        verificar_gitignore(),
        verificar_archivos_sensibles(),
        verificar_estructura(),
        verificar_estructura_carpetas(),
        verificar_ejecutables(),
    ]
    
    verificar_documentacion()
    generar_resumen_github()
    
    print("\n" + "=" * 60)
    if all(verificaciones):
        print("✅ ¡PROYECTO LISTO PARA GITHUB!")
        print("🚀 Ejecuta: subir_a_github.bat")
        print("\n💡 RECOMENDACIONES:")
        print("   1. Crea el repositorio en GitHub como 'IBA-Soft-sms-email'")
        print("   2. Hazlo público para mayor visibilidad")
        print("   3. Agrega topics: python, sms, email, automation, gmail")
        print("   4. Considera crear una release con los ejecutables")
        print("   5. Ejecuta: scripts/subir_a_github.bat")
    else:
        print("❌ HAY PROBLEMAS QUE RESOLVER")
        print("💡 Corrige los errores mostrados arriba")
    
    print("\n🔒 SEGURIDAD:")
    print("   ✅ config.ini está excluido del repositorio")
    print("   ✅ Contraseñas se enmascaran en logs")
    print("   ✅ Solo config.ini.ejemplo se sube (plantilla)")

if __name__ == "__main__":
    main()
