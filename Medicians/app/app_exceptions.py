__author__ = 'manya'
class DuplicateHandleError(Exception):
    def __init__(self, message, errors):
        super(DuplicateHandleError, self).__init__(message)
        self.errors = errors