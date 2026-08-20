from de import DifferentialEvolution
from pso import ParticleSwarmOptimization
from random_forest import model
import pandas as pd

print("=" * 50)
print(" Intelligent Task Offloading System ")
print("=" * 50)

while True:

    print("\nChoose an Option")
    print("1. Run Differential Evolution (DE)")
    print("2. Run Particle Swarm Optimization (PSO)")
    print("3. Predict Best Algorithm using Random Forest")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":

        de = DifferentialEvolution()

        solution, fitness = de.optimize()

        print("\n===== Differential Evolution =====")
        print("Best Solution:")
        print(solution)

        print("\nBest Fitness:")
        print(fitness)

    elif choice == "2":

        pso = ParticleSwarmOptimization()

        solution, fitness = pso.optimize()

        print("\n===== Particle Swarm Optimization =====")
        print("Best Solution:")
        print(solution)

        print("\nBest Fitness:")
        print(fitness)

    elif choice == "3":

        tasks = int(input("\nEnter Number of Tasks: "))

        queue_wait = tasks + 100
        response_time = tasks + 200
        energy = 0.193
        offload = 10.5
        overloads = int(tasks * 0.95)

        new_data = pd.DataFrame({
            "Tasks": [tasks],
            "QueueWait": [queue_wait],
            "ResponseTime": [response_time],
            "EnergyPerTask": [energy],
            "OffloadPercentage": [offload],
            "Overloads": [overloads]
        })

        prediction = model.predict(new_data)

        print("\nPredicted Best Algorithm:", prediction[0])

    elif choice == "4":

        print("\nThank you!")
        break

    else:

        print("\nInvalid Choice!")