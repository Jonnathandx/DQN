import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Ruta al archivo summary.xml generado por SUMO
summary_file = "rl_summary.xml"

# Cargar archivo
tree = ET.parse(summary_file)
root = tree.getroot()

# Listas para almacenar los datos
times = []
mean_waiting_times = []
halting_vehicles = []
arrived_vehicles = []
inserted_vehicles = []
running_vehicles = []

# Extraer información de cada paso
for step in root.findall("step"):
    times.append(float(step.attrib["time"]))
    mean_waiting_times.append(float(step.attrib["meanWaitingTime"]))
    halting_vehicles.append(int(step.attrib["halting"]))
    arrived_vehicles.append(int(step.attrib["arrived"]))
    inserted_vehicles.append(int(step.attrib["inserted"]))
    running_vehicles.append(int(step.attrib["running"]))

# Flujo: vehículos que completaron su viaje por paso
flow = arrived_vehicles

# === Gráfico 1: Tiempo de espera promedio ===
plt.figure()
plt.plot(times, mean_waiting_times, label="Tiempo medio de espera", color="blue", linewidth=3)
plt.xlabel("Tiempo [s]", fontsize=14)
plt.ylabel("Espera promedio [s]", fontsize=14)
plt.title("Tiempo medio de espera por paso", fontsize=16)
plt.grid(True)
plt.legend(fontsize=14)
plt.show()

# === Gráfico 2: Vehículos detenidos ===
plt.figure()
plt.plot(times, halting_vehicles, label="Vehículos detenidos", color="red", linewidth=3)
plt.xlabel("Tiempo [s]", fontsize=14)
plt.ylabel("Cantidad", fontsize=14)
plt.title("Número de vehículos detenidos por paso", fontsize=16)
plt.grid(True)
plt.legend(fontsize=14)
plt.show()

# === Gráfico 3: Flujo vehicular ===
plt.figure()
plt.plot(times, flow, label="Vehículos que llegaron a destino", color="green", linewidth=3)
plt.xlabel("Tiempo [s]", fontsize=14)
plt.ylabel("Vehículos", fontsize=14)
plt.title("Flujo vehicular por paso", fontsize=16)
plt.grid(True)
plt.legend(fontsize=14)
plt.show()
