import tasks

for i in range(5):
    if (i % 2) == 0:
        tasks.taskA.delay()
    else:
        tasks.taskB.delay()

