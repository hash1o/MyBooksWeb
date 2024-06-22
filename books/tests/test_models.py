
from django.test import TestCase

from books.models import *

from datetime import datetime,timezone

class UserModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='BBBB', password='qwerty', email='1@bbb.com')

    def test_default_values(self):
        self.assertEquals(self.user.username, 'BBBB')
        self.assertEquals(self.user.email, '1@bbb.com')
        self.assertEquals(self.user.is_active, True)
        self.assertEquals(self.user.is_staff, False)
        self.assertEquals(self.user.is_admin, False)

class ProfileTest(TestCase):
    
    def setUp(self):
        self.datetimenow = datetime.now(timezone.utc)
        self.user = User.objects.create(username='aaaa', password='aaaaa', email='y@y.com')

    
    def test_default_values(self):
        

        #一意性制約のため、profileを削除する (既にprofileが存在するから)
        Profile.objects.filter(user=self.user).delete()

        #新しくprofileを作成する
        profile = Profile.objects.create(
            user = self.user,
            name = "山田太郎",
            zipcode = "100-8111",
            prefecture = "東京都",
            city = "千代田区",
            address1 = "千代田1-1",
            address2 = "",
            tel = "03-3213-1111",
            created_at = self.datetimenow,
            updated_at = self.datetimenow,
            
            )
        
        self.assertEquals(profile.user.username, "aaaa")
        self.assertEquals(profile.user.email, "y@y.com")
        self.assertEquals(profile.name, "山田太郎")
        self.assertEquals(profile.zipcode, "100-8111")
        self.assertEquals(profile.prefecture, "東京都")
        self.assertEquals(profile.city, "千代田区")
        self.assertEquals(profile.address1, "千代田1-1")
        self.assertEquals(profile.address2, "")
        self.assertEquals(profile.tel, "03-3213-1111")
        
        #ミリ秒単位は誤差が生じるため切り捨てを行い、確認する
        self.assertEquals(profile.created_at.replace(microsecond=0), self.datetimenow.replace(microsecond=0))
        self.assertEquals(profile.updated_at.replace(microsecond=0), self.datetimenow.replace(microsecond=0))
        
    
    
class MemoBookTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='userA', password='qwerty', email='1aaaaa2@2aaaaa1.com')

    def test_default_values(self):
        book = MemoBook.objects.create(
            user=self.user,
            book_id="eX_eEAAAQBAJ",
            title="世界一流エンジニアの思考法",
            memo="おもしろかったです。",
            bookjson={'kind': 'books#volume', 'id': 'eX_eEAAAQBAJ'}
            )

        self.assertEquals(book.user.username, 'userA')
        self.assertEquals(book.user.email, '1aaaaa2@2aaaaa1.com')
        
        self.assertEquals(book.book_id, 'eX_eEAAAQBAJ')
        self.assertEquals(book.title, '世界一流エンジニアの思考法')
        self.assertEquals(book.memo, 'おもしろかったです。')
        self.assertEquals(book.bookjson, {'kind': 'books#volume', 'id': 'eX_eEAAAQBAJ'})