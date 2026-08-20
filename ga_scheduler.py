import random
import time

# -------------------------
# CONFIGURATION
# -------------------------

NUM_TASKS = 12000
NUM_VMS = 50

POP_SIZE = 30
GENERATIONS = 50
MUTATION_RATE = 0.05

# -------------------------
# TASKS & VMS
# -------------------------

def generate_tasks(n):
    return [random.randint(1000, 10000)
            for _ in range(n)]

def generate_vms(n):
    return [random.randint(1000, 2500)
            for _ in range(n)]

# -------------------------
# FITNESS
# -------------------------

def calculate_makespan(solution,
                       tasks,
                       vms):

    vm_loads = [0] * len(vms)

    for task_id, vm_id in enumerate(solution):

        exec_time = tasks[task_id] / vms[vm_id]

        vm_loads[vm_id] += exec_time

    return max(vm_loads)

def fitness(solution,
            tasks,
            vms):

    return 1 / (
        calculate_makespan(
            solution,
            tasks,
            vms
        ) + 1
    )

# -------------------------
# POPULATION
# -------------------------

def create_population():

    population = []

    for _ in range(POP_SIZE):

        chromosome = [
            random.randint(
                0,
                NUM_VMS - 1
            )
            for _ in range(NUM_TASKS)
        ]

        population.append(chromosome)

    return population

# -------------------------
# SELECTION
# -------------------------

def select_parent(population,
                  tasks,
                  vms):

    tournament = random.sample(
        population,
        3
    )

    tournament.sort(
        key=lambda x:
        fitness(
            x,
            tasks,
            vms
        ),
        reverse=True
    )

    return tournament[0]

# -------------------------
# CROSSOVER
# -------------------------

def crossover(parent1,
              parent2):

    point = random.randint(
        0,
        NUM_TASKS - 1
    )

    child = (
        parent1[:point]
        +
        parent2[point:]
    )

    return child

# -------------------------
# MUTATION
# -------------------------

def mutate(child):

    for i in range(len(child)):

        if random.random() < MUTATION_RATE:

            child[i] = random.randint(
                0,
                NUM_VMS - 1
            )

    return child

# -------------------------
# GA
# -------------------------

def genetic_algorithm(
        tasks,
        vms):

    population = create_population()

    for _ in range(GENERATIONS):

        new_population = []

        for _ in range(POP_SIZE):

            p1 = select_parent(
                population,
                tasks,
                vms
            )

            p2 = select_parent(
                population,
                tasks,
                vms
            )

            child = crossover(
                p1,
                p2
            )

            child = mutate(child)

            new_population.append(
                child
            )

        population = new_population

    best = max(
        population,
        key=lambda x:
        fitness(
            x,
            tasks,
            vms
        )
    )

    return best

# -------------------------
# MAIN
# -------------------------

start = time.time()

tasks = generate_tasks(
    NUM_TASKS
)

vms = generate_vms(
    NUM_VMS
)

best_solution = genetic_algorithm(
    tasks,
    vms
)

makespan = calculate_makespan(
    best_solution,
    tasks,
    vms
)

energy = makespan * NUM_TASKS

cost = energy * 0.05

end = time.time()

print("\nGA RESULTS")
print("=" * 40)

print(f"Makespan : {makespan:.2f}")
print(f"Energy   : {energy:.2f}")
print(f"Cost     : {cost:.2f}")
print(f"Runtime  : {end-start:.2f} sec")