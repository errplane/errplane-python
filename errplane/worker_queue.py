import time
import requests
import json
import hashlib
import logging
import base64

from threading import Thread
from Queue import Queue

class WorkerQueue:
  def __init__(self, api_key, application_id,
               environment, max_items, max_post_size, worker_threads, worker_thread_interval):
    logging.debug("[Errplane] Initializing threaded queue with maximum of " + str(max_items) + " items.")
    self._items = Queue(max_items)

    self.api_key = api_key
    self.application_id = application_id
    self.environment = environment

    self.max_post_size = max_post_size
    self.worker_thread_interval = worker_thread_interval

    self._threads = []

    for n in range(worker_threads):
      thread = Thread(target=self.process)
      thread.setDaemon(True)
      self._threads.append(thread)
      thread.start()

  def push(self, item):
    try:
      return self._items.put_nowait(item)
    except:
      return None

  def pop(self):
    try:
      return self._items.get_nowait()
    except:
      return None

  def process(self):
    logging.debug("[Errplane] Spawning worker thread.")
    while True:
      try:
        time.sleep(self.worker_thread_interval)

        while self._items.qsize():
            points = []
            while self._items.qsize() and len(points) < self.max_post_size:
              point = self.pop()
              if point: points.append(point)

            lines = []
            for point in points:
              line = point["name"]
              line += " " + str(point["value"])
              line += " " + point["timestamp"]
              if point["context"]: line += " " + base64.b64encode(point["context"])
              lines.append(line)

            data = "\n".join(lines)
            url = "https://apiv2.errplane.com/databases/" + self.application_id + self.environment + "/points?api_key=" + self.api_key

            logging.debug("[Errplane] POSTing data:")
            logging.debug(data)

            requests.post(url, data=data, headers={'Connection':'close'})

            if self._items.qsize() < self.max_post_size:
              break

      except Exception as e:
        logging.error("[Errplane] Caught exception in thread: " + e.message)
