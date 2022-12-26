
""" Module to extract particular data from MongoDB Database """

from pymongo import MongoClient


class DbQueries():
    def __init__(self):
        #Connects to MondoDB database hosted in localhost
        client = MongoClient('localhost', 27017)
        mydatabase = client['Inspection']
        self.mycollection = mydatabase['Company1']
        
    def status_filter(self,status):
        """ This method is called to get a list of unit ids of particular status group

        Args:
            status (String): String is passed which contains 'Good' or 'Bad' status

        Returns:
            List: The list of unit_ids whose status is either good or bad.
                  Returns empty list if other than Good or Bad status is inserted
        """
        unit_ids = []
        if status != "All":
            for row in self.mycollection.find({ "status": status}):
                unit_ids.append(row["unit_id"])
        else:
            for row in self.mycollection.find({}):
                unit_ids.append(row["unit_id"])
        return unit_ids
    
    def count(self):
        """ After calling this method you will get the count of entries present in the Company1 table

        Returns:
            Int: Returns count of entries present in table
        """
        return self.mycollection.count_documents({})
    
    def id_status(self, unit_id):
        """ This method with help to get the product's status after you provide unit_id

        Args:
            unit_id (int): This variable includes the product's valid unit_id 

        Returns:
            String: String value "Good" or "Bad" is returned if valid unit_id is passed
        """
        col = self.mycollection.find({"unit_id": unit_id})
        for i in  col:
            return i['status']
            


