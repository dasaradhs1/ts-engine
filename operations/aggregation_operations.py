from pyspark.sql.types import LongType, DoubleType, FloatType, IntegerType, ShortType, ByteType


class SupportedReduceOperations:
    def __init__(self):
        self.operation = {
            "Sum": {
                "ref_to_func": lambda x, y: x + y,
                "input_type": LongType(),
                "output_type": LongType()
            },
            "Mult": {
                "ref_to_func": lambda x, y: x * y,
                "input_type": LongType(),
                "output_type": LongType()
            },
            "Min": {
                "ref_to_func": lambda x, y: x if x < y else y,
                "input_type": LongType(),
                "output_type": LongType()
            },
            "Max": {
                "ref_to_func": lambda x, y: x if x > y else y,
                "input_type": LongType(),
                "output_type": LongType()
            }
        }

        self._type_transform_rule = {DoubleType(): 5, FloatType(): 4, LongType(): 3, IntegerType(): 2,
                                     ShortType(): 1, ByteType(): 0}
        self.numeric_types = self._type_transform_rule.keys()

    def check_type_arg_function(self, type_input_arg, function_name):
        if (self._type_transform_rule[self.operation[function_name]["input_type"]] >= self._type_transform_rule[
            type_input_arg]) \
                and (self._type_transform_rule[type_input_arg] >= self._type_transform_rule[
                    self.operation[function_name]["output_type"]]):
            return True
        else:
            return False