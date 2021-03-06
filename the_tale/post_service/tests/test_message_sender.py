# coding: utf-8
import mock

from dext.settings import settings

from the_tale.common.utils import testcase


from the_tale.post_service.prototypes import MessagePrototype
from the_tale.post_service.conf import post_service_settings
from the_tale.post_service.message_handlers import TestHandler

from the_tale.amqp_environment import environment


@mock.patch('the_tale.post_service.conf.post_service_settings.ENABLE_MESSAGE_SENDER', True)
class MessageSenderTests(testcase.TestCase):

    def setUp(self):
        super(MessageSenderTests, self).setUp()
        self.message = MessagePrototype.create(TestHandler())

        environment.deinitialize()
        environment.initialize()

        self.worker = environment.workers.message_sender

    def test_send_message_skipped(self):
        self.worker.send_message(self.message)
        self.assertTrue(self.message.state.is_SKIPPED)

    def test_send_message_processed(self):
        settings[post_service_settings.SETTINGS_ALLOWED_KEY] = 'allowed'
        self.worker.send_message(self.message)
        self.assertTrue(self.message.state.is_PROCESSED)

    def test_send_message_forces_process(self):
        settings[post_service_settings.SETTINGS_FORCE_ALLOWED_KEY] = TestHandler().settings_type_uid
        self.worker.send_message(self.message)
        self.assertTrue(self.message.state.is_PROCESSED)
