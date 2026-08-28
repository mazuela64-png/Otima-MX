# Aplicación de Control Comercial - O'tima México
# Módulo de gestión para pipeline de laboratorios farmacéuticos y dispositivos médicos

class OtimaComercialMX:
    def __init__(self):
        self.pipeline = []

    def registrar_contacto(self, laboratorio, contacto, cargo, linkedin, estatus="Por Contactar"):
        nuevo_lead = {
            "Laboratorio": laboratorio,
            "Contacto": contacto,
            "Cargo": cargo,
            "LinkedIn": linkedin,
            "Estatus": estatus
        }
        self.pipeline.append(nuevo_lead)
        print(f"[ÉXITO] Lead agregado: {contacto} de {laboratorio}")

    def mostrar_pipeline(self):
        print("\n--- PIPELINE COMERCIAL O'TIMA MÉXICO ---")
        for lead in self.pipeline:
            print(f"Empresa: {lead['Laboratorio']} | Contacto: {lead['Contacto']} ({
