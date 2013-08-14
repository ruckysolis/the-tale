# coding: utf-8

from common.utils import testcase

from forum.prototypes import CategoryPrototype, SubCategoryPrototype, ThreadPrototype, PostPrototype
from forum.models import Thread, Post

from accounts.models import Award, AWARD_TYPE
from accounts.logic import register_user
from accounts.prototypes import AccountPrototype

from blogs.prototypes import PostPrototype as BlogPostPrototype, POST_STATE as BLOG_POST_STATE
from blogs.conf import blogs_settings

from game.logic import create_test_map

from game.bills.prototypes import BillPrototype, VotePrototype
from game.bills.bills import PlaceRenaming
from game.bills.models import Vote
from game.bills.conf import bills_settings
from game.bills.relations import BILL_STATE, VOTE_TYPE

from game.phrase_candidates.prototypes import PhraseCandidatePrototype
from game.phrase_candidates.models import PHRASE_CANDIDATE_STATE

from accounts.might import calculate_might

class CalculateMightTests(testcase.TestCase):

    def setUp(self):
        super(CalculateMightTests, self).setUp()
        self.place_1, self.place_2, self.place_3 = create_test_map()

        result, account_id, bundle_id = register_user('test_user', 'test_user@test.com', '111111')
        self.account = AccountPrototype.get_by_id(account_id)

        result, account_id, bundle_id = register_user('test_user_2', 'test_user_2@test.com', '111111', referral_of_id=self.account.id)
        self.account_2 = AccountPrototype.get_by_id(account_id)

        self.forum_category = CategoryPrototype.create('category', 'category-slug', 0)
        self.bills_subcategory = SubCategoryPrototype.create(self.forum_category, 'subcategory', order=0, uid=bills_settings.FORUM_CATEGORY_UID)
        self.blogs_subcategory = SubCategoryPrototype.create(self.forum_category, blogs_settings.FORUM_CATEGORY_UID + '-caption', order=1, uid=blogs_settings.FORUM_CATEGORY_UID)


    def test_initialize(self):
        self.assertEqual(self.account.might, 0)

    def test_no_might(self):
        self.assertEqual(calculate_might(self.account), 0)

    def test_forum_thread_might(self):
        ThreadPrototype.create(self.bills_subcategory, 'caption', self.account, 'text')

        self.assertTrue(calculate_might(self.account) > 0)
        self.assertEqual(calculate_might(self.account_2), 0)

    def test_forum_post_might(self):
        thread = ThreadPrototype.create(self.bills_subcategory, 'caption', self.account_2, 'text')
        PostPrototype.create(thread, self.account, 'text')

        self.assertTrue(calculate_might(self.account) > 0)
        self.assertTrue(calculate_might(self.account_2) > 0)

    def test_accepted_bill_might(self):
        old_might = calculate_might(self.account)
        bill_data = PlaceRenaming(place_id=self.place_1.id, base_name='bill_place')
        bill = BillPrototype.create(self.account, 'caption', 'rationale', bill_data)
        bill.state = BILL_STATE.ACCEPTED
        bill.save()

        Post.objects.all().delete()
        Thread.objects.all().delete()
        Vote.objects.all().delete()

        self.assertTrue(calculate_might(self.account) > old_might)
        self.assertEqual(calculate_might(self.account_2), 0)

    def test_voted_bill_might(self):
        old_might = calculate_might(self.account)
        bill_data = PlaceRenaming(place_id=self.place_1.id, base_name='bill_place')
        bill = BillPrototype.create(self.account, 'caption', 'rationale', bill_data)
        bill.state = BILL_STATE.VOTING
        bill.save()

        Post.objects.all().delete()
        Thread.objects.all().delete()
        Vote.objects.all().delete()

        self.assertEqual(calculate_might(self.account), old_might)
        self.assertEqual(calculate_might(self.account_2), 0)

    def test_rejected_bill_might(self):
        old_might = calculate_might(self.account)
        bill_data = PlaceRenaming(place_id=self.place_1.id, base_name='bill_place')
        bill = BillPrototype.create(self.account, 'caption', 'rationale', bill_data)
        bill.state = BILL_STATE.REJECTED
        bill.save()

        Post.objects.all().delete()
        Thread.objects.all().delete()
        Vote.objects.all().delete()

        self.assertEqual(calculate_might(self.account), old_might)
        self.assertEqual(calculate_might(self.account_2), 0)

    def test_forum_vote_might(self):
        old_might = calculate_might(self.account)
        bill_data = PlaceRenaming(place_id=self.place_1.id, base_name='bill_place')
        bill = BillPrototype.create(self.account_2, 'caption', 'rationale', bill_data)
        bill.state = BILL_STATE.REJECTED
        bill.save()

        Post.objects.all().delete()
        Thread.objects.all().delete()
        Vote.objects.all().delete()

        self.assertEqual(calculate_might(self.account_2), old_might)
        self.assertEqual(calculate_might(self.account), 0)

        VotePrototype.create(self.account, bill, VOTE_TYPE.FOR)
        self.assertTrue(calculate_might(self.account) > 0)

        Vote.objects.all().delete()
        VotePrototype.create(self.account, bill, VOTE_TYPE.AGAINST)
        self.assertTrue(calculate_might(self.account) > 0)

        Vote.objects.all().delete()
        VotePrototype.create(self.account, bill, VOTE_TYPE.REFRAINED)
        self.assertEqual(calculate_might(self.account), 0)

    def test_phrase_candidate_might(self):
        old_might = calculate_might(self.account)
        phrase =  PhraseCandidatePrototype.create(type_='type',
                                                  type_name=u'type name',
                                                  subtype='subtype',
                                                  subtype_name=u'subtype name',
                                                  author=self.account,
                                                  text=u'text')

        self.assertEqual(old_might, calculate_might(self.account))
        phrase.state = PHRASE_CANDIDATE_STATE.ADDED
        phrase.save()

        new_might = calculate_might(self.account)
        self.assertTrue(new_might > old_might)

        phrase =  PhraseCandidatePrototype.create(type_='type',
                                                  type_name=u'type name',
                                                  subtype='subtype',
                                                  subtype_name=u'subtype name',
                                                  author=self.account_2,
                                                  text=u'text')
        phrase.state = PHRASE_CANDIDATE_STATE.ADDED
        phrase.save()

        self.assertEqual(new_might, calculate_might(self.account))


    def test_folclor_might(self):
        old_might = calculate_might(self.account)
        post = BlogPostPrototype.create(author=self.account, caption='caption', text='text')

        Post.objects.all().delete()
        Thread.objects.all().delete()
        Vote.objects.all().delete()

        self.assertEqual(old_might, calculate_might(self.account))

        post.state = BLOG_POST_STATE.ACCEPTED
        post._model.votes = 2
        post.save()

        new_might = calculate_might(self.account)
        self.assertTrue(new_might > old_might)

        post = BlogPostPrototype.create(author=self.account_2, caption='caption', text='text')

        Post.objects.all().delete()
        Thread.objects.all().delete()
        Vote.objects.all().delete()

        post.state = BLOG_POST_STATE.ACCEPTED
        post._model.votes = 1
        post.save()

        self.assertEqual(new_might, calculate_might(self.account))

    def test_custom_might(self):
        Award.objects.create(account=self.account._model, type=AWARD_TYPE.BUG_MINOR)
        self.assertTrue(calculate_might(self.account) > 0)

    def test_referral_custom_might(self):
        self.account_2.set_might(666)

        self.assertTrue(calculate_might(self.account) > 0)