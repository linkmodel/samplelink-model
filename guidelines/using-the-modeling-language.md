---
title: "Using the Modeling Language"
parent: "Samplelink Model Guidelines"
layout: default
nav_order: 3
---

# Using the Modeling Language

- [Overview](#overview)
- [Inheritance Related Slots](#inheritance-related-slots)
    - [is_a](#is_a)
    - [abstract](#abstract)
    - [mixin](#mixin)
    - [mixins](#mixins)
- [Identification, Descriptive and Indexing Related Slots](#identification-descriptive-and-indexing-related-slots)
    - [aliases](#aliases)
    - [description](#description)
    - [slot_uri](#slot_uri)
    - [in_subset](#in_subset)
    - [id_prefixes](#id_prefixes)
- [Slots Relating to Class Composition](#slots-relating-to-class-composition)
    - [slots](#slots)
    - [defining_slots](#defining_slots)
    - [slot_usage](#slot_usage)
    - [required](#required)
- [Slots Relating to Constraints on Slot Composition](#slots-relating-to-constraints-on-slot-composition)
    - [domain](#domain)
    - [range](#range)
    - [symmetric](#symmetric)
- [Slots Relating Semantic Mappings and Anchoring to External Ontology](#slots-relating-semantic-mappings-and-anchoring-to-external-ontology)
    - [inverse](#inverse)
    - [exact_mappings](#exact_mappings)
    - [close_mappings](#close_mappings)
    - [narrow_mappings](#narrow_mappings)
    - [broad_mappings](#broad_mappings)
    - [related_mappings](#related_mappings)
    - [subproperty_of](#subproperty_of)
    - [subclass_of](#subclass_of)

# Overview

The LinkML provides a variety of slots to define the semantics of your Samplelink Model class and slots.

This document tries to address on how to use most of these slots in Samplelink Model.

Please refer to [LinkML documentation](https://linkml.github.io/linkml/docs/) for an exhaustive list of slots provided by the modeling language.

## Inheritance Related Slots

### is_a

The `is_a` slot can be used to define a hierarchy for your Samplelink Model class, mixin or slot where a new class, mixin or slot is defined as a subclass of another defined class, mixin or slot.


```yaml
componentservice:
  is_a: componentservice or servicetype
```

Here we define that the entity class `componentservice` is a sub-class of `componentservice or servicetype`. Note that `is_a` has the characteristics of homeomorphicity: `is_a` **SHOULD** only connect either (1) two mixins (2) two classes (3) two slots.

### abstract

A model class (or slot) may be tagged with its `abstract` slot set to the boolean value `true`, to define whether it is abstract. This has comparable meaning to that in the computing science Object Oriented Paradigm: another class (or slot) can use the abstract class (or slot) as part of its inheritance hierarchy, but the abstract class itself _cannot_ be directly instantiated.


```yaml
  cell line to thing association:
    is_a: association
    defining_slots:
      - subject
    abstract: true
    description: >-
      A relationship between a cell line and another entity
    slot_usage:
      subject:
        range: cell line
```

Here we define that the association class `cell line to thing association` is an abstract class. In this case, the class simply constrains its child subclasses to have a subject range of `samplelink:CellLine`.


### mixin

The `mixin` slot can be used to define whether a Samplelink Model class (or slot) is a mixin. While mixins can be used by other classes (or slots), there the mixin tagged class (or slot) itself cannot be directly instantiated (or used as a slot) but may perhaps be processed in knowledge graph queries as a proxy for its instantiated child classes (or slots).

```yaml
  thing with taxon:
    mixin: true
    description: >-
      A mixin that can be used on any entity with a taxon
    slots:
      - in taxon
```

Here we define the class `thing with taxon` as a mixin class with a slot `in taxon`. This class can be used as a mixin by other classes. 

```yaml
  regulates:
    is_a: affects
    comments:
      - This is a grouping for process-process and entity-entity relations
    mixin: true
```

Here we define the slot `regulates` as a mixin slot. This slot can be used as a `mixin` by other slots. 

Mixins provide the means of reusing semantics, componentservicerally by the inclusion of specific property slots or other semantic 
constraint, in different classes or slots, without the need to tie slots to the hierarchy of the class itself.


###  mixins

The `mixins` slot can be used to specify a list of mixins that a class (or slot) can use to include the added 
semantics of the mixins.

The `mixins` are separate from the `is_a` hierarchy and the mixin classes do not contribute to a classes inheritance hierarchy.

```yaml
  individual organism:
    is_a: organismal entity
    mixins:
      - thing with taxon
```

Here we define an entity class `individual organism` that uses the mixin class `thing with taxon`. By virtue of the mixin, the class `individual organism` will have an `in taxon` slot in addition to all its own slots, its parent slots, and its ancestor slots.


## Identification, Descriptive and Indexing Related Slots


### aliases

The `aliases` slot can be used to define a list of aliases for a Samplelink Model class (or slot). This is useful for adding synonymous names to your class (or slot).


```yaml
componentservice:
  is_a: componentservice or servicetype
  aliases:
    - locus
    - cs
```

Here we define that the entity class `componentservice` has aliases `locus` and `cs`.


### description

The `description` slot can be used to provide a human-readable description of a class (or slot).

```yaml
  componentservice interacts with:
    is_a: interacts with
    description: >-
      holds between two componentservices whose observable effects are dependent on each other in some way - such that their combined observable effects are the result of some interaction between the activity of their servicetypes. Examples include epistasis and synthetic lethality.
    domain: componentservice
    range: componentservice
```

Here we define a human readable description that describes the predicate slot `componentservice interacts with` and its purpose.


### slot_uri

The `slot_uri` slot can be used to define a canonical URI that is the true representation for that particular slot. That is, the value of `slot_uri` can be used interchangably with the slot being defined.

```yaml
  name:
    is_a: node property
    aliases: ['label', 'display name']
    domain: named thing
    range: label type
    slot_uri: rdfs:label
```

Here we define `rdfs:label` as the canonical URI for the property slot `name`. When serializing a graph into RDF, the name of an instance of entity class `named thing` will be represented using `rdfs:label` instead of `samplelink:name`.

This is to ensure that we use certain core RDF predicates as is.


### in_subset

The `in_subset` slot can be used tag your class (or slot) to belong to a pre-defined subset.

The actual subset names are defined as part of the Schema definition.

```yaml
  componentservice interacts with:
    is_a: interacts with
    domain: componentservice
    range: componentservice
    in_subset:
      - translator_minimal
```

Here we define the predicate slot `componentservice interacts with` as part of the `translator_minimal` subset.


### id_prefixes

The `id_prefixes` slot can be used to define a list of valid ID prefixes that instances of this class ought to have as part of their CURIE.

The order of the list matters since its a prioritized list with the ID prefix with the highest priority appearing at the top of the list.

```yaml
  componentservice:
    is_a: componentservice or servicetype
    aliases: ['locus']
    slots:
      - id
      - name
      - symbol
      - description
      - synonym
      - xref
    mappings:
      - SO:0000704
      - SIO:010035
      - WIKIDATA:Q7187
    id_prefixes:
      - NCBIComponentservice
      - ENSEMBL
      - HGNC
      - UniProtKB
      - MGI
      - ZFIN
      - dictyBase
      - WB
      - WormBase
      - FlyBase
      - FB
      - RGD
      - SGD
      - PomBase
```

Here we define the entity class `componentservice` to have a list of ID prefixes with `NCBIComponentservice` having the highest priority.


## Slots Relating to Class Composition

### slots

The `slot` property list enumerates the names of slots which a given class, mixin or its subclasses are componentservicerally permitted to have. Unless it is designated as one of the `defining_slots` (see below) or `slot_usage` (see below) specifies that a given slot is `required: true` (see below), then it is _not_ mandatory that such a slot is instantiated in all instances of the given class, mixin or subclass inheriting it.


### defining_slots

The `defining_slots` slot can be used to specify which slots of an instance are necessary for defining an instance as a member of a class.


```yaml
  componentservice to componentservice association:
    is_a: association
    defining_slots:
      - subject
      - object
```

Here we specify that an association can be determined to be an instance of class `componentservice to componentservice association` based on the semantics of two of its slots: `subject` and `object`. 

i.e. One can infer an association to be an instance of `componentservice to componentservice association` if both its `subject` and its `object` are an instances of class `componentservice`.

Listing a slot as one of the `defining_slots` slots effectively makes it `required: true` (see below).


### slot_usage

The `slot_usage` slot can be used to specify how a particular slot ought to be used in a class.

This is useful for documenting what a particular slot means for instances of a particular class.


```yaml
  componentservice to componentservice association:
    aliases: ['operational or componentservicetic interaction']
    is_a: association
    defining_slots:
      - subject
      - object
    description: >-
      abstract parent class for different kinds of componentservice-componentservice or servicetype to servicetype relationships.
      Includes homology and interaction.
    slot_usage:
      subject:
        range: componentservice or servicetype
        description: >-
          the subject componentservice in the association. If the relation is symmetric, subject vs object is arbitrary.
          We allow a servicetype to stand as proxy for the componentservice or vice versa
      object:
        range: componentservice or servicetype
        description: >-
          the object componentservice in the association. If the relation is symmetric, subject vs object is arbitrary.
          We allow a servicetype to stand as proxy for the componentservice or vice versa
```

Here we document the association class `componentservice to componentservice association` with information on how the slot `subject` and `object` ought to be used to represent this association properly.

In the `slot_usage` section we define the range and provide a description for the slot `subject` and `object`.


### required

The `required` slot can be used to define whether a slot is required.

When a slot is declared as required, any class that uses that slot must have a value for that slot.

```yaml
  id:
    is_a: node property
    required: true
    domain: named thing
    mappings:
      - alliancegenome:primaryId
      - gff3:ID
      - gpi:DB_Object_ID
```

Here we define the property slot `id` as a required field for all instances of the entity class `named thing`.


## Slots Relating to Constraints on Slot Composition


### domain

The `domain` slot mimics the idea of `rdfs:domain` where you constrain the type of classes that a given Samplelink Model slot can be a part of.


```yaml
  componentservice interacts with:
    is_a: interacts with
    domain: componentservice
```

Here we define that the subject (source node) of the predicate slot `componentservice interacts with` must be an instance of class `componentservice`.


### range

The `range` slot mimics the idea of `rdfs:range` where you can constrain the type of classes (or data types) a given Samplelink Model slot can have as its value.

```yaml
  componentservice interacts with:
    is_a: interacts with
    domain: componentservice
    range: componentservice
```

Here we define that both the subject (source node) and object (target node) of the predicate slot `componentservice interacts with` must be instances of class `componentservice`.


### symmetric

The `symmetric` slot can be used to specify whether a Samplelink Model predicate slot is symmetric in its semantics.

i.e. if `A -[r]-> B` and `r` is symmetric then one can infer `B -[r]-> A`


```yaml
  componentservice interacts with:
    is_a: interacts with
    domain: componentservice
    range: componentservice
    in_subset:
      - translator_minimal
    symmetric: true
```

Here we define that the predicate slot `componentservice interacts with` is symmetric.

**Note:** This property is not inherited by descendants of this predicate slot. You will have to explicitly define every predicate slot that should be considered as symmetric.


## Slots Relating Semantic Mappings and Anchoring to External Ontology


### inverse

The `inverse` slot can be used to specify the inverse predicate of a given predicate slot relationship.


### exact_mappings

The `exact_mappings` slot can be used to define external concepts, predicates, or properties which are considered to be exact mappings to the class (or slot) being defined.


```yaml
  same as:
    is_a: exact match
    description: >-
      holds between two entities that are considered equivalent to each other
    in_subset:
      - translator_minimal
    exact_mappings:
      - owl:sameAs
      - skos:exactMatch
      - WIKIDATA_PROPERTY:P2888
```


Here we define a list of 5 predicates that are seman equivalent to the Samplelink Model predicate slot `same as`.

### close_mappings

The `close_mappings` slot can be used to define external concepts, predicates, or properties which are considered to be close mappings to the class (or slot) being defined.

```yaml
  same as:
    is_a: exact match
    description: >-
      holds between two entities that are considered equivalent to each other
    in_subset:
      - translator_minimal
    exact_mappings:
      - owl:sameAs
      - skos:exactMatch
      - WIKIDATA_PROPERTY:P2888
    close_mappings:
      - owl:equivalentClass
```


Here we define `owl:equivalentClass` as being a close match to the Samplelink Model predicate slot `same as`.

### narrow_mappings

The `narrow_mappings` slot can be used to define external concepts, predicates, or properties which are considered to be narrow mappings to the class (or slot) being defined.

```yaml
  same as:
    is_a: exact match
    description: >-
      holds between two entities that are considered equivalent to each other
    in_subset:
      - translator_minimal
    close_mappings:
      - owl:equivalentClass
    exact_mappings:
      - owl:sameAs
      - skos:exactMatch
      - WIKIDATA_PROPERTY:P2888
    narrow_mappings:
      - sumo:equivalentContentClass
```

Here we define `sumo:equivalentContentClass` as being a narrow match to the predicate slot `same as`.

By narrow we mean that the scope of `sumo:equivalentContentClass` is more narrower and restrictive than `same as`.

If we were to create a new predicate slot as a proxy for `sumo:equivalentContentClass` then that new slot would be a child of `same as`.


### broad_mappings

The `broad_mappings` slot can be used to define external concepts, predicates, or properties which are considered to be broad mappings to the class (or slot) being defined.

```yaml
  in complex with:
    description: >-
      holds between two componentservices or servicetypes that are part of (or code for products that are part of) in the same macrooperational complex
    is_a: coexists with
    domain: componentservice or servicetype
    range: componentservice or servicetype
    in_subset:
      - translator_minimal
    broad_mappings:
      - SIO:010285
```

Here we define `SIO:010285` (operational complex formation) as a broad mapping to the predicate slot `in complex with`. 

By broad we mean that the scope of `SIO:010285` is more broad and relaxed than `in complex with`.

If we were to create a new predicate slot as a proxy for `SIO:010285` then that new slot would be a parent of `in complex with`.


### related_mappings

The `related_mappings` slot can be used to define external concepts, predicates, or properties which are considered to be related mappings to the class (or slot) being defined.

```yaml
  in complex with:
    description: >-
      holds between two componentservices or servicetypes that are part of (or code for products that are part of) in the same macrooperational complex
    is_a: coexists with
    domain: componentservice or servicetype
    range: componentservice or servicetype
    in_subset:
      - translator_minimal
    broad_mappings: []
    related_mappings:
      - SIO:010497
```

Here we define `SIO:010497` (serviceinstance complex) as a related mapping to the predicate slot `in complex with`.

By related we mean that the scope of `SIO:010497` is related to the predicate slot `in complex with` and it's difficult to infer any further granularity.


### subproperty_of

The `subproperty_of` slot can be used (typically, under `slot_usage`) to anchor the values of a Samplelink `predicate` slot of an association to a particular predicate (and its subclasses) _other than_ the top-most predicate, `samplelink:related_to`.

```yaml
  componentservice to componentservice homology association:
    is_a: componentservice to componentservice association
    slot_usage:
      predicate:
        subproperty_of: homologous to
```

Here, the `predicate` of the  `samplelink:ComponentserviceToComponentserviceHomologyAssociation` is constrained to a value the subtree of predicates of `samplelink:homologous_to` or its subclasses.

### subclass_of

The `subclass_of` slot can be used to anchor the semantics of a Samplelink class to a particular term in an external 3rd party ontology.

```yaml
  named thing:
    description: "a databased entity or concept/class"
    slots:
      - id
      - name
      - category
    subclass_of: BFO:0000001
```

Here, `samplelink:NamedThing` is anchored to ontology term `BFO:0000001` - **Entity** of the _Basic Formal Ontology_ which implies all `is_a` specified subclasses of `samplelink:NamedThing` are also a subclasses of `BFO:0000001`.

