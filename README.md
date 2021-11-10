[![](https://img.shields.io/github/license/linkmodel/samplelink-model)](https://img.shields.io/github/license/linkmodel/samplelink-model)
[![Samplelink Model](https://img.shields.io/github/v/release/linkmodel/samplelink-model?style=flat-square)](https://img.shields.io/github/v/release/linkmodel/samplelink-model?style=flat-square)
[![Python 3.7](https://upload.wikimedia.org/wikipedia/commons/f/fc/Blue_Python_3.7_Shield_Badge.svg)](https://www.python.org/downloads/release/python-370/)
![Regenerate Samplelink Model Artifacts](https://github.com/linkmodel/samplelink-model/workflows/Regenerate%20Samplelink%20Model%20Artifacts/badge.svg)
![Deploy Documentation](https://github.com/linkmodel/samplelink-model/workflows/Deploy%20Documentation/badge.svg)

<img src="images/samplelink-logo.png" width="20%">


# Samplelink Model (experimental)

Quickstart docs:

- Browse the model: [https://linkmodel.github.io/samplelink-model](https://linkmodel.github.io/samplelink-model)
  - [named thing](https://linkmodel.github.io/samplelink-model/docs/NamedThing.html)
  - [association](https://linkmodel.github.io/samplelink-model/docs/Association.html)
  - [predicate](https://linkmodel.github.io/samplelink-model/docs/predicates.html)


See also [Samplelink Model Guidelines](guidelines/README.md) for understanding, curating, and working with the model.

## Introduction

The purpose of the Samplelink Model is to provide a high-level datamodel of Cyber system entities (component, component services, observability, Service unit, errors, networks, instances, control actor, etc), their properties, relationships, and enumerate ways in which they can be associated.

The representation is independent of storage technology or metamodel (Solr documents, neo4j/property graphs, RDF/OWL, JSON, CSVs, etc). Different mappings to each of these are provided.

The specification of the Samplelink Model is a [single YAML file](samplelink-model.yaml) built using [linkml](https://github.com/linkml/linkml).

The basic elements of the YAML are:

 - Class Definitions: definitions of upper level *classes* representing both 'named thing' and 'association'
 - Slot Definitions: definitions of *slots* (aka properties) that can be used to relate members of these classes to other classes or data types. Slots collectively refer to predicates, node properties, and edge properties

This model is experimental, and not used in other projects.


## Organization

The main source of truth is [samplelink-model.yaml](samplelink-model.yaml). This is a YAML file that is intended to
be relatively simple to view and edit in its native form.

The yaml definition is currently used to derive:

  - [JSON Schema](json-schema)
  - [Python dataclasses](samplelink/model.py)
  - [Java code gen](java)
  - [ProtoBuf definitions](samplelink-model.proto)
  - [GraphQL](samplelink-model.graphql)
  - [RDF](samplelink-model.ttl)
  - [OWL](samplelink-model.owl.ttl)
  - [RDF Shape Expressions](samplelink-model.shex)
  - [JSON-LD context](context.jsonld)
  - [Graphviz](graphviz)
  - [GOlr YAML schemas](golr-views)
    - these can be compiled down to Solr XML schemas
    - these are also intermediate targets used within the BBOP/AmiGO framework
  - [Markdown documentation](docs)



## Make and build instructions

Prerequisites: Python 3.7+ and pipenv. Beware - more dependencies are listed in next section.

To install pipenv,

```sh
pip3 install pipenv
```

To install the project,
```sh
make install
```

To regenerate artifacts from the Samplelink Model YAML,

```sh
make
```

**Note:** the Makefile requires the following dependencies to be installed:

## Dependencies

### jsonschema

[jsonschema](https://json-schema.org/)

Generally install using 

```sh
pip3 install jsonschema
```

### jsonschema2pojo

[jsonschema2pojo](https://github.com/joelittlejohn/jsonschema2pojo)

If you are on a Mac, it can be installed using `brew`:
```sh
brew install jsonschema2pojo
```
For other OS environments, download the latest release then extract it into your execution path. eg
```sh
wget https://github.com/joelittlejohn/jsonschema2pojo/releases/download/jsonschema2pojo-1.1.1/jsonschema2pojo-1.1.1.tar.gz
tar -xvzf jsonschema2pojo-1.1.1.tar.gz
export PATH=$PATH:`pwd`/jsonschema2pojo-1.1.1/bin
```

### GraphViz

See [GraphViz site](https://graphviz.org/) for installation in your operating system.



## How do I use Samplelink Model YAML programatically?

For operations such as CURIE lookup, finding class by synonyms, get parents, get ancestors, etc. please make use of [link-model-toolkit](https://github.com/linkmodel/link-model-toolkit/). It provides a convenience methods for traversing Samplelink Model.
