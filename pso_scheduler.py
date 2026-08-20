import random
import time

NUM_TASKS = 12000
NUM_VMS = 50

NUM_PARTICLES = 30
MAX_ITER = 50

# -------------------------
# TASKS & VMS
# -------------------------

def generate_tasks(n):
    return [random.randint(1000,10000)
            for _ in range(n)]

def generate_vms(n):
    return [random.randint(1000,2500)
            for _ in range(n)]

# -------------------------
# MAKESPAN
# -------------------------

def calculate_makespan(solution,
                       tasks,
                       vms):

    vm_loads = [0] * len(vms)

    for t, vm in enumerate(solution):

        vm_loads[vm] += (
            tasks[t] / vms[vm]
        )

    return max(vm_loads)

# -------------------------
# PARTICLE
# -------------------------

def create_particle():

    return [
        random.randint(
            0,
            NUM_VMS-1
        )
        for _ in range(NUM_TASKS)
    ]

# -------------------------
# PSO
# -------------------------

def pso(tasks,vms):

    particles = [
        create_particle()
        for _ in range(NUM_PARTICLES)
    ]

    pbest = particles[:]

    gbest = min(
        particles,
        key=lambda x:
        calculate_makespan(
            x,
            tasks,
            vms
        )
    )

    for _ in range(MAX_ITER):

        for i in range(NUM_PARTICLES):

            particle = particles[i]

            for j in range(NUM_TASKS):

                r = random.random()

                if r < 0.3:

                    particle[j] = pbest[i][j]

                elif r < 0.6:

                    particle[j] = gbest[j]

                else:

                    particle[j] = random.randint(
                        0,
                        NUM_VMS-1
                    )

            if (
                calculate_makespan(
                    particle,
                    tasks,
                    vms
                )
                <
                calculate_makespan(
                    pbest[i],
                    tasks,
                    vms
                )
            ):
                pbest[i] = particle[:]

        gbest = min(
            pbest,
            key=lambda x:
            calculate_makespan(
                x,
                tasks,
                vms
            )
        )

    return gbest

# -------------------------
# MAIN
# -------------------------

start = time.time()

tasks = generate_tasks(NUM_TASKS)

vms = generate_vms(NUM_VMS)

best = pso(tasks,vms)

makespan = calculate_makespan(
    best,
    tasks,
    vms
)

energy = makespan * NUM_TASKS

cost = energy * 0.05

end = time.time()

print("\nPSO RESULTS")
print("="*40)

print(f"Makespan : {makespan:.2f}")
print(f"Energy   : {energy:.2f}")
print(f"Cost     : {cost:.2f}")
print(f"Runtime  : {end-start:.2f} sec")