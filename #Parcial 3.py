#Parcial 3
import re, requests, json, os
from collections import Counter

class ProcesadorLogs:
    REGEX = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(\d{2}\/\b[a-zA-Z]{3}\b\/\d{4})\:\d{2}\:\d{2}:\d{2}\s\+\d{4}\]\s\"(\b[a-zA-Z]{3,7}\b)\s(\/\S+)\sHTTP"

    def __init__(self, rutas_archivos):
        self.rutas_archivos = rutas_archivos
        self.entradas_logs = []
        self.ips_contadas = Counter()
        self.resultados = []

    def extraer_logs(self):
        for ruta in self.rutas_archivos:
            try:
                with open(ruta, "rt") as archivo:
                    for linea in archivo:
                        coincidencias = self._extraer_de_linea(linea)
                        if coincidencias:
                            self.entradas_logs.extend(coincidencias)
            except FileNotFoundError:
                print(f"El archivo {ruta} no se encontró.")

    def _extraer_de_linea(self, linea):
        return re.findall(self.REGEX, linea)

    def contar_ips(self):
        self.ips_contadas = Counter(self.entradas_logs)

    def procesar_ataques(self):
        for (ip, fecha, metodo, ruta), cantidad in self.ips_contadas.items():
            ubicacion = ServicioUbicacion.obtener_ubicacion(ip)
            entrada_ataque = {
                "pais": ubicacion["pais"],
                "ip": ip,
                "ataques": [
                    {
                        "fecha": fecha,
                        "metodo": metodo,
                        "ruta": ruta,
                        "cantidad": cantidad
                    }
                ]
            }
            self.resultados.append(entrada_ataque)

    def guardar_resultados(self, archivo_salida="resultados.json"):
        with open(archivo_salida, "w") as archivo:
            json.dump(self.resultados, archivo, indent=4)
        print(f"Los resultados han sido guardados como '{archivo_salida}' en:", os.getcwd())


class ServicioUbicacion:
    URI = "http://ip-api.com/json/"

    def obtener_ubicacion(ip):
        try:
            respuesta = requests.get(f"{ServicioUbicacion.URI}{ip}").json()
            return {
                "pais": respuesta.get("country"),
                "ciudad": respuesta.get("city")
            }
        except Exception as e:
            print(f"Error al obtener la ubicación para {ip}: {e}")
            return {
                "pais": None,
                "ciudad": None
            }


if __name__ == "__main__":
    rutas_archivos = [
        r"C:\Users\306\Downloads\Logs\Acces_log1.log",
        r"C:\Users\306\Downloads\Logs\Acces_log2.log",
        r"C:\Users\306\Downloads\Logs\Acces_log3.log"
    ]

    procesador = ProcesadorLogs(rutas_archivos)
    procesador.extraer_logs()
    procesador.contar_ips()
    procesador.procesar_ataques()
    procesador.guardar_resultados()