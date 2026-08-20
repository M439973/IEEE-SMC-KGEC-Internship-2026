import random
import math
import time

# -----------------------------
# CONFIGURATION
# -----------------------------
NUM_TASKS = 12000
NUM_VMS = 50

POPULATION_SIZE = 50
MAX_ITER = 50

W1 = 0.45
W2 = 0.30
W3 = 0.25

INITIAL_TEMP = 100
COOLING_RATE = 0.95


# -----------------------------
# TASK GENERATION
# -----------------------------
def generate_tasks(num_tasks):
    tasks = []

    for i in range(num_tasks):
        tasks.append({
            "id": i,
            "length": random.randint(1000, 25000)
        })

    return tasks


# -----------------------------
# VM GENERATION
# -----------------------------
def generate_vms(num_vms):
    vms = []

    for i in range(num_vms):
        vms.append({
            "id": i,
            "mips": random.randint(1000, 2500),
            "cost": random.uniform(0.1, 0.5),
            "power_idle": 50,
            "power_max": 150
        })

    return vms


# -----------------------------
# EXECUTION TIME
# -----------------------------
def execution_time(task, vm):
    return task["length"] / vm["mips"]


# -----------------------------
# MAKESPAN
# -----------------------------
def calculate_makespan(schedule, tasks, vms):

    vm_times = [0] * len(vms)

    for task_id, vm_id in enumerate(schedule):

        vm_times[vm_id] += execution_time(
            tasks[task_id],
            vms[vm_id]
        )

    return max(vm_times), vm_times


# -----------------------------
# COST
# -----------------------------
def calculate_cost(vm_times, vms):

    total_cost = 0

    for i in range(len(vms)):
        total_cost += vm_times[i] * vms[i]["cost"]

    return total_cost


# -----------------------------
# ENERGY
# -----------------------------
def calculate_energy(vm_times, vms):

    energy = 0

    for i in range(len(vms)):

        utilization = min(vm_times[i] / max(vm_times), 1)

        power = (
            vms[i]["power_idle"]
            + (vms[i]["power_max"] - vms[i]["power_idle"])
            * utilization
        )

        energy += power * vm_times[i]

    return energy


# -----------------------------
# FITNESS FUNCTION
# -----------------------------
def fitness(schedule, tasks, vms):

    makespan, vm_times = calculate_makespan(
        schedule,
        tasks,
        vms
    )

    cost = calculate_cost(vm_times, vms)

    energy = calculate_energy(vm_times, vms)

    fitness_value = (
        W1 * makespan
        + W2 * cost
        + W3 * energy
    )

    return fitness_value


# -----------------------------
# INITIAL POPULATION
# -----------------------------
def initialize_population():

    population = []

    for _ in range(POPULATION_SIZE):

        solution = [
            random.randint(0, NUM_VMS - 1)
            for _ in range(NUM_TASKS)
        ]

        population.append(solution)

    return population


# -----------------------------
# CSO UPDATE
# -----------------------------
def cso_update(solution):

    new_solution = solution.copy()

    num_changes = random.randint(1, 5)

    for _ in range(num_changes):

        task_index = random.randint(
            0,
            len(solution) - 1
        )

        new_solution[task_index] = random.randint(
            0,
            NUM_VMS - 1
        )

    return new_solution


# -----------------------------
# SA NEIGHBOR
# -----------------------------
def generate_neighbor(solution):

    neighbor = solution.copy()

    task = random.randint(
        0,
        len(solution) - 1
    )

    neighbor[task] = random.randint(
        0,
        NUM_VMS - 1
    )

    return neighbor


# -----------------------------
# SIMULATED ANNEALING
# -----------------------------
def simulated_annealing(
        solution,
        tasks,
        vms,
        temperature):

    current = solution.copy()

    current_fit = fitness(
        current,
        tasks,
        vms
    )

    neighbor = generate_neighbor(current)

    neighbor_fit = fitness(
        neighbor,
        tasks,
        vms
    )

    delta = neighbor_fit - current_fit

    if delta < 0:
        current = neighbor

    else:

        probability = math.exp(
            -delta / temperature
        )

        if random.random() < probability:
            current = neighbor

    return current


# -----------------------------
# HYBRID CSO-SA
# -----------------------------
def hybrid_cso_sa(tasks, vms):

    population = initialize_population()

    temperature = INITIAL_TEMP

    best_solution = None
    best_fitness = float("inf")

    for iteration in range(MAX_ITER):

        scored_population = []

        for solution in population:

            fit = fitness(
                solution,
                tasks,
                vms
            )

            scored_population.append(
                (fit, solution)
            )

        scored_population.sort(
            key=lambda x: x[0]
        )

        if scored_population[0][0] < best_fitness:

            best_fitness = scored_population[0][0]
            best_solution = scored_population[0][1]

        print(
            f"Iteration {iteration+1} "
            f"Best Fitness = {best_fitness:.2f}"
        )

        # CSO exploration

        new_population = []

        for _, solution in scored_population:

            updated = cso_update(solution)

            new_population.append(updated)

        # SA exploitation on top 5

        for i in range(5):

            new_population[i] = simulated_annealing(
                new_population[i],
                tasks,
                vms,
                temperature
            )

        temperature *= COOLING_RATE

        population = new_population

    return best_solution, best_fitness


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    print("Generating Tasks...")
    tasks = generate_tasks(NUM_TASKS)

    print("Generating VMs...")
    vms = generate_vms(NUM_VMS)

    start = time.time()

    best_schedule, best_fit = hybrid_cso_sa(
        tasks,
        vms
    )

    end = time.time()

    makespan, vm_times = calculate_makespan(
        best_schedule,
        tasks,
        vms
    )

    energy = calculate_energy(
        vm_times,
        vms
    )

    cost = calculate_cost(
        vm_times,
        vms
    )

    print("\nRESULTS")
    print("=" * 40)

    print(f"Makespan : {makespan:.2f}")
    print(f"Energy   : {energy:.2f}")
    print(f"Cost     : {cost:.2f}")
    print(f"Fitness  : {best_fit:.2f}")
    print(f"Runtime  : {end-start:.2f} sec")