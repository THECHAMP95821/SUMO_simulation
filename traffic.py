import traci
import os
import time  # Added for introducing delays

# Set SUMO_HOME environment variable
os.environ["SUMO_HOME"] = r"C:/Program Files (x86)/Eclipse/Sumo"

# Start SUMO with GUI
sumo_cmd = [
    r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo-gui",
    "-c", r"C:\Users\Parv Malhotra\Desktop\traffic\traffic.sumocfg"
]
traci.start(sumo_cmd)

# Set GUI speed (default 1.0x, lower is slower)
gui_speed = 0.1  # Adjust to control the speed (e.g., 0.5 for half-speed)

# Simulation step
step = 0
max_steps = 1000  # Run for 1000 steps

# Maintain a set of added vehicle IDs
added_vehicles = set()

# Dataset with dynamic vehicle data, including entry times
dataset = [
    {
        'number_of_vehicles_detected': 8,
        'detected_vehicles': [
            {'vehicle_id': 1, 'vehicle_type': 'car', 'speed_info': {'kph': 1.13}, 'entry_time': 0},
            {'vehicle_id': 2, 'vehicle_type': 'car', 'speed_info': {'kph': 3.74}, 'entry_time': 5},
            {'vehicle_id': 3, 'vehicle_type': 'car', 'speed_info': {'kph': 5.07}, 'entry_time': 10},
            {'vehicle_id': 4, 'vehicle_type': 'car', 'speed_info': {'kph': 5.53}, 'entry_time': 15},
            {'vehicle_id': 5, 'vehicle_type': 'car', 'speed_info': {'kph': 2.27}, 'entry_time': 20},
            {'vehicle_id': 6, 'vehicle_type': 'car', 'speed_info': {'kph': 2.00}, 'entry_time': 25},
            {'vehicle_id': 7, 'vehicle_type': 'truck', 'speed_info': {'kph': 2.12}, 'entry_time': 30},
            {'vehicle_id': 8, 'vehicle_type': 'car', 'speed_info': {'kph': 5}, 'entry_time': 35},
        ]
    },
    {
        'number_of_vehicles_detected': 9,
        'detected_vehicles': [
            {'vehicle_id': 1, 'vehicle_type': 'car', 'speed_info': {'kph': 1.13}, 'entry_time': 0},
            {'vehicle_id': 2, 'vehicle_type': 'car', 'speed_info': {'kph': 3.74}, 'entry_time': 5},
            {'vehicle_id': 3, 'vehicle_type': 'car', 'speed_info': {'kph': 5.07}, 'entry_time': 10},
            {'vehicle_id': 4, 'vehicle_type': 'car', 'speed_info': {'kph': 5.53}, 'entry_time': 15},
            {'vehicle_id': 5, 'vehicle_type': 'car', 'speed_info': {'kph': 2.27}, 'entry_time': 20},
            {'vehicle_id': 6, 'vehicle_type': 'car', 'speed_info': {'kph': 2.00}, 'entry_time': 25},
            {'vehicle_id': 7, 'vehicle_type': 'truck', 'speed_info': {'kph': 2.12}, 'entry_time': 30},
            {'vehicle_id': 8, 'vehicle_type': 'car', 'speed_info': {'kph': 1}, 'entry_time': 35},
            {'vehicle_id': 9, 'vehicle_type': 'car', 'speed_info': {'kph': 2}, 'entry_time': 40},
        ]
    },
    {
        'number_of_vehicles_detected': 10,
        'detected_vehicles': [
            {'vehicle_id': 1, 'vehicle_type': 'car', 'speed_info': {'kph': 2.13}, 'entry_time': 0},
            {'vehicle_id': 2, 'vehicle_type': 'car', 'speed_info': {'kph': 3.74}, 'entry_time': 5},
            {'vehicle_id': 3, 'vehicle_type': 'car', 'speed_info': {'kph': 5.07}, 'entry_time': 10},
            {'vehicle_id': 4, 'vehicle_type': 'car', 'speed_info': {'kph': 5.53}, 'entry_time': 15},
            {'vehicle_id': 5, 'vehicle_type': 'car', 'speed_info': {'kph': 2.27}, 'entry_time': 20},
            {'vehicle_id': 6, 'vehicle_type': 'car', 'speed_info': {'kph': 2.00}, 'entry_time': 25},
            {'vehicle_id': 7, 'vehicle_type': 'truck', 'speed_info': {'kph': 2.12}, 'entry_time': 30},
            {'vehicle_id': 8, 'vehicle_type': 'car', 'speed_info': {'kph': 3}, 'entry_time': 35},
            {'vehicle_id': 9, 'vehicle_type': 'car', 'speed_info': {'kph': 2}, 'entry_time': 40},
            {'vehicle_id': 10, 'vehicle_type': 'car', 'speed_info': {'kph': 2}, 'entry_time': 41},
        ]
    },
    {
        'number_of_vehicles_detected': 11,
        'detected_vehicles': [
            {'vehicle_id': 1, 'vehicle_type': 'car', 'speed_info': {'kph': 2.13}, 'entry_time': 0},
            {'vehicle_id': 2, 'vehicle_type': 'car', 'speed_info': {'kph': 3.74}, 'entry_time': 5},
            {'vehicle_id': 3, 'vehicle_type': 'car', 'speed_info': {'kph': 5.07}, 'entry_time': 10},
            {'vehicle_id': 4, 'vehicle_type': 'car', 'speed_info': {'kph': 5.53}, 'entry_time': 15},
            {'vehicle_id': 5, 'vehicle_type': 'car', 'speed_info': {'kph': 2.27}, 'entry_time': 20},
            {'vehicle_id': 6, 'vehicle_type': 'car', 'speed_info': {'kph': 2.00}, 'entry_time': 25},
            {'vehicle_id': 7, 'vehicle_type': 'truck', 'speed_info': {'kph': 2.12}, 'entry_time': 30},
            {'vehicle_id': 8, 'vehicle_type': 'car', 'speed_info': {'kph': 3}, 'entry_time': 35},
            {'vehicle_id': 9, 'vehicle_type': 'car', 'speed_info': {'kph': 2}, 'entry_time': 40},
            {'vehicle_id': 10, 'vehicle_type': 'car', 'speed_info': {'kph': 2}, 'entry_time': 41},
            {'vehicle_id': 11, 'vehicle_type': 'car', 'speed_info': {'kph': 3.7}, 'entry_time': 42},
        ]
    },
]

# Flatten dataset to track vehicles with their entry times
vehicles_to_add = []
for entry in dataset:
    vehicles_to_add.extend(entry['detected_vehicles'])

while step < max_steps:
    print(f"Simulation step: {step}")  # Debugging step

    # Advance simulation
    traci.simulationStep()

    # Slow down the simulation using time.sleep()
    time.sleep(gui_speed)  # Introduce delay to make simulation slower

    # Check and add vehicles scheduled for the current step
    for vehicle in vehicles_to_add:
        vehicle_id = str(vehicle['vehicle_id'])
        entry_time = vehicle['entry_time']
        vehicle_type = vehicle['vehicle_type']
        speed = vehicle['speed_info']['kph'] or 0  # Default to 0 if speed is None

        # Add vehicle only if the current step matches the entry time and it hasn't been added
        if step == entry_time and vehicle_id not in added_vehicles:
            try:
                print(f"Adding vehicle {vehicle_id} at step {step} with speed {speed} kph")  # Debug
                traci.vehicle.add(vehID=vehicle_id, routeID="route1to2", typeID=vehicle_type)
                traci.vehicle.setSpeed(vehicle_id, speed / 3.6)  # Convert kph to m/s
                added_vehicles.add(vehicle_id)  # Mark vehicle as added
            except traci.TraCIException as e:
                print(f"Error adding vehicle {vehicle_id}: {e}")

    # Optionally: Print all active vehicles in the simulation
    active_vehicles = traci.vehicle.getIDList()
    print(f"Active vehicles: {active_vehicles}")

    # Increment step
    step += 1

# Close the simulation
traci.close()
