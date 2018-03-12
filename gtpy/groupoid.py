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
        self.identitiey = self.__find_identitiey()

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
                    raise RuntimeError('Binary operation is not vailed | '+error) from error
        return carrier_set

    def get_carrier(self):
        "return carrier"
        return self.carrier

    def set_carrier(self, carrier_set):
        "set carrier value"
        self.carrier = carrier_set

    def __find_identitiey(self):
        identitiey = None
        for element1 in self.carrier:
            for element2 in self.carrier:
                if self.binary_operation(element1, element2) == element1:
                    identitiey = element1
                    break
        return identitiey

    def get_identitiey(self):
        "Returning identitiey element of carrier"
        return self.identitiey
