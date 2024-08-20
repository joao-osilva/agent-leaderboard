from redis import Redis
from rq import Queue

# Connect to Redis server
redis_conn = Redis(host='redis-16597.c15.us-east-1-4.ec2.redns.redis-cloud.com', port=16597)
queue = Queue('default', connection=redis_conn)

def run_task(task):
    job = queue.enqueue(task)
