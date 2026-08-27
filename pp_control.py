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
            print(f"Empresa: {lead['Laboratorio']} | Contacto: {lead['Contacto']} ({lead['Cargo']}) | Estatus: {lead['Estatus']}")

# Ejemplo de uso operativo para prospección inicial
if __name__ == "__main__":
    crm = OtimaComercialMX()
    # Aquí puedes registrar tus prospectos detectados en la ruta de trabajo
    crm.registrar_contacto("Laboratorio Ejemplo S.A. de C.V.", "Lic. Roberto Gómez", "Director de Sales Effectiveness", "linkedin.com/in/ejemplo", "Por Contactar")
    crm.mostrar_pipeline()
