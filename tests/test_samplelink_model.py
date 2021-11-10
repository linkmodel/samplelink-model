import unittest

from linkml.utils.schemaloader import SchemaLoader

from samplelink import SAMPLELINK_MODEL_YAML


class SamplelinkModelTestCase(unittest.TestCase):
    def test_samplelink_model(self):
        """ Make sure the samplelink model is valid """
        schema = SchemaLoader(SAMPLELINK_MODEL_YAML)
        errors = []
        try:
            schema.resolve()
        except ValueError as e:
            errors.append(str(e))
        if not errors:
            errors = schema.synopsis.errors()
        self.assertEqual([], errors, "samplelink-model.yaml - errors detected")


if __name__ == '__main__':
    unittest.main()
