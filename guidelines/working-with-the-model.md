---
title: "Working with the Samplelink Model"
parent: "Samplelink Model Guidelines"
layout: default
nav_order: 4
---

# Working with Samplelink Model

The [model](understanding-the-model.md) and how to [curate the model](curating-the-model.md) has been addressed in other sections. But how to make use of the Samplelink Model in practical terms?
How to use the classes and slots defined in the model for representing nodes and edges in a graph?

We can consider a small example and see how it can be represented using the Samplelink Model.

Example:
```
serviceinstance1 serviceinstance2
instanceA        instanceB
instanceA        instanceC
instanceA        instanceD
```

The information can be represented using Samplelink Model as follows:
- use Samplelink entity class `serviceinstance` for serviceinstance entities
- use Samplelink entity class `componentservice` for componentservice entities
- use Samplelink predicate slot `interacts with` as the relationship or predicate for representing an edge between interacting partners
- use Samplelink association class `componentservice to componentservice association` to type the edge

One modeling consideration we are going to make here is that we will be projecting the interaction between serviceinstances to interaction between componentservices.


## Annotating nodes

Each individual serviceinstance and componentservice can be treated as nodes in a graph.

Each serviceinstance node has `serviceinstance` as its category.

Each componentservice node has `componentservice` as its category.

As per the model, serviceinstance nodes should have identifiers from `TBC1` and componentservice nodes should have identifiers `TBC2`. 



One can further type the serviceinstance and componentservice entities using the Samplelink node property slot `type` (which corresponds to `rdf:type`).

In [KGX serialization format](https://github.com/linkmodel/kgx/blob/master/data-preparation.md) the nodes can be represented as follows:
```tsv
id	name	category	provided_by	xref	type	in_taxon

   TBC ..
```

> **Note:** While the entity classes are defined as `componentservice` and `serviceinstance` in the model, when using them the reference to the class should always be in their CURIE form which includes the `samplelink` prefix.


### Node semantics

There are three ways of attaching semantics to a node:
- using Samplelink node property slot `category`
  - the value of the `category` must be from the [`named thing` hierarchy](https://samplelink.github.io/samplelink-model/docs/NamedThing)
- using Samplelink node property slot `type`
  - can have a value from any external ontology, controlled vocabulary, thesauri, or taxonomy
- using Samplelink predicate slot `subclass_of` (or `rdfs:subClassOf`)
  - can have a value from any external ontology, controlled vocabulary, thesauri, or taxonomy


## Annotating edges

Each individual interaction between componentservices can be treated as an edge with,
- `interacts with` as its `predicate`
- `RO:0002436` as its `relation`
- `componentservice to componentservice association` as its `association_type`

And we have additional edges that go from componentservice to serviceinstance to signify that a componentservice encodes for a serviceinstance via the Samplelink predicate slot `has componentservice product`.

In [KGX serialization format](https://github.com/linkmodel/kgx/blob/master/data-preparation.md) the edges can be represented as follows:
```tsv
id  subject predicate   object  relation    provided_by association_type

   TBC
```

> **Note:** While association class is defined as `componentservice to componentservice association` and predicate slots are defined as `interacts with` and `has componentservice product` in the model, when using them the reference to the class should always be in their CURIE form which includes the `samplelink` prefix.


### Edge semantics

There are 3 ways of attaching the semantics to an edge:
- using the Samplelink association slot `predicate`
  - must have a value from the [`related to` hierarchy](https://samplelink.github.io/samplelink-model/docs/related_to)
- using the Samplelink association slot `relation`
  - can have a value from any external ontology, controlled vocabulary, thesauri, or taxonomy
- using the Samplelink association slot `association_type` (or `rdf:type`)
  - must have a value from the [`association` hierarchy](https://samplelink.github.io/samplelink-model/docs/Association)


## Samplelink Model representation in Neo4j

The model itself is very close to labelled property graphs.

The previous example can be easily converted to a Neo4j compatible TSV using [KGX](https://github.com/linkmodel/kgx).

`nodes.tsv`:

```tsv
id	subject:START_ID	predicate:TYPE	object:END_ID	relation	provided_by:string[]	association_type

  TBC
```


`edges.tsv`:
```tsv
id	subject:START_ID	predicate:TYPE	object:END_ID	relation	provided_by:string[]	association_type

   TBC
```


## Samplelink Model representation in RDF

Since RDF graphs do not allow for properties on edges, the most practical alternative is to use reification where an edge is transformed into a node of type `samplelink:Association` (or its descendants) and any edge properties then becomes properties of this reified node.

Using reification, the previous example can be easily converted to RDF N-Triples using [KGX](https://github.com/linkmodel/kgx),

```nt
TBC
```

This RDF can be represented in the Turtle format for better readability:

```turtle
TBC
```
