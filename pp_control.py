import json
from datetime import datetime, timedelta

class OtimaPipelineMX:
    def __init__(self, json_path="laboratorios_mx.json"):
        self.json_path = json_path
        self.data = self._cargar_datos()

    def _cargar_datos(self):
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"pais": "México", "prospectos": []}

    def generar_reporte_acciones(self):
        print("=" * 60)
        print(" PIPELINE COMERCIAL O'TIMA - PENETRACIÓN MÉXICO")
        print(" Solución: SIP (Sales Incentive Planning)")
        print("=" * 60)

        hoy = datetime.now()
        fecha_contacto = hoy.strftime("%Y-%m-%d")
        fecha_seguimiento = (hoy + timedelta(days=4)).strftime("%Y-%m-%d")

        for idx, item in enumerate(self.data.get("prospectos", []), start=1):
            empresa = item.get("empresa", "N/A")
            contacto = item.get("contacto_clave", "Por definir")
            cargo = item.get("cargo", "N/A")
            estatus = item.get("estatus", "Por Contactar")
            modulos = ", ".join(item.get("modulos_de_interes", ["SIP Core"]))

            print(f"\n[{idx}] {empresa}")
            print(f"    Contacto: {contacto} | Cargo: {cargo}")
            print(f"    Estatus: {estatus}")
            print(f"    Módulos clave: {modulos}")
            print(f"    Fecha sugerida 1er contacto: {fecha_contacto}")
            print(f"    Fecha límite seguimiento:    {fecha_seguimiento}")
            print(f"    Enfoque LinkedIn: Automatización ETL/IQVIA, gobierno de datos y cero hojas manuales.")

if __name__ == "__main__":
    pipeline = OtimaPipelineMX()
    pipeline.generar_reporte_acciones()
