"""
API Class
"""

##########################
# Imports
##########################
from vron.connector.api.api import Api
from vron.connector.models import Config, Log





##########################
# Class definitions
##########################
class Availability( Api ):
    """
    Availability Class. Responsible for:

     1- Reading the fields from Viator request
     2- Creating the request for RON
     3- Returning XML response to Viator
    """

    def __init__( self, xml_root ):
        """
        Constructor responsible to authenticate the request

        :param: xml_root
        :return: None
        """

        # Extends constructor from parent class for extra processing
        super( Availability, self ).__init__( xml_root )

        # Declares additional class attributes
        self.request_status = { 'Status': '', 'Error': '', 'ErrorCode': '', 'ErrorMessage': '', 'ErrorDetails': '' }
        self.transaction_status = { 'Status': '', 'RejectionReasonDetails': '', 'RejectionReason': '' }

    def process( self ):
        """
        Passes viator data and makes RON request

        :return: String
        """
        pass

    def format_response( self ):
        """
        Returns XML response to Viator

        :return: String
        """
        pass