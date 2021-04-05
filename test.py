# This file contains unit tests for the 3 functions

import unittest
from functions import *
from main import *

class Tests(unittest.TestCase):
    def test_part1(self):
        '''
        Tests legacy_notification_port function
        '''
        old = [
          {
            "datestring": "2021-03-20T00:37:48.100Z",
            "priority": "HIGH",
            "msg": "Title: Lorem ipsum",
            "deduplication_id": "5061f93f04b40914"
          },
          {
            "datestring": "2021-03-19T00:29:04.375Z",
            "priority": "LOW",
            "msg": "Title: Lorem ipsum",
            "deduplication_id": "d7ab10a2f69d9b74"
          },
          {
            "datestring": "2021-03-22T08:11:39.890Z",
            "priority": "MID",
            "msg": "Title: Lorem ipsum",
            "deduplication_id": "05cd9812771f377f"
          },
          {
            "datestring": "2021-03-17T23:42:10.342Z",
            "priority": "MID",
            "msg": "Title: Lorem ipsum",
            "deduplication_id": "051672714e534945"
          },
          {
            "datestring": "2021-03-17T17:46:54.823Z",
            "priority": "HIGH",
            "msg": "Title: Lorem ipsum",
            "deduplication_id": "338733350510bc9b"
          }]
          new = [
             {
                "timestamp":1616200668100,
                "priority":2,
                "body":"Lorem ipsum",
                "title":"Title",
                "deduplication_id":"5061f93f04b40914"
             },
             {
                "timestamp":1616113744375,
                "priority":0,
                "body":"Lorem ipsum",
                "title":"Title",
                "deduplication_id":"d7ab10a2f69d9b74"
             },
             {
                "timestamp":1616400699890,
                "priority":1,
                "body":"Lorem ipsum",
                "title":"Title",
                "deduplication_id":"05cd9812771f377f"
             },
             {
                "timestamp":1616024530342,
                "priority":1,
                "body":"Lorem ipsum",
                "title":"Title",
                "deduplication_id":"051672714e534945"
             },
             {
                "timestamp":1616003214823,
                "priority":2,
                "body":"Lorem ipsum",
                "title":"Title",
                "deduplication_id":"338733350510bc9b"
             }]
             self.assertEqual(new, legacy_notification_port(old))

    def test_part2(self):
        '''
        Tests deduplicating function
        '''
        old = [
         {
            "timestamp":1616200668100,
            "priority":2,
            "body":"Lorem ipsum",
            "title":"Title",
            "deduplication_id":"5061f93f04b40914"
         },
         {
            "timestamp":1616113744375,
            "priority":2,
            "body":"Lorem ipsum",
            "title":"Title",
            "deduplication_id":"5061f93f04b40914"
         },
         {
            "timestamp":1616400699890,
            "priority":1,
            "body":"Lorem ipsum",
            "title":"Title",
            "deduplication_id":"05cd9812771f377f"
         },
         {
            "timestamp":1616024530342,
            "priority":2,
            "body":"Lorem ipsum",
            "title":"Title",
            "deduplication_id":"05cd9812771f377f"
         },
         {
            "timestamp":1616003214823,
            "priority":0,
            "body":"Lorem ipsum",
            "title":"Title",
            "deduplication_id":"338733350510bc9b"
         }]
         new = [
          {
             "timestamp":1616200668100,
             "priority":2,
             "body":"Lorem ipsum",
             "title":"Title",
             "deduplication_id":"5061f93f04b40914"
          },
          {
             "timestamp":1616024530342,
             "priority":2,
             "body":"Lorem ipsum",
             "title":"Title",
             "deduplication_id":"05cd9812771f377f"
          },
          {
             "timestamp":1616003214823,
             "priority":0,
             "body":"Lorem ipsum",
             "title":"Title",
             "deduplication_id":"338733350510bc9b"
          }]
          self.assertEqual(new, deduplicating(old))

    def test_part3(self):
        '''
        Test sorting function
        '''
        old = [
           {
              "timestamp":1616200668100,
              "priority":0,
              "body":"Lorem ipsum",
              "title":"Title",
              "deduplication_id":"5061f93f04b40914"
           },
           {
              "timestamp":1616200668100,
              "priority":2,
              "body":"Lorem ipsum",
              "title":"Title",
              "deduplication_id":"d7ab10a2f69d9b74"
           },
           {
              "timestamp":1616200668106,
              "priority":1,
              "body":"Lorem ipsum",
              "title":"Title",
              "deduplication_id":"05cd9812771f377f"
           },
           {
              "timestamp":1616200668109,
              "priority":1,
              "body":"Lorem ipsum",
              "title":"Title",
              "deduplication_id":"051672714e534945"
           },
           {
              "timestamp":1616200668011,
              "priority":2,
              "body":"Lorem ipsum",
              "title":"Title",
              "deduplication_id":"338733350510bc9b"
           }]

        new = [
           {
              "timestamp":1616200668011,
              "priority":2,
              "body":"Lorem ipsum",
              "title":"Title",
              "deduplication_id":"338733350510bc9b"
           }
          {
             "timestamp":1616200668100,
             "priority":2,
             "body":"Lorem ipsum",
             "title":"Title",
             "deduplication_id":"d7ab10a2f69d9b74"
          },
           {
              "timestamp":1616200668100,
              "priority":0,
              "body":"Lorem ipsum",
              "title":"Title",
              "deduplication_id":"5061f93f04b40914"
           },
           {
              "timestamp":1616200668106,
              "priority":1,
              "body":"Lorem ipsum",
              "title":"Title",
              "deduplication_id":"05cd9812771f377f"
           },
           {
              "timestamp":1616200668109,
              "priority":1,
              "body":"Lorem ipsum",
              "title":"Title",
              "deduplication_id":"051672714e534945"
           }
        ]
        self.assertEqual(new, sorting(old))



if __name == '__main__':
    unittest.main()
