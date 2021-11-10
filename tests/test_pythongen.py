import unittest
from types import ModuleType

from linkml.generators.pythongen import PythonGenerator

from samplelink import SAMPLELINK_MODEL_YAML


class PythonGenTestCase(unittest.TestCase):
    def gen_and_comp_python(self, yaml_file: str) -> None:
        """
         Generate a python image of the metamodel and verify that it parses
        :param yaml_file: YAML model definition

        """
        model_python = PythonGenerator(yaml_file).serialize()

        spec = compile(model_python, 'test', 'exec')
        module = ModuleType('test')
        exec(spec, module.__dict__)

    def test_samplelinkmodel(self):
        self.gen_and_comp_python(SAMPLELINK_MODEL_YAML)


if __name__ == '__main__':
    unittest.main()
