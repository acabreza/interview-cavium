'''
Created on May 11, 2015

@author: acabreza
'''
class MockedConnection():
    """TBD: Mocked connection class to customize return data.""" 
    def __init__(self):
        pass
    
    def get_body(self):
        return '{}'
    
    def get_content_type(self):
        return "application/json"
    
    def get_status_code(self):
        return 200