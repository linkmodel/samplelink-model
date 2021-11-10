# link model file locations
import os

basedir = os.path.abspath(os.path.join(__file__, '..', '..'))
SAMPLELINK_MODEL_YAML = os.path.join(basedir, 'samplelink-model.yaml')
SAMPLELINK_MODEL_JSONLD = os.path.join(basedir, 'context.jsonld')
SAMPLELINK_MODEL_SHEX = os.path.join(basedir, 'shex', 'samplelink-model.shex')
SAMPLELINK_MODEL_RDF = os.path.join(basedir, 'rdf', 'samplelink-model.ttl')
SAMPLELINK_MODEL_OWL = os.path.join(basedir, 'ontology', 'samplelink-model.owl')
SAMPLELINK_MODEL_JSON = os.path.join(basedir, 'samplelink-model.json')
SAMPLELINK_MODEL_JSON_SCHEMA = os.path.join(basedir, 'json-schema', 'samplelink-model.json')
SAMPLELINK_MODEL_JAVA = os.path.join(basedir, 'java')
SAMPLELINK_MODEL_PYTHON = os.path.join(basedir, 'samplelink', 'model.py')
