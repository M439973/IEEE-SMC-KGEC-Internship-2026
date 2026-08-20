import matplotlib.pyplot as plt

tasks = [6000, 9000, 12000]

cso_sa = [2075.21, 2993.80, 3522.51]
rr = [615.52, 915.13, 1369.94]
random_sched = [717.04, 1064.15, 1371.88]
ga = [550.90, 785.96, 1140.99]
pso = [574.35, 893.15, 1213.92]

plt.figure(figsize=(8,5))

plt.plot(tasks, cso_sa, marker='o', label='CSO-SA')
plt.plot(tasks, rr, marker='o', label='Round Robin')
plt.plot(tasks, random_sched, marker='o', label='Random')
plt.plot(tasks, ga, marker='o', label='GA')
plt.plot(tasks, pso, marker='o', label='PSO')

plt.xlabel("Number of Tasks")
plt.ylabel("Makespan")
plt.title("Makespan Comparison")

plt.legend()

plt.grid(True)

plt.show()