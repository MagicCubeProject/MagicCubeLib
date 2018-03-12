class Groupoid(object):
    """
    A Groupoid is a pair of non-empty set(called carrier) ,
    and the binary operation in that set
    """
    def __init__(self, carrier_set, binary_operation):
        """
        initialyze sdhdfhj
        """
        self.carrier = self.__verify_carrier(carrier_set, binary_operation)
        self.binary_operation = binary_operation

    def __verify_carrier(self, carrier_set, binary_operation):
        for element1 in carrier_set:
            for element2 in carrier_set:
                try:
                    if not binary_operation(element1, element2) in carrier_set:
                        error_message = """
                        {element1}*{element2} not in {carrier_set}
                        the binary operation not defined"
                        """
                        raise RuntimeError(error_message)
                except Exception as error:
                    raise RuntimeError('Binary operation is not vailed') from error
            return carrier_set

    def get_carrier(self):
        "return carrier"
        return self.carrier

    def set_carrier(self, carrier_set):
        "set carrier value"
        self.carrie = carrier_set
