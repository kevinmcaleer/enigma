import dispy

nodes = ['192.168.2.*','192.168.1.*']

def add_number(num):
    result = num + 1
    return result

cluster = dispy.JobCluster(add_number, nodes=nodes, loglevel=dispy.logger.DEBUG)

jobs = []
id=1
for n in range(1,100):
    job = cluster.submit(n)
    job.id = id # Associate an ID to the job
    jobs.append(job)
    id += 1   # Next job

print( "Waiting..." )
cluster.wait()

for job in jobs:
    print(f"job {job.id} result is: {job.result}")