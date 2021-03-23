import unittest
from Frontend.dashboard import Hotel
import Backend.database
import model.model



class test(unittest.TestCase):


    def setUp(self):
        self.s=Hotel
        self.sorted_list=[1,2,3,4,5,6]

    def test_merge_sort_text(self):
        p_text = [123456, 234567, 112233, 113322, 98765]
        self.assertEqual([ 98765, 112233, 113322, 123456, 234567],
                         self.s.mergesort(p_text))



    def test_mergesort(self):
        num=[10,2,11,5,1]
        check=self.s.mergesort(num)
        self.assertEqual([1,2,5,10,11],check)

    def test_binarysearch(self):
        expected = '1'
        item=1
        actual = self.s.binary_search.mobile(self.sorted_list,item)
        self.assertNotEqual(expected, actual)

class Test_dbconect(unittest.TestCase):
    def setUp(self):
        self.a=Backend.database.DBConnect()

    def test_insert(self):
        query="insert into new_table values(%s,%s,%s,%s,%s)"
        values=(123456,"aashish","damak",9814002893,"male")
        self.a.insert(query,values)
        query1="select * from new_table where employee_ref =123456"
        actual=self.a.view(query1)
        self.assertEqual([(123456,"aashish","damak",9814002893,"male")],actual)

    def test_update(self):
        """
                Function to test if the update works or not.
        """
        query = "insert into new_table values(%s,%s,%s,%s,%s)"
        values = (1234567, "aashish", "damak", 9814002893, "male")
        self.a.insert(query, values)
        query1 = "update new_table set name=%s where employee_ref=%s"
        values1 = ("royan",1234567)
        self.a.update(query1, values1)
        query2 = "select * from new_table where employee_ref=1234567"
        actual = self.a.view(query2)
        self.assertEqual([(1234567, "royan", "damak",  9814002893, "male")], actual)

class Test_User(unittest.TestCase):
    """
    Class Test_User tests the User class from model.User.
    """
    def setUp(self):
        self.obj_model = model.model.User('employee_ref', 'name', 'address', 'mobile', 'gender')

    def test_set_Contact(self):
        self.obj_model.set_mobile(1001)
        self.assertEqual(1001, self.obj_model.get_Contact())

    def test_set_Dateofdeparture(self):
        with self.assertRaises(ValueError):
            self.obj_model.set_DateofDeparture(100)



if __name__ == " __main__ ":
    unittest.main()
