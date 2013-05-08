# coding: utf-8

from django.utils.log import getLogger

from dext.settings import settings

from common.amqp_queues import connection, BaseWorker
from common import postponed_tasks

from accounts.prototypes import AccountPrototype


class AccountManagerException(Exception): pass


class Worker(BaseWorker):

    logger = getLogger('the-tale.workers.accounts_accounts_manager')
    name = 'accounts manager'
    command_name = 'accounts_accounts_manager'

    def __init__(self, messages_queue, stop_queue):
        super(Worker, self).__init__(command_queue=messages_queue)
        self.stop_queue = connection.SimpleQueue(stop_queue)
        self.initialized = True

    def clean_queues(self):
        super(Worker, self).clean_queues()
        self.stop_queue.queue.purge()

    def initialize(self):
        postponed_tasks.autodiscover()
        postponed_tasks.PostponedTaskPrototype.reset_all()
        self.logger.info('ACCOUNT_MANAGER INITIALIZED')

    def run(self):

        while not self.exception_raised and not self.stop_required:
            game_cmd = self.command_queue.get(block=True)
            game_cmd.ack()

            settings.refresh()
            self.process_cmd(game_cmd.payload)

    def cmd_task(self, task_id):
        return self.send_cmd('task', {'task_id': task_id})

    def process_task(self, task_id):
        task = postponed_tasks.PostponedTaskPrototype.get_by_id(task_id)
        task.process(self.logger)
        task.do_postsave_actions()

    def cmd_update_active_state(self, account_id):
        return self.send_cmd('update_active_state', {'account_id': account_id})

    def process_update_active_state(self, account_id):
        AccountPrototype.get_by_id(account_id).update_active_state()

    def cmd_stop(self):
        return self.send_cmd('stop')

    def process_stop(self):
        self.initialized = False
        self.stop_required = True
        self.stop_queue.put({'code': 'stopped', 'worker': 'accounts_manager'}, serializer='json', compression=None)
        self.logger.info('ACCOUNTS MANAGER STOPPED')