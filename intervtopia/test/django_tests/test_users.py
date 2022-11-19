from django.test import TestCase
from users.models import Language, Company, Position, Calendar, CustomUser, RandomMatching, PreferenceMatching
# Create your tests here.

class TestLanguage(TestCase):

    def test_add(self):
        # Test insertion: valid input
        self.assertEqual(Language.add('TestLang'), Language.objects.get(lang_name = 'TestLang'))
        # Test insertion: invalid input
        self.assertRaisesMessage(ValueError, "input cannot be empty", Language.add(''))
        self.assertWarnsMessage(UserWarning, 
            "This language has not been seen before, please make sure it is valid", 
            Language.add('anvnoadnvandoanigfnaoi')
        )
        
    def test_remove(self):
        # Test remove a language from the database
        Language.add('TestLang')
        Language.remove('TestLang')
        self.assertEqual(len(Language.objects.filter(lang_name = 'TestLang')), 0)
        # If the input is empty raise an error
        self.assertRaisesMessage(ValueError, "input cannot be empty", Language.remove(''))
        # If the input is not in the database, raise an error
        self.assertRaisesMessage(ValueError, 'TestLang is not in the database', Language.remove('TestLang'))

    def test_get(self):
        Language.add('TestLang')
        self.assertEqual(Language.get('TestLang').lang_name, 'TestLang')
        self.assertRaisesMessage(ValueError, "input cannot be empty", Language.get(''))
        Language.remove('TestLang')
        self.assertRaisesMessage(ValueError, 'TestLang is not in the database', Language.get('TestLang'))

class TestCompany(TestCase):
    testCompany = 'TestCompany'

    def test_add(self):
        # Test insertion: valid input
        self.assertEqual(Company.add(self.testCompany), Company.objects.get(company_name = self.testCompany))
        # Test insertion: invalid input
        self.assertRaisesMessage(ValueError, "input cannot be empty", Company.add(''))
        self.assertWarnsMessage(UserWarning, 
            "This company has not been seen before, please make sure it is valid", 
            Company.add('anvnoadnvandoanigfnaoi')
        )
        
    def test_remove(self):
        # Test remove a company from the database
        Company.add(self.testCompany)
        Company.remove(self.testCompany)
        self.assertEqual(len(Company.objects.filter(company_name = self.testCompany)), 0)
        # If the input is empty raise an error
        self.assertRaisesMessage(ValueError, "input cannot be empty", Company.remove(''))
        # If the input is not in the database, raise an error
        self.assertRaisesMessage(ValueError, 'TestCompany is not in the database', Company.remove(self.testCompany))

    def test_get(self):
        Company.add(self.testCompany)
        self.assertEqual(Company.get(self.testCompany).company_name, self.testCompany)
        self.assertRaisesMessage(ValueError, "input cannot be empty", Company.get(''))
        Company.remove(self.testCompany)
        self.assertRaisesMessage(ValueError, 'TestCompany is not in the database', Company.get(self.testCompany))

    def test_update(self):
        Company.add(self.testCompany)
        self.assertEqual(Company.update(self.testCompany, 'NewTestCompany').company_name, 'NewTestCompany')
        self.assertRaisesMessage(ValueError, "input cannot be empty", Company.update(self.testCompany, ''))
        self.assertRaisesMessage(ValueError, "input cannot be empty", Company.update('', self.testCompany))
        self.assertRaisesMessage(ValueError, "input cannot be empty", Company.update('', ''))
        self.assertRaisesMessage(ValueError, "RandomTestCompany is not in the database", Company.update('RandomTestCompany', self.testCompany))
        Company.remove(self.testCompany)

class TestPosition(TestCase):
    testPosition = 'TestPosition'

    def test_add(self):
        # Test insertion: valid input
        self.assertEqual(Position.add(self.testPosition), Position.objects.get(position_name = self.testPosition))
        # Test insertion: invalid input
        self.assertRaisesMessage(ValueError, "input cannot be empty", Position.add(''))
        self.assertWarnsMessage(UserWarning, 
            "This position has not been seen before, please make sure it is valid", 
            Position.add('anvnoadnvandoanigfnaoi')
        )
        
    def test_remove(self):
        # Test remove a company from the database
        Position.add(self.testPosition)
        Position.remove(self.testPosition)
        self.assertEqual(len(Position.objects.filter(position_name = self.testPosition)), 0)
        # If the input is empty raise an error
        self.assertRaisesMessage(ValueError, "input cannot be empty", Position.remove(''))
        # If the input is not in the database, raise an error
        self.assertRaisesMessage(ValueError, 'TestPosition is not in the database', Position.remove(self.testPosition))

    def test_get(self):
        Position.add(self.testPosition)
        self.assertEqual(Position.get(self.testPosition).position_name, self.testPosition)
        self.assertRaisesMessage(ValueError, "input cannot be empty", Position.get(''))
        Position.remove(self.testPosition)
        self.assertRaisesMessage(ValueError, 'TestPosition is not in the database', Position.get(self.testPosition))

    def test_update(self):
        Position.add(self.testPosition)
        self.assertEqual(Position.update(self.testPosition, 'NewTestPosition').position_name, 'NewTestPosition')
        self.assertRaisesMessage(ValueError, "input cannot be empty", Position.update(self.testPosition, ''))
        self.assertRaisesMessage(ValueError, "input cannot be empty", Position.update('', self.testPosition))
        self.assertRaisesMessage(ValueError, "input cannot be empty", Position.update('', ''))
        self.assertRaisesMessage(ValueError, "RandomTestPosition is not in the database", Position.update('RandomTestPosition', self.testPosition))
        
class TestCalendar(TestCase):
    testCalendarURL = 'https://calendar.google.com/calendar/u/0/r'

    def test_add(self):
        # Test insertion: valid input
        self.assertEqual(Calendar.add(self.testCalendarURL), Calendar.objects.get(ext_url = self.testCalendarURL))
        # Test insertion: invalid input
        self.assertRaisesMessage(ValueError, "input cannot be empty", Calendar.add(''))
        
    def test_remove(self):
        Calendar.add(self.testCalendarURL)
        Calendar.remove(self.testCalendarURL)
        self.assertEqual(len(Calendar.objects.filter(ext_url = self.testCalendarURL)), 0)
        # If the input is empty raise an error
        self.assertRaisesMessage(ValueError, "input cannot be empty", Calendar.remove(''))
        # If the input is not in the database, raise an error
        self.assertRaisesMessage(ValueError, 'TestLang is not in the database')

    def test_get(self):
        Calendar.add(self.testCalendarURL)
        self.assertEqual(Calendar.get(self.testCalendarURL).ext_url, self.testCalendarURL)
        self.assertRaisesMessage(ValueError, "input cannot be empty", Calendar.get(''))
        Calendar.remove(self.testCalendarURL)

    def test_update(self):
        Calendar.add(self.testCalendarURL)
        self.assertEqual(Position.update(self.testCalendarURL, 'NewTestURL').ext_url, 'NewTestURL')
        self.assertRaisesMessage(ValueError, "input cannot be empty", Calendar.update(self.testCalendarURL, ''))
        self.assertRaisesMessage(ValueError, "input cannot be empty", Calendar.update('', self.testCalendarURL))
        self.assertRaisesMessage(ValueError, "input cannot be empty", Calendar.update('', ''))
        self.assertRaisesMessage(ValueError, "RondamTestURL is not in the database", Calendar.update('RandomTestPosition', self.testCalendarURL))

class TestCustomUser(TestCase):
    user = CustomUser()

    def test_create_user_base(self):
        '''
        Test function: create_user_base
        Testcases:
            1. the function should create a CustomUser object, store it in the database and return the object
            2. the function should take care of invalid inputs
        '''
        user = CustomUser.create_user_base(username = 'Test user', password='123456', email='test@intervtopia.com')
        self.assertEqual(user.username, 'Test user')
        self.assertEqual(user.password, '123456')
        self.assertEqual(user.email, 'test@intervtopia.com')
        self.assertRaises(ValueError, CustomUser.create_user_base(username='', password='', email=''))
        self.assertRaisesMessage(ValueError, 
            "Username Test user is taken, pick another name", 
            CustomUser.create_user_base(username='Test user', password='abdvajdiavna', email='test@intervtopia.com')
        )

    def test_add_target_company(self):
        '''
        Test function: add_target_company
        Testcases:
            1. the function should return 0 if the input is a valid company name
            2. the function should return -1 if the input is an empty string
            3. the function should raise a ValueError if the input is an empty string
            4. the function should raise a UserWarning if the input is a company has not been seemed before, 
                as the user may enter some random string that is not a valid company name. 
                It cannot be an error, as there may be programming languages that has not been stored in our database
        '''
        self.assertEqual(self.user.add_target_company('Google'), 0)
        self.assertTrue(Company.get('Google') in self.user.target_companys)
        self.assertNotEqual(self.user.add_target_company(''), 0)
        
        
    def test_remove_target_company(self):
        '''
        Test function: add_target_company
        Testcases:
            1. the function should return 0 if the input is a valid company name
            2. the function should return -1 if the input is an empty string
            3. the function should raise a ValueError if the input is an empty string
            4. the function should raise a UserWarning if the input is a language has not been seemed before, 
                as the user may enter some random string that is not a valid programming language. 
                It cannot be an error, as there may be programming languages that has not been stored in our database
        '''
        self.user.add_target_company('Google')
        self.assertEqual(self.user.remove_target_company('Google'), 0)
        self.assertNotEqual(self.user.remove_target_company(''), 0)
        self.assertRaisesMessage(ValueError,
            'Invalid input: input is empty',
            self.user.remove_target_company('')
        )
        self.assertRaisesMessage(ValueError, 
            'Invalid input: Google is not in the list',
            self.user.remove_target_company('Google')
        )

    def test_add_target_position(self):
        '''
        Test function: add_target_position
        Testcases:
            1. the function should return 0 if the input is a valid company name
            2. the function should return -1 if the input is an empty string
            3. the function should raise a ValueError if the input is an empty string
            4. the function should raise a UserWarning if the input is a language has not been seemed before, 
                as the user may enter some random string that is not a valid programming language. 
                It cannot be an error, as there may be programming languages that has not been stored in our database
        '''
        self.assertEqual(self.user.add_target_position('Software Engineer'), 0)
        self.assertTrue(Position.get('Software Engineer') in self.user.target_positions)
        self.assertNotEqual(self.user.add_target_position(''), 0)

    def test_remove_target_position(self):
        self.user.add_target_position('Software Engineer')
        self.assertEqual(self.user.remove_target_position('Software Engineer'), 0)
        self.assertNotEqual(self.user.remove_target_position(''), 0)
        self.assertRaisesMessage(ValueError,
            'Invalid input: input is empty',
            self.user.remove_target_position('')
        )
        self.assertRaisesMessage(ValueError, 
            'Invalid input: Software Engineer is not in the list',
            self.user.remove_target_position('Software Engineer')
        )

    def test_add_preferred_language(self):
        '''
        Test function: add_preferred_language
        Testcases:
            1. the function should return 0 if the input is a valid programming language
            2. the function should return False if the input is an empty string
            3. the function should raise a ValueError if the input is an empty string
            4. the function should raise a UserWarning if the input is a language has not been seemed before, 
                as the user may enter some random string that is not a valid programming language. 
                It cannot be an error, as there may be programming languages that has not been stored in our database
        '''
        self.assertEqual(self.user.add_preferred_language('Python'), 0)
        self.assertTrue(Language.get('Python') in self.user.preferred_languages)
        self.assertNotEqual(self.user.add_preferred_language(''), 0)

    def test_remove_preferred_language(self):
        self.user.add_preferred_language('Python')
        self.assertEqual(self.user.add_preferred_language('Python'), 0)
        self.assertNotEqual(self.user.add_preferred_language(''), 0)
        self.assertRaisesMessage(ValueError,
            'Invalid input: input is empty',
            self.user.add_preferred_language('')
        )
        self.assertRaisesMessage(ValueError, 
            'Invalid input: Python is not in the list',
            self.user.add_preferred_language('Python')
        )

    def test_set_preferred_difficulty(self):
        self.assertEqual(self.user.set_preferred_difficulty('Easy'), 0)
        self.assertTrue(self.user.preferred_difficulty == 'Easy')
        self.assertEqual(self.user.set_preferred_difficulty('Medium'), 0)
        self.assertTrue(self.user.preferred_difficulty == 'Medium')
        self.assertEqual(self.user.set_preferred_difficulty('Hard'), 0)
        self.assertTrue(self.user.preferred_difficulty == 'Hard')
        self.assertRaisesMessage(ValueError, 'Invalid input', self.user.set_preferred_difficulty('Very Hard'))

    def test_history(self):
        '''
        Test functions: update_history, get_historic_meetings
        '''
        self.assertEqual(self.user.update_history({"new meeting 1": "Meeting 1 info"}), 0)
        self.assertEqual(self.user.update_history({"new meeting 2": "Meeting 2 info"}), 0)
        self.assertDictEqual({"new meeting 1": "Meeting 1 info", "new meeting 2": "Meeting 2 info"}, self.user.get_historic_meetings())

    def test_set_calendar(self):
        '''
        Test function: set_calendar
        '''
        self.assertEqual(self.user.set_calendar('https://calendar.google.com/calendar/u/0/r'), 0)
        self.assertEqual(self.user.calendar, 'https://calendar.google.com/calendar/u/0/r')
        

    def test_set_rating(self):
        self.assertEqual(self.user.set_rating(3.4), 0)
        self.assertRaisesMessage(ValueError, "Invalid input: the rating should be in range [0, 5]", self.user.set_rating(-2.0))
        self.assertRaisesMessage(ValueError, "Invalid input: the rating should be in range [0, 5]", self.user.set_rating(7.2))

    def set_matching_strategy(self):
        self.assertEqual(self.user.set_matching_strategy('random'), 0)
        self.assertEqual(self.user.matchingStrategy, RandomMatching())
        self.assertEqual(self.user.set_matching_strategy('preference'), 0)
        self.assertEqual(self.user.matchingStrategy, PreferenceMatching())
        self.assertRaisesMessage(ValueError, 'Invalid input', self.user.set_matching_strategy('anjdvanivoa'))


class TestMatchingStrategy(TestCase):
    user1 = CustomUser()
    def test_get_pair(self):
        # The get_pair function should never return the user object itself
        self.user1.set_matching_strategy('random')
        self.assertNotEqual(self.user1.matchingStrategy.getPair(user=self.user1), self.user1)
        self.assertNotEqual(PreferenceMatching.getPair(user=self.user1), self.user1)