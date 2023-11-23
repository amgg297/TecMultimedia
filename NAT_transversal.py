#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import minimal
import stun
import sounddevice as sd
import psutil

class NAT_transversal:
    def __init__(self):
        # Constructor de la clase, aquí puedes realizar inicializaciones necesarias
        pass

    def get_external_endpoint(self):
        # Utiliza stun.get_ip_info() para obtener la información de STUN
        _, external_endpoint, _ = stun.get_ip_info()
        return external_endpoint

    def classify_nat_device(self):
        # Aquí deberías implementar la lógica real para clasificar el NAT
        # Puedes utilizar bibliotecas existentes o implementar la lógica por ti mismo
        # Devuelvo "Full Cone NAT" como ejemplo
        return "Full Cone NAT"

    def run_nattraversal(self, nat_traversal_running, new_command_parameter):
        if nat_traversal_running:
            # Simulando la obtención del punto final externo a través de STUN
            external_endpoint = self.get_external_endpoint()

            # Simulando la clasificación del dispositivo NAT
            nat_classification = self.classify_nat_device()

            # Imprimiendo el punto final externo y la clasificación
            print(f"External Endpoint: {external_endpoint}")
            print(f"NAT Classification: {nat_classification}")

            # Salir según el nuevo parámetro de línea de comandos
            if new_command_parameter == "--exit9":
                exit()
        else:
            print("NAT traversal is not running.")

# Ejemplo de uso
nat_instance = NAT_transversal()
nat_instance.run_nattraversal(nat_traversal_running=True, new_command_parameter="--exit9")