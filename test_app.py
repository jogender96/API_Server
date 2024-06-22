# test_app.py
import unittest
from app import app

class TestGraphQL(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_branches(self):
        query = '''
        query {
            allBranches {
                branch
                bank {
                    name
                }
                ifsc
            }
        }
        '''
        response = self.app.post('/gql', json={'query': query})
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('data', data)
        self.assertIn('allBranches', data['data'])

if __name__ == '__main__':
    unittest.main()
