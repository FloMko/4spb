# get config
import yaml
import logging
import requests

import atexit
from apscheduler.schedulers.blocking import BlockingScheduler



class Scheduler:
    """
    class for rest interaction
    """

    def __init__(self):
        cfg = yaml.safe_load(open("config.yaml"))
        self.api_url = cfg['api_url']
        self.scheduler = BlockingScheduler()
        self.scheduler.add_job(self.update_cluster, 'interval', minutes=10)

    def update_cluster(self):
        resp = requests.get(self.api_url + 'update_cluster/')
        logging.debug('update status' + resp.text)

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    Scheduler().scheduler.start()
    # Shut down the scheduler when exiting the app
    atexit.register(Scheduler().scheduler.shutdown())