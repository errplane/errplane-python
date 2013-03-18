import time

from threading import Thread
from worker_queue import WorkerQueue

class Errplane(object):
  def __init__(self, api_key, application_id,
               environment="development",
               max_items=10000,
               max_post_size=200, worker_threads=3, worker_thread_interval=5):
    self._queue = WorkerQueue(api_key, application_id, environment,
                              max_items, max_post_size, worker_threads, worker_thread_interval)

  def report(self, name, value=1, timestamp="now", context=None):
    point = {}
    point["name"] = name
    point["value"] = value
    point["timestamp"] = timestamp
    point["context"] = context
    self._queue.push(point)

  def heartbeat(self, name, interval, value=1, context=None):
    thread = Thread(target=self._heartbeat, args=(name, interval, value, context))
    thread.setDaemon(True)
    thread.start()

  def _heartbeat(self, name, interval, value, context):
    while True:
      time.sleep(interval)
      self.report(name, value=value, context=context)



