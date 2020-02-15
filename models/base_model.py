#!/usr/bin/python3
""" This is the base class for the AirBnB clone """

import datetime
import json
import uuid

class BaseModel():
    """ This class is the base model for all the AirBnB subclasses. """

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    def __init__(self, id=None, created_at=None, updated_at=None):
        """ Initializes the class. """

        self.id = str(uuid.uuid4())
        self.created_at = created_at
        self.updated_at = updated_at

    """====================================================================="""
    """== METHODS =========================================================="""
    """====================================================================="""

    """-----------"""
    """- Public --"""
    """-----------"""

    def __str__(self):
        """ Defines what the class should print. """
        name = self.__class__.__name__
        text = ("[{}] ({}) <{}>".format(name, self.id, self.__dict__))
        return text

    def save(self):
        """ Updates the public instance attribute "update_at" with the current
            datetime.                                                       """
        updated = datetime.datetime.now()
        self.__updated_at = datetime.datetime.isoformat(updated)


    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the
            instance.                                                       """
        dictt = self.__dict__
        dictt['__class__'] = self.__class__.__name__
        dictt['created_at'] = self.__created_at
        dictt['updated_at'] = self.__updated_at

        return dictt

    """-----------"""
    """- Private -"""
    """-----------"""

    """-----------"""
    """-- Class --"""
    """-----------"""

    """-----------"""
    """-- Static -"""
    """-----------"""

    """====================================================================="""
    """== SETTERS & GETTERS ================================================"""
    """====================================================================="""

    @property
    def created_at(self):
        """ Property created_at. """
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        """ Setter for created_at. """
        creation = datetime.datetime.now()
        self.__created_at = datetime.datetime.isoformat(creation)

    @property
    def updated_at(self):
        """ Property updated_at. """
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value):
        updated = datetime.datetime.now()
        self.__updated_at = datetime.datetime.isoformat(updated)