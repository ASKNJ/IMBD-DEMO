import unittest
from my_App import views
import requests


class TestImbdViews(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setup parameters")
        cls.auth_header = {"Authorization": "7d36a61151ea48c6a900b80644ef0264"}
        cls.header = {}
        cls.data = {}

    @classmethod
    def tearDownClass(cls):
        print("Ending Process")

    def setup(self):
        print("Starting tests")

    def tearDown(self):
        print("Ending tests")

    def test_get_movies(self):
        url = "https://imbdweb.herokuapp.com/getMovies/"
        """Run test for free version i.e. anonymous user."""
        self.test_response1 = requests.request("GET", url=url, headers=self.header, data=self.data)
        self.assertEqual(self.test_response1.status_code, 200)
        """ Run test for auth version"""
        self.test_response2 = requests.request("GET", url=url, headers=self.auth_header, data=self.data)
        self.assertEqual(self.test_response1.status_code, 200)

    def test_search_movies(self):
        url = "https://imbdweb.herokuapp.com/searchMovies/Cabiria/"
        """Run test for free version i.e. anonymous user."""
        self.test_response1 = requests.request("GET", url=url, headers=self.header, data=self.data)
        self.assertEqual(self.test_response1.status_code, 200)
        """ Run test for auth version"""
        self.test_response2 = requests.request("GET", url=url, headers=self.auth_header, data=self.data)
        self.assertEqual(self.test_response1.status_code, 200)

    def test_patch(self):
        url = "https://imbdweb.herokuapp.com/updateData/1/"
        self.data = "{\n    \"movie_name\": \"Psychos.\"}"
        self.test_response1 = requests.request("PATCH", url=url, headers=self.auth_header, data=self.data)
        self.assertEqual(self.test_response1.status_code, 200)

    def test_post(self):
        url = "https://imbdweb.herokuapp.com/addData/"
        self.data = "{\n    \"99popularity\": 84.0,\n    \"director\": \"Chris Nola.\",\n    \"genre\": [\n      " \
                    "\"Adventure\",\n      \" Family\",\n      \" Fantasy\"\n    ],\n    \"imdb_score\": 9.3," \
                    "\n    \"name\": \"The Wizard of Harry Potter\"\n} "
        self.test_response1 = requests.request("POST", url=url, headers=self.auth_header, data=self.data)
        self.assertEqual(self.test_response1.status_code, 200)

    def test_delete(self):
        url = "https://imbdweb.herokuapp.com/deleteData/249/"
        self.test_response1 = requests.request("DELETE", url=url, headers=self.auth_header, data=self.data)
        self.assertEqual(self.test_response1.status_code, 200)
