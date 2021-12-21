from flask import Flask
import rq_dashboard

from rq import Queue
from redis import Redis
from datetime import datetime, timedelta

from Redis1 import print_numbers
from rq.registry import ScheduledJobRegistry
from rq import Connection, Queue, Worker
from rq_scheduler import Scheduler


app = Flask(__name__)
app.config.from_object(rq_dashboard.default_settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")


@app.route("/")
def initialize__queue(queue_name):

  queue = Queue(queue_name, connection=Redis())
  # scheduler = Scheduler(queue_names,connection=Redis())
  
  # print(queue.started_job_registry)  # Returns StartedJobRegistry
  # queue.deferred_job_registry   # Returns DeferredJobRegistry
  # queue.finished_job_registry  # Returns FinishedJobRegistry
  # queue.failed_job_registry  # Returns FailedJobRegistry
  # print(queue.scheduled_job_registry)  # Returns ScheduledJobRegistry
  # burst = False

  # job = queue.enqueue(print_numbers, 'https://picsum.photos/v2/list')
  # job = queue.enqueue_in(timedelta(milliseconds=2), print_numbers,'https://picsum.photos/v2/list')
  # job = queue.enqueue_at(datetime(2021, 12, 21, 16, 16,00), print_numbers, 'https://picsum.photos/v2/list')
  
  print("ASDFGHJ")

  print(job in queue) 
  print('Job enqueued_at: ' , job.enqueued_at)
  registry = ScheduledJobRegistry(queue=queue)
  print(job in registry)  
# 

  worker = Worker(queue)
  worker.work()


with Connection():
  initialize__queue('Queue_ONe')

  # initialize__queue('2')

if __name__ == "__main__":
    app.run()


# def image_download(url):
#     # resp = requests.get(url)
#     # return len(resp.text.split())


#     r = requests.get(url)
#     pak_json = r.json()

        



# redis_conn = Redis()
# q = Queue(connection=redis_conn)  # no args implies the default queue



# job = q.enqueue(image_download, 'https://picsum.photos/v2/list')
# print("REsult : ",job.result)