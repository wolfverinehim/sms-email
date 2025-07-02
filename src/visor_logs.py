#!/usr/bin/env python3
"""
Visor de logs para el sistema IBA-Soft Envío SMS/Email
Permite visualizar y analizar los logs generados por la aplicación
"""

import os
import glob
from datetime import datetime, timedelta
import re

class VisorLogs:
    def __init__(self, directorio_logs="logs"):
        self.directorio_logs = directorio_logs
        
    def listar_archivos_log(self):
        """Lista todos los archivos de log disponibles"""
        patron = os.path.join(self.directorio_logs, "envio_sms_email_*.log")
        archivos = glob.glob(patron)
        archivos.sort(reverse=True)  # Más recientes primero
        return archivos
    
    def mostrar_logs_recientes(self, horas=24):
        """Muestra los logs de las últimas X horas"""
        print(f"📊 LOGS DE LAS ÚLTIMAS {horas} HORAS")
        print("=" * 60)
        
        archivos = self.listar_archivos_log()
        if not archivos:
            print("❌ No se encontraron archivos de log")
            return
        
        # Filtrar por fecha
        fecha_limite = datetime.now() - timedelta(hours=horas)
        
        for archivo in archivos:
            # Extraer fecha del nombre del archivo
            nombre = os.path.basename(archivo)
            match = re.search(r'envio_sms_email_(\d{8})\.log', nombre)
            if match:
                fecha_str = match.group(1)
                fecha_archivo = datetime.strptime(fecha_str, '%Y%m%d')
                
                if fecha_archivo >= fecha_limite.replace(hour=0, minute=0, second=0, microsecond=0):
                    print(f"\n📅 {archivo}")
                    print("-" * 40)
                    self.mostrar_contenido_archivo(archivo)
    
    def mostrar_contenido_archivo(self, archivo, lineas=50):
        """Muestra el contenido de un archivo de log"""
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                lineas_archivo = f.readlines()
            
            # Mostrar las últimas N líneas
            lineas_mostrar = lineas_archivo[-lineas:] if len(lineas_archivo) > lineas else lineas_archivo
            
            for linea in lineas_mostrar:
                linea = linea.strip()
                if linea:
                    # Colorear según el tipo de log
                    if "ERROR" in linea:
                        print(f"🔴 {linea}")
                    elif "ÉXITO" in linea:
                        print(f"🟢 {linea}")
                    elif "INICIO" in linea:
                        print(f"🔵 {linea}")
                    elif "FIN" in linea:
                        print(f"🟡 {linea}")
                    else:
                        print(f"   {linea}")
                        
        except Exception as e:
            print(f"❌ Error leyendo archivo {archivo}: {e}")
    
    def estadisticas_logs(self):
        """Genera estadísticas de los logs"""
        print("📈 ESTADÍSTICAS DE LOGS")
        print("=" * 60)
        
        archivos = self.listar_archivos_log()
        if not archivos:
            print("❌ No se encontraron archivos de log")
            return
        
        total_sms = 0
        total_email = 0
        total_errores = 0
        total_exitos = 0
        
        for archivo in archivos:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                
                # Contar operaciones
                total_sms += contenido.count("INICIO SMS")
                total_email += contenido.count("INICIO EMAIL")
                total_errores += contenido.count("Estado: ERROR")
                total_exitos += contenido.count("Estado: ÉXITO")
                
            except Exception as e:
                print(f"⚠️ Error procesando {archivo}: {e}")
        
        print(f"📱 Total SMS enviados: {total_sms}")
        print(f"📧 Total Emails enviados: {total_email}")
        print(f"✅ Operaciones exitosas: {total_exitos}")
        print(f"❌ Operaciones con error: {total_errores}")
        
        if total_sms + total_email > 0:
            tasa_exito = (total_exitos / (total_sms + total_email)) * 100
            print(f"📊 Tasa de éxito: {tasa_exito:.2f}%")
    
    def buscar_en_logs(self, termino):
        """Busca un término específico en todos los logs"""
        print(f"🔍 BUSCANDO: '{termino}'")
        print("=" * 60)
        
        archivos = self.listar_archivos_log()
        encontrados = 0
        
        for archivo in archivos:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    lineas = f.readlines()
                
                for i, linea in enumerate(lineas, 1):
                    if termino.lower() in linea.lower():
                        print(f"📁 {os.path.basename(archivo)}:{i}")
                        print(f"   {linea.strip()}")
                        encontrados += 1
                        
            except Exception as e:
                print(f"⚠️ Error buscando en {archivo}: {e}")
        
        print(f"\n🎯 Encontradas {encontrados} coincidencias")
    
    def limpiar_logs_antiguos(self, dias=30):
        """Limpia logs más antiguos que X días"""
        print(f"🧹 LIMPIANDO LOGS ANTERIORES A {dias} DÍAS")
        print("=" * 60)
        
        fecha_limite = datetime.now() - timedelta(days=dias)
        archivos = self.listar_archivos_log()
        eliminados = 0
        
        for archivo in archivos:
            try:
                # Obtener fecha de modificación del archivo
                fecha_mod = datetime.fromtimestamp(os.path.getmtime(archivo))
                
                if fecha_mod < fecha_limite:
                    os.remove(archivo)
                    print(f"🗑️ Eliminado: {os.path.basename(archivo)}")
                    eliminados += 1
                    
            except Exception as e:
                print(f"⚠️ Error eliminando {archivo}: {e}")
        
        print(f"✅ Se eliminaron {eliminados} archivos de log")

def menu_principal():
    """Menú principal del visor de logs"""
    visor = VisorLogs()
    
    while True:
        print("\n" + "=" * 60)
        print("📊 VISOR DE LOGS - IBA-Soft Envío SMS/Email")
        print("=" * 60)
        print("1. 📋 Ver logs recientes (últimas 24 horas)")
        print("2. 📈 Estadísticas generales")
        print("3. 🔍 Buscar en logs")
        print("4. 📅 Ver logs de fecha específica")
        print("5. 🧹 Limpiar logs antiguos")
        print("6. 📁 Listar todos los archivos de log")
        print("7. 🚪 Salir")
        print("-" * 60)
        
        opcion = input("Elige una opción (1-7): ").strip()
        
        if opcion == "1":
            horas = input("¿Cuántas horas atrás? (24): ").strip()
            horas = int(horas) if horas.isdigit() else 24
            visor.mostrar_logs_recientes(horas)
            
        elif opcion == "2":
            visor.estadisticas_logs()
            
        elif opcion == "3":
            termino = input("Término a buscar: ").strip()
            if termino:
                visor.buscar_en_logs(termino)
            
        elif opcion == "4":
            fecha = input("Fecha (YYYYMMDD) o ENTER para hoy: ").strip()
            if not fecha:
                fecha = datetime.now().strftime("%Y%m%d")
            
            archivo_log = os.path.join("logs", f"envio_sms_email_{fecha}.log")
            if os.path.exists(archivo_log):
                print(f"\n📅 LOG DEL {fecha}")
                print("-" * 40)
                visor.mostrar_contenido_archivo(archivo_log, 100)
            else:
                print(f"❌ No se encontró log para la fecha {fecha}")
                
        elif opcion == "5":
            dias = input("¿Eliminar logs anteriores a cuántos días? (30): ").strip()
            dias = int(dias) if dias.isdigit() else 30
            confirmar = input(f"¿Confirmas eliminar logs anteriores a {dias} días? (s/N): ").strip().lower()
            if confirmar == 's':
                visor.limpiar_logs_antiguos(dias)
            else:
                print("❌ Operación cancelada")
                
        elif opcion == "6":
            archivos = visor.listar_archivos_log()
            print(f"\n📁 ARCHIVOS DE LOG DISPONIBLES ({len(archivos)})")
            print("-" * 40)
            for archivo in archivos:
                try:
                    tamaño = os.path.getsize(archivo) / 1024  # KB
                    fecha_mod = datetime.fromtimestamp(os.path.getmtime(archivo))
                    print(f"📄 {os.path.basename(archivo)} ({tamaño:.1f} KB) - {fecha_mod.strftime('%Y-%m-%d %H:%M')}")
                except Exception as e:
                    print(f"📄 {os.path.basename(archivo)} (error: {e})")
                    
        elif opcion == "7":
            print("👋 ¡Hasta luego!")
            break
            
        else:
            print("❌ Opción no válida")
        
        input("\nPresiona ENTER para continuar...")

if __name__ == "__main__":
    menu_principal()
