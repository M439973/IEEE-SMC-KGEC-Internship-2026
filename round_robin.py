import random
import time

# -------------------------
# CONFIGURATION
# -------------------------

NUM_TASKS = 12000
NUM_VMS = 50

# -------------------------
# TASK GENERATION
# -------------------------

def generate_tasks(num_tasks):
    return [random.randint(1000, 10000)
            for _ in range(num_tasks)]

# -------------------------
# VM GENERATION
# -------------------------

def generate_vms(num_vms):
    return [random.randint(1000, 2500)
            for _ in range(num_vms)]

# -------------------------
# ROUND ROBIN SCHEDULER
# -------------------------

def round_robin_schedule(tasks, vms):

    vm_loads = [0] * len(vms)

    for i, task in enumerate(tasks):

        vm_id = i % len(vms)

        exec_time = task / vms[vm_id]

        vm_loads[vm_id] += exec_time

    makespan = max(vm_loads)

    energy = sum(vm_loads) * 100

    cost = sum(vm_loads) * 5

    return makespan, energy, cost

# -------------------------
# MAIN
# -------------------------

start = time.time()

tasks = generate_tasks(NUM_TASKS)

vms = generate_vms(NUM_VMS)

makespan, energy, cost = round_robin_schedule(
    tasks,
    vms
)

end = time.time()

print("\nROUND ROBIN RESULTS")
print("=" * 40)

print(f"Makespan : {makespan:.2f}")
print(f"Energy   : {energy:.2f}")
print(f"Cost     : {cost:.2f}")
print(f"Runtime  : {end-start:.2f} sec")