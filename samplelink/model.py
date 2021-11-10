# Auto generated from samplelink-model.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-10T01:31:13
# Schema: Samplelink-Model
#
# id: https://w3id.org/samplelink
# description: Entity and association taxonomy and datamodel for computer services data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Double, Float, Integer, String, Time, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDTime

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ACMBOOKS = CurieNamespace('ACMBOOKS', 'https://dl.acm.org/action/doSearch?SeriesKey=acmbooks&AllField=')
ACMJOURNALS = CurieNamespace('ACMJOURNALS', 'https://dl.acm.org/action/doSearch?ConceptID=118230&AllField=')
AML = CurieNamespace('AML', 'https://w3id.org/i40/aml#')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
BTO = CurieNamespace('BTO', 'http://purl.obolibrary.org/obo/BTO_')
CDAO = CurieNamespace('CDAO', 'http://purl.obolibrary.org/obo/CDAO_')
CIO = CurieNamespace('CIO', 'http://purl.obolibrary.org/obo/CIO_')
COAR_RESOURCE = CurieNamespace('COAR_RESOURCE', 'http://vocabularies.coar-repositories.org/documentation/resource_types/')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
CTRL = CurieNamespace('CTRL', 'https://w3id.org/ibp/CTRLont#')
CVE = CurieNamespace('CVE', 'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=')
ECO = CurieNamespace('ECO', 'https://evidenceontology.org/term/')
EDAM = CurieNamespace('EDAM', 'http://edamontology.org/')
EDAM_DATA = CurieNamespace('EDAM-DATA', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('EDAM-FORMAT', 'http://edamontology.org/format_')
EDAM_OPERATION = CurieNamespace('EDAM-OPERATION', 'http://edamontology.org/operation_')
EDAM_TOPIC = CurieNamespace('EDAM-TOPIC', 'http://edamontology.org/topic_')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
ERO = CurieNamespace('ERO', 'http://purl.obolibrary.org/obo/ERO_')
EXO = CurieNamespace('EXO', 'http://purl.obolibrary.org/obo/ExO_')
EXO = CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/ExO_')
GOLD_META = CurieNamespace('GOLD_META', 'http://identifiers.org/gold.meta/')
GR = CurieNamespace('GR', 'http://purl.org/goodrelations/v1#')
GSID = CurieNamespace('GSID', 'https://scholar.google.com/citations?user=')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
IDO = CurieNamespace('IDO', 'http://purl.obolibrary.org/obo/IDO_')
LCSH = CurieNamespace('LCSH', 'http://id.loc.gov/authorities/subjects/')
LCSH_PUB = CurieNamespace('LCSH_PUB', 'http://id.loc.gov/vocabulary/mgovtpubtype/')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
MAID = CurieNamespace('MAID', 'https://academic.microsoft.com/#/detail/')
MMO = CurieNamespace('MMO', 'http://purl.obolibrary.org/obo/MMO_')
NBO = CurieNamespace('NBO', 'http://purl.obolibrary.org/obo/NBO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
NMR = CurieNamespace('NMR', 'http://purl.obolibrary.org/obo/NMR_')
OAE = CurieNamespace('OAE', 'http://purl.obolibrary.org/obo/OAE_')
OBO = CurieNamespace('OBO', 'http://purl.obolibrary.org/obo/')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
OM = CurieNamespace('OM', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/pato#')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
PW = CurieNamespace('PW', 'http://purl.obolibrary.org/obo/PW_')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
RNACENTRAL = CurieNamespace('RNACENTRAL', 'http://identifiers.org/rnacentral/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RESEARCHID = CurieNamespace('ResearchID', 'https://publons.com/researcher/')
SAN = CurieNamespace('SAN', 'https://www.irit.fr/recherches/MELODI/ontologies/SAN')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
STATO = CurieNamespace('STATO', 'http://purl.obolibrary.org/obo/STATO_')
SWO = CurieNamespace('SWO', 'http://purl.obolibrary.org/obo/SWO_')
SCOPUSID = CurieNamespace('ScopusID', 'https://www.scopus.com/authid/detail.uri?authorId=')
TAXRANK = CurieNamespace('TAXRANK', 'http://purl.obolibrary.org/obo/TAXRANK_')
UO = CurieNamespace('UO', 'https://www.ebi.ac.uk/ols/ontologies/uo')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
XAPI = CurieNamespace('XAPI', 'http://ns.inria.fr/ludo/v1/docs/xapi.html#')
XXXX = CurieNamespace('XXXX', 'http://example.org/UNKNOWN/XXXX/')
SAMPLELINK = CurieNamespace('samplelink', 'https://w3id.org/samplelink/vocab/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DCTYPES = CurieNamespace('dctypes', 'http://purl.org/dc/dcmitype/')
DOI = CurieNamespace('doi', 'http://identifiers.org/doi/')
DWC = CurieNamespace('dwc', 'https://dwc.tdwg.org/terms/#dc:')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
GEOLINK = CurieNamespace('geolink', 'http://schema.geolink.org/1.0/base/main.html#')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
GVP = CurieNamespace('gvp', 'http://vocab.getty.edu/ontology#')
ISBN = CurieNamespace('isbn', 'https://grp.isbn-international.org/content/using-register')
ISNI = CurieNamespace('isni', 'http://example.org/UNKNOWN/isni/')
ISSN = CurieNamespace('issn', 'http://identifiers.org/issn/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OPENVOCAB = CurieNamespace('openvocab', 'https://vocab.org/open/#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RR = CurieNamespace('rr', 'https://www.w3.org/ns/r2rml#')
SCHEMA = CurieNamespace('schema', 'https://schema.org/')
SKOS = CurieNamespace('skos', 'https://www.w3.org/TR/skos-reference/#')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'https://www.w3.org/TR/vocab-ssn/#')
SSN_SYSTEM = CurieNamespace('ssn-system', 'http://www.w3.org/ns/ssn/systems/')
SUMO = CurieNamespace('sumo', 'http://sigma.ontologyportal.org:8080/sigma/TreeView.jsp?flang=SUO-KIF&kb=SUMO&simple=yes&term=')
SUMO_WN = CurieNamespace('sumo-wn', 'http://sigma.ontologyportal.org:8080/sigma/WordNet.jsp?POS=0&word=')
UBERON = CurieNamespace('uberon', 'http://purl.obolibrary.org/obo/UBERON_')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SAMPLELINK


# Types
class ControlPlaneValue(str):
    """ A control plane """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "control plane value"
    type_model_uri = SAMPLELINK.ControlPlaneValue


class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the samplelink model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the samplelink class, for example samplelink:Service. For an RDF representation, the value should be a URI such as https://w3id.org/samplelink/vocab/Service """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "category type"
    type_model_uri = SAMPLELINK.CategoryType


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = SAMPLELINK.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = SAMPLELINK.LabelType


class PredicateType(Uriorcurie):
    """ A CURIE from the samplelink related_to hierarchy. For example, samplelink:related_to, samplelink:causes, samplelink:repairs. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "predicate type"
    type_model_uri = SAMPLELINK.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = SAMPLELINK.NarrativeText


class SymbolType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = SAMPLELINK.SymbolType


class Frequency(String):
    type_class_uri = UO["0000105"]
    type_class_curie = "UO:0000105"
    type_name = "frequency"
    type_model_uri = SAMPLELINK.Frequency


class PercentageFrequencyValue(Double):
    type_class_uri = UO["0000187"]
    type_class_curie = "UO:0000187"
    type_name = "percentage frequency value"
    type_model_uri = SAMPLELINK.PercentageFrequencyValue


class Quotient(Double):
    type_class_uri = UO["0010006"]
    type_class_curie = "UO:0010006"
    type_name = "quotient"
    type_model_uri = SAMPLELINK.Quotient


class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = SAMPLELINK.Unit


class TimeType(Time):
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time type"
    type_model_uri = SAMPLELINK.TimeType


class ComputationalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "computational sequence"
    type_model_uri = SAMPLELINK.ComputationalSequence


# Class references
class EntityId(extended_str):
    pass


class NamedThingId(EntityId):
    pass


class OntologyClassId(NamedThingId):
    pass


class RelationshipTypeId(OntologyClassId):
    pass


class ComponentserviceOntologyClassId(OntologyClassId):
    pass


class TaxonomicRankId(OntologyClassId):
    pass


class SystemTaxonId(OntologyClassId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class AgentId(AdministrativeEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class DatasetId(InformationContentEntityId):
    pass


class DatasetDistributionId(InformationContentEntityId):
    pass


class DatasetVersionId(DatasetId):
    pass


class DistributionLevelId(DatasetVersionId):
    pass


class DatasetSummaryId(DatasetVersionId):
    pass


class ConfidenceLevelId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class BookId(PublicationId):
    pass


class BookChapterId(PublicationId):
    pass


class SerialId(PublicationId):
    pass


class ArticleId(PublicationId):
    pass


class CyberEntityId(NamedThingId):
    pass


class ActivityId(NamedThingId):
    pass


class ProcedureId(NamedThingId):
    pass


class PhenomenonId(NamedThingId):
    pass


class DeviceId(NamedThingId):
    pass


class ResourceSampleId(CyberEntityId):
    pass


class PlanetaryEntityId(NamedThingId):
    pass


class EnvironmentalProcessId(PlanetaryEntityId):
    pass


class EnvironmentalFeatureId(PlanetaryEntityId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class GeographicLocationAtTimeId(GeographicLocationId):
    pass


class ComputationalEntityId(NamedThingId):
    pass


class OperationalEntityId(ComputationalEntityId):
    pass


class ComputationalProcessOrActivityId(ComputationalEntityId):
    pass


class OperationalActivityId(ComputationalProcessOrActivityId):
    pass


class ComputationalProcessId(ComputationalProcessOrActivityId):
    pass


class PathwayId(ComputationalProcessId):
    pass


class CyberProcessId(ComputationalProcessId):
    pass


class BehaviorId(ComputationalProcessId):
    pass


class DeathId(ComputationalProcessId):
    pass


class ControlActorId(OperationalEntityId):
    pass


class PowerId(ControlActorId):
    pass


class ConsumedResourceId(ControlActorId):
    pass


class AdministrativeOperationId(OperationalEntityId):
    pass


class NotificationComponentId(ControlActorId):
    pass


class EnvironmentalNotificationContaminantId(NotificationComponentId):
    pass


class AwarenessId(NotificationComponentId):
    pass


class DataId(NotificationComponentId):
    pass


class DatastreamId(DataId):
    pass


class BitstreamId(DataId):
    pass


class MessagePassingId(BitstreamId):
    pass


class NotificationId(OperationalEntityId):
    pass


class ControllerId(ControlActorId):
    pass


class SystemicEntityId(ComputationalEntityId):
    pass


class LifecycleStageId(SystemicEntityId):
    pass


class IndividualSystemId(SystemicEntityId):
    pass


class PopulationOfIndividualSystemsId(SystemicEntityId):
    pass


class StudyPopulationId(PopulationOfIndividualSystemsId):
    pass


class ErrorOrObservableFeatureId(ComputationalEntityId):
    pass


class ErrorId(ErrorOrObservableFeatureId):
    pass


class ObservableFeatureId(ErrorOrObservableFeatureId):
    pass


class BehavioralFeatureId(ObservableFeatureId):
    pass


class DeploymentEntityId(SystemicEntityId):
    pass


class ServiceunitId(DeploymentEntityId):
    pass


class ComponentId(DeploymentEntityId):
    pass


class ComponentTypeId(SystemicEntityId):
    pass


class GrossDeploymentStructureId(DeploymentEntityId):
    pass


class WorkloadEntityId(OperationalEntityId):
    pass


class WorkloadId(WorkloadEntityId):
    pass


class ComponentserviceinstanceId(WorkloadEntityId):
    pass


class DaemonId(WorkloadEntityId):
    pass


class CodingSequenceId(WorkloadEntityId):
    pass


class ServiceinstanceId(WorkloadEntityId):
    pass


class ServiceinstanceIsoformId(ServiceinstanceId):
    pass


class KernelServicetypeId(ComponentserviceinstanceId):
    pass


class KernelServicetypeIsoformId(KernelServicetypeId):
    pass


class NoncodingKernelServicetypeId(KernelServicetypeId):
    pass


class KernelMessageId(NoncodingKernelServicetypeId):
    pass


class KernelInterruptId(NoncodingKernelServicetypeId):
    pass


class ComponentserviceFamilyId(OperationalEntityId):
    pass


class ServiceunittypeId(WorkloadEntityId):
    pass


class VariantcomponentservicetypeId(WorkloadEntityId):
    pass


class SequenceVariantId(WorkloadEntityId):
    pass


class MonomericVariantId(SequenceVariantId):
    pass


class ReagentTargetedComponentserviceId(WorkloadEntityId):
    pass


class EmpiricalEntityId(NamedThingId):
    pass


class EmpiricalTrialId(EmpiricalEntityId):
    pass


class EmpiricalInterventionId(EmpiricalEntityId):
    pass


class EmpiricalFindingId(ObservableFeatureId):
    pass


class OfflineMaintenanceId(EmpiricalInterventionId):
    pass


class CaseId(IndividualSystemId):
    pass


class CohortId(StudyPopulationId):
    pass


class ComponentserviceBackgroundExposureId(WorkloadEntityId):
    pass


class FaultyProcessId(ComputationalProcessId):
    pass


class ErrorOrObservableFeatureExposureId(ErrorOrObservableFeatureId):
    pass


class FaultyProcessExposureId(FaultyProcessId):
    pass


class FaultyDeploymentStructureId(DeploymentEntityId):
    pass


class FaultyDeploymentExposureId(FaultyDeploymentStructureId):
    pass


class OrchestrationExposureId(ControlActorId):
    pass


class ComplexOrchestrationExposureId(OrchestrationExposureId):
    pass


class AdministrativeOperationalExposureId(AdministrativeOperationId):
    pass


class AdministrativeOperationalToComponentserviceInteractionExposureId(AdministrativeOperationalExposureId):
    pass


class RepairingId(NamedThingId):
    pass


class BioticExposureId(SystemTaxonId):
    pass


class GeographicExposureId(GeographicLocationId):
    pass


class EnvironmentalExposureId(EnvironmentalProcessId):
    pass


class BehavioralExposureId(BehaviorId):
    pass


class SocioeconomicExposureId(BehaviorId):
    pass


class FaultyProcessOutcomeId(FaultyProcessId):
    pass


class FaultyDeploymentOutcomeId(FaultyDeploymentStructureId):
    pass


class ErrorOrObservableFeatureOutcomeId(ErrorOrObservableFeatureId):
    pass


class BehavioralOutcomeId(BehaviorId):
    pass


class OfflineMaintenanceOutcomeId(OfflineMaintenanceId):
    pass


class MortalityOutcomeId(DeathId):
    pass


class EpidemiologicalOutcomeId(ComputationalEntityId):
    pass


class SocioeconomicOutcomeId(BehaviorId):
    pass


class AssociationId(EntityId):
    pass


class ContributorAssociationId(AssociationId):
    pass


class ServiceunittypeToServiceunittypePartAssociationId(AssociationId):
    pass


class ServiceunittypeToComponentserviceAssociationId(AssociationId):
    pass


class ServiceunittypeToVariantAssociationId(AssociationId):
    pass


class ComponentserviceToComponentserviceAssociationId(AssociationId):
    pass


class ComponentserviceToComponentserviceHomologyAssociationId(ComponentserviceToComponentserviceAssociationId):
    pass


class ComponentserviceToComponentserviceCoavailabilityAssociationId(ComponentserviceToComponentserviceAssociationId):
    pass


class PairwiseComponentserviceToComponentserviceInteractionId(ComponentserviceToComponentserviceAssociationId):
    pass


class PairwiseOperationallyInteractionId(PairwiseComponentserviceToComponentserviceInteractionId):
    pass


class ComponentTypeToErrorOrObservableFeatureAssociationId(AssociationId):
    pass


class OrchestrationToOrchestrationAssociationId(AssociationId):
    pass


class OrchestrationToOrchestrationDerivationAssociationId(OrchestrationToOrchestrationAssociationId):
    pass


class OrchestrationToErrorOrObservableFeatureAssociationId(AssociationId):
    pass


class OrchestrationToPathwayAssociationId(AssociationId):
    pass


class OrchestrationToComponentserviceAssociationId(AssociationId):
    pass


class AdministrativeOperationalToComponentserviceAssociationId(AssociationId):
    pass


class ResourceSampleDerivationAssociationId(AssociationId):
    pass


class ResourceSampleToErrorOrObservableFeatureAssociationId(AssociationId):
    pass


class ErrorToExposureEventAssociationId(AssociationId):
    pass


class ExposureEventToOutcomeAssociationId(AssociationId):
    pass


class ErrorOrObservableFeatureAssociationToLocationAssociationId(AssociationId):
    pass


class ErrorOrObservableFeatureToLocationAssociationId(AssociationId):
    pass


class ServiceunittypeToObservableFeatureAssociationId(AssociationId):
    pass


class ExposureEventToObservableFeatureAssociationId(AssociationId):
    pass


class ErrorToObservableFeatureAssociationId(AssociationId):
    pass


class CaseToObservableFeatureAssociationId(AssociationId):
    pass


class BehaviorToBehavioralFeatureAssociationId(AssociationId):
    pass


class ComponentserviceToObservableFeatureAssociationId(AssociationId):
    pass


class ComponentserviceToErrorAssociationId(AssociationId):
    pass


class VariantToComponentserviceAssociationId(AssociationId):
    pass


class VariantToComponentserviceAvailabilityAssociationId(VariantToComponentserviceAssociationId):
    pass


class VariantToPopulationAssociationId(AssociationId):
    pass


class PopulationToPopulationAssociationId(AssociationId):
    pass


class VariantToObservableFeatureAssociationId(AssociationId):
    pass


class VariantToErrorAssociationId(AssociationId):
    pass


class ServiceunittypeToErrorAssociationId(AssociationId):
    pass


class ComponentserviceAsAModelOfErrorAssociationId(ComponentserviceToErrorAssociationId):
    pass


class VariantAsAModelOfErrorAssociationId(VariantToErrorAssociationId):
    pass


class ServiceunittypeAsAModelOfErrorAssociationId(ServiceunittypeToErrorAssociationId):
    pass


class ComponentTypeAsAModelOfErrorAssociationId(ComponentTypeToErrorOrObservableFeatureAssociationId):
    pass


class SystemicEntityAsAModelOfErrorAssociationId(AssociationId):
    pass


class ComponentserviceHasVariantThatContributesToErrorAssociationId(ComponentserviceToErrorAssociationId):
    pass


class ComponentserviceToAvailabilitySiteAssociationId(AssociationId):
    pass


class SequenceVariantModulatesRepairingAssociationId(AssociationId):
    pass


class FunctionalAssociationId(AssociationId):
    pass


class MacrooperationalMachineMixinToOperationalActivityAssociationId(FunctionalAssociationId):
    pass


class MacrooperationalMachineMixinToComputationalProcessAssociationId(FunctionalAssociationId):
    pass


class MacrooperationalMachineMixinToComponentAssociationId(FunctionalAssociationId):
    pass


class ComponentserviceToGoTermAssociationId(FunctionalAssociationId):
    pass


class SequenceAssociationId(AssociationId):
    pass


class ComponentserviceSequenceLocalizationId(SequenceAssociationId):
    pass


class SequenceFeatureRelationshipId(AssociationId):
    pass


class ComponentserviceinstanceToComponentserviceRelationshipId(SequenceFeatureRelationshipId):
    pass


class ComponentserviceToServicetypeRelationshipId(SequenceFeatureRelationshipId):
    pass


class DaemonToComponentserviceinstanceRelationshipId(SequenceFeatureRelationshipId):
    pass


class ComponentserviceRegulatoryRelationshipId(AssociationId):
    pass


class DeploymentEntityToDeploymentEntityAssociationId(AssociationId):
    pass


class DeploymentEntityToDeploymentEntityPartOfAssociationId(DeploymentEntityToDeploymentEntityAssociationId):
    pass


class DeploymentEntityToDeploymentEntityOntogenicAssociationId(DeploymentEntityToDeploymentEntityAssociationId):
    pass


class Annotation(YAMLRoot):
    """
    Samplelink Model root class for entity annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Annotation
    class_class_curie: ClassVar[str] = "samplelink:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Annotation


@dataclass
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, available as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.QuantityValue
    class_class_curie: ClassVar[str] = "samplelink:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.QuantityValue

    has_unit: Optional[Union[str, Unit]] = None
    has_numeric_value: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, Unit):
            self.has_unit = Unit(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        super().__post_init__(**kwargs)


@dataclass
class Attribute(Annotation):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Attribute
    class_class_curie: ClassVar[str] = "samplelink:Attribute"
    class_name: ClassVar[str] = "attribute"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Attribute

    has_attribute_type: Union[str, OntologyClassId] = None
    name: Optional[Union[str, LabelType]] = None
    has_quantitative_value: Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]] = empty_list()
    has_qualitative_value: Optional[Union[str, NamedThingId]] = None
    iri: Optional[Union[str, IriType]] = None
    source: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.has_attribute_type):
            self.MissingRequiredField("has_attribute_type")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.has_quantitative_value, list):
            self.has_quantitative_value = [self.has_quantitative_value] if self.has_quantitative_value is not None else []
        self.has_quantitative_value = [v if isinstance(v, QuantityValue) else QuantityValue(**as_dict(v)) for v in self.has_quantitative_value]

        if self.has_qualitative_value is not None and not isinstance(self.has_qualitative_value, NamedThingId):
            self.has_qualitative_value = NamedThingId(self.has_qualitative_value)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if self.source is not None and not isinstance(self.source, LabelType):
            self.source = LabelType(self.source)

        super().__post_init__(**kwargs)


class AttributeType(YAMLRoot):
    """
    A property or characteristic type of an entity. For example, an apple may have properties types such as color
    type, shape type, age type, crispiness type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.AttributeType
    class_class_curie: ClassVar[str] = "samplelink:AttributeType"
    class_name: ClassVar[str] = "attribute type"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.AttributeType


@dataclass
class ComputationalArchitecturalStyle(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComputationalArchitecturalStyle
    class_class_curie: ClassVar[str] = "samplelink:ComputationalArchitecturalStyle"
    class_name: ClassVar[str] = "computational architectural style"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComputationalArchitecturalStyle

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class ObservableArchitecturalStyle(ComputationalArchitecturalStyle):
    """
    An attribute corresponding to the observable architectural style of the individual, based upon the reproductive
    applications present.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ObservableArchitecturalStyle
    class_class_curie: ClassVar[str] = "samplelink:ObservableArchitecturalStyle"
    class_name: ClassVar[str] = "observable architectural style"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ObservableArchitecturalStyle

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class MicroserviceArchitecturalStyle(ComputationalArchitecturalStyle):
    """
    An attribute corresponding to the microservice architectural style of the individual, based upon microservice
    composition of architectural style containers.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.MicroserviceArchitecturalStyle
    class_class_curie: ClassVar[str] = "samplelink:MicroserviceArchitecturalStyle"
    class_name: ClassVar[str] = "microservice architectural style"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.MicroserviceArchitecturalStyle

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a observable feature or error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SeverityValue
    class_class_curie: ClassVar[str] = "samplelink:SeverityValue"
    class_name: ClassVar[str] = "severity value"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SeverityValue

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class FrequencyValue(Attribute):
    """
    describes the frequency of occurrence of an event or condition
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.FrequencyValue
    class_class_curie: ClassVar[str] = "samplelink:FrequencyValue"
    class_name: ClassVar[str] = "frequency value"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.FrequencyValue

    has_attribute_type: Union[str, OntologyClassId] = None

class RelationshipQuantifier(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.RelationshipQuantifier
    class_class_curie: ClassVar[str] = "samplelink:RelationshipQuantifier"
    class_name: ClassVar[str] = "relationship quantifier"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.RelationshipQuantifier


class SensitivityQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SensitivityQuantifier
    class_class_curie: ClassVar[str] = "samplelink:SensitivityQuantifier"
    class_name: ClassVar[str] = "sensitivity quantifier"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SensitivityQuantifier


class SpecificityQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SpecificityQuantifier
    class_class_curie: ClassVar[str] = "samplelink:SpecificityQuantifier"
    class_name: ClassVar[str] = "specificity quantifier"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SpecificityQuantifier


class PathognomonicityQuantifier(SpecificityQuantifier):
    """
    A relationship quantifier between a variant or symptom and a error, which is high when the presence of the feature
    implies the existence of the error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.PathognomonicityQuantifier
    class_class_curie: ClassVar[str] = "samplelink:PathognomonicityQuantifier"
    class_name: ClassVar[str] = "pathognomonicity quantifier"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.PathognomonicityQuantifier


@dataclass
class FrequencyQuantifier(RelationshipQuantifier):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.FrequencyQuantifier
    class_class_curie: ClassVar[str] = "samplelink:FrequencyQuantifier"
    class_name: ClassVar[str] = "frequency quantifier"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.FrequencyQuantifier

    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_quotient: Optional[float] = None
    has_percentage: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        super().__post_init__(**kwargs)


@dataclass
class Entity(YAMLRoot):
    """
    Root Samplelink Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Entity
    class_class_curie: ClassVar[str] = "samplelink:Entity"
    class_name: ClassVar[str] = "entity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Entity

    id: Union[str, EntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    iri: Optional[Union[str, IriType]] = None
    type: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    source: Optional[Union[str, LabelType]] = None
    provided_by: Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]] = empty_list()
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        if self.source is not None and not isinstance(self.source, LabelType):
            self.source = LabelType(self.source)

        if not isinstance(self.provided_by, list):
            self.provided_by = [self.provided_by] if self.provided_by is not None else []
        self.provided_by = [v if isinstance(v, AgentId) else AgentId(v) for v in self.provided_by]

        self._normalize_inlined_as_dict(slot_name="has_attribute", slot_type=Attribute, key_name="has attribute type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.NamedThing
    class_class_curie: ClassVar[str] = "samplelink:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.NamedThing

    id: Union[str, NamedThingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.category]

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OntologyClass
    class_class_curie: ClassVar[str] = "samplelink:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OntologyClass

    id: Union[str, OntologyClassId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.RelationshipType
    class_class_curie: ClassVar[str] = "samplelink:RelationshipType"
    class_name: ClassVar[str] = "relationship type"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.RelationshipType

    id: Union[str, RelationshipTypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceOntologyClass(OntologyClass):
    """
    an ontology class that describes a controlling aspect of a componentservice, servicetype or complex
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceOntologyClass
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceOntologyClass"
    class_name: ClassVar[str] = "componentservice ontology class"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceOntologyClass

    id: Union[str, ComponentserviceOntologyClassId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceOntologyClassId):
            self.id = ComponentserviceOntologyClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.TaxonomicRank
    class_class_curie: ClassVar[str] = "samplelink:TaxonomicRank"
    class_name: ClassVar[str] = "taxonomic rank"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.TaxonomicRank

    id: Union[str, TaxonomicRankId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TaxonomicRankId):
            self.id = TaxonomicRankId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SystemTaxon(OntologyClass):
    """
    A classification of a set of systems. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria).
    Can also be used to represent strains or subspecies.
    """
    _inherited_slots: ClassVar[List[str]] = ["subclass_of"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SystemTaxon
    class_class_curie: ClassVar[str] = "samplelink:SystemTaxon"
    class_name: ClassVar[str] = "system taxon"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SystemTaxon

    id: Union[str, SystemTaxonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_taxonomic_rank: Optional[Union[str, TaxonomicRankId]] = None
    subclass_of: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemTaxonId):
            self.id = SystemTaxonId(self.id)

        if self.has_taxonomic_rank is not None and not isinstance(self.has_taxonomic_rank, TaxonomicRankId):
            self.has_taxonomic_rank = TaxonomicRankId(self.has_taxonomic_rank)

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.subclass_of]

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeEntity
    class_class_curie: ClassVar[str] = "samplelink:AdministrativeEntity"
    class_name: ClassVar[str] = "administrative entity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeEntity

    id: Union[str, AdministrativeEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class Agent(AdministrativeEntity):
    """
    service, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Agent
    class_class_curie: ClassVar[str] = "samplelink:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Agent

    id: Union[str, AgentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    affiliation: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    address: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation] if self.affiliation is not None else []
        self.affiliation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.affiliation]

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.InformationContentEntity
    class_class_curie: ClassVar[str] = "samplelink:InformationContentEntity"
    class_name: ClassVar[str] = "information content entity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    license: Optional[str] = None
    rights: Optional[str] = None
    format: Optional[str] = None
    creation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Dataset
    class_class_curie: ClassVar[str] = "samplelink:Dataset"
    class_name: ClassVar[str] = "dataset"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Dataset

    id: Union[str, DatasetId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DatasetDistribution(InformationContentEntity):
    """
    an item that holds distribution level information about a dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.DatasetDistribution
    class_class_curie: ClassVar[str] = "samplelink:DatasetDistribution"
    class_name: ClassVar[str] = "dataset distribution"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.DatasetDistribution

    id: Union[str, DatasetDistributionId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    distribution_download_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetDistributionId):
            self.id = DatasetDistributionId(self.id)

        if self.distribution_download_url is not None and not isinstance(self.distribution_download_url, str):
            self.distribution_download_url = str(self.distribution_download_url)

        super().__post_init__(**kwargs)


@dataclass
class DatasetVersion(Dataset):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.DatasetVersion
    class_class_curie: ClassVar[str] = "samplelink:DatasetVersion"
    class_name: ClassVar[str] = "dataset version"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.DatasetVersion

    id: Union[str, DatasetVersionId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_dataset: Optional[Union[str, DatasetId]] = None
    ingest_date: Optional[str] = None
    has_distribution: Optional[Union[str, DatasetDistributionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetVersionId):
            self.id = DatasetVersionId(self.id)

        if self.has_dataset is not None and not isinstance(self.has_dataset, DatasetId):
            self.has_dataset = DatasetId(self.has_dataset)

        if self.ingest_date is not None and not isinstance(self.ingest_date, str):
            self.ingest_date = str(self.ingest_date)

        if self.has_distribution is not None and not isinstance(self.has_distribution, DatasetDistributionId):
            self.has_distribution = DatasetDistributionId(self.has_distribution)

        super().__post_init__(**kwargs)


@dataclass
class DistributionLevel(DatasetVersion):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.DistributionLevel
    class_class_curie: ClassVar[str] = "samplelink:DistributionLevel"
    class_name: ClassVar[str] = "distribution level"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.DistributionLevel

    id: Union[str, DistributionLevelId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    download_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.download_url is not None and not isinstance(self.download_url, str):
            self.download_url = str(self.download_url)

        super().__post_init__(**kwargs)


@dataclass
class DatasetSummary(DatasetVersion):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.DatasetSummary
    class_class_curie: ClassVar[str] = "samplelink:DatasetSummary"
    class_name: ClassVar[str] = "dataset summary"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.DatasetSummary

    id: Union[str, DatasetSummaryId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    source_web_page: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.source_web_page is not None and not isinstance(self.source_web_page, str):
            self.source_web_page = str(self.source_web_page)

        super().__post_init__(**kwargs)


@dataclass
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ConfidenceLevel
    class_class_curie: ClassVar[str] = "samplelink:ConfidenceLevel"
    class_name: ClassVar[str] = "confidence level"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ConfidenceLevel

    id: Union[str, ConfidenceLevelId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EvidenceType
    class_class_curie: ClassVar[str] = "samplelink:EvidenceType"
    class_name: ClassVar[str] = "evidence type"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EvidenceType

    id: Union[str, EvidenceTypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal
    or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or
    section highlighted by NLP). The scope is intended to be general and include information published on the web, as
    well as printed resources, either directly or in one of the Publication Samplelink category subclasses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Publication
    class_class_curie: ClassVar[str] = "samplelink:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Publication

    id: Union[str, PublicationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    authors: Optional[Union[str, List[str]]] = empty_list()
    pages: Optional[Union[str, List[str]]] = empty_list()
    summary: Optional[str] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    lcsh_terms: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if not isinstance(self.pages, list):
            self.pages = [self.pages] if self.pages is not None else []
        self.pages = [v if isinstance(v, str) else str(v) for v in self.pages]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if not isinstance(self.lcsh_terms, list):
            self.lcsh_terms = [self.lcsh_terms] if self.lcsh_terms is not None else []
        self.lcsh_terms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.lcsh_terms]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Book(Publication):
    """
    This class may rarely be available except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Book
    class_class_curie: ClassVar[str] = "samplelink:Book"
    class_name: ClassVar[str] = "book"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Book

    id: Union[str, BookId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookId):
            self.id = BookId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class BookChapter(Publication):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.BookChapter
    class_class_curie: ClassVar[str] = "samplelink:BookChapter"
    class_name: ClassVar[str] = "book chapter"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.BookChapter

    id: Union[str, BookChapterId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    published_in: Union[str, URIorCURIE] = None
    volume: Optional[str] = None
    chapter: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookChapterId):
            self.id = BookChapterId(self.id)

        if self._is_empty(self.published_in):
            self.MissingRequiredField("published_in")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.chapter is not None and not isinstance(self.chapter, str):
            self.chapter = str(self.chapter)

        super().__post_init__(**kwargs)


@dataclass
class Serial(Publication):
    """
    This class may rarely be available except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Serial
    class_class_curie: ClassVar[str] = "samplelink:Serial"
    class_name: ClassVar[str] = "serial"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Serial

    id: Union[str, SerialId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    iso_abbreviation: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SerialId):
            self.id = SerialId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        super().__post_init__(**kwargs)


@dataclass
class Article(Publication):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Article
    class_class_curie: ClassVar[str] = "samplelink:Article"
    class_name: ClassVar[str] = "article"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Article

    id: Union[str, ArticleId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    type: str = None
    published_in: Union[str, URIorCURIE] = None
    iso_abbreviation: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArticleId):
            self.id = ArticleId(self.id)

        if self._is_empty(self.published_in):
            self.MissingRequiredField("published_in")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        super().__post_init__(**kwargs)


class CyberEssenceOrOccurrent(YAMLRoot):
    """
    Either a cyber or processual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.CyberEssenceOrOccurrent
    class_class_curie: ClassVar[str] = "samplelink:CyberEssenceOrOccurrent"
    class_name: ClassVar[str] = "cyber essence or occurrent"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.CyberEssenceOrOccurrent


class CyberEssence(CyberEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have cyber properties such as mass, volume, or charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.CyberEssence
    class_class_curie: ClassVar[str] = "samplelink:CyberEssence"
    class_name: ClassVar[str] = "cyber essence"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.CyberEssence


@dataclass
class CyberEntity(NamedThing):
    """
    An entity that has digital reality (a.k.a. cyber essence).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.CyberEntity
    class_class_curie: ClassVar[str] = "samplelink:CyberEntity"
    class_name: ClassVar[str] = "cyber entity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.CyberEntity

    id: Union[str, CyberEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CyberEntityId):
            self.id = CyberEntityId(self.id)

        super().__post_init__(**kwargs)


class Occurrent(CyberEssenceOrOccurrent):
    """
    A processual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Occurrent
    class_class_curie: ClassVar[str] = "samplelink:Occurrent"
    class_name: ClassVar[str] = "occurrent"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Occurrent


class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral healthy, organization or mechanical actor in the world
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ActivityAndBehavior
    class_class_curie: ClassVar[str] = "samplelink:ActivityAndBehavior"
    class_name: ClassVar[str] = "activity and behavior"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ActivityAndBehavior


@dataclass
class Activity(NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include
    consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Activity
    class_class_curie: ClassVar[str] = "samplelink:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Activity

    id: Union[str, ActivityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Procedure(NamedThing):
    """
    A series of actions conducted in a certain order or manner
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Procedure
    class_class_curie: ClassVar[str] = "samplelink:Procedure"
    class_name: ClassVar[str] = "procedure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Procedure

    id: Union[str, ProcedureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Phenomenon(NamedThing):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Phenomenon
    class_class_curie: ClassVar[str] = "samplelink:Phenomenon"
    class_name: ClassVar[str] = "phenomenon"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Phenomenon

    id: Union[str, PhenomenonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Device
    class_class_curie: ClassVar[str] = "samplelink:Device"
    class_name: ClassVar[str] = "device"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Device

    id: Union[str, DeviceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        super().__post_init__(**kwargs)


class SubjectOfInvestigation(YAMLRoot):
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SubjectOfInvestigation
    class_class_curie: ClassVar[str] = "samplelink:SubjectOfInvestigation"
    class_name: ClassVar[str] = "subject of investigation"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SubjectOfInvestigation


@dataclass
class ResourceSample(CyberEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a
    portion of a event) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.
    [SIO]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ResourceSample
    class_class_curie: ClassVar[str] = "samplelink:ResourceSample"
    class_name: ClassVar[str] = "resource sample"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ResourceSample

    id: Union[str, ResourceSampleId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceSampleId):
            self.id = ResourceSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.PlanetaryEntity
    class_class_curie: ClassVar[str] = "samplelink:PlanetaryEntity"
    class_name: ClassVar[str] = "planetary entity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.PlanetaryEntity

    id: Union[str, PlanetaryEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalProcess(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EnvironmentalProcess
    class_class_curie: ClassVar[str] = "samplelink:EnvironmentalProcess"
    class_name: ClassVar[str] = "environmental process"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EnvironmentalProcess

    id: Union[str, EnvironmentalProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalProcessId):
            self.id = EnvironmentalProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalFeature(PlanetaryEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EnvironmentalFeature
    class_class_curie: ClassVar[str] = "samplelink:EnvironmentalFeature"
    class_name: ClassVar[str] = "environmental feature"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EnvironmentalFeature

    id: Union[str, EnvironmentalFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalFeatureId):
            self.id = EnvironmentalFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.GeographicLocation
    class_class_curie: ClassVar[str] = "samplelink:GeographicLocation"
    class_name: ClassVar[str] = "geographic location"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.GeographicLocation

    id: Union[str, GeographicLocationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        super().__post_init__(**kwargs)


@dataclass
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.GeographicLocationAtTime
    class_class_curie: ClassVar[str] = "samplelink:GeographicLocationAtTime"
    class_name: ClassVar[str] = "geographic location at time"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.GeographicLocationAtTime

    id: Union[str, GeographicLocationAtTimeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicLocationAtTimeId):
            self.id = GeographicLocationAtTimeId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class ComputationalEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComputationalEntity
    class_class_curie: ClassVar[str] = "samplelink:ComputationalEntity"
    class_name: ClassVar[str] = "computational entity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComputationalEntity

    id: Union[str, ComputationalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

@dataclass
class ThingWithTaxon(YAMLRoot):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual systems;
    componentservices, their servicetypes and other operation entities; computer parts; computational processes
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ThingWithTaxon
    class_class_curie: ClassVar[str] = "samplelink:ThingWithTaxon"
    class_name: ClassVar[str] = "thing with taxon"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ThingWithTaxon

    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class OperationalEntity(ComputationalEntity):
    """
    A componentservice, servicetype, small task or macrotask (including serviceinstance complex)"
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OperationalEntity
    class_class_curie: ClassVar[str] = "samplelink:OperationalEntity"
    class_name: ClassVar[str] = "operational entity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OperationalEntity

    id: Union[str, OperationalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperationalEntityId):
            self.id = OperationalEntityId(self.id)

        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class ComputationalProcessOrActivity(ComputationalEntity):
    """
    Either an individual operational activity, or a collection of causally connected operational activities
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComputationalProcessOrActivity
    class_class_curie: ClassVar[str] = "samplelink:ComputationalProcessOrActivity"
    class_name: ClassVar[str] = "computational process or activity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComputationalProcessOrActivity

    id: Union[str, ComputationalProcessOrActivityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_input: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_output: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    enabled_by: Optional[Union[Union[str, CyberEntityId], List[Union[str, CyberEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComputationalProcessOrActivityId):
            self.id = ComputationalProcessOrActivityId(self.id)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_output]

        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by] if self.enabled_by is not None else []
        self.enabled_by = [v if isinstance(v, CyberEntityId) else CyberEntityId(v) for v in self.enabled_by]

        super().__post_init__(**kwargs)


@dataclass
class OperationalActivity(ComputationalProcessOrActivity):
    """
    An execution of a operational function carried out by a servicetype or macrooperational complex.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OperationalActivity
    class_class_curie: ClassVar[str] = "samplelink:OperationalActivity"
    class_name: ClassVar[str] = "operational activity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OperationalActivity

    id: Union[str, OperationalActivityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_input: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()
    has_output: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()
    enabled_by: Optional[Union[Union[dict, "MacrooperationalMachineMixin"], List[Union[dict, "MacrooperationalMachineMixin"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperationalActivityId):
            self.id = OperationalActivityId(self.id)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_output]

        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by] if self.enabled_by is not None else []
        self.enabled_by = [v if isinstance(v, MacrooperationalMachineMixin) else MacrooperationalMachineMixin(**as_dict(v)) for v in self.enabled_by]

        super().__post_init__(**kwargs)


@dataclass
class ComputationalProcess(ComputationalProcessOrActivity):
    """
    One or more causally connected executions of operational functions
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComputationalProcess
    class_class_curie: ClassVar[str] = "samplelink:ComputationalProcess"
    class_name: ClassVar[str] = "computational process"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComputationalProcess

    id: Union[str, ComputationalProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComputationalProcessId):
            self.id = ComputationalProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Pathway(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Pathway
    class_class_curie: ClassVar[str] = "samplelink:Pathway"
    class_name: ClassVar[str] = "pathway"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Pathway

    id: Union[str, PathwayId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CyberProcess(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.CyberProcess
    class_class_curie: ClassVar[str] = "samplelink:CyberProcess"
    class_name: ClassVar[str] = "cyber process"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.CyberProcess

    id: Union[str, CyberProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CyberProcessId):
            self.id = CyberProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Behavior(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Behavior
    class_class_curie: ClassVar[str] = "samplelink:Behavior"
    class_name: ClassVar[str] = "behavior"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Behavior

    id: Union[str, BehaviorId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehaviorId):
            self.id = BehaviorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Death(ComputationalProcess):
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Death
    class_class_curie: ClassVar[str] = "samplelink:Death"
    class_name: ClassVar[str] = "death"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Death

    id: Union[str, DeathId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeathId):
            self.id = DeathId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Cluster(YAMLRoot):
    """
    The cyber combination of two or more operational entities in which the identities are retained and are mixed in
    the form of solutions,
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Cluster
    class_class_curie: ClassVar[str] = "samplelink:Cluster"
    class_name: ClassVar[str] = "cluster"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Cluster

    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor] if self.has_control_actor is not None else []
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class ControlActor(OperationalEntity):
    """
    May be a orchestration entity or a formulation with a orchestration entity as active ingredient, or a complex
    resource with multiple orchestration entities as part
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ControlActor
    class_class_curie: ClassVar[str] = "samplelink:ControlActor"
    class_name: ClassVar[str] = "control actor"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ControlActor

    id: Union[str, ControlActorId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlActorId):
            self.id = ControlActorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Power(ControlActor):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Power
    class_class_curie: ClassVar[str] = "samplelink:Power"
    class_name: ClassVar[str] = "power"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Power

    id: Union[str, PowerId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PowerId):
            self.id = PowerId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ConsumedResource(ControlActor):
    """
    A control actor (often a cluster) consumed for information, engineering or technical use.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ConsumedResource
    class_class_curie: ClassVar[str] = "samplelink:ConsumedResource"
    class_name: ClassVar[str] = "consumed resource"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ConsumedResource

    id: Union[str, ConsumedResourceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsumedResourceId):
            self.id = ConsumedResourceId(self.id)

        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor] if self.has_control_actor is not None else []
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperation(OperationalEntity):
    """
    A event intended for use in the diagnosis, cure, mitigation, repairing, or prevention of error
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeOperation
    class_class_curie: ClassVar[str] = "samplelink:AdministrativeOperation"
    class_name: ClassVar[str] = "administrative operation"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeOperation

    id: Union[str, AdministrativeOperationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdministrativeOperationId):
            self.id = AdministrativeOperationId(self.id)

        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor] if self.has_control_actor is not None else []
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class NotificationComponent(ControlActor):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.NotificationComponent
    class_class_curie: ClassVar[str] = "samplelink:NotificationComponent"
    class_name: ClassVar[str] = "notification component"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.NotificationComponent

    id: Union[str, NotificationComponentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotificationComponentId):
            self.id = NotificationComponentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalNotificationContaminant(NotificationComponent):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EnvironmentalNotificationContaminant
    class_class_curie: ClassVar[str] = "samplelink:EnvironmentalNotificationContaminant"
    class_name: ClassVar[str] = "environmental notification contaminant"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EnvironmentalNotificationContaminant

    id: Union[str, EnvironmentalNotificationContaminantId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalNotificationContaminantId):
            self.id = EnvironmentalNotificationContaminantId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Awareness(NotificationComponent):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Awareness
    class_class_curie: ClassVar[str] = "samplelink:Awareness"
    class_name: ClassVar[str] = "awareness"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Awareness

    id: Union[str, AwarenessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AwarenessId):
            self.id = AwarenessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Data(NotificationComponent):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Data
    class_class_curie: ClassVar[str] = "samplelink:Data"
    class_name: ClassVar[str] = "data"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Data

    id: Union[str, DataId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataId):
            self.id = DataId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Datastream(Data):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Datastream
    class_class_curie: ClassVar[str] = "samplelink:Datastream"
    class_name: ClassVar[str] = "datastream"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Datastream

    id: Union[str, DatastreamId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatastreamId):
            self.id = DatastreamId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Bitstream(Data):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Bitstream
    class_class_curie: ClassVar[str] = "samplelink:Bitstream"
    class_name: ClassVar[str] = "bitstream"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Bitstream

    id: Union[str, BitstreamId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BitstreamId):
            self.id = BitstreamId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MessagePassing(Bitstream):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.MessagePassing
    class_class_curie: ClassVar[str] = "samplelink:MessagePassing"
    class_name: ClassVar[str] = "message passing"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.MessagePassing

    id: Union[str, MessagePassingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MessagePassingId):
            self.id = MessagePassingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Notification(OperationalEntity):
    """
    A event consumed by a healthy system as a source of information
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon", "has_data"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Notification
    class_class_curie: ClassVar[str] = "samplelink:Notification"
    class_name: ClassVar[str] = "notification"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Notification

    id: Union[str, NotificationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_data: Optional[Union[Union[str, DataId], List[Union[str, DataId]]]] = empty_list()
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotificationId):
            self.id = NotificationId(self.id)

        if not isinstance(self.has_data, list):
            self.has_data = [self.has_data] if self.has_data is not None else []
        self.has_data = [v if isinstance(v, DataId) else DataId(v) for v in self.has_data]

        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor] if self.has_control_actor is not None else []
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class Controller(ControlActor):
    """
    Any intermediate or servicetype resulting from director supervision. Includes primary and secondary controllers.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Controller
    class_class_curie: ClassVar[str] = "samplelink:Controller"
    class_name: ClassVar[str] = "controller"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Controller

    id: Union[str, ControllerId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    is_controller: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControllerId):
            self.id = ControllerId(self.id)

        if self.is_controller is not None and not isinstance(self.is_controller, Bool):
            self.is_controller = Bool(self.is_controller)

        super().__post_init__(**kwargs)


@dataclass
class SystemAttribute(Attribute):
    """
    describes a characteristic of an systemic entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SystemAttribute
    class_class_curie: ClassVar[str] = "samplelink:SystemAttribute"
    class_name: ClassVar[str] = "system attribute"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SystemAttribute

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class ObservableQuality(SystemAttribute):
    """
    A property of a observable
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ObservableQuality
    class_class_curie: ClassVar[str] = "samplelink:ObservableQuality"
    class_name: ClassVar[str] = "observable quality"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ObservableQuality

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Inheritance(SystemAttribute):
    """
    The pattern or 'mode' in which a particular service trait or disorder is passed from one generation to the next,
    e.g. autosomal dominant, autosomal recessive, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Inheritance
    class_class_curie: ClassVar[str] = "samplelink:Inheritance"
    class_name: ClassVar[str] = "inheritance"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Inheritance

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class SystemicEntity(ComputationalEntity):
    """
    A named entity that is either a part of a system, a whole system, population or clade of systems, excluding
    operational entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SystemicEntity
    class_class_curie: ClassVar[str] = "samplelink:SystemicEntity"
    class_name: ClassVar[str] = "systemic entity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SystemicEntity

    id: Union[str, SystemicEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="has_attribute", slot_type=Attribute, key_name="has attribute type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class LifecycleStage(SystemicEntity):
    """
    A stage of development or growth of a system.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.LifecycleStage
    class_class_curie: ClassVar[str] = "samplelink:LifecycleStage"
    class_name: ClassVar[str] = "lifecycle stage"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.LifecycleStage

    id: Union[str, LifecycleStageId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LifecycleStageId):
            self.id = LifecycleStageId(self.id)

        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class IndividualSystem(SystemicEntity):
    """
    An instance of an system. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID:
    ORCID:0000-0002-5355-2576
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.IndividualSystem
    class_class_curie: ClassVar[str] = "samplelink:IndividualSystem"
    class_name: ClassVar[str] = "individual system"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.IndividualSystem

    id: Union[str, IndividualSystemId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IndividualSystemId):
            self.id = IndividualSystemId(self.id)

        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class PopulationOfIndividualSystems(SystemicEntity):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, services, observabilitys.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.PopulationOfIndividualSystems
    class_class_curie: ClassVar[str] = "samplelink:PopulationOfIndividualSystems"
    class_name: ClassVar[str] = "population of individual systems"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.PopulationOfIndividualSystems

    id: Union[str, PopulationOfIndividualSystemsId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PopulationOfIndividualSystemsId):
            self.id = PopulationOfIndividualSystemsId(self.id)

        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class StudyPopulation(PopulationOfIndividualSystems):
    """
    A group of individuals banded together or repaired as a group as participants in a research study.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.StudyPopulation
    class_class_curie: ClassVar[str] = "samplelink:StudyPopulation"
    class_name: ClassVar[str] = "study population"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.StudyPopulation

    id: Union[str, StudyPopulationId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyPopulationId):
            self.id = StudyPopulationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeature(ComputationalEntity):
    """
    Either one of a error or an individual observable feature. Some knowledge resources such as Monarch treat these as
    distinct, others conflate.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeature
    class_class_curie: ClassVar[str] = "samplelink:ErrorOrObservableFeature"
    class_name: ClassVar[str] = "error or observable feature"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeature

    id: Union[str, ErrorOrObservableFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ErrorOrObservableFeatureId):
            self.id = ErrorOrObservableFeatureId(self.id)

        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class Error(ErrorOrObservableFeature):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Error
    class_class_curie: ClassVar[str] = "samplelink:Error"
    class_name: ClassVar[str] = "error"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Error

    id: Union[str, ErrorId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ErrorId):
            self.id = ErrorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ObservableFeature(ErrorOrObservableFeature):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ObservableFeature
    class_class_curie: ClassVar[str] = "samplelink:ObservableFeature"
    class_name: ClassVar[str] = "observable feature"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ObservableFeature

    id: Union[str, ObservableFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservableFeatureId):
            self.id = ObservableFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralFeature(ObservableFeature):
    """
    A observable feature which is behavioral in nature.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.BehavioralFeature
    class_class_curie: ClassVar[str] = "samplelink:BehavioralFeature"
    class_name: ClassVar[str] = "behavioral feature"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.BehavioralFeature

    id: Union[str, BehavioralFeatureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehavioralFeatureId):
            self.id = BehavioralFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntity(SystemicEntity):
    """
    A process location, serviceunit type or gross deployment part
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.DeploymentEntity
    class_class_curie: ClassVar[str] = "samplelink:DeploymentEntity"
    class_name: ClassVar[str] = "deployment entity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.DeploymentEntity

    id: Union[str, DeploymentEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    in_taxon: Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeploymentEntityId):
            self.id = DeploymentEntityId(self.id)

        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, SystemTaxonId) else SystemTaxonId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class Serviceunit(DeploymentEntity):
    """
    The set of components, whose part functionalily combines to form a desired service, must tightly collaborate as a
    group, logically named serviceunit (pod). A serviceunit represents a single instance of a running process in a
    cluster. It can be deployed, isolated, and repaired independently.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Serviceunit
    class_class_curie: ClassVar[str] = "samplelink:Serviceunit"
    class_name: ClassVar[str] = "serviceunit"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Serviceunit

    id: Union[str, ServiceunitId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceunitId):
            self.id = ServiceunitId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Component(DeploymentEntity):
    """
    The component is the smallest system entity, located in or around a serviceunit It can be deployed, isolated, and
    repaired independently. Each component belongs to one, and only one, serviceunit.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Component
    class_class_curie: ClassVar[str] = "samplelink:Component"
    class_name: ClassVar[str] = "component"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Component

    id: Union[str, ComponentId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentId):
            self.id = ComponentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ComponentType(SystemicEntity):
    """
    A component type defines the set of components running the same software and sharing the same configuration. It's
    a single point of configuration control.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentType
    class_class_curie: ClassVar[str] = "samplelink:ComponentType"
    class_name: ClassVar[str] = "component type"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentType

    id: Union[str, ComponentTypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentTypeId):
            self.id = ComponentTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GrossDeploymentStructure(DeploymentEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.GrossDeploymentStructure
    class_class_curie: ClassVar[str] = "samplelink:GrossDeploymentStructure"
    class_name: ClassVar[str] = "gross deployment structure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.GrossDeploymentStructure

    id: Union[str, GrossDeploymentStructureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GrossDeploymentStructureId):
            self.id = GrossDeploymentStructureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixin(YAMLRoot):
    """
    A union of componentservice, servicetype, and macrooperational complex. These are the basic units of function in a
    component. They either carry out individual computational activities, or they encode tasks which do this.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalMachineMixin
    class_class_curie: ClassVar[str] = "samplelink:MacrooperationalMachineMixin"
    class_name: ClassVar[str] = "macrooperational machine mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalMachineMixin

    name: Optional[Union[str, SymbolType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, SymbolType):
            self.name = SymbolType(self.name)

        super().__post_init__(**kwargs)


class ComponentserviceOrServicetype(MacrooperationalMachineMixin):
    """
    a union of componentservice loci or servicetypes. Frequently an identifier for one will be used as proxy for
    another
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceOrServicetype
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceOrServicetype"
    class_name: ClassVar[str] = "componentservice or servicetype"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceOrServicetype


@dataclass
class Componentservice(ComponentserviceOrServicetype):
    """
    A component service.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Componentservice
    class_class_curie: ClassVar[str] = "samplelink:Componentservice"
    class_name: ClassVar[str] = "componentservice"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Componentservice

    symbol: Optional[str] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class ServicetypeMixin(ComponentserviceOrServicetype):
    """
    The controlling operational servicetype of a single componentservice locus. ServiceType product are either
    serviceinstances or supervisor tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ServicetypeMixin
    class_class_curie: ClassVar[str] = "samplelink:ServicetypeMixin"
    class_name: ClassVar[str] = "servicetype mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ServicetypeMixin

    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


class ServicetypeIsoformMixin(ServicetypeMixin):
    """
    This is an abstract class that can be mixed in with different kinds of servicetypes to indicate that the
    servicetype is intended to represent a specific isoform rather than a canonical or reference or generic
    servicetype. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all
    isoforms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ServicetypeIsoformMixin
    class_class_curie: ClassVar[str] = "samplelink:ServicetypeIsoformMixin"
    class_name: ClassVar[str] = "servicetype isoform mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ServicetypeIsoformMixin


class MacrooperationalComplexMixin(MacrooperationalMachineMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalComplexMixin
    class_class_curie: ClassVar[str] = "samplelink:MacrooperationalComplexMixin"
    class_name: ClassVar[str] = "macrooperational complex mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalComplexMixin


@dataclass
class WorkloadEntity(OperationalEntity):
    """
    An entity that can either be directly located on a workload (componentservice, componentserviceinstance, daemon,
    regulatory region) or is encoded in a workload (serviceinstance)
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.WorkloadEntity
    class_class_curie: ClassVar[str] = "samplelink:WorkloadEntity"
    class_name: ClassVar[str] = "workload entity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.WorkloadEntity

    id: Union[str, WorkloadEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkloadEntityId):
            self.id = WorkloadEntityId(self.id)

        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        super().__post_init__(**kwargs)


@dataclass
class Workload(WorkloadEntity):
    """
    A workload is the sum of componentservice resources within a serviceunit or virion.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Workload
    class_class_curie: ClassVar[str] = "samplelink:Workload"
    class_name: ClassVar[str] = "workload"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Workload

    id: Union[str, WorkloadId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkloadId):
            self.id = WorkloadId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Componentserviceinstance(WorkloadEntity):
    """
    The unit of service workload the component is capable of providing or protecting.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Componentserviceinstance
    class_class_curie: ClassVar[str] = "samplelink:Componentserviceinstance"
    class_name: ClassVar[str] = "componentserviceinstance"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Componentserviceinstance

    id: Union[str, ComponentserviceinstanceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceinstanceId):
            self.id = ComponentserviceinstanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Daemon(WorkloadEntity):
    """
    A region of the componentserviceinstance sequence within a componentservice.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Daemon
    class_class_curie: ClassVar[str] = "samplelink:Daemon"
    class_name: ClassVar[str] = "daemon"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Daemon

    id: Union[str, DaemonId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DaemonId):
            self.id = DaemonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CodingSequence(WorkloadEntity):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.CodingSequence
    class_class_curie: ClassVar[str] = "samplelink:CodingSequence"
    class_name: ClassVar[str] = "coding sequence"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.CodingSequence

    id: Union[str, CodingSequenceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CodingSequenceId):
            self.id = CodingSequenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Serviceinstance(WorkloadEntity):
    """
    A servicetype that is composed of a chain of instruction sequences and is produced by translation of kernel message
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Serviceinstance
    class_class_curie: ClassVar[str] = "samplelink:Serviceinstance"
    class_name: ClassVar[str] = "serviceinstance"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Serviceinstance

    id: Union[str, ServiceinstanceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceinstanceId):
            self.id = ServiceinstanceId(self.id)

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class ServiceinstanceIsoform(Serviceinstance):
    """
    Represents a serviceinstance that is a specific isoform of the canonical or reference serviceinstance.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ServiceinstanceIsoform
    class_class_curie: ClassVar[str] = "samplelink:ServiceinstanceIsoform"
    class_name: ClassVar[str] = "serviceinstance isoform"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ServiceinstanceIsoform

    id: Union[str, ServiceinstanceIsoformId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceinstanceIsoformId):
            self.id = ServiceinstanceIsoformId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class KernelServicetype(Componentserviceinstance):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.KernelServicetype
    class_class_curie: ClassVar[str] = "samplelink:KernelServicetype"
    class_name: ClassVar[str] = "kernel servicetype"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.KernelServicetype

    id: Union[str, KernelServicetypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    synonym: Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]] = empty_list()
    xref: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KernelServicetypeId):
            self.id = KernelServicetypeId(self.id)

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, LabelType) else LabelType(v) for v in self.synonym]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, IriType) else IriType(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class KernelServicetypeIsoform(KernelServicetype):
    """
    Represents a serviceinstance that is a specific isoform of the canonical or reference kernel
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.KernelServicetypeIsoform
    class_class_curie: ClassVar[str] = "samplelink:KernelServicetypeIsoform"
    class_name: ClassVar[str] = "kernel servicetype isoform"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.KernelServicetypeIsoform

    id: Union[str, KernelServicetypeIsoformId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KernelServicetypeIsoformId):
            self.id = KernelServicetypeIsoformId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class NoncodingKernelServicetype(KernelServicetype):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.NoncodingKernelServicetype
    class_class_curie: ClassVar[str] = "samplelink:NoncodingKernelServicetype"
    class_name: ClassVar[str] = "noncoding kernel servicetype"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.NoncodingKernelServicetype

    id: Union[str, NoncodingKernelServicetypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoncodingKernelServicetypeId):
            self.id = NoncodingKernelServicetypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class KernelMessage(NoncodingKernelServicetype):
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.KernelMessage
    class_class_curie: ClassVar[str] = "samplelink:KernelMessage"
    class_name: ClassVar[str] = "kernel message"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.KernelMessage

    id: Union[str, KernelMessageId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KernelMessageId):
            self.id = KernelMessageId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class KernelInterrupt(NoncodingKernelServicetype):
    """
    TBD
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.KernelInterrupt
    class_class_curie: ClassVar[str] = "samplelink:KernelInterrupt"
    class_name: ClassVar[str] = "kernel interrupt"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.KernelInterrupt

    id: Union[str, KernelInterruptId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KernelInterruptId):
            self.id = KernelInterruptId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceGroupingMixin(YAMLRoot):
    """
    any grouping of multiple componentservices or servicetypes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceGroupingMixin
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceGroupingMixin"
    class_name: ClassVar[str] = "componentservice grouping mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceGroupingMixin

    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype] if self.has_componentservice_or_servicetype is not None else []
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**as_dict(v)) for v in self.has_componentservice_or_servicetype]

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceFamily(OperationalEntity):
    """
    any grouping of multiple componentservices or servicetypes related by common descent
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceFamily
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceFamily"
    class_name: ClassVar[str] = "componentservice family"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceFamily

    id: Union[str, ComponentserviceFamilyId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceFamilyId):
            self.id = ComponentserviceFamilyId(self.id)

        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype] if self.has_componentservice_or_servicetype is not None else []
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**as_dict(v)) for v in self.has_componentservice_or_servicetype]

        super().__post_init__(**kwargs)


@dataclass
class Homogeneity(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Homogeneity
    class_class_curie: ClassVar[str] = "samplelink:Homogeneity"
    class_name: ClassVar[str] = "homogeneity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Homogeneity

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Serviceunittype(WorkloadEntity):
    """
    An information content entity that describes a workload by specifying the total variation in service sequence
    and/or componentservice availability, relative to some established background
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Serviceunittype
    class_class_curie: ClassVar[str] = "samplelink:Serviceunittype"
    class_name: ClassVar[str] = "serviceunittype"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Serviceunittype

    id: Union[str, ServiceunittypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_homogeneity: Optional[Union[dict, Homogeneity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceunittypeId):
            self.id = ServiceunittypeId(self.id)

        if self.has_homogeneity is not None and not isinstance(self.has_homogeneity, Homogeneity):
            self.has_homogeneity = Homogeneity(**as_dict(self.has_homogeneity))

        super().__post_init__(**kwargs)


@dataclass
class Variantcomponentservicetype(WorkloadEntity):
    """
    A set of zero or more variantcomponentservices on a single instance of a Sequence
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Variantcomponentservicetype
    class_class_curie: ClassVar[str] = "samplelink:Variantcomponentservicetype"
    class_name: ClassVar[str] = "variantcomponentservicetype"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Variantcomponentservicetype

    id: Union[str, VariantcomponentservicetypeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantcomponentservicetypeId):
            self.id = VariantcomponentservicetypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SequenceVariant(WorkloadEntity):
    """
    A variantcomponentservice that varies in its sequence from what is considered the reference
    variantcomponentservice at that locus.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SequenceVariant
    class_class_curie: ClassVar[str] = "samplelink:SequenceVariant"
    class_name: ClassVar[str] = "sequence variant"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SequenceVariant

    id: Union[str, SequenceVariantId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_componentservice: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()
    has_computational_sequence: Optional[Union[str, ComputationalSequence]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)

        if not isinstance(self.has_componentservice, list):
            self.has_componentservice = [self.has_componentservice] if self.has_componentservice is not None else []
        self.has_componentservice = [v if isinstance(v, Componentservice) else Componentservice(**as_dict(v)) for v in self.has_componentservice]

        if self.has_computational_sequence is not None and not isinstance(self.has_computational_sequence, ComputationalSequence):
            self.has_computational_sequence = ComputationalSequence(self.has_computational_sequence)

        super().__post_init__(**kwargs)


@dataclass
class MonomericVariant(SequenceVariant):
    """
    A single monomeric position in the service monomeric variants are single monomeric positions in service DNA at
    which different sequence alternatives exist
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.MonomericVariant
    class_class_curie: ClassVar[str] = "samplelink:MonomericVariant"
    class_name: ClassVar[str] = "monomeric variant"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.MonomericVariant

    id: Union[str, MonomericVariantId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonomericVariantId):
            self.id = MonomericVariantId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ReagentTargetedComponentservice(WorkloadEntity):
    """
    A componentservice altered in its availability level in the context of some experiment as a result of being
    targeted by componentservice-knockdown reagent(s).
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ReagentTargetedComponentservice
    class_class_curie: ClassVar[str] = "samplelink:ReagentTargetedComponentservice"
    class_name: ClassVar[str] = "reagent targeted componentservice"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ReagentTargetedComponentservice

    id: Union[str, ReagentTargetedComponentserviceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReagentTargetedComponentserviceId):
            self.id = ReagentTargetedComponentserviceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalAttribute(Attribute):
    """
    Attributes relating to a empirical manifestation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalAttribute
    class_class_curie: ClassVar[str] = "samplelink:EmpiricalAttribute"
    class_name: ClassVar[str] = "empirical attribute"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalAttribute

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class EmpiricalMeasurement(EmpiricalAttribute):
    """
    A empirical measurement is a special kind of attribute which results from a quality of serviceunit observation
    from a subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalMeasurement
    class_class_curie: ClassVar[str] = "samplelink:EmpiricalMeasurement"
    class_name: ClassVar[str] = "empirical measurement"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalMeasurement

    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.has_attribute_type):
            self.MissingRequiredField("has_attribute_type")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalModifier(EmpiricalAttribute):
    """
    Used to characterize and specify the observable abnormalities defined in the observable abnormality sub-ontology,
    with respect to severity, laterality, and other aspects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalModifier
    class_class_curie: ClassVar[str] = "samplelink:EmpiricalModifier"
    class_name: ClassVar[str] = "empirical modifier"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalModifier

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class EmpiricalCourse(EmpiricalAttribute):
    """
    The course a error typically takes from its onset, progression in time, and eventual resolution or death of the
    affected individual
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalCourse
    class_class_curie: ClassVar[str] = "samplelink:EmpiricalCourse"
    class_name: ClassVar[str] = "empirical course"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalCourse

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Onset(EmpiricalCourse):
    """
    The age group in which (error) symptom manifestations appear
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Onset
    class_class_curie: ClassVar[str] = "samplelink:Onset"
    class_name: ClassVar[str] = "onset"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Onset

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class EmpiricalEntity(NamedThing):
    """
    Any entity or process that exists in the empirical domain and outside the computational realm. Errors are placed
    under computational entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalEntity
    class_class_curie: ClassVar[str] = "samplelink:EmpiricalEntity"
    class_name: ClassVar[str] = "empirical entity"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalEntity

    id: Union[str, EmpiricalEntityId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmpiricalEntityId):
            self.id = EmpiricalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalTrial(EmpiricalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalTrial
    class_class_curie: ClassVar[str] = "samplelink:EmpiricalTrial"
    class_name: ClassVar[str] = "empirical trial"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalTrial

    id: Union[str, EmpiricalTrialId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmpiricalTrialId):
            self.id = EmpiricalTrialId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalIntervention(EmpiricalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalIntervention
    class_class_curie: ClassVar[str] = "samplelink:EmpiricalIntervention"
    class_name: ClassVar[str] = "empirical intervention"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalIntervention

    id: Union[str, EmpiricalInterventionId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmpiricalInterventionId):
            self.id = EmpiricalInterventionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EmpiricalFinding(ObservableFeature):
    """
    this category is currently considered broad enough to tag empirical lab measurements and other computational
    attributes taken as 'empirical traits' with some statistical score, for example, a p value in componentservice
    associations.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalFinding
    class_class_curie: ClassVar[str] = "samplelink:EmpiricalFinding"
    class_name: ClassVar[str] = "empirical finding"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EmpiricalFinding

    id: Union[str, EmpiricalFindingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Optional[Union[Union[dict, EmpiricalAttribute], List[Union[dict, EmpiricalAttribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmpiricalFindingId):
            self.id = EmpiricalFindingId(self.id)

        self._normalize_inlined_as_dict(slot_name="has_attribute", slot_type=EmpiricalAttribute, key_name="has attribute type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class OfflineMaintenance(EmpiricalIntervention):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OfflineMaintenance
    class_class_curie: ClassVar[str] = "samplelink:OfflineMaintenance"
    class_name: ClassVar[str] = "offline maintenance"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OfflineMaintenance

    id: Union[str, OfflineMaintenanceId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OfflineMaintenanceId):
            self.id = OfflineMaintenanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SocioeconomicAttribute(Attribute):
    """
    Attributes relating to a socioeconomic manifestation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SocioeconomicAttribute
    class_class_curie: ClassVar[str] = "samplelink:SocioeconomicAttribute"
    class_name: ClassVar[str] = "socioeconomic attribute"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SocioeconomicAttribute

    has_attribute_type: Union[str, OntologyClassId] = None

@dataclass
class Case(IndividualSystem):
    """
    An individual system that has a patient role in some empirical context.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Case
    class_class_curie: ClassVar[str] = "samplelink:Case"
    class_name: ClassVar[str] = "case"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Case

    id: Union[str, CaseId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CaseId):
            self.id = CaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Cohort(StudyPopulation):
    """
    A group of individuals banded together or repaired as a group who share common characteristics. A cohort 'study'
    is a particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through
    time.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Cohort
    class_class_curie: ClassVar[str] = "samplelink:Cohort"
    class_name: ClassVar[str] = "cohort"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Cohort

    id: Union[str, CohortId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CohortId):
            self.id = CohortId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEvent(YAMLRoot):
    """
    A (possibly time bounded) incidence of a feature of the environment of an system that influences one or more
    observability of that system, potentially mediated by serviceunits
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ExposureEvent
    class_class_curie: ClassVar[str] = "samplelink:ExposureEvent"
    class_name: ClassVar[str] = "exposure event"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ExposureEvent

    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceBackgroundExposure(WorkloadEntity):
    """
    A service background exposure is where an individual's specific service background of serviceunits, sequence
    variants or other pre-existing service conditions constitute a kind of 'exposure' to the system, leading to or
    influencing an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceBackgroundExposure
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceBackgroundExposure"
    class_name: ClassVar[str] = "componentservice background exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceBackgroundExposure

    id: Union[str, ComponentserviceBackgroundExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None
    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceBackgroundExposureId):
            self.id = ComponentserviceBackgroundExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype] if self.has_componentservice_or_servicetype is not None else []
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**as_dict(v)) for v in self.has_componentservice_or_servicetype]

        super().__post_init__(**kwargs)


class FaultyEntityMixin(YAMLRoot):
    """
    A faulty (abnormal) structure or process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.FaultyEntityMixin
    class_class_curie: ClassVar[str] = "samplelink:FaultyEntityMixin"
    class_name: ClassVar[str] = "faulty entity mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.FaultyEntityMixin


@dataclass
class FaultyProcess(ComputationalProcess):
    """
    A compulogic function or a process having an abnormal or deleterious effect at the subcomponent, component,
    multi-component, node, or system level.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.FaultyProcess
    class_class_curie: ClassVar[str] = "samplelink:FaultyProcess"
    class_name: ClassVar[str] = "faulty process"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.FaultyProcess

    id: Union[str, FaultyProcessId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultyProcessId):
            self.id = FaultyProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureExposure(ErrorOrObservableFeature):
    """
    A error or observable feature exposure is where a error state is manifested which represents an precondition,
    leading to or influencing an outcome, e.g. hypertension leading to a related error outcome such as cardiovascular
    error.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeatureExposure
    class_class_curie: ClassVar[str] = "samplelink:ErrorOrObservableFeatureExposure"
    class_name: ClassVar[str] = "error or observable feature exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeatureExposure

    id: Union[str, ErrorOrObservableFeatureExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ErrorOrObservableFeatureExposureId):
            self.id = ErrorOrObservableFeatureExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class FaultyProcessExposure(FaultyProcess):
    """
    A faulty process, when viewed as an exposure, representing an precondition, leading to or influencing an outcome,
    e.g. autoimmunity leading to disease.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.FaultyProcessExposure
    class_class_curie: ClassVar[str] = "samplelink:FaultyProcessExposure"
    class_name: ClassVar[str] = "faulty process exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.FaultyProcessExposure

    id: Union[str, FaultyProcessExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultyProcessExposureId):
            self.id = FaultyProcessExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class FaultyDeploymentStructure(DeploymentEntity):
    """
    An deployment structure with the potential of have an abnormal or deleterious effect at the process, serviceunit,
    multiserviceunit, or systemal level.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.FaultyDeploymentStructure
    class_class_curie: ClassVar[str] = "samplelink:FaultyDeploymentStructure"
    class_name: ClassVar[str] = "faulty deployment structure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.FaultyDeploymentStructure

    id: Union[str, FaultyDeploymentStructureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultyDeploymentStructureId):
            self.id = FaultyDeploymentStructureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FaultyDeploymentExposure(FaultyDeploymentStructure):
    """
    An abnormal deployment structure, when viewed as an exposure, representing an precondition, leading to or
    influencing an outcome,
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.FaultyDeploymentExposure
    class_class_curie: ClassVar[str] = "samplelink:FaultyDeploymentExposure"
    class_name: ClassVar[str] = "faulty deployment exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.FaultyDeploymentExposure

    id: Union[str, FaultyDeploymentExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultyDeploymentExposureId):
            self.id = FaultyDeploymentExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationExposure(ControlActor):
    """
    A orchestration exposure is an intake of a particular control actor, other than a administrative operation.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationExposure
    class_class_curie: ClassVar[str] = "samplelink:OrchestrationExposure"
    class_name: ClassVar[str] = "orchestration exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationExposure

    id: Union[str, OrchestrationExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrchestrationExposureId):
            self.id = OrchestrationExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class ComplexOrchestrationExposure(OrchestrationExposure):
    """
    A complex orchestration exposure is an intake of a orchestration cluster (e.g. gasoline), other than a
    administrative operation.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComplexOrchestrationExposure
    class_class_curie: ClassVar[str] = "samplelink:ComplexOrchestrationExposure"
    class_name: ClassVar[str] = "complex orchestration exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComplexOrchestrationExposure

    id: Union[str, ComplexOrchestrationExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_control_actor: Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComplexOrchestrationExposureId):
            self.id = ComplexOrchestrationExposureId(self.id)

        if not isinstance(self.has_control_actor, list):
            self.has_control_actor = [self.has_control_actor] if self.has_control_actor is not None else []
        self.has_control_actor = [v if isinstance(v, ControlActorId) else ControlActorId(v) for v in self.has_control_actor]

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalExposure(AdministrativeOperation):
    """
    A administrative operational exposure is an intake of a particular administrative operation.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeOperationalExposure
    class_class_curie: ClassVar[str] = "samplelink:AdministrativeOperationalExposure"
    class_name: ClassVar[str] = "administrative operational exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeOperationalExposure

    id: Union[str, AdministrativeOperationalExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdministrativeOperationalExposureId):
            self.id = AdministrativeOperationalExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalToComponentserviceInteractionExposure(AdministrativeOperationalExposure):
    """
    administrative operational to componentservice interaction exposure is a administrative operational exposure is
    where the interactions of the administrative operational with specific componentservices are known to constitute
    an 'exposure' to the system, leading to or influencing an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeOperationalToComponentserviceInteractionExposure
    class_class_curie: ClassVar[str] = "samplelink:AdministrativeOperationalToComponentserviceInteractionExposure"
    class_name: ClassVar[str] = "administrative operational to componentservice interaction exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeOperationalToComponentserviceInteractionExposure

    id: Union[str, AdministrativeOperationalToComponentserviceInteractionExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_componentservice_or_servicetype: Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdministrativeOperationalToComponentserviceInteractionExposureId):
            self.id = AdministrativeOperationalToComponentserviceInteractionExposureId(self.id)

        if not isinstance(self.has_componentservice_or_servicetype, list):
            self.has_componentservice_or_servicetype = [self.has_componentservice_or_servicetype] if self.has_componentservice_or_servicetype is not None else []
        self.has_componentservice_or_servicetype = [v if isinstance(v, Componentservice) else Componentservice(**as_dict(v)) for v in self.has_componentservice_or_servicetype]

        super().__post_init__(**kwargs)


@dataclass
class Repairing(NamedThing):
    """
    A repairing is targeted at a error or observability and may involve multiple administrative operational
    'exposures', engineering devices and/or procedures
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Repairing
    class_class_curie: ClassVar[str] = "samplelink:Repairing"
    class_name: ClassVar[str] = "repairing"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Repairing

    id: Union[str, RepairingId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_administrative_operation: Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]] = empty_list()
    has_device: Optional[Union[Union[str, DeviceId], List[Union[str, DeviceId]]]] = empty_list()
    has_procedure: Optional[Union[Union[str, ProcedureId], List[Union[str, ProcedureId]]]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RepairingId):
            self.id = RepairingId(self.id)

        if not isinstance(self.has_administrative_operation, list):
            self.has_administrative_operation = [self.has_administrative_operation] if self.has_administrative_operation is not None else []
        self.has_administrative_operation = [v if isinstance(v, AdministrativeOperationId) else AdministrativeOperationId(v) for v in self.has_administrative_operation]

        if not isinstance(self.has_device, list):
            self.has_device = [self.has_device] if self.has_device is not None else []
        self.has_device = [v if isinstance(v, DeviceId) else DeviceId(v) for v in self.has_device]

        if not isinstance(self.has_procedure, list):
            self.has_procedure = [self.has_procedure] if self.has_procedure is not None else []
        self.has_procedure = [v if isinstance(v, ProcedureId) else ProcedureId(v) for v in self.has_procedure]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class BioticExposure(SystemTaxon):
    """
    A biotic exposure is an intake of (sometimes faulty) computational systems (including viruses)
    """
    _inherited_slots: ClassVar[List[str]] = ["subclass_of"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.BioticExposure
    class_class_curie: ClassVar[str] = "samplelink:BioticExposure"
    class_name: ClassVar[str] = "biotic exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.BioticExposure

    id: Union[str, BioticExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BioticExposureId):
            self.id = BioticExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class GeographicExposure(GeographicLocation):
    """
    A geographic exposure is a factor relating to geographic proximity to some impactful entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.GeographicExposure
    class_class_curie: ClassVar[str] = "samplelink:GeographicExposure"
    class_name: ClassVar[str] = "geographic exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.GeographicExposure

    id: Union[str, GeographicExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicExposureId):
            self.id = GeographicExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalExposure(EnvironmentalProcess):
    """
    A environmental exposure is a factor relating to abiotic processes in the environment including atmospheric (heat,
    cold, general pollution) and water-born contaminants
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EnvironmentalExposure
    class_class_curie: ClassVar[str] = "samplelink:EnvironmentalExposure"
    class_name: ClassVar[str] = "environmental exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EnvironmentalExposure

    id: Union[str, EnvironmentalExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalExposureId):
            self.id = EnvironmentalExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralExposure(Behavior):
    """
    A behavioral exposure is a factor relating to behavior impacting an individual.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.BehavioralExposure
    class_class_curie: ClassVar[str] = "samplelink:BehavioralExposure"
    class_name: ClassVar[str] = "behavioral exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.BehavioralExposure

    id: Union[str, BehavioralExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehavioralExposureId):
            self.id = BehavioralExposureId(self.id)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


@dataclass
class SocioeconomicExposure(Behavior):
    """
    A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g.
    poverty).
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SocioeconomicExposure
    class_class_curie: ClassVar[str] = "samplelink:SocioeconomicExposure"
    class_name: ClassVar[str] = "socioeconomic exposure"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SocioeconomicExposure

    id: Union[str, SocioeconomicExposureId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None
    has_attribute: Union[Union[dict, SocioeconomicAttribute], List[Union[dict, SocioeconomicAttribute]]] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SocioeconomicExposureId):
            self.id = SocioeconomicExposureId(self.id)

        if self._is_empty(self.has_attribute):
            self.MissingRequiredField("has_attribute")
        self._normalize_inlined_as_dict(slot_name="has_attribute", slot_type=SocioeconomicAttribute, key_name="has attribute type", keyed=False)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


class Outcome(YAMLRoot):
    """
    An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of
    various categories of possible computational or non-computational (e.g. empirical) outcomes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Outcome
    class_class_curie: ClassVar[str] = "samplelink:Outcome"
    class_name: ClassVar[str] = "outcome"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Outcome


@dataclass
class FaultyProcessOutcome(FaultyProcess):
    """
    An outcome resulting from an exposure event which is the manifestation of a faulty process.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.FaultyProcessOutcome
    class_class_curie: ClassVar[str] = "samplelink:FaultyProcessOutcome"
    class_name: ClassVar[str] = "faulty process outcome"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.FaultyProcessOutcome

    id: Union[str, FaultyProcessOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultyProcessOutcomeId):
            self.id = FaultyProcessOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class FaultyDeploymentOutcome(FaultyDeploymentStructure):
    """
    An outcome resulting from an exposure event which is the manifestation of an abnormal deployment structure.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.FaultyDeploymentOutcome
    class_class_curie: ClassVar[str] = "samplelink:FaultyDeploymentOutcome"
    class_name: ClassVar[str] = "faulty deployment outcome"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.FaultyDeploymentOutcome

    id: Union[str, FaultyDeploymentOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FaultyDeploymentOutcomeId):
            self.id = FaultyDeploymentOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureOutcome(ErrorOrObservableFeature):
    """
    logical outcomes resulting from an exposure event which is the manifestation of a error or other characteristic
    observability.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeatureOutcome
    class_class_curie: ClassVar[str] = "samplelink:ErrorOrObservableFeatureOutcome"
    class_name: ClassVar[str] = "error or observable feature outcome"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeatureOutcome

    id: Union[str, ErrorOrObservableFeatureOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ErrorOrObservableFeatureOutcomeId):
            self.id = ErrorOrObservableFeatureOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BehavioralOutcome(Behavior):
    """
    An outcome resulting from an exposure event which is the manifestation of individual behavior.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.BehavioralOutcome
    class_class_curie: ClassVar[str] = "samplelink:BehavioralOutcome"
    class_name: ClassVar[str] = "behavioral outcome"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.BehavioralOutcome

    id: Union[str, BehavioralOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehavioralOutcomeId):
            self.id = BehavioralOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OfflineMaintenanceOutcome(OfflineMaintenance):
    """
    An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room
    visit) or chronic (inpatient) offline maintenance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OfflineMaintenanceOutcome
    class_class_curie: ClassVar[str] = "samplelink:OfflineMaintenanceOutcome"
    class_name: ClassVar[str] = "offline maintenance outcome"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OfflineMaintenanceOutcome

    id: Union[str, OfflineMaintenanceOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OfflineMaintenanceOutcomeId):
            self.id = OfflineMaintenanceOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MortalityOutcome(Death):
    """
    An outcome of death from resulting from an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.MortalityOutcome
    class_class_curie: ClassVar[str] = "samplelink:MortalityOutcome"
    class_name: ClassVar[str] = "mortality outcome"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.MortalityOutcome

    id: Union[str, MortalityOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MortalityOutcomeId):
            self.id = MortalityOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EpidemiologicalOutcome(ComputationalEntity):
    """
    An epidemiological outcome, such as societal error burden, resulting from an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EpidemiologicalOutcome
    class_class_curie: ClassVar[str] = "samplelink:EpidemiologicalOutcome"
    class_name: ClassVar[str] = "epidemiological outcome"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EpidemiologicalOutcome

    id: Union[str, EpidemiologicalOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EpidemiologicalOutcomeId):
            self.id = EpidemiologicalOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SocioeconomicOutcome(Behavior):
    """
    An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure
    event
    """
    _inherited_slots: ClassVar[List[str]] = ["has_input", "has_output", "enabled_by"]

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SocioeconomicOutcome
    class_class_curie: ClassVar[str] = "samplelink:SocioeconomicOutcome"
    class_name: ClassVar[str] = "socioeconomic outcome"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SocioeconomicOutcome

    id: Union[str, SocioeconomicOutcomeId] = None
    category: Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SocioeconomicOutcomeId):
            self.id = SocioeconomicOutcomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.Association
    class_class_curie: ClassVar[str] = "samplelink:Association"
    class_name: ClassVar[str] = "association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.Association

    id: Union[str, AssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    negated: Optional[Union[bool, Bool]] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()
    publications: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.relation):
            self.MissingRequiredField("relation")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, AssociationId) else AssociationId(v) for v in self.category]

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.qualifiers]

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.publications]

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class ContributorAssociation(Association):
    """
    Any association between an entity (such as a publication) and various agents that contribute to its realisation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ContributorAssociation
    class_class_curie: ClassVar[str] = "samplelink:ContributorAssociation"
    class_name: ClassVar[str] = "contributor association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ContributorAssociation

    id: Union[str, ContributorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, InformationContentEntityId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, AgentId] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContributorAssociationId):
            self.id = ContributorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, InformationContentEntityId):
            self.subject = InformationContentEntityId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AgentId):
            self.object = AgentId(self.object)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.qualifiers]

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToServiceunittypePartAssociation(Association):
    """
    Any association between one serviceunittype and a microservice entity that is a subset of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToServiceunittypePartAssociation
    class_class_curie: ClassVar[str] = "samplelink:ServiceunittypeToServiceunittypePartAssociation"
    class_name: ClassVar[str] = "serviceunittype to serviceunittype part association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToServiceunittypePartAssociation

    id: Union[str, ServiceunittypeToServiceunittypePartAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    object: Union[str, ServiceunittypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceunittypeToServiceunittypePartAssociationId):
            self.id = ServiceunittypeToServiceunittypePartAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ServiceunittypeId):
            self.object = ServiceunittypeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToComponentserviceAssociation(Association):
    """
    Any association between a serviceunittype and a componentservice. The serviceunittype have have multiple variants
    in that componentservice or a single one. There is no assumption of cardinality
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "samplelink:ServiceunittypeToComponentserviceAssociation"
    class_name: ClassVar[str] = "serviceunittype to componentservice association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToComponentserviceAssociation

    id: Union[str, ServiceunittypeToComponentserviceAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    object: Union[dict, Componentservice] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceunittypeToComponentserviceAssociationId):
            self.id = ServiceunittypeToComponentserviceAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, Componentservice):
            self.object = Componentservice(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToVariantAssociation(Association):
    """
    Any association between a serviceunittype and a sequence variant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToVariantAssociation
    class_class_curie: ClassVar[str] = "samplelink:ServiceunittypeToVariantAssociation"
    class_name: ClassVar[str] = "serviceunittype to variant association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToVariantAssociation

    id: Union[str, ServiceunittypeToVariantAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    object: Union[str, SequenceVariantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceunittypeToVariantAssociationId):
            self.id = ServiceunittypeToVariantAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToComponentserviceAssociation(Association):
    """
    abstract parent class for different kinds of componentservice-serviceunit or servicetype to servicetype
    relationships. Includes homology and interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceToComponentserviceAssociation"
    class_name: ClassVar[str] = "componentservice to componentservice association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToComponentserviceAssociation

    id: Union[str, ComponentserviceToComponentserviceAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToComponentserviceHomologyAssociation(ComponentserviceToComponentserviceAssociation):
    """
    A homology association between two componentservices. May be orthology (in which case the species of subject and
    object should differ) or paralogy (in which case the species may be the same)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToComponentserviceHomologyAssociation
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceToComponentserviceHomologyAssociation"
    class_name: ClassVar[str] = "componentservice to componentservice homology association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToComponentserviceHomologyAssociation

    id: Union[str, ComponentserviceToComponentserviceHomologyAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceToComponentserviceHomologyAssociationId):
            self.id = ComponentserviceToComponentserviceHomologyAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceAvailabilityMixin(YAMLRoot):
    """
    Observed componentservice availability intensity, context (site, stage) and associated observable status within
    which the availability occurs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceAvailabilityMixin
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceAvailabilityMixin"
    class_name: ClassVar[str] = "componentservice availability mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceAvailabilityMixin

    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    availability_site: Optional[Union[str, DeploymentEntityId]] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    observable_state: Optional[Union[str, ErrorOrObservableFeatureId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.availability_site is not None and not isinstance(self.availability_site, DeploymentEntityId):
            self.availability_site = DeploymentEntityId(self.availability_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.observable_state is not None and not isinstance(self.observable_state, ErrorOrObservableFeatureId):
            self.observable_state = ErrorOrObservableFeatureId(self.observable_state)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToComponentserviceCoavailabilityAssociation(ComponentserviceToComponentserviceAssociation):
    """
    Indicates that two componentservices are co-available, generally under the same conditions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToComponentserviceCoavailabilityAssociation
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceToComponentserviceCoavailabilityAssociation"
    class_name: ClassVar[str] = "componentservice to componentservice coavailability association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToComponentserviceCoavailabilityAssociation

    id: Union[str, ComponentserviceToComponentserviceCoavailabilityAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None
    predicate: Union[str, PredicateType] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    availability_site: Optional[Union[str, DeploymentEntityId]] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    observable_state: Optional[Union[str, ErrorOrObservableFeatureId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceToComponentserviceCoavailabilityAssociationId):
            self.id = ComponentserviceToComponentserviceCoavailabilityAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.availability_site is not None and not isinstance(self.availability_site, DeploymentEntityId):
            self.availability_site = DeploymentEntityId(self.availability_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.observable_state is not None and not isinstance(self.observable_state, ErrorOrObservableFeatureId):
            self.observable_state = ErrorOrObservableFeatureId(self.observable_state)

        super().__post_init__(**kwargs)


@dataclass
class PairwiseComponentserviceToComponentserviceInteraction(ComponentserviceToComponentserviceAssociation):
    """
    An interaction between two componentservices or two servicetypes. May be cyber (e.g. serviceinstance binding) or
    service (between componentservices). May be symmetric (e.g. serviceinstance interaction) or directed (e.g.
    phosphorylation)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.PairwiseComponentserviceToComponentserviceInteraction
    class_class_curie: ClassVar[str] = "samplelink:PairwiseComponentserviceToComponentserviceInteraction"
    class_name: ClassVar[str] = "pairwise componentservice to componentservice interaction"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.PairwiseComponentserviceToComponentserviceInteraction

    id: Union[str, PairwiseComponentserviceToComponentserviceInteractionId] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PairwiseComponentserviceToComponentserviceInteractionId):
            self.id = PairwiseComponentserviceToComponentserviceInteractionId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.relation):
            self.MissingRequiredField("relation")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)

        super().__post_init__(**kwargs)


@dataclass
class PairwiseOperationallyInteraction(PairwiseComponentserviceToComponentserviceInteraction):
    """
    An interaction at the operational level between two cyber entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.PairwiseOperationallyInteraction
    class_class_curie: ClassVar[str] = "samplelink:PairwiseOperationallyInteraction"
    class_name: ClassVar[str] = "pairwise operationally interaction"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.PairwiseOperationallyInteraction

    id: Union[str, PairwiseOperationallyInteractionId] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, OperationalEntityId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[str, OperationalEntityId] = None
    interacting_tasks_category: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PairwiseOperationallyInteractionId):
            self.id = PairwiseOperationallyInteractionId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OperationalEntityId):
            self.subject = OperationalEntityId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.relation):
            self.MissingRequiredField("relation")
        if not isinstance(self.relation, URIorCURIE):
            self.relation = URIorCURIE(self.relation)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, OperationalEntityId):
            self.object = OperationalEntityId(self.object)

        if self.interacting_tasks_category is not None and not isinstance(self.interacting_tasks_category, OntologyClassId):
            self.interacting_tasks_category = OntologyClassId(self.interacting_tasks_category)

        super().__post_init__(**kwargs)


@dataclass
class ComponentTypeToEntityAssociationMixin(YAMLRoot):
    """
    An relationship between a component type and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentTypeToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:ComponentTypeToEntityAssociationMixin"
    class_name: ClassVar[str] = "component type to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentTypeToEntityAssociationMixin

    subject: Union[str, ComponentTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentTypeId):
            self.subject = ComponentTypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentTypeToErrorOrObservableFeatureAssociation(Association):
    """
    An relationship between a component type and a error or a observability, where the component type is derived from
    an individual with that error or observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentTypeToErrorOrObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "samplelink:ComponentTypeToErrorOrObservableFeatureAssociation"
    class_name: ClassVar[str] = "component type to error or observable feature association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentTypeToErrorOrObservableFeatureAssociation

    id: Union[str, ComponentTypeToErrorOrObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentTypeToErrorOrObservableFeatureAssociationId):
            self.id = ComponentTypeToErrorOrObservableFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ErrorOrObservableFeatureId):
            self.subject = ErrorOrObservableFeatureId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OperationalEntityToEntityAssociationMixin(YAMLRoot):
    """
    An interaction between a operational entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OperationalEntityToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:OperationalEntityToEntityAssociationMixin"
    class_name: ClassVar[str] = "operational entity to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OperationalEntityToEntityAssociationMixin

    subject: Union[str, OperationalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OperationalEntityId):
            self.subject = OperationalEntityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalToEntityAssociationMixin(OperationalEntityToEntityAssociationMixin):
    """
    An interaction between a administrative operational and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeOperationalToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:AdministrativeOperationalToEntityAssociationMixin"
    class_name: ClassVar[str] = "administrative operational to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeOperationalToEntityAssociationMixin

    subject: Union[str, AdministrativeOperationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, AdministrativeOperationId):
            self.subject = AdministrativeOperationId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToEntityAssociationMixin(OperationalEntityToEntityAssociationMixin):
    """
    An interaction between a orchestration entity and another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:OrchestrationToEntityAssociationMixin"
    class_name: ClassVar[str] = "orchestration to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToEntityAssociationMixin

    subject: Union[str, ControlActorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ControlActorId):
            self.subject = ControlActorId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class CaseToEntityAssociationMixin(YAMLRoot):
    """
    An abstract association for use where the case is the subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.CaseToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:CaseToEntityAssociationMixin"
    class_name: ClassVar[str] = "case to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.CaseToEntityAssociationMixin

    subject: Union[str, CaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, CaseId):
            self.subject = CaseId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToOrchestrationAssociation(Association):
    """
    A relationship between two orchestration entities. This can encompass actual interactions as well as temporal
    causal edges, e.g. one orchestration converted to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToOrchestrationAssociation
    class_class_curie: ClassVar[str] = "samplelink:OrchestrationToOrchestrationAssociation"
    class_name: ClassVar[str] = "orchestration to orchestration association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToOrchestrationAssociation

    id: Union[str, OrchestrationToOrchestrationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, ControlActorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrchestrationToOrchestrationAssociationId):
            self.id = OrchestrationToOrchestrationAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ControlActorId):
            self.object = ControlActorId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToOrchestrationDerivationAssociation(OrchestrationToOrchestrationAssociation):
    """
    A causal relationship between two orchestration entities, where the subject represents the upstream entity and the
    object represents the downstream. For any such association there is an implicit reaction:
    IF
    R has-input C1 AND
    R has-output C2 AND
    R enabled-by P AND
    R type Reaction
    THEN
    C1 derives-into C2 <<catalyst qualifier P>>
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToOrchestrationDerivationAssociation
    class_class_curie: ClassVar[str] = "samplelink:OrchestrationToOrchestrationDerivationAssociation"
    class_name: ClassVar[str] = "orchestration to orchestration derivation association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToOrchestrationDerivationAssociation

    id: Union[str, OrchestrationToOrchestrationDerivationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ControlActorId] = None
    object: Union[str, ControlActorId] = None
    predicate: Union[str, PredicateType] = None
    catalyst_qualifier: Optional[Union[Union[dict, MacrooperationalMachineMixin], List[Union[dict, MacrooperationalMachineMixin]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrchestrationToOrchestrationDerivationAssociationId):
            self.id = OrchestrationToOrchestrationDerivationAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ControlActorId):
            self.subject = ControlActorId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ControlActorId):
            self.object = ControlActorId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if not isinstance(self.catalyst_qualifier, list):
            self.catalyst_qualifier = [self.catalyst_qualifier] if self.catalyst_qualifier is not None else []
        self.catalyst_qualifier = [v if isinstance(v, MacrooperationalMachineMixin) else MacrooperationalMachineMixin(**as_dict(v)) for v in self.catalyst_qualifier]

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToErrorOrObservableFeatureAssociation(Association):
    """
    An interaction between a orchestration entity and a observability or error, where the presence of the
    orchestration gives rise to or exacerbates the observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToErrorOrObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "samplelink:OrchestrationToErrorOrObservableFeatureAssociation"
    class_name: ClassVar[str] = "orchestration to error or observable feature association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToErrorOrObservableFeatureAssociation

    id: Union[str, OrchestrationToErrorOrObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrchestrationToErrorOrObservableFeatureAssociationId):
            self.id = OrchestrationToErrorOrObservableFeatureAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ErrorOrObservableFeatureId):
            self.object = ErrorOrObservableFeatureId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToPathwayAssociation(Association):
    """
    An interaction between a orchestration entity and a computational process or pathway.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToPathwayAssociation
    class_class_curie: ClassVar[str] = "samplelink:OrchestrationToPathwayAssociation"
    class_name: ClassVar[str] = "orchestration to pathway association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToPathwayAssociation

    id: Union[str, OrchestrationToPathwayAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, PathwayId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrchestrationToPathwayAssociationId):
            self.id = OrchestrationToPathwayAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OrchestrationToComponentserviceAssociation(Association):
    """
    An interaction between a orchestration entity and a componentservice or servicetype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "samplelink:OrchestrationToComponentserviceAssociation"
    class_name: ClassVar[str] = "orchestration to componentservice association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.OrchestrationToComponentserviceAssociation

    id: Union[str, OrchestrationToComponentserviceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrchestrationToComponentserviceAssociationId):
            self.id = OrchestrationToComponentserviceAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeOperationalToComponentserviceAssociation(Association):
    """
    An interaction between a administrative operational and a componentservice or servicetype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeOperationalToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "samplelink:AdministrativeOperationalToComponentserviceAssociation"
    class_name: ClassVar[str] = "administrative operational to componentservice association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.AdministrativeOperationalToComponentserviceAssociation

    id: Union[str, AdministrativeOperationalToComponentserviceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdministrativeOperationalToComponentserviceAssociationId):
            self.id = AdministrativeOperationalToComponentserviceAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class ResourceSampleToEntityAssociationMixin(YAMLRoot):
    """
    An association between a resource sample and something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ResourceSampleToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:ResourceSampleToEntityAssociationMixin"
    class_name: ClassVar[str] = "resource sample to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ResourceSampleToEntityAssociationMixin

    subject: Union[str, ResourceSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ResourceSampleId):
            self.subject = ResourceSampleId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ResourceSampleDerivationAssociation(Association):
    """
    An association between a resource sample and the resource entity from which it is derived.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ResourceSampleDerivationAssociation
    class_class_curie: ClassVar[str] = "samplelink:ResourceSampleDerivationAssociation"
    class_name: ClassVar[str] = "resource sample derivation association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ResourceSampleDerivationAssociation

    id: Union[str, ResourceSampleDerivationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ResourceSampleId] = None
    object: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceSampleDerivationAssociationId):
            self.id = ResourceSampleDerivationAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ResourceSampleId):
            self.subject = ResourceSampleId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ResourceSampleToErrorOrObservableFeatureAssociation(Association):
    """
    An association between a resource sample and a error or observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ResourceSampleToErrorOrObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "samplelink:ResourceSampleToErrorOrObservableFeatureAssociation"
    class_name: ClassVar[str] = "resource sample to error or observable feature association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ResourceSampleToErrorOrObservableFeatureAssociation

    id: Union[str, ResourceSampleToErrorOrObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceSampleToErrorOrObservableFeatureAssociationId):
            self.id = ResourceSampleToErrorOrObservableFeatureAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ErrorToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ErrorToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:ErrorToEntityAssociationMixin"
    class_name: ClassVar[str] = "error to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ErrorToEntityAssociationMixin

    subject: Union[str, ErrorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ErrorId):
            self.subject = ErrorId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class EntityToExposureEventAssociationMixin(YAMLRoot):
    """
    An association between some entity and an exposure event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EntityToExposureEventAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:EntityToExposureEventAssociationMixin"
    class_name: ClassVar[str] = "entity to exposure event association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EntityToExposureEventAssociationMixin

    object: Union[dict, ExposureEvent] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ExposureEvent):
            self.object = ExposureEvent(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class ErrorToExposureEventAssociation(Association):
    """
    An association between an exposure event and a error.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ErrorToExposureEventAssociation
    class_class_curie: ClassVar[str] = "samplelink:ErrorToExposureEventAssociation"
    class_name: ClassVar[str] = "error to exposure event association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ErrorToExposureEventAssociation

    id: Union[str, ErrorToExposureEventAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ErrorToExposureEventAssociationId):
            self.id = ErrorToExposureEventAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToEntityAssociationMixin(YAMLRoot):
    """
    An association between some exposure event and some entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ExposureEventToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:ExposureEventToEntityAssociationMixin"
    class_name: ClassVar[str] = "exposure event to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ExposureEventToEntityAssociationMixin

    subject: Union[dict, ExposureEvent] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ExposureEvent):
            self.subject = ExposureEvent(**as_dict(self.subject))

        super().__post_init__(**kwargs)


@dataclass
class EntityToOutcomeAssociationMixin(YAMLRoot):
    """
    An association between some entity and an outcome
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EntityToOutcomeAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:EntityToOutcomeAssociationMixin"
    class_name: ClassVar[str] = "entity to outcome association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EntityToOutcomeAssociationMixin

    object: Union[dict, Outcome] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, Outcome):
            self.object = Outcome()

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToOutcomeAssociation(Association):
    """
    An association between an exposure event and an outcome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ExposureEventToOutcomeAssociation
    class_class_curie: ClassVar[str] = "samplelink:ExposureEventToOutcomeAssociation"
    class_name: ClassVar[str] = "exposure event to outcome association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ExposureEventToOutcomeAssociation

    id: Union[str, ExposureEventToOutcomeAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    has_population_context: Optional[Union[str, PopulationOfIndividualSystemsId]] = None
    has_temporal_context: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureEventToOutcomeAssociationId):
            self.id = ExposureEventToOutcomeAssociationId(self.id)

        if self.has_population_context is not None and not isinstance(self.has_population_context, PopulationOfIndividualSystemsId):
            self.has_population_context = PopulationOfIndividualSystemsId(self.has_population_context)

        if self.has_temporal_context is not None and not isinstance(self.has_temporal_context, TimeType):
            self.has_temporal_context = TimeType(self.has_temporal_context)

        super().__post_init__(**kwargs)


@dataclass
class FrequencyQualifierMixin(YAMLRoot):
    """
    Qualifier for frequency type associations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.FrequencyQualifierMixin
    class_class_curie: ClassVar[str] = "samplelink:FrequencyQualifierMixin"
    class_name: ClassVar[str] = "frequency qualifier mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.FrequencyQualifierMixin

    frequency_qualifier: Optional[Union[dict, FrequencyValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(**as_dict(self.frequency_qualifier))

        super().__post_init__(**kwargs)


@dataclass
class EntityToFeatureOrErrorQualifiersMixin(FrequencyQualifierMixin):
    """
    Qualifiers for entity to error or observability associations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EntityToFeatureOrErrorQualifiersMixin
    class_class_curie: ClassVar[str] = "samplelink:EntityToFeatureOrErrorQualifiersMixin"
    class_name: ClassVar[str] = "entity to feature or error qualifiers mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EntityToFeatureOrErrorQualifiersMixin

    severity_qualifier: Optional[Union[dict, SeverityValue]] = None
    onset_qualifier: Optional[Union[dict, Onset]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.severity_qualifier is not None and not isinstance(self.severity_qualifier, SeverityValue):
            self.severity_qualifier = SeverityValue(**as_dict(self.severity_qualifier))

        if self.onset_qualifier is not None and not isinstance(self.onset_qualifier, Onset):
            self.onset_qualifier = Onset(**as_dict(self.onset_qualifier))

        super().__post_init__(**kwargs)


@dataclass
class EntityToObservableFeatureAssociationMixin(EntityToFeatureOrErrorQualifiersMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EntityToObservableFeatureAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:EntityToObservableFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to observable feature association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EntityToObservableFeatureAssociationMixin

    object: Union[str, ObservableFeatureId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ObservableFeatureId):
            self.object = ObservableFeatureId(self.object)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**as_dict(self.architectural_style_qualifier))

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        super().__post_init__(**kwargs)


@dataclass
class EntityToErrorAssociationMixin(EntityToFeatureOrErrorQualifiersMixin):
    """
    mixin class for any association whose object (target node) is a error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EntityToErrorAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:EntityToErrorAssociationMixin"
    class_name: ClassVar[str] = "entity to error association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EntityToErrorAssociationMixin

    object: Union[str, ErrorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ErrorId):
            self.object = ErrorId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeatureToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:ErrorOrObservableFeatureToEntityAssociationMixin"
    class_name: ClassVar[str] = "error or observable feature to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeatureToEntityAssociationMixin

    subject: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ErrorOrObservableFeatureId):
            self.subject = ErrorOrObservableFeatureId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureAssociationToLocationAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeatureAssociationToLocationAssociation
    class_class_curie: ClassVar[str] = "samplelink:ErrorOrObservableFeatureAssociationToLocationAssociation"
    class_name: ClassVar[str] = "error or observable feature association to location association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeatureAssociationToLocationAssociation

    id: Union[str, ErrorOrObservableFeatureAssociationToLocationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, DeploymentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ErrorOrObservableFeatureAssociationToLocationAssociationId):
            self.id = ErrorOrObservableFeatureAssociationToLocationAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ErrorOrObservableFeatureToLocationAssociation(Association):
    """
    An association between either a error or a observable feature and an deployment entity, where the error/feature
    manifests in that site.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeatureToLocationAssociation
    class_class_curie: ClassVar[str] = "samplelink:ErrorOrObservableFeatureToLocationAssociation"
    class_name: ClassVar[str] = "error or observable feature to location association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ErrorOrObservableFeatureToLocationAssociation

    id: Union[str, ErrorOrObservableFeatureToLocationAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[str, DeploymentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ErrorOrObservableFeatureToLocationAssociationId):
            self.id = ErrorOrObservableFeatureToLocationAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class EntityToErrorOrObservableFeatureAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.EntityToErrorOrObservableFeatureAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:EntityToErrorOrObservableFeatureAssociationMixin"
    class_name: ClassVar[str] = "entity to error or observable feature association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.EntityToErrorOrObservableFeatureAssociationMixin

    object: Union[str, ErrorOrObservableFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ErrorOrObservableFeatureId):
            self.object = ErrorOrObservableFeatureId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:ServiceunittypeToEntityAssociationMixin"
    class_name: ClassVar[str] = "serviceunittype to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToEntityAssociationMixin

    subject: Union[str, ServiceunittypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToObservableFeatureAssociation(Association):
    """
    Any association between one serviceunittype and a observable feature, where having the serviceunittype confers the
    observability, either in isolation or through environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "samplelink:ServiceunittypeToObservableFeatureAssociation"
    class_name: ClassVar[str] = "serviceunittype to observable feature association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToObservableFeatureAssociation

    id: Union[str, ServiceunittypeToObservableFeatureAssociationId] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[str, ServiceunittypeId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceunittypeToObservableFeatureAssociationId):
            self.id = ServiceunittypeToObservableFeatureAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**as_dict(self.architectural_style_qualifier))

        super().__post_init__(**kwargs)


@dataclass
class ExposureEventToObservableFeatureAssociation(Association):
    """
    Any association between an environment and a observable feature, where being in the environment influences the
    observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ExposureEventToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "samplelink:ExposureEventToObservableFeatureAssociation"
    class_name: ClassVar[str] = "exposure event to observable feature association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ExposureEventToObservableFeatureAssociation

    id: Union[str, ExposureEventToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ExposureEvent] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureEventToObservableFeatureAssociationId):
            self.id = ExposureEventToObservableFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ExposureEvent):
            self.subject = ExposureEvent(**as_dict(self.subject))

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**as_dict(self.architectural_style_qualifier))

        super().__post_init__(**kwargs)


@dataclass
class ErrorToObservableFeatureAssociation(Association):
    """
    An association between a error and a observable feature in which the observable feature is associated with the
    error in some way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ErrorToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "samplelink:ErrorToObservableFeatureAssociation"
    class_name: ClassVar[str] = "error to observable feature association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ErrorToObservableFeatureAssociation

    id: Union[str, ErrorToObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ErrorToObservableFeatureAssociationId):
            self.id = ErrorToObservableFeatureAssociationId(self.id)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**as_dict(self.architectural_style_qualifier))

        super().__post_init__(**kwargs)


@dataclass
class CaseToObservableFeatureAssociation(Association):
    """
    An association between a case (e.g. individual patient) and a observable feature in which the individual has or
    has had the observability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.CaseToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "samplelink:CaseToObservableFeatureAssociation"
    class_name: ClassVar[str] = "case to observable feature association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.CaseToObservableFeatureAssociation

    id: Union[str, CaseToObservableFeatureAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CaseToObservableFeatureAssociationId):
            self.id = CaseToObservableFeatureAssociationId(self.id)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**as_dict(self.architectural_style_qualifier))

        super().__post_init__(**kwargs)


@dataclass
class BehaviorToBehavioralFeatureAssociation(Association):
    """
    An association between an aggregate behavior and a behavioral feature manifested by the individual exhibited or
    has exhibited the behavior.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.BehaviorToBehavioralFeatureAssociation
    class_class_curie: ClassVar[str] = "samplelink:BehaviorToBehavioralFeatureAssociation"
    class_name: ClassVar[str] = "behavior to behavioral feature association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.BehaviorToBehavioralFeatureAssociation

    id: Union[str, BehaviorToBehavioralFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, BehaviorId] = None
    object: Union[str, BehavioralFeatureId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehaviorToBehavioralFeatureAssociationId):
            self.id = BehaviorToBehavioralFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, BehaviorId):
            self.subject = BehaviorId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BehavioralFeatureId):
            self.object = BehavioralFeatureId(self.object)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**as_dict(self.architectural_style_qualifier))

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceToEntityAssociationMixin"
    class_name: ClassVar[str] = "componentservice to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToEntityAssociationMixin

    subject: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**as_dict(self.subject))

        super().__post_init__(**kwargs)


@dataclass
class VariantToEntityAssociationMixin(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.VariantToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:VariantToEntityAssociationMixin"
    class_name: ClassVar[str] = "variant to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.VariantToEntityAssociationMixin

    subject: Union[str, SequenceVariantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToObservableFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceToObservableFeatureAssociation"
    class_name: ClassVar[str] = "componentservice to observable feature association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToObservableFeatureAssociation

    id: Union[str, ComponentserviceToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceToObservableFeatureAssociationId):
            self.id = ComponentserviceToObservableFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**as_dict(self.subject))

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**as_dict(self.architectural_style_qualifier))

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToErrorAssociation
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceToErrorAssociation"
    class_name: ClassVar[str] = "componentservice to error association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToErrorAssociation

    id: Union[str, ComponentserviceToErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceToErrorAssociationId):
            self.id = ComponentserviceToErrorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**as_dict(self.subject))

        super().__post_init__(**kwargs)


@dataclass
class VariantToComponentserviceAssociation(Association):
    """
    An association between a variant and a componentservice, where the variant has a componentservice association with
    the componentservice (i.e. is in linkage disequilibrium)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.VariantToComponentserviceAssociation
    class_class_curie: ClassVar[str] = "samplelink:VariantToComponentserviceAssociation"
    class_name: ClassVar[str] = "variant to componentservice association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.VariantToComponentserviceAssociation

    id: Union[str, VariantToComponentserviceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, Componentservice] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantToComponentserviceAssociationId):
            self.id = VariantToComponentserviceAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, Componentservice):
            self.object = Componentservice(**as_dict(self.object))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class VariantToComponentserviceAvailabilityAssociation(VariantToComponentserviceAssociation):
    """
    An association between a variant and availability of a componentservice (i.e. e-QTL)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.VariantToComponentserviceAvailabilityAssociation
    class_class_curie: ClassVar[str] = "samplelink:VariantToComponentserviceAvailabilityAssociation"
    class_name: ClassVar[str] = "variant to componentservice availability association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.VariantToComponentserviceAvailabilityAssociation

    id: Union[str, VariantToComponentserviceAvailabilityAssociationId] = None
    subject: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    object: Union[dict, Componentservice] = None
    predicate: Union[str, PredicateType] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None
    availability_site: Optional[Union[str, DeploymentEntityId]] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    observable_state: Optional[Union[str, ErrorOrObservableFeatureId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantToComponentserviceAvailabilityAssociationId):
            self.id = VariantToComponentserviceAvailabilityAssociationId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        if self.availability_site is not None and not isinstance(self.availability_site, DeploymentEntityId):
            self.availability_site = DeploymentEntityId(self.availability_site)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.observable_state is not None and not isinstance(self.observable_state, ErrorOrObservableFeatureId):
            self.observable_state = ErrorOrObservableFeatureId(self.observable_state)

        super().__post_init__(**kwargs)


@dataclass
class VariantToPopulationAssociation(Association):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.VariantToPopulationAssociation
    class_class_curie: ClassVar[str] = "samplelink:VariantToPopulationAssociation"
    class_name: ClassVar[str] = "variant to population association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.VariantToPopulationAssociation

    id: Union[str, VariantToPopulationAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, PopulationOfIndividualSystemsId] = None
    has_quotient: Optional[float] = None
    has_count: Optional[int] = None
    has_total: Optional[int] = None
    has_percentage: Optional[float] = None
    frequency_qualifier: Optional[Union[dict, FrequencyValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantToPopulationAssociationId):
            self.id = VariantToPopulationAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PopulationOfIndividualSystemsId):
            self.object = PopulationOfIndividualSystemsId(self.object)

        if self.has_quotient is not None and not isinstance(self.has_quotient, float):
            self.has_quotient = float(self.has_quotient)

        if self.has_count is not None and not isinstance(self.has_count, int):
            self.has_count = int(self.has_count)

        if self.has_total is not None and not isinstance(self.has_total, int):
            self.has_total = int(self.has_total)

        if self.has_percentage is not None and not isinstance(self.has_percentage, float):
            self.has_percentage = float(self.has_percentage)

        if self.frequency_qualifier is not None and not isinstance(self.frequency_qualifier, FrequencyValue):
            self.frequency_qualifier = FrequencyValue(**as_dict(self.frequency_qualifier))

        super().__post_init__(**kwargs)


@dataclass
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.PopulationToPopulationAssociation
    class_class_curie: ClassVar[str] = "samplelink:PopulationToPopulationAssociation"
    class_name: ClassVar[str] = "population to population association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.PopulationToPopulationAssociation

    id: Union[str, PopulationToPopulationAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, PopulationOfIndividualSystemsId] = None
    object: Union[str, PopulationOfIndividualSystemsId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PopulationToPopulationAssociationId):
            self.id = PopulationToPopulationAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, PopulationOfIndividualSystemsId):
            self.subject = PopulationOfIndividualSystemsId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, PopulationOfIndividualSystemsId):
            self.object = PopulationOfIndividualSystemsId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class VariantToObservableFeatureAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.VariantToObservableFeatureAssociation
    class_class_curie: ClassVar[str] = "samplelink:VariantToObservableFeatureAssociation"
    class_name: ClassVar[str] = "variant to observable feature association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.VariantToObservableFeatureAssociation

    id: Union[str, VariantToObservableFeatureAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SequenceVariantId] = None
    architectural_style_qualifier: Optional[Union[dict, ComputationalArchitecturalStyle]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantToObservableFeatureAssociationId):
            self.id = VariantToObservableFeatureAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.architectural_style_qualifier is not None and not isinstance(self.architectural_style_qualifier, ComputationalArchitecturalStyle):
            self.architectural_style_qualifier = ComputationalArchitecturalStyle(**as_dict(self.architectural_style_qualifier))

        super().__post_init__(**kwargs)


@dataclass
class VariantToErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.VariantToErrorAssociation
    class_class_curie: ClassVar[str] = "samplelink:VariantToErrorAssociation"
    class_name: ClassVar[str] = "variant to error association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.VariantToErrorAssociation

    id: Union[str, VariantToErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantToErrorAssociationId):
            self.id = VariantToErrorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeToErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToErrorAssociation
    class_class_curie: ClassVar[str] = "samplelink:ServiceunittypeToErrorAssociation"
    class_name: ClassVar[str] = "serviceunittype to error association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeToErrorAssociation

    id: Union[str, ServiceunittypeToErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceunittypeToErrorAssociationId):
            self.id = ServiceunittypeToErrorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ModelToErrorAssociationMixin(YAMLRoot):
    """
    This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in
    that it recapitulates some features of the error in a way that is useful for studying the error outside a patient
    carrying the error
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ModelToErrorAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:ModelToErrorAssociationMixin"
    class_name: ClassVar[str] = "model to error association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ModelToErrorAssociationMixin

    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceAsAModelOfErrorAssociation(ComponentserviceToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "componentservice as a model of error association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceAsAModelOfErrorAssociation

    id: Union[str, ComponentserviceAsAModelOfErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceAsAModelOfErrorAssociationId):
            self.id = ComponentserviceAsAModelOfErrorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**as_dict(self.subject))

        super().__post_init__(**kwargs)


@dataclass
class VariantAsAModelOfErrorAssociation(VariantToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.VariantAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "samplelink:VariantAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "variant as a model of error association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.VariantAsAModelOfErrorAssociation

    id: Union[str, VariantAsAModelOfErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, SequenceVariantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariantAsAModelOfErrorAssociationId):
            self.id = VariantAsAModelOfErrorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ServiceunittypeAsAModelOfErrorAssociation(ServiceunittypeToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "samplelink:ServiceunittypeAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "serviceunittype as a model of error association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ServiceunittypeAsAModelOfErrorAssociation

    id: Union[str, ServiceunittypeAsAModelOfErrorAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    subject: Union[str, ServiceunittypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceunittypeAsAModelOfErrorAssociationId):
            self.id = ServiceunittypeAsAModelOfErrorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ServiceunittypeId):
            self.subject = ServiceunittypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentTypeAsAModelOfErrorAssociation(ComponentTypeToErrorOrObservableFeatureAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentTypeAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "samplelink:ComponentTypeAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "component type as a model of error association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentTypeAsAModelOfErrorAssociation

    id: Union[str, ComponentTypeAsAModelOfErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ComponentTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentTypeAsAModelOfErrorAssociationId):
            self.id = ComponentTypeAsAModelOfErrorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentTypeId):
            self.subject = ComponentTypeId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class SystemicEntityAsAModelOfErrorAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SystemicEntityAsAModelOfErrorAssociation
    class_class_curie: ClassVar[str] = "samplelink:SystemicEntityAsAModelOfErrorAssociation"
    class_name: ClassVar[str] = "systemic entity as a model of error association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SystemicEntityAsAModelOfErrorAssociation

    id: Union[str, SystemicEntityAsAModelOfErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SystemicEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemicEntityAsAModelOfErrorAssociationId):
            self.id = SystemicEntityAsAModelOfErrorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SystemicEntityId):
            self.subject = SystemicEntityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceHasVariantThatContributesToErrorAssociation(ComponentserviceToErrorAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceHasVariantThatContributesToErrorAssociation
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceHasVariantThatContributesToErrorAssociation"
    class_name: ClassVar[str] = "componentservice has variant that contributes to error association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceHasVariantThatContributesToErrorAssociation

    id: Union[str, ComponentserviceHasVariantThatContributesToErrorAssociationId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    sequence_variant_qualifier: Optional[Union[str, SequenceVariantId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceHasVariantThatContributesToErrorAssociationId):
            self.id = ComponentserviceHasVariantThatContributesToErrorAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**as_dict(self.subject))

        if self.sequence_variant_qualifier is not None and not isinstance(self.sequence_variant_qualifier, SequenceVariantId):
            self.sequence_variant_qualifier = SequenceVariantId(self.sequence_variant_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToAvailabilitySiteAssociation(Association):
    """
    An association between a componentservice and an availability site, possibly qualified by stage/timing info.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToAvailabilitySiteAssociation
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceToAvailabilitySiteAssociation"
    class_name: ClassVar[str] = "componentservice to availability site association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToAvailabilitySiteAssociation

    id: Union[str, ComponentserviceToAvailabilitySiteAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[str, DeploymentEntityId] = None
    predicate: Union[str, PredicateType] = None
    stage_qualifier: Optional[Union[str, LifecycleStageId]] = None
    quantifier_qualifier: Optional[Union[str, OntologyClassId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceToAvailabilitySiteAssociationId):
            self.id = ComponentserviceToAvailabilitySiteAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.stage_qualifier is not None and not isinstance(self.stage_qualifier, LifecycleStageId):
            self.stage_qualifier = LifecycleStageId(self.stage_qualifier)

        if self.quantifier_qualifier is not None and not isinstance(self.quantifier_qualifier, OntologyClassId):
            self.quantifier_qualifier = OntologyClassId(self.quantifier_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class SequenceVariantModulatesRepairingAssociation(Association):
    """
    An association between a sequence variant and a repairing or health intervention. The repairing object itself
    encompasses both the error and the administrative operational used.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SequenceVariantModulatesRepairingAssociation
    class_class_curie: ClassVar[str] = "samplelink:SequenceVariantModulatesRepairingAssociation"
    class_name: ClassVar[str] = "sequence variant modulates repairing association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SequenceVariantModulatesRepairingAssociation

    id: Union[str, SequenceVariantModulatesRepairingAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, SequenceVariantId] = None
    object: Union[str, RepairingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, RepairingId):
            self.object = RepairingId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class FunctionalAssociation(Association):
    """
    An association between a macrooperational machine mixin (componentservice, servicetype or complex of servicetypes)
    and either a operational activity, a computational process or a component location in which a function is
    executed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.FunctionalAssociation
    class_class_curie: ClassVar[str] = "samplelink:FunctionalAssociation"
    class_name: ClassVar[str] = "functional association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.FunctionalAssociation

    id: Union[str, FunctionalAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, ComponentserviceOntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionalAssociationId):
            self.id = FunctionalAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, MacrooperationalMachineMixin):
            self.subject = MacrooperationalMachineMixin(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComponentserviceOntologyClassId):
            self.object = ComponentserviceOntologyClassId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToEntityAssociationMixin(YAMLRoot):
    """
    an association which has a macrooperational machine mixin mixin as a subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalMachineMixinToEntityAssociationMixin
    class_class_curie: ClassVar[str] = "samplelink:MacrooperationalMachineMixinToEntityAssociationMixin"
    class_name: ClassVar[str] = "macrooperational machine mixin to entity association mixin"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalMachineMixinToEntityAssociationMixin

    subject: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToOperationalActivityAssociation(FunctionalAssociation):
    """
    A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a
    operational activity (as represented in the GO operational function branch), where the entity carries out the
    activity, or contributes to its execution
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalMachineMixinToOperationalActivityAssociation
    class_class_curie: ClassVar[str] = "samplelink:MacrooperationalMachineMixinToOperationalActivityAssociation"
    class_name: ClassVar[str] = "macrooperational machine mixin to operational activity association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalMachineMixinToOperationalActivityAssociation

    id: Union[str, MacrooperationalMachineMixinToOperationalActivityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, OperationalActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MacrooperationalMachineMixinToOperationalActivityAssociationId):
            self.id = MacrooperationalMachineMixinToOperationalActivityAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, OperationalActivityId):
            self.object = OperationalActivityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToComputationalProcessAssociation(FunctionalAssociation):
    """
    A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a
    computational process or pathway (as represented in the GO computational process branch), where the entity carries
    out some part of the process, regulates it, or acts upstream of it
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalMachineMixinToComputationalProcessAssociation
    class_class_curie: ClassVar[str] = "samplelink:MacrooperationalMachineMixinToComputationalProcessAssociation"
    class_name: ClassVar[str] = "macrooperational machine mixin to computational process association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalMachineMixinToComputationalProcessAssociation

    id: Union[str, MacrooperationalMachineMixinToComputationalProcessAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, ComputationalProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MacrooperationalMachineMixinToComputationalProcessAssociationId):
            self.id = MacrooperationalMachineMixinToComputationalProcessAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComputationalProcessId):
            self.object = ComputationalProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class MacrooperationalMachineMixinToComponentAssociation(FunctionalAssociation):
    """
    A functional association between a macrooperational machine mixin (componentservice, servicetype or complex) and a
    component (as represented in the GO component branch), where the entity carries out its function in the component
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalMachineMixinToComponentAssociation
    class_class_curie: ClassVar[str] = "samplelink:MacrooperationalMachineMixinToComponentAssociation"
    class_name: ClassVar[str] = "macrooperational machine mixin to component association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.MacrooperationalMachineMixinToComponentAssociation

    id: Union[str, MacrooperationalMachineMixinToComponentAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, MacrooperationalMachineMixin] = None
    object: Union[str, ComponentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MacrooperationalMachineMixinToComponentAssociationId):
            self.id = MacrooperationalMachineMixinToComponentAssociationId(self.id)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComponentId):
            self.object = ComponentId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToGoTermAssociation(FunctionalAssociation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToGoTermAssociation
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceToGoTermAssociation"
    class_name: ClassVar[str] = "componentservice to go term association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToGoTermAssociation

    id: Union[str, ComponentserviceToGoTermAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, OperationalEntityId] = None
    object: Union[str, ComponentserviceOntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceToGoTermAssociationId):
            self.id = ComponentserviceToGoTermAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, OperationalEntityId):
            self.subject = OperationalEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComponentserviceOntologyClassId):
            self.object = ComponentserviceOntologyClassId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class SequenceAssociation(Association):
    """
    An association between a sequence feature and a workload entity it is localized to.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SequenceAssociation
    class_class_curie: ClassVar[str] = "samplelink:SequenceAssociation"
    class_name: ClassVar[str] = "sequence association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SequenceAssociation

    id: Union[str, SequenceAssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceAssociationId):
            self.id = SequenceAssociationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceSequenceLocalization(SequenceAssociation):
    """
    A relationship between a sequence feature and a workload entity it is localized to. The reference entity may be a
    container, componentservice or information entity such as a namespace.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceSequenceLocalization
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceSequenceLocalization"
    class_name: ClassVar[str] = "componentservice sequence localization"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceSequenceLocalization

    id: Union[str, ComponentserviceSequenceLocalizationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, WorkloadEntityId] = None
    object: Union[str, WorkloadEntityId] = None
    predicate: Union[str, PredicateType] = None
    start_interbase_coordinate: Optional[int] = None
    end_interbase_coordinate: Optional[int] = None
    workload_build: Optional[str] = None
    strand: Optional[str] = None
    phase: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceSequenceLocalizationId):
            self.id = ComponentserviceSequenceLocalizationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, WorkloadEntityId):
            self.subject = WorkloadEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, WorkloadEntityId):
            self.object = WorkloadEntityId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self.start_interbase_coordinate is not None and not isinstance(self.start_interbase_coordinate, int):
            self.start_interbase_coordinate = int(self.start_interbase_coordinate)

        if self.end_interbase_coordinate is not None and not isinstance(self.end_interbase_coordinate, int):
            self.end_interbase_coordinate = int(self.end_interbase_coordinate)

        if self.workload_build is not None and not isinstance(self.workload_build, str):
            self.workload_build = str(self.workload_build)

        if self.strand is not None and not isinstance(self.strand, str):
            self.strand = str(self.strand)

        if self.phase is not None and not isinstance(self.phase, str):
            self.phase = str(self.phase)

        super().__post_init__(**kwargs)


@dataclass
class SequenceFeatureRelationship(Association):
    """
    For example, a particular daemon is part of a particular componentserviceinstance or componentservice
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.SequenceFeatureRelationship
    class_class_curie: ClassVar[str] = "samplelink:SequenceFeatureRelationship"
    class_name: ClassVar[str] = "sequence feature relationship"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.SequenceFeatureRelationship

    id: Union[str, SequenceFeatureRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, WorkloadEntityId] = None
    object: Union[str, WorkloadEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceFeatureRelationshipId):
            self.id = SequenceFeatureRelationshipId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, WorkloadEntityId):
            self.subject = WorkloadEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, WorkloadEntityId):
            self.object = WorkloadEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceinstanceToComponentserviceRelationship(SequenceFeatureRelationship):
    """
    A componentservice is a collection of componentserviceinstances
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceinstanceToComponentserviceRelationship
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceinstanceToComponentserviceRelationship"
    class_name: ClassVar[str] = "componentserviceinstance to componentservice relationship"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceinstanceToComponentserviceRelationship

    id: Union[str, ComponentserviceinstanceToComponentserviceRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, ComponentserviceinstanceId] = None
    object: Union[dict, Componentservice] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceinstanceToComponentserviceRelationshipId):
            self.id = ComponentserviceinstanceToComponentserviceRelationshipId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentserviceinstanceId):
            self.subject = ComponentserviceinstanceId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, Componentservice):
            self.object = Componentservice(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceToServicetypeRelationship(SequenceFeatureRelationship):
    """
    A componentservice is transcribed and potentially translated to a servicetype
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToServicetypeRelationship
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceToServicetypeRelationship"
    class_name: ClassVar[str] = "componentservice to servicetype relationship"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceToServicetypeRelationship

    id: Union[str, ComponentserviceToServicetypeRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[dict, Componentservice] = None
    object: Union[dict, ServicetypeMixin] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceToServicetypeRelationshipId):
            self.id = ComponentserviceToServicetypeRelationshipId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, Componentservice):
            self.subject = Componentservice(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ServicetypeMixin):
            self.object = ServicetypeMixin(**as_dict(self.object))

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class DaemonToComponentserviceinstanceRelationship(SequenceFeatureRelationship):
    """
    A componentserviceinstance is formed from multiple daemons
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.DaemonToComponentserviceinstanceRelationship
    class_class_curie: ClassVar[str] = "samplelink:DaemonToComponentserviceinstanceRelationship"
    class_name: ClassVar[str] = "daemon to componentserviceinstance relationship"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.DaemonToComponentserviceinstanceRelationship

    id: Union[str, DaemonToComponentserviceinstanceRelationshipId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DaemonId] = None
    object: Union[str, ComponentserviceinstanceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DaemonToComponentserviceinstanceRelationshipId):
            self.id = DaemonToComponentserviceinstanceRelationshipId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, DaemonId):
            self.subject = DaemonId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComponentserviceinstanceId):
            self.object = ComponentserviceinstanceId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ComponentserviceRegulatoryRelationship(Association):
    """
    A regulatory relationship between two componentservices
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceRegulatoryRelationship
    class_class_curie: ClassVar[str] = "samplelink:ComponentserviceRegulatoryRelationship"
    class_name: ClassVar[str] = "componentservice regulatory relationship"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.ComponentserviceRegulatoryRelationship

    id: Union[str, ComponentserviceRegulatoryRelationshipId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    predicate: Union[str, PredicateType] = None
    subject: Union[dict, ComponentserviceOrServicetype] = None
    object: Union[dict, ComponentserviceOrServicetype] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentserviceRegulatoryRelationshipId):
            self.id = ComponentserviceRegulatoryRelationshipId(self.id)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, ComponentserviceOrServicetype):
            self.subject = ComponentserviceOrServicetype(**as_dict(self.subject))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ComponentserviceOrServicetype):
            self.object = ComponentserviceOrServicetype(**as_dict(self.object))

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntityToDeploymentEntityAssociation(Association):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.DeploymentEntityToDeploymentEntityAssociation
    class_class_curie: ClassVar[str] = "samplelink:DeploymentEntityToDeploymentEntityAssociation"
    class_name: ClassVar[str] = "deployment entity to deployment entity association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.DeploymentEntityToDeploymentEntityAssociation

    id: Union[str, DeploymentEntityToDeploymentEntityAssociationId] = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DeploymentEntityId] = None
    object: Union[str, DeploymentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeploymentEntityToDeploymentEntityAssociationId):
            self.id = DeploymentEntityToDeploymentEntityAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, DeploymentEntityId):
            self.subject = DeploymentEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntityToDeploymentEntityPartOfAssociation(DeploymentEntityToDeploymentEntityAssociation):
    """
    A relationship between two deployment entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between components and componentservices, between
    componentservice and servicegroup/replicasets, servicegroup/replicasets and whole systems
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.DeploymentEntityToDeploymentEntityPartOfAssociation
    class_class_curie: ClassVar[str] = "samplelink:DeploymentEntityToDeploymentEntityPartOfAssociation"
    class_name: ClassVar[str] = "deployment entity to deployment entity part of association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.DeploymentEntityToDeploymentEntityPartOfAssociation

    id: Union[str, DeploymentEntityToDeploymentEntityPartOfAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DeploymentEntityId] = None
    object: Union[str, DeploymentEntityId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeploymentEntityToDeploymentEntityPartOfAssociationId):
            self.id = DeploymentEntityToDeploymentEntityPartOfAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, DeploymentEntityId):
            self.subject = DeploymentEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class DeploymentEntityToDeploymentEntityOntogenicAssociation(DeploymentEntityToDeploymentEntityAssociation):
    """
    A relationship between two deployment entities where the relationship is ontogenic, i.e. the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLELINK.DeploymentEntityToDeploymentEntityOntogenicAssociation
    class_class_curie: ClassVar[str] = "samplelink:DeploymentEntityToDeploymentEntityOntogenicAssociation"
    class_name: ClassVar[str] = "deployment entity to deployment entity ontogenic association"
    class_model_uri: ClassVar[URIRef] = SAMPLELINK.DeploymentEntityToDeploymentEntityOntogenicAssociation

    id: Union[str, DeploymentEntityToDeploymentEntityOntogenicAssociationId] = None
    relation: Union[str, URIorCURIE] = None
    category: Union[Union[str, AssociationId], List[Union[str, AssociationId]]] = None
    subject: Union[str, DeploymentEntityId] = None
    object: Union[str, DeploymentEntityId] = None
    predicate: Union[str, PredicateType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeploymentEntityToDeploymentEntityOntogenicAssociationId):
            self.id = DeploymentEntityToDeploymentEntityOntogenicAssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, DeploymentEntityId):
            self.subject = DeploymentEntityId(self.subject)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, DeploymentEntityId):
            self.object = DeploymentEntityId(self.object)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.has_attribute = Slot(uri=SAMPLELINK.has_attribute, name="has attribute", curie=SAMPLELINK.curie('has_attribute'),
                   model_uri=SAMPLELINK.has_attribute, domain=None, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.has_attribute_type = Slot(uri=SAMPLELINK.has_attribute_type, name="has attribute type", curie=SAMPLELINK.curie('has_attribute_type'),
                   model_uri=SAMPLELINK.has_attribute_type, domain=AttributeType, range=Union[str, OntologyClassId])

slots.has_qualitative_value = Slot(uri=SAMPLELINK.has_qualitative_value, name="has qualitative value", curie=SAMPLELINK.curie('has_qualitative_value'),
                   model_uri=SAMPLELINK.has_qualitative_value, domain=Attribute, range=Optional[Union[str, NamedThingId]])

slots.has_quantitative_value = Slot(uri=SAMPLELINK.has_quantitative_value, name="has quantitative value", curie=SAMPLELINK.curie('has_quantitative_value'),
                   model_uri=SAMPLELINK.has_quantitative_value, domain=Attribute, range=Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]])

slots.has_numeric_value = Slot(uri=SAMPLELINK.has_numeric_value, name="has numeric value", curie=SAMPLELINK.curie('has_numeric_value'),
                   model_uri=SAMPLELINK.has_numeric_value, domain=QuantityValue, range=Optional[float])

slots.has_unit = Slot(uri=SAMPLELINK.has_unit, name="has unit", curie=SAMPLELINK.curie('has_unit'),
                   model_uri=SAMPLELINK.has_unit, domain=QuantityValue, range=Optional[Union[str, Unit]])

slots.node_property = Slot(uri=SAMPLELINK.node_property, name="node property", curie=SAMPLELINK.curie('node_property'),
                   model_uri=SAMPLELINK.node_property, domain=NamedThing, range=Optional[str])

slots.id = Slot(uri=SAMPLELINK.id, name="id", curie=SAMPLELINK.curie('id'),
                   model_uri=SAMPLELINK.id, domain=None, range=URIRef)

slots.iri = Slot(uri=SAMPLELINK.iri, name="iri", curie=SAMPLELINK.curie('iri'),
                   model_uri=SAMPLELINK.iri, domain=None, range=Optional[Union[str, IriType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=SAMPLELINK.type, domain=None, range=Optional[str])

slots.category = Slot(uri=SAMPLELINK.category, name="category", curie=SAMPLELINK.curie('category'),
                   model_uri=SAMPLELINK.category, domain=Entity, range=Union[Union[str, CategoryType], List[Union[str, CategoryType]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=SAMPLELINK.name, domain=None, range=Optional[Union[str, LabelType]])

slots.source = Slot(uri=SAMPLELINK.source, name="source", curie=SAMPLELINK.curie('source'),
                   model_uri=SAMPLELINK.source, domain=None, range=Optional[Union[str, LabelType]])

slots.filler = Slot(uri=SAMPLELINK.filler, name="filler", curie=SAMPLELINK.curie('filler'),
                   model_uri=SAMPLELINK.filler, domain=NamedThing, range=Optional[Union[str, NamedThingId]])

slots.symbol = Slot(uri=SAMPLELINK.symbol, name="symbol", curie=SAMPLELINK.curie('symbol'),
                   model_uri=SAMPLELINK.symbol, domain=NamedThing, range=Optional[str])

slots.synonym = Slot(uri=SAMPLELINK.synonym, name="synonym", curie=SAMPLELINK.curie('synonym'),
                   model_uri=SAMPLELINK.synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.has_topic = Slot(uri=SAMPLELINK.has_topic, name="has topic", curie=SAMPLELINK.curie('has_topic'),
                   model_uri=SAMPLELINK.has_topic, domain=NamedThing, range=Optional[Union[str, OntologyClassId]])

slots.xref = Slot(uri=SAMPLELINK.xref, name="xref", curie=SAMPLELINK.curie('xref'),
                   model_uri=SAMPLELINK.xref, domain=NamedThing, range=Optional[Union[Union[str, IriType], List[Union[str, IriType]]]])

slots.full_name = Slot(uri=SAMPLELINK.full_name, name="full name", curie=SAMPLELINK.curie('full_name'),
                   model_uri=SAMPLELINK.full_name, domain=NamedThing, range=Optional[Union[str, LabelType]])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=SAMPLELINK.description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.systematic_synonym = Slot(uri=SIO['000122'], name="systematic synonym", curie=SIO.curie('000122'),
                   model_uri=SAMPLELINK.systematic_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.affiliation = Slot(uri=SAMPLELINK.affiliation, name="affiliation", curie=SAMPLELINK.curie('affiliation'),
                   model_uri=SAMPLELINK.affiliation, domain=Agent, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.address = Slot(uri=SAMPLELINK.address, name="address", curie=SAMPLELINK.curie('address'),
                   model_uri=SAMPLELINK.address, domain=NamedThing, range=Optional[str])

slots.latitude = Slot(uri=SAMPLELINK.latitude, name="latitude", curie=SAMPLELINK.curie('latitude'),
                   model_uri=SAMPLELINK.latitude, domain=NamedThing, range=Optional[float])

slots.longitude = Slot(uri=SAMPLELINK.longitude, name="longitude", curie=SAMPLELINK.curie('longitude'),
                   model_uri=SAMPLELINK.longitude, domain=NamedThing, range=Optional[float])

slots.timepoint = Slot(uri=SAMPLELINK.timepoint, name="timepoint", curie=SAMPLELINK.curie('timepoint'),
                   model_uri=SAMPLELINK.timepoint, domain=NamedThing, range=Optional[Union[str, TimeType]])

slots.creation_date = Slot(uri=SAMPLELINK.creation_date, name="creation date", curie=SAMPLELINK.curie('creation_date'),
                   model_uri=SAMPLELINK.creation_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.update_date = Slot(uri=SAMPLELINK.update_date, name="update date", curie=SAMPLELINK.curie('update_date'),
                   model_uri=SAMPLELINK.update_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.aggregate_statistic = Slot(uri=SAMPLELINK.aggregate_statistic, name="aggregate statistic", curie=SAMPLELINK.curie('aggregate_statistic'),
                   model_uri=SAMPLELINK.aggregate_statistic, domain=NamedThing, range=Optional[str])

slots.has_count = Slot(uri=SAMPLELINK.has_count, name="has count", curie=SAMPLELINK.curie('has_count'),
                   model_uri=SAMPLELINK.has_count, domain=NamedThing, range=Optional[int])

slots.has_total = Slot(uri=SAMPLELINK.has_total, name="has total", curie=SAMPLELINK.curie('has_total'),
                   model_uri=SAMPLELINK.has_total, domain=NamedThing, range=Optional[int])

slots.has_quotient = Slot(uri=SAMPLELINK.has_quotient, name="has quotient", curie=SAMPLELINK.curie('has_quotient'),
                   model_uri=SAMPLELINK.has_quotient, domain=NamedThing, range=Optional[float])

slots.has_percentage = Slot(uri=SAMPLELINK.has_percentage, name="has percentage", curie=SAMPLELINK.curie('has_percentage'),
                   model_uri=SAMPLELINK.has_percentage, domain=NamedThing, range=Optional[float])

slots.has_dataset = Slot(uri=DCT.source, name="has dataset", curie=DCT.curie('source'),
                   model_uri=SAMPLELINK.has_dataset, domain=DatasetVersion, range=Optional[Union[str, DatasetId]])

slots.source_web_page = Slot(uri=SAMPLELINK.source_web_page, name="source web page", curie=SAMPLELINK.curie('source_web_page'),
                   model_uri=SAMPLELINK.source_web_page, domain=None, range=Optional[str])

slots.source_logo = Slot(uri=SCHEMA.logo, name="source logo", curie=SCHEMA.curie('logo'),
                   model_uri=SAMPLELINK.source_logo, domain=None, range=Optional[str])

slots.retrieved_on = Slot(uri=SAMPLELINK.retrieved_on, name="retrieved on", curie=SAMPLELINK.curie('retrieved_on'),
                   model_uri=SAMPLELINK.retrieved_on, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.version_of = Slot(uri=SAMPLELINK.version_of, name="version of", curie=SAMPLELINK.curie('version_of'),
                   model_uri=SAMPLELINK.version_of, domain=DatasetVersion, range=Optional[Union[str, DatasetId]])

slots.version = Slot(uri=SAMPLELINK.version, name="version", curie=SAMPLELINK.curie('version'),
                   model_uri=SAMPLELINK.version, domain=Dataset, range=Optional[str])

slots.license = Slot(uri=SAMPLELINK.license, name="license", curie=SAMPLELINK.curie('license'),
                   model_uri=SAMPLELINK.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=SAMPLELINK.rights, name="rights", curie=SAMPLELINK.curie('rights'),
                   model_uri=SAMPLELINK.rights, domain=InformationContentEntity, range=Optional[str])

slots.format = Slot(uri=SAMPLELINK.format, name="format", curie=SAMPLELINK.curie('format'),
                   model_uri=SAMPLELINK.format, domain=InformationContentEntity, range=Optional[str])

slots.created_with = Slot(uri=SAMPLELINK.created_with, name="created_with", curie=SAMPLELINK.curie('created_with'),
                   model_uri=SAMPLELINK.created_with, domain=Dataset, range=Optional[str])

slots.download_url = Slot(uri=DCAT.downloadURL, name="download url", curie=DCAT.curie('downloadURL'),
                   model_uri=SAMPLELINK.download_url, domain=None, range=Optional[str])

slots.dataset_download_url = Slot(uri=DCAT.downloadURL, name="dataset download url", curie=DCAT.curie('downloadURL'),
                   model_uri=SAMPLELINK.dataset_download_url, domain=Dataset, range=Optional[str])

slots.distribution_download_url = Slot(uri=SAMPLELINK.distribution_download_url, name="distribution download url", curie=SAMPLELINK.curie('distribution_download_url'),
                   model_uri=SAMPLELINK.distribution_download_url, domain=DatasetDistribution, range=Optional[str])

slots.ingest_date = Slot(uri=PAV.version, name="ingest date", curie=PAV.curie('version'),
                   model_uri=SAMPLELINK.ingest_date, domain=DatasetVersion, range=Optional[str])

slots.has_distribution = Slot(uri=DCT.distribution, name="has distribution", curie=DCT.curie('distribution'),
                   model_uri=SAMPLELINK.has_distribution, domain=DatasetVersion, range=Optional[Union[str, DatasetDistributionId]])

slots.published_in = Slot(uri=SAMPLELINK.published_in, name="published in", curie=SAMPLELINK.curie('published_in'),
                   model_uri=SAMPLELINK.published_in, domain=Publication, range=Optional[Union[str, URIorCURIE]])

slots.iso_abbreviation = Slot(uri=SAMPLELINK.iso_abbreviation, name="iso abbreviation", curie=SAMPLELINK.curie('iso_abbreviation'),
                   model_uri=SAMPLELINK.iso_abbreviation, domain=Publication, range=Optional[str])

slots.authors = Slot(uri=SAMPLELINK.authors, name="authors", curie=SAMPLELINK.curie('authors'),
                   model_uri=SAMPLELINK.authors, domain=Publication, range=Optional[Union[str, List[str]]])

slots.volume = Slot(uri=SAMPLELINK.volume, name="volume", curie=SAMPLELINK.curie('volume'),
                   model_uri=SAMPLELINK.volume, domain=Publication, range=Optional[str])

slots.chapter = Slot(uri=SAMPLELINK.chapter, name="chapter", curie=SAMPLELINK.curie('chapter'),
                   model_uri=SAMPLELINK.chapter, domain=BookChapter, range=Optional[str])

slots.issue = Slot(uri=SAMPLELINK.issue, name="issue", curie=SAMPLELINK.curie('issue'),
                   model_uri=SAMPLELINK.issue, domain=Publication, range=Optional[str])

slots.pages = Slot(uri=SAMPLELINK.pages, name="pages", curie=SAMPLELINK.curie('pages'),
                   model_uri=SAMPLELINK.pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.summary = Slot(uri=SAMPLELINK.summary, name="summary", curie=SAMPLELINK.curie('summary'),
                   model_uri=SAMPLELINK.summary, domain=Publication, range=Optional[str])

slots.keywords = Slot(uri=SAMPLELINK.keywords, name="keywords", curie=SAMPLELINK.curie('keywords'),
                   model_uri=SAMPLELINK.keywords, domain=Publication, range=Optional[Union[str, List[str]]])

slots.lcsh_terms = Slot(uri=SAMPLELINK.lcsh_terms, name="lcsh terms", curie=SAMPLELINK.curie('lcsh_terms'),
                   model_uri=SAMPLELINK.lcsh_terms, domain=Publication, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.has_computational_sequence = Slot(uri=SAMPLELINK.has_computational_sequence, name="has computational sequence", curie=SAMPLELINK.curie('has_computational_sequence'),
                   model_uri=SAMPLELINK.has_computational_sequence, domain=NamedThing, range=Optional[Union[str, ComputationalSequence]])

slots.has_componentservice_or_servicetype = Slot(uri=SAMPLELINK.has_componentservice_or_servicetype, name="has componentservice or servicetype", curie=SAMPLELINK.curie('has_componentservice_or_servicetype'),
                   model_uri=SAMPLELINK.has_componentservice_or_servicetype, domain=NamedThing, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.has_componentservice = Slot(uri=SAMPLELINK.has_componentservice, name="has componentservice", curie=SAMPLELINK.curie('has_componentservice'),
                   model_uri=SAMPLELINK.has_componentservice, domain=NamedThing, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.has_homogeneity = Slot(uri=SAMPLELINK.has_homogeneity, name="has homogeneity", curie=SAMPLELINK.curie('has_homogeneity'),
                   model_uri=SAMPLELINK.has_homogeneity, domain=WorkloadEntity, range=Optional[Union[dict, "Homogeneity"]])

slots.has_control_plane = Slot(uri=SAMPLELINK.has_control_plane, name="has control plane", curie=SAMPLELINK.curie('has_control_plane'),
                   model_uri=SAMPLELINK.has_control_plane, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.is_controller = Slot(uri=SAMPLELINK.is_controller, name="is controller", curie=SAMPLELINK.curie('is_controller'),
                   model_uri=SAMPLELINK.is_controller, domain=Controller, range=Optional[Union[bool, Bool]])

slots.has_control_actor = Slot(uri=SAMPLELINK.has_control_actor, name="has control actor", curie=SAMPLELINK.curie('has_control_actor'),
                   model_uri=SAMPLELINK.has_control_actor, domain=NamedThing, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.has_administrative_operation = Slot(uri=SAMPLELINK.has_administrative_operation, name="has administrative operation", curie=SAMPLELINK.curie('has_administrative_operation'),
                   model_uri=SAMPLELINK.has_administrative_operation, domain=NamedThing, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]])

slots.has_device = Slot(uri=SAMPLELINK.has_device, name="has device", curie=SAMPLELINK.curie('has_device'),
                   model_uri=SAMPLELINK.has_device, domain=NamedThing, range=Optional[Union[Union[str, DeviceId], List[Union[str, DeviceId]]]])

slots.has_procedure = Slot(uri=SAMPLELINK.has_procedure, name="has procedure", curie=SAMPLELINK.curie('has_procedure'),
                   model_uri=SAMPLELINK.has_procedure, domain=NamedThing, range=Optional[Union[Union[str, ProcedureId], List[Union[str, ProcedureId]]]])

slots.has_gateway = Slot(uri=SAMPLELINK.has_gateway, name="has gateway", curie=SAMPLELINK.curie('has_gateway'),
                   model_uri=SAMPLELINK.has_gateway, domain=None, range=Optional[Union[str, SystemicEntityId]])

slots.has_stressor = Slot(uri=SAMPLELINK.has_stressor, name="has stressor", curie=SAMPLELINK.curie('has_stressor'),
                   model_uri=SAMPLELINK.has_stressor, domain=None, range=Optional[str])

slots.has_route = Slot(uri=SAMPLELINK.has_route, name="has route", curie=SAMPLELINK.curie('has_route'),
                   model_uri=SAMPLELINK.has_route, domain=None, range=Optional[str])

slots.has_population_context = Slot(uri=SAMPLELINK.has_population_context, name="has population context", curie=SAMPLELINK.curie('has_population_context'),
                   model_uri=SAMPLELINK.has_population_context, domain=Association, range=Optional[Union[str, PopulationOfIndividualSystemsId]])

slots.has_temporal_context = Slot(uri=SAMPLELINK.has_temporal_context, name="has temporal context", curie=SAMPLELINK.curie('has_temporal_context'),
                   model_uri=SAMPLELINK.has_temporal_context, domain=Association, range=Optional[Union[str, TimeType]])

slots.related_to = Slot(uri=SAMPLELINK.related_to, name="related to", curie=SAMPLELINK.curie('related_to'),
                   model_uri=SAMPLELINK.related_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.superclass_of = Slot(uri=SAMPLELINK.superclass_of, name="superclass of", curie=SAMPLELINK.curie('superclass_of'),
                   model_uri=SAMPLELINK.superclass_of, domain=OntologyClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.subclass_of = Slot(uri=RDFS.subClassOf, name="subclass of", curie=RDFS.curie('subClassOf'),
                   model_uri=SAMPLELINK.subclass_of, domain=OntologyClass, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.same_as = Slot(uri=SAMPLELINK.same_as, name="same as", curie=SAMPLELINK.curie('same_as'),
                   model_uri=SAMPLELINK.same_as, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.close_match = Slot(uri=SAMPLELINK.close_match, name="close match", curie=SAMPLELINK.curie('close_match'),
                   model_uri=SAMPLELINK.close_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.exact_match = Slot(uri=SAMPLELINK.exact_match, name="exact match", curie=SAMPLELINK.curie('exact_match'),
                   model_uri=SAMPLELINK.exact_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.broad_match = Slot(uri=SAMPLELINK.broad_match, name="broad match", curie=SAMPLELINK.curie('broad_match'),
                   model_uri=SAMPLELINK.broad_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.narrow_match = Slot(uri=SAMPLELINK.narrow_match, name="narrow match", curie=SAMPLELINK.curie('narrow_match'),
                   model_uri=SAMPLELINK.narrow_match, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contributor = Slot(uri=SAMPLELINK.contributor, name="contributor", curie=SAMPLELINK.curie('contributor'),
                   model_uri=SAMPLELINK.contributor, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.provider = Slot(uri=SAMPLELINK.provider, name="provider", curie=SAMPLELINK.curie('provider'),
                   model_uri=SAMPLELINK.provider, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.publisher = Slot(uri=SAMPLELINK.publisher, name="publisher", curie=SAMPLELINK.curie('publisher'),
                   model_uri=SAMPLELINK.publisher, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.editor = Slot(uri=SAMPLELINK.editor, name="editor", curie=SAMPLELINK.curie('editor'),
                   model_uri=SAMPLELINK.editor, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.author = Slot(uri=SAMPLELINK.author, name="author", curie=SAMPLELINK.curie('author'),
                   model_uri=SAMPLELINK.author, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.interacts_with = Slot(uri=SAMPLELINK.interacts_with, name="interacts with", curie=SAMPLELINK.curie('interacts_with'),
                   model_uri=SAMPLELINK.interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.cyber_interaction_with = Slot(uri=SAMPLELINK.cyber_interaction_with, name="cyber interaction with", curie=SAMPLELINK.curie('cyber_interaction_with'),
                   model_uri=SAMPLELINK.cyber_interaction_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.operationally_interacts_with = Slot(uri=SAMPLELINK.operationally_interacts_with, name="operationally interacts with", curie=SAMPLELINK.curie('operationally_interacts_with'),
                   model_uri=SAMPLELINK.operationally_interacts_with, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.componentservice_interacts_with = Slot(uri=SAMPLELINK.componentservice_interacts_with, name="componentservice interacts with", curie=SAMPLELINK.curie('componentservice_interacts_with'),
                   model_uri=SAMPLELINK.componentservice_interacts_with, domain=Componentservice, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.affects = Slot(uri=SAMPLELINK.affects, name="affects", curie=SAMPLELINK.curie('affects'),
                   model_uri=SAMPLELINK.affects, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affected_by = Slot(uri=SAMPLELINK.affected_by, name="affected by", curie=SAMPLELINK.curie('affected_by'),
                   model_uri=SAMPLELINK.affected_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.control_role_mixin = Slot(uri=SAMPLELINK.control_role_mixin, name="control role mixin", curie=SAMPLELINK.curie('control_role_mixin'),
                   model_uri=SAMPLELINK.control_role_mixin, domain=None, range=Optional[str])

slots.computational_role_mixin = Slot(uri=SAMPLELINK.computational_role_mixin, name="computational role mixin", curie=SAMPLELINK.curie('computational_role_mixin'),
                   model_uri=SAMPLELINK.computational_role_mixin, domain=None, range=Optional[str])

slots.affects_abundance_of = Slot(uri=SAMPLELINK.affects_abundance_of, name="affects abundance of", curie=SAMPLELINK.curie('affects_abundance_of'),
                   model_uri=SAMPLELINK.affects_abundance_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_abundance_of = Slot(uri=SAMPLELINK.increases_abundance_of, name="increases abundance of", curie=SAMPLELINK.curie('increases_abundance_of'),
                   model_uri=SAMPLELINK.increases_abundance_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_abundance_of = Slot(uri=SAMPLELINK.decreases_abundance_of, name="decreases abundance of", curie=SAMPLELINK.curie('decreases_abundance_of'),
                   model_uri=SAMPLELINK.decreases_abundance_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_activity_of = Slot(uri=SAMPLELINK.affects_activity_of, name="affects activity of", curie=SAMPLELINK.curie('affects_activity_of'),
                   model_uri=SAMPLELINK.affects_activity_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_activity_of = Slot(uri=SAMPLELINK.increases_activity_of, name="increases activity of", curie=SAMPLELINK.curie('increases_activity_of'),
                   model_uri=SAMPLELINK.increases_activity_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_activity_of = Slot(uri=SAMPLELINK.decreases_activity_of, name="decreases activity of", curie=SAMPLELINK.curie('decreases_activity_of'),
                   model_uri=SAMPLELINK.decreases_activity_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_availability_of = Slot(uri=SAMPLELINK.affects_availability_of, name="affects availability of", curie=SAMPLELINK.curie('affects_availability_of'),
                   model_uri=SAMPLELINK.affects_availability_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.increases_availability_of = Slot(uri=SAMPLELINK.increases_availability_of, name="increases availability of", curie=SAMPLELINK.curie('increases_availability_of'),
                   model_uri=SAMPLELINK.increases_availability_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.decreases_availability_of = Slot(uri=SAMPLELINK.decreases_availability_of, name="decreases availability of", curie=SAMPLELINK.curie('decreases_availability_of'),
                   model_uri=SAMPLELINK.decreases_availability_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.affects_assignment_of = Slot(uri=SAMPLELINK.affects_assignment_of, name="affects assignment of", curie=SAMPLELINK.curie('affects_assignment_of'),
                   model_uri=SAMPLELINK.affects_assignment_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_assignment_of = Slot(uri=SAMPLELINK.increases_assignment_of, name="increases assignment of", curie=SAMPLELINK.curie('increases_assignment_of'),
                   model_uri=SAMPLELINK.increases_assignment_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_assignment_of = Slot(uri=SAMPLELINK.decreases_assignment_of, name="decreases assignment of", curie=SAMPLELINK.curie('decreases_assignment_of'),
                   model_uri=SAMPLELINK.decreases_assignment_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_localization_of = Slot(uri=SAMPLELINK.affects_localization_of, name="affects localization of", curie=SAMPLELINK.curie('affects_localization_of'),
                   model_uri=SAMPLELINK.affects_localization_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_localization_of = Slot(uri=SAMPLELINK.increases_localization_of, name="increases localization of", curie=SAMPLELINK.curie('increases_localization_of'),
                   model_uri=SAMPLELINK.increases_localization_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_localization_of = Slot(uri=SAMPLELINK.decreases_localization_of, name="decreases localization of", curie=SAMPLELINK.curie('decreases_localization_of'),
                   model_uri=SAMPLELINK.decreases_localization_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_supervision_of = Slot(uri=SAMPLELINK.affects_supervision_of, name="affects supervision of", curie=SAMPLELINK.curie('affects_supervision_of'),
                   model_uri=SAMPLELINK.affects_supervision_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_supervision_of = Slot(uri=SAMPLELINK.increases_supervision_of, name="increases supervision of", curie=SAMPLELINK.curie('increases_supervision_of'),
                   model_uri=SAMPLELINK.increases_supervision_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_supervision_of = Slot(uri=SAMPLELINK.decreases_supervision_of, name="decreases supervision of", curie=SAMPLELINK.curie('decreases_supervision_of'),
                   model_uri=SAMPLELINK.decreases_supervision_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_operational_modification_of = Slot(uri=SAMPLELINK.affects_operational_modification_of, name="affects operational modification of", curie=SAMPLELINK.curie('affects_operational_modification_of'),
                   model_uri=SAMPLELINK.affects_operational_modification_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_operational_modification_of = Slot(uri=SAMPLELINK.increases_operational_modification_of, name="increases operational modification of", curie=SAMPLELINK.curie('increases_operational_modification_of'),
                   model_uri=SAMPLELINK.increases_operational_modification_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_operational_modification_of = Slot(uri=SAMPLELINK.decreases_operational_modification_of, name="decreases operational modification of", curie=SAMPLELINK.curie('decreases_operational_modification_of'),
                   model_uri=SAMPLELINK.decreases_operational_modification_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_instantiation_of = Slot(uri=SAMPLELINK.affects_instantiation_of, name="affects instantiation of", curie=SAMPLELINK.curie('affects_instantiation_of'),
                   model_uri=SAMPLELINK.affects_instantiation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_instantiation_of = Slot(uri=SAMPLELINK.increases_instantiation_of, name="increases instantiation of", curie=SAMPLELINK.curie('increases_instantiation_of'),
                   model_uri=SAMPLELINK.increases_instantiation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_instantiation_of = Slot(uri=SAMPLELINK.decreases_instantiation_of, name="decreases instantiation of", curie=SAMPLELINK.curie('decreases_instantiation_of'),
                   model_uri=SAMPLELINK.decreases_instantiation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_degradation_of = Slot(uri=SAMPLELINK.affects_degradation_of, name="affects degradation of", curie=SAMPLELINK.curie('affects_degradation_of'),
                   model_uri=SAMPLELINK.affects_degradation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_degradation_of = Slot(uri=SAMPLELINK.increases_degradation_of, name="increases degradation of", curie=SAMPLELINK.curie('increases_degradation_of'),
                   model_uri=SAMPLELINK.increases_degradation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_degradation_of = Slot(uri=SAMPLELINK.decreases_degradation_of, name="decreases degradation of", curie=SAMPLELINK.curie('decreases_degradation_of'),
                   model_uri=SAMPLELINK.decreases_degradation_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_updates_rate_of = Slot(uri=SAMPLELINK.affects_updates_rate_of, name="affects updates rate of", curie=SAMPLELINK.curie('affects_updates_rate_of'),
                   model_uri=SAMPLELINK.affects_updates_rate_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.increases_updates_rate_of = Slot(uri=SAMPLELINK.increases_updates_rate_of, name="increases updates rate of", curie=SAMPLELINK.curie('increases_updates_rate_of'),
                   model_uri=SAMPLELINK.increases_updates_rate_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.decreases_updates_rate_of = Slot(uri=SAMPLELINK.decreases_updates_rate_of, name="decreases updates rate of", curie=SAMPLELINK.curie('decreases_updates_rate_of'),
                   model_uri=SAMPLELINK.decreases_updates_rate_of, domain=OperationalEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.affects_response_to = Slot(uri=SAMPLELINK.affects_response_to, name="affects response to", curie=SAMPLELINK.curie('affects_response_to'),
                   model_uri=SAMPLELINK.affects_response_to, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_response_to = Slot(uri=SAMPLELINK.increases_response_to, name="increases response to", curie=SAMPLELINK.curie('increases_response_to'),
                   model_uri=SAMPLELINK.increases_response_to, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_response_to = Slot(uri=SAMPLELINK.decreases_response_to, name="decreases response to", curie=SAMPLELINK.curie('decreases_response_to'),
                   model_uri=SAMPLELINK.decreases_response_to, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_splicing_of = Slot(uri=SAMPLELINK.affects_splicing_of, name="affects splicing of", curie=SAMPLELINK.curie('affects_splicing_of'),
                   model_uri=SAMPLELINK.affects_splicing_of, domain=OperationalEntity, range=Optional[Union[Union[str, ComponentserviceinstanceId], List[Union[str, ComponentserviceinstanceId]]]])

slots.increases_splicing_of = Slot(uri=SAMPLELINK.increases_splicing_of, name="increases splicing of", curie=SAMPLELINK.curie('increases_splicing_of'),
                   model_uri=SAMPLELINK.increases_splicing_of, domain=OperationalEntity, range=Optional[Union[Union[str, ComponentserviceinstanceId], List[Union[str, ComponentserviceinstanceId]]]])

slots.decreases_splicing_of = Slot(uri=SAMPLELINK.decreases_splicing_of, name="decreases splicing of", curie=SAMPLELINK.curie('decreases_splicing_of'),
                   model_uri=SAMPLELINK.decreases_splicing_of, domain=OperationalEntity, range=Optional[Union[Union[str, ComponentserviceinstanceId], List[Union[str, ComponentserviceinstanceId]]]])

slots.affects_stability_of = Slot(uri=SAMPLELINK.affects_stability_of, name="affects stability of", curie=SAMPLELINK.curie('affects_stability_of'),
                   model_uri=SAMPLELINK.affects_stability_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_stability_of = Slot(uri=SAMPLELINK.increases_stability_of, name="increases stability of", curie=SAMPLELINK.curie('increases_stability_of'),
                   model_uri=SAMPLELINK.increases_stability_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_stability_of = Slot(uri=SAMPLELINK.decreases_stability_of, name="decreases stability of", curie=SAMPLELINK.curie('decreases_stability_of'),
                   model_uri=SAMPLELINK.decreases_stability_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_transport_of = Slot(uri=SAMPLELINK.affects_transport_of, name="affects transport of", curie=SAMPLELINK.curie('affects_transport_of'),
                   model_uri=SAMPLELINK.affects_transport_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_transport_of = Slot(uri=SAMPLELINK.increases_transport_of, name="increases transport of", curie=SAMPLELINK.curie('increases_transport_of'),
                   model_uri=SAMPLELINK.increases_transport_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_transport_of = Slot(uri=SAMPLELINK.decreases_transport_of, name="decreases transport of", curie=SAMPLELINK.curie('decreases_transport_of'),
                   model_uri=SAMPLELINK.decreases_transport_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_output_of = Slot(uri=SAMPLELINK.affects_output_of, name="affects output of", curie=SAMPLELINK.curie('affects_output_of'),
                   model_uri=SAMPLELINK.affects_output_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_output_of = Slot(uri=SAMPLELINK.increases_output_of, name="increases output of", curie=SAMPLELINK.curie('increases_output_of'),
                   model_uri=SAMPLELINK.increases_output_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_output_of = Slot(uri=SAMPLELINK.decreases_output_of, name="decreases output of", curie=SAMPLELINK.curie('decreases_output_of'),
                   model_uri=SAMPLELINK.decreases_output_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.affects_uptake_of = Slot(uri=SAMPLELINK.affects_uptake_of, name="affects uptake of", curie=SAMPLELINK.curie('affects_uptake_of'),
                   model_uri=SAMPLELINK.affects_uptake_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_uptake_of = Slot(uri=SAMPLELINK.increases_uptake_of, name="increases uptake of", curie=SAMPLELINK.curie('increases_uptake_of'),
                   model_uri=SAMPLELINK.increases_uptake_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.decreases_uptake_of = Slot(uri=SAMPLELINK.decreases_uptake_of, name="decreases uptake of", curie=SAMPLELINK.curie('decreases_uptake_of'),
                   model_uri=SAMPLELINK.decreases_uptake_of, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.regulates = Slot(uri=SAMPLELINK.regulates, name="regulates", curie=SAMPLELINK.curie('regulates'),
                   model_uri=SAMPLELINK.regulates, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.regulated_by = Slot(uri=SAMPLELINK.regulated_by, name="regulated by", curie=SAMPLELINK.curie('regulated_by'),
                   model_uri=SAMPLELINK.regulated_by, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.positively_regulates = Slot(uri=SAMPLELINK.positively_regulates, name="positively regulates", curie=SAMPLELINK.curie('positively_regulates'),
                   model_uri=SAMPLELINK.positively_regulates, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.positively_regulated_by = Slot(uri=SAMPLELINK.positively_regulated_by, name="positively regulated by", curie=SAMPLELINK.curie('positively_regulated_by'),
                   model_uri=SAMPLELINK.positively_regulated_by, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.negatively_regulates = Slot(uri=SAMPLELINK.negatively_regulates, name="negatively regulates", curie=SAMPLELINK.curie('negatively_regulates'),
                   model_uri=SAMPLELINK.negatively_regulates, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.negatively_regulated_by = Slot(uri=SAMPLELINK.negatively_regulated_by, name="negatively regulated by", curie=SAMPLELINK.curie('negatively_regulated_by'),
                   model_uri=SAMPLELINK.negatively_regulated_by, domain=None, range=Optional[Union[dict, "CyberEssenceOrOccurrent"]])

slots.regulates_process_to_process = Slot(uri=SAMPLELINK.regulates_process_to_process, name="regulates, process to process", curie=SAMPLELINK.curie('regulates_process_to_process'),
                   model_uri=SAMPLELINK.regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.regulated_by_process_to_process = Slot(uri=SAMPLELINK.regulated_by_process_to_process, name="regulated by, process to process", curie=SAMPLELINK.curie('regulated_by_process_to_process'),
                   model_uri=SAMPLELINK.regulated_by_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.positively_regulates_process_to_process = Slot(uri=SAMPLELINK.positively_regulates_process_to_process, name="positively regulates, process to process", curie=SAMPLELINK.curie('positively_regulates_process_to_process'),
                   model_uri=SAMPLELINK.positively_regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.positively_regulated_by_process_to_process = Slot(uri=SAMPLELINK.positively_regulated_by_process_to_process, name="positively regulated by, process to process", curie=SAMPLELINK.curie('positively_regulated_by_process_to_process'),
                   model_uri=SAMPLELINK.positively_regulated_by_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.negatively_regulates_process_to_process = Slot(uri=SAMPLELINK.negatively_regulates_process_to_process, name="negatively regulates, process to process", curie=SAMPLELINK.curie('negatively_regulates_process_to_process'),
                   model_uri=SAMPLELINK.negatively_regulates_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.negatively_regulated_by_process_to_process = Slot(uri=SAMPLELINK.negatively_regulated_by_process_to_process, name="negatively regulated by, process to process", curie=SAMPLELINK.curie('negatively_regulated_by_process_to_process'),
                   model_uri=SAMPLELINK.negatively_regulated_by_process_to_process, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.regulates_entity_to_entity = Slot(uri=SAMPLELINK.regulates_entity_to_entity, name="regulates, entity to entity", curie=SAMPLELINK.curie('regulates_entity_to_entity'),
                   model_uri=SAMPLELINK.regulates_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.regulated_by_entity_to_entity = Slot(uri=SAMPLELINK.regulated_by_entity_to_entity, name="regulated by, entity to entity", curie=SAMPLELINK.curie('regulated_by_entity_to_entity'),
                   model_uri=SAMPLELINK.regulated_by_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.positively_regulates_entity_to_entity = Slot(uri=SAMPLELINK.positively_regulates_entity_to_entity, name="positively regulates, entity to entity", curie=SAMPLELINK.curie('positively_regulates_entity_to_entity'),
                   model_uri=SAMPLELINK.positively_regulates_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.positively_regulated_by_entity_to_entity = Slot(uri=SAMPLELINK.positively_regulated_by_entity_to_entity, name="positively regulated by, entity to entity", curie=SAMPLELINK.curie('positively_regulated_by_entity_to_entity'),
                   model_uri=SAMPLELINK.positively_regulated_by_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.negatively_regulates_entity_to_entity = Slot(uri=SAMPLELINK.negatively_regulates_entity_to_entity, name="negatively regulates, entity to entity", curie=SAMPLELINK.curie('negatively_regulates_entity_to_entity'),
                   model_uri=SAMPLELINK.negatively_regulates_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.negatively_regulated_by_entity_to_entity = Slot(uri=SAMPLELINK.negatively_regulated_by_entity_to_entity, name="negatively regulated by, entity to entity", curie=SAMPLELINK.curie('negatively_regulated_by_entity_to_entity'),
                   model_uri=SAMPLELINK.negatively_regulated_by_entity_to_entity, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.disrupts = Slot(uri=SAMPLELINK.disrupts, name="disrupts", curie=SAMPLELINK.curie('disrupts'),
                   model_uri=SAMPLELINK.disrupts, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.disrupted_by = Slot(uri=SAMPLELINK.disrupted_by, name="disrupted by", curie=SAMPLELINK.curie('disrupted_by'),
                   model_uri=SAMPLELINK.disrupted_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_servicetype = Slot(uri=SAMPLELINK.has_servicetype, name="has servicetype", curie=SAMPLELINK.curie('has_servicetype'),
                   model_uri=SAMPLELINK.has_servicetype, domain=Componentservice, range=Optional[Union[Union[dict, "ServicetypeMixin"], List[Union[dict, "ServicetypeMixin"]]]])

slots.homologous_to = Slot(uri=SAMPLELINK.homologous_to, name="homologous to", curie=SAMPLELINK.curie('homologous_to'),
                   model_uri=SAMPLELINK.homologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.paralogous_to = Slot(uri=SAMPLELINK.paralogous_to, name="paralogous to", curie=SAMPLELINK.curie('paralogous_to'),
                   model_uri=SAMPLELINK.paralogous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.orthologous_to = Slot(uri=SAMPLELINK.orthologous_to, name="orthologous to", curie=SAMPLELINK.curie('orthologous_to'),
                   model_uri=SAMPLELINK.orthologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.xenologous_to = Slot(uri=SAMPLELINK.xenologous_to, name="xenologous to", curie=SAMPLELINK.curie('xenologous_to'),
                   model_uri=SAMPLELINK.xenologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.coexists_with = Slot(uri=SAMPLELINK.coexists_with, name="coexists with", curie=SAMPLELINK.curie('coexists_with'),
                   model_uri=SAMPLELINK.coexists_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.in_pathway_with = Slot(uri=SAMPLELINK.in_pathway_with, name="in pathway with", curie=SAMPLELINK.curie('in_pathway_with'),
                   model_uri=SAMPLELINK.in_pathway_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.in_complex_with = Slot(uri=SAMPLELINK.in_complex_with, name="in complex with", curie=SAMPLELINK.curie('in_complex_with'),
                   model_uri=SAMPLELINK.in_complex_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.in_serviceunit_population_with = Slot(uri=SAMPLELINK.in_serviceunit_population_with, name="in serviceunit population with", curie=SAMPLELINK.curie('in_serviceunit_population_with'),
                   model_uri=SAMPLELINK.in_serviceunit_population_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.colocalizes_with = Slot(uri=SAMPLELINK.colocalizes_with, name="colocalizes with", curie=SAMPLELINK.curie('colocalizes_with'),
                   model_uri=SAMPLELINK.colocalizes_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.componentservice_association = Slot(uri=SAMPLELINK.componentservice_association, name="componentservice association", curie=SAMPLELINK.curie('componentservice_association'),
                   model_uri=SAMPLELINK.componentservice_association, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.componentservice_associated_with_condition = Slot(uri=SAMPLELINK.componentservice_associated_with_condition, name="componentservice associated with condition", curie=SAMPLELINK.curie('componentservice_associated_with_condition'),
                   model_uri=SAMPLELINK.componentservice_associated_with_condition, domain=Componentservice, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.condition_associated_with_componentservice = Slot(uri=SAMPLELINK.condition_associated_with_componentservice, name="condition associated with componentservice", curie=SAMPLELINK.curie('condition_associated_with_componentservice'),
                   model_uri=SAMPLELINK.condition_associated_with_componentservice, domain=ErrorOrObservableFeature, range=Optional[Union[Union[dict, "Componentservice"], List[Union[dict, "Componentservice"]]]])

slots.affects_risk_for = Slot(uri=SAMPLELINK.affects_risk_for, name="affects risk for", curie=SAMPLELINK.curie('affects_risk_for'),
                   model_uri=SAMPLELINK.affects_risk_for, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.predisposes = Slot(uri=SAMPLELINK.predisposes, name="predisposes", curie=SAMPLELINK.curie('predisposes'),
                   model_uri=SAMPLELINK.predisposes, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contributes_to = Slot(uri=SAMPLELINK.contributes_to, name="contributes to", curie=SAMPLELINK.curie('contributes_to'),
                   model_uri=SAMPLELINK.contributes_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.causes = Slot(uri=SAMPLELINK.causes, name="causes", curie=SAMPLELINK.curie('causes'),
                   model_uri=SAMPLELINK.causes, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.caused_by = Slot(uri=SAMPLELINK.caused_by, name="caused by", curie=SAMPLELINK.curie('caused_by'),
                   model_uri=SAMPLELINK.caused_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.ameliorates = Slot(uri=SAMPLELINK.ameliorates, name="ameliorates", curie=SAMPLELINK.curie('ameliorates'),
                   model_uri=SAMPLELINK.ameliorates, domain=ComputationalEntity, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.exacerbates = Slot(uri=SAMPLELINK.exacerbates, name="exacerbates", curie=SAMPLELINK.curie('exacerbates'),
                   model_uri=SAMPLELINK.exacerbates, domain=ComputationalEntity, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.repairs = Slot(uri=SAMPLELINK.repairs, name="repairs", curie=SAMPLELINK.curie('repairs'),
                   model_uri=SAMPLELINK.repairs, domain=Repairing, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.repaired_by = Slot(uri=SAMPLELINK.repaired_by, name="repaired by", curie=SAMPLELINK.curie('repaired_by'),
                   model_uri=SAMPLELINK.repaired_by, domain=ErrorOrObservableFeature, range=Optional[Union[Union[str, RepairingId], List[Union[str, RepairingId]]]])

slots.approved_to_repair = Slot(uri=SAMPLELINK.approved_to_repair, name="approved to repair", curie=SAMPLELINK.curie('approved_to_repair'),
                   model_uri=SAMPLELINK.approved_to_repair, domain=Repairing, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.approved_for_repairing_by = Slot(uri=SAMPLELINK.approved_for_repairing_by, name="approved for repairing by", curie=SAMPLELINK.curie('approved_for_repairing_by'),
                   model_uri=SAMPLELINK.approved_for_repairing_by, domain=ErrorOrObservableFeature, range=Optional[Union[Union[str, RepairingId], List[Union[str, RepairingId]]]])

slots.prevents = Slot(uri=SAMPLELINK.prevents, name="prevents", curie=SAMPLELINK.curie('prevents'),
                   model_uri=SAMPLELINK.prevents, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.prevented_by = Slot(uri=SAMPLELINK.prevented_by, name="prevented by", curie=SAMPLELINK.curie('prevented_by'),
                   model_uri=SAMPLELINK.prevented_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.correlated_with = Slot(uri=SAMPLELINK.correlated_with, name="correlated with", curie=SAMPLELINK.curie('correlated_with'),
                   model_uri=SAMPLELINK.correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.positively_correlated_with = Slot(uri=SAMPLELINK.positively_correlated_with, name="positively correlated with", curie=SAMPLELINK.curie('positively_correlated_with'),
                   model_uri=SAMPLELINK.positively_correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.negatively_correlated_with = Slot(uri=SAMPLELINK.negatively_correlated_with, name="negatively correlated with", curie=SAMPLELINK.curie('negatively_correlated_with'),
                   model_uri=SAMPLELINK.negatively_correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.coavailable_with = Slot(uri=SAMPLELINK.coavailable_with, name="coavailable with", curie=SAMPLELINK.curie('coavailable_with'),
                   model_uri=SAMPLELINK.coavailable_with, domain=None, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.has_marker = Slot(uri=SAMPLELINK.has_marker, name="has marker", curie=SAMPLELINK.curie('has_marker'),
                   model_uri=SAMPLELINK.has_marker, domain=ErrorOrObservableFeature, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.marker_for = Slot(uri=SAMPLELINK.marker_for, name="marker for", curie=SAMPLELINK.curie('marker_for'),
                   model_uri=SAMPLELINK.marker_for, domain=OperationalEntity, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.available_in = Slot(uri=SAMPLELINK.available_in, name="available in", curie=SAMPLELINK.curie('available_in'),
                   model_uri=SAMPLELINK.available_in, domain=None, range=Optional[Union[Union[str, DeploymentEntityId], List[Union[str, DeploymentEntityId]]]])

slots.unavailable_in = Slot(uri=SAMPLELINK.unavailable_in, name="unavailable in", curie=SAMPLELINK.curie('unavailable_in'),
                   model_uri=SAMPLELINK.unavailable_in, domain=DeploymentEntity, range=Optional[Union[Union[dict, "ComponentserviceOrServicetype"], List[Union[dict, "ComponentserviceOrServicetype"]]]])

slots.has_observability = Slot(uri=SAMPLELINK.has_observability, name="has observability", curie=SAMPLELINK.curie('has_observability'),
                   model_uri=SAMPLELINK.has_observability, domain=ComputationalEntity, range=Optional[Union[Union[str, ObservableFeatureId], List[Union[str, ObservableFeatureId]]]])

slots.occurs_in = Slot(uri=SAMPLELINK.occurs_in, name="occurs in", curie=SAMPLELINK.curie('occurs_in'),
                   model_uri=SAMPLELINK.occurs_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.located_in = Slot(uri=SAMPLELINK.located_in, name="located in", curie=SAMPLELINK.curie('located_in'),
                   model_uri=SAMPLELINK.located_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.location_of = Slot(uri=SAMPLELINK.location_of, name="location of", curie=SAMPLELINK.curie('location_of'),
                   model_uri=SAMPLELINK.location_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.similar_to = Slot(uri=SAMPLELINK.similar_to, name="similar to", curie=SAMPLELINK.curie('similar_to'),
                   model_uri=SAMPLELINK.similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.orchestrationly_similar_to = Slot(uri=SAMPLELINK.orchestrationly_similar_to, name="orchestrationly similar to", curie=SAMPLELINK.curie('orchestrationly_similar_to'),
                   model_uri=SAMPLELINK.orchestrationly_similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_sequence_location = Slot(uri=SAMPLELINK.has_sequence_location, name="has sequence location", curie=SAMPLELINK.curie('has_sequence_location'),
                   model_uri=SAMPLELINK.has_sequence_location, domain=WorkloadEntity, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.model_of = Slot(uri=SAMPLELINK.model_of, name="model of", curie=SAMPLELINK.curie('model_of'),
                   model_uri=SAMPLELINK.model_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.overlaps = Slot(uri=SAMPLELINK.overlaps, name="overlaps", curie=SAMPLELINK.curie('overlaps'),
                   model_uri=SAMPLELINK.overlaps, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_part = Slot(uri=SAMPLELINK.has_part, name="has part", curie=SAMPLELINK.curie('has_part'),
                   model_uri=SAMPLELINK.has_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.part_of = Slot(uri=SAMPLELINK.part_of, name="part of", curie=SAMPLELINK.curie('part_of'),
                   model_uri=SAMPLELINK.part_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_input = Slot(uri=SAMPLELINK.has_input, name="has input", curie=SAMPLELINK.curie('has_input'),
                   model_uri=SAMPLELINK.has_input, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_output = Slot(uri=SAMPLELINK.has_output, name="has output", curie=SAMPLELINK.curie('has_output'),
                   model_uri=SAMPLELINK.has_output, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_participant = Slot(uri=SAMPLELINK.has_participant, name="has participant", curie=SAMPLELINK.curie('has_participant'),
                   model_uri=SAMPLELINK.has_participant, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.participates_in = Slot(uri=SAMPLELINK.participates_in, name="participates in", curie=SAMPLELINK.curie('participates_in'),
                   model_uri=SAMPLELINK.participates_in, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.actively_involved_in = Slot(uri=SAMPLELINK.actively_involved_in, name="actively involved in", curie=SAMPLELINK.curie('actively_involved_in'),
                   model_uri=SAMPLELINK.actively_involved_in, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.capable_of = Slot(uri=SAMPLELINK.capable_of, name="capable of", curie=SAMPLELINK.curie('capable_of'),
                   model_uri=SAMPLELINK.capable_of, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.enables = Slot(uri=SAMPLELINK.enables, name="enables", curie=SAMPLELINK.curie('enables'),
                   model_uri=SAMPLELINK.enables, domain=CyberEntity, range=Optional[Union[Union[str, ComputationalProcessOrActivityId], List[Union[str, ComputationalProcessOrActivityId]]]])

slots.enabled_by = Slot(uri=SAMPLELINK.enabled_by, name="enabled by", curie=SAMPLELINK.curie('enabled_by'),
                   model_uri=SAMPLELINK.enabled_by, domain=ComputationalProcessOrActivity, range=Optional[Union[Union[str, CyberEntityId], List[Union[str, CyberEntityId]]]])

slots.derives_into = Slot(uri=SAMPLELINK.derives_into, name="derives into", curie=SAMPLELINK.curie('derives_into'),
                   model_uri=SAMPLELINK.derives_into, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.derives_from = Slot(uri=SAMPLELINK.derives_from, name="derives from", curie=SAMPLELINK.curie('derives_from'),
                   model_uri=SAMPLELINK.derives_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_controller_of = Slot(uri=SAMPLELINK.is_controller_of, name="is controller of", curie=SAMPLELINK.curie('is_controller_of'),
                   model_uri=SAMPLELINK.is_controller_of, domain=ControlActor, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.has_controller = Slot(uri=SAMPLELINK.has_controller, name="has controller", curie=SAMPLELINK.curie('has_controller'),
                   model_uri=SAMPLELINK.has_controller, domain=ControlActor, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.notification_component_of = Slot(uri=SAMPLELINK.notification_component_of, name="notification component of", curie=SAMPLELINK.curie('notification_component_of'),
                   model_uri=SAMPLELINK.notification_component_of, domain=NotificationComponent, range=Optional[Union[Union[str, NotificationId], List[Union[str, NotificationId]]]])

slots.has_notification_component = Slot(uri=SAMPLELINK.has_notification_component, name="has notification component", curie=SAMPLELINK.curie('has_notification_component'),
                   model_uri=SAMPLELINK.has_notification_component, domain=Notification, range=Optional[Union[Union[str, NotificationComponentId], List[Union[str, NotificationComponentId]]]])

slots.data_of = Slot(uri=SAMPLELINK.data_of, name="data of", curie=SAMPLELINK.curie('data_of'),
                   model_uri=SAMPLELINK.data_of, domain=NotificationComponent, range=Optional[Union[Union[str, NotificationId], List[Union[str, NotificationId]]]])

slots.has_data = Slot(uri=SAMPLELINK.has_data, name="has data", curie=SAMPLELINK.curie('has_data'),
                   model_uri=SAMPLELINK.has_data, domain=Notification, range=Optional[Union[Union[str, DataId], List[Union[str, DataId]]]])

slots.is_active_ingredient_of = Slot(uri=SAMPLELINK.is_active_ingredient_of, name="is active ingredient of", curie=SAMPLELINK.curie('is_active_ingredient_of'),
                   model_uri=SAMPLELINK.is_active_ingredient_of, domain=ControlActor, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]], mappings = [RO["0002249"]])

slots.has_active_ingredient = Slot(uri=SAMPLELINK.has_active_ingredient, name="has active ingredient", curie=SAMPLELINK.curie('has_active_ingredient'),
                   model_uri=SAMPLELINK.has_active_ingredient, domain=AdministrativeOperation, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]], mappings = [RO["0002248"]])

slots.is_excipient_of = Slot(uri=SAMPLELINK.is_excipient_of, name="is excipient of", curie=SAMPLELINK.curie('is_excipient_of'),
                   model_uri=SAMPLELINK.is_excipient_of, domain=ControlActor, range=Optional[Union[Union[str, AdministrativeOperationId], List[Union[str, AdministrativeOperationId]]]], mappings = [WIKIDATA.Q902638])

slots.has_excipient = Slot(uri=SAMPLELINK.has_excipient, name="has excipient", curie=SAMPLELINK.curie('has_excipient'),
                   model_uri=SAMPLELINK.has_excipient, domain=AdministrativeOperation, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]], mappings = [WIKIDATA.Q902638])

slots.manifestation_of = Slot(uri=SAMPLELINK.manifestation_of, name="manifestation of", curie=SAMPLELINK.curie('manifestation_of'),
                   model_uri=SAMPLELINK.manifestation_of, domain=NamedThing, range=Optional[Union[Union[str, ErrorId], List[Union[str, ErrorId]]]])

slots.produces = Slot(uri=SAMPLELINK.produces, name="produces", curie=SAMPLELINK.curie('produces'),
                   model_uri=SAMPLELINK.produces, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.produced_by = Slot(uri=SAMPLELINK.produced_by, name="produced by", curie=SAMPLELINK.curie('produced_by'),
                   model_uri=SAMPLELINK.produced_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.temporally_related_to = Slot(uri=SAMPLELINK.temporally_related_to, name="temporally related to", curie=SAMPLELINK.curie('temporally_related_to'),
                   model_uri=SAMPLELINK.temporally_related_to, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.precedes = Slot(uri=SAMPLELINK.precedes, name="precedes", curie=SAMPLELINK.curie('precedes'),
                   model_uri=SAMPLELINK.precedes, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.preceded_by = Slot(uri=SAMPLELINK.preceded_by, name="preceded by", curie=SAMPLELINK.curie('preceded_by'),
                   model_uri=SAMPLELINK.preceded_by, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.directly_interacts_with = Slot(uri=SAMPLELINK.directly_interacts_with, name="directly interacts with", curie=SAMPLELINK.curie('directly_interacts_with'),
                   model_uri=SAMPLELINK.directly_interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affects_availability_in = Slot(uri=SAMPLELINK.affects_availability_in, name="affects availability in", curie=SAMPLELINK.curie('affects_availability_in'),
                   model_uri=SAMPLELINK.affects_availability_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_variant_part = Slot(uri=SAMPLELINK.has_variant_part, name="has variant part", curie=SAMPLELINK.curie('has_variant_part'),
                   model_uri=SAMPLELINK.has_variant_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.related_condition = Slot(uri=SAMPLELINK.related_condition, name="related condition", curie=SAMPLELINK.curie('related_condition'),
                   model_uri=SAMPLELINK.related_condition, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_sequence_variant_of = Slot(uri=SAMPLELINK.is_sequence_variant_of, name="is sequence variant of", curie=SAMPLELINK.curie('is_sequence_variant_of'),
                   model_uri=SAMPLELINK.is_sequence_variant_of, domain=SequenceVariant, range=Optional[Union[Union[str, WorkloadEntityId], List[Union[str, WorkloadEntityId]]]])

slots.is_missense_variant_of = Slot(uri=SAMPLELINK.is_missense_variant_of, name="is missense variant of", curie=SAMPLELINK.curie('is_missense_variant_of'),
                   model_uri=SAMPLELINK.is_missense_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_synonymous_variant_of = Slot(uri=SAMPLELINK.is_synonymous_variant_of, name="is synonymous variant of", curie=SAMPLELINK.curie('is_synonymous_variant_of'),
                   model_uri=SAMPLELINK.is_synonymous_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_nonsense_variant_of = Slot(uri=SAMPLELINK.is_nonsense_variant_of, name="is nonsense variant of", curie=SAMPLELINK.curie('is_nonsense_variant_of'),
                   model_uri=SAMPLELINK.is_nonsense_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_protocol_variant_of = Slot(uri=SAMPLELINK.is_protocol_variant_of, name="is protocol variant of", curie=SAMPLELINK.curie('is_protocol_variant_of'),
                   model_uri=SAMPLELINK.is_protocol_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_splice_site_variant_of = Slot(uri=SAMPLELINK.is_splice_site_variant_of, name="is splice site variant of", curie=SAMPLELINK.curie('is_splice_site_variant_of'),
                   model_uri=SAMPLELINK.is_splice_site_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_nearby_variant_of = Slot(uri=SAMPLELINK.is_nearby_variant_of, name="is nearby variant of", curie=SAMPLELINK.curie('is_nearby_variant_of'),
                   model_uri=SAMPLELINK.is_nearby_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.is_non_coding_variant_of = Slot(uri=SAMPLELINK.is_non_coding_variant_of, name="is non coding variant of", curie=SAMPLELINK.curie('is_non_coding_variant_of'),
                   model_uri=SAMPLELINK.is_non_coding_variant_of, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.error_has_basis_in = Slot(uri=SAMPLELINK.error_has_basis_in, name="error has basis in", curie=SAMPLELINK.curie('error_has_basis_in'),
                   model_uri=SAMPLELINK.error_has_basis_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.causes_adverse_event = Slot(uri=SAMPLELINK.causes_adverse_event, name="causes adverse event", curie=SAMPLELINK.curie('causes_adverse_event'),
                   model_uri=SAMPLELINK.causes_adverse_event, domain=AdministrativeOperation, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.contraindicated_for = Slot(uri=SAMPLELINK.contraindicated_for, name="contraindicated for", curie=SAMPLELINK.curie('contraindicated_for'),
                   model_uri=SAMPLELINK.contraindicated_for, domain=AdministrativeOperation, range=Optional[Union[Union[str, ErrorOrObservableFeatureId], List[Union[str, ErrorOrObservableFeatureId]]]])

slots.has_not_completed = Slot(uri=SAMPLELINK.has_not_completed, name="has not completed", curie=SAMPLELINK.curie('has_not_completed'),
                   model_uri=SAMPLELINK.has_not_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_completed = Slot(uri=SAMPLELINK.has_completed, name="has completed", curie=SAMPLELINK.curie('has_completed'),
                   model_uri=SAMPLELINK.has_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.decreases_operational_interaction = Slot(uri=SAMPLELINK.decreases_operational_interaction, name="decreases operational interaction", curie=SAMPLELINK.curie('decreases_operational_interaction'),
                   model_uri=SAMPLELINK.decreases_operational_interaction, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.increases_operational_interaction = Slot(uri=SAMPLELINK.increases_operational_interaction, name="increases operational interaction", curie=SAMPLELINK.curie('increases_operational_interaction'),
                   model_uri=SAMPLELINK.increases_operational_interaction, domain=OperationalEntity, range=Optional[Union[Union[str, OperationalEntityId], List[Union[str, OperationalEntityId]]]])

slots.in_linkage_disequilibrium_with = Slot(uri=SAMPLELINK.in_linkage_disequilibrium_with, name="in linkage disequilibrium with", curie=SAMPLELINK.curie('in_linkage_disequilibrium_with'),
                   model_uri=SAMPLELINK.in_linkage_disequilibrium_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_increased_amount = Slot(uri=SAMPLELINK.has_increased_amount, name="has increased amount", curie=SAMPLELINK.curie('has_increased_amount'),
                   model_uri=SAMPLELINK.has_increased_amount, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_decreased_amount = Slot(uri=SAMPLELINK.has_decreased_amount, name="has decreased amount", curie=SAMPLELINK.curie('has_decreased_amount'),
                   model_uri=SAMPLELINK.has_decreased_amount, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.lacks_part = Slot(uri=SAMPLELINK.lacks_part, name="lacks part", curie=SAMPLELINK.curie('lacks_part'),
                   model_uri=SAMPLELINK.lacks_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.develops_from = Slot(uri=SAMPLELINK.develops_from, name="develops from", curie=SAMPLELINK.curie('develops_from'),
                   model_uri=SAMPLELINK.develops_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.in_taxon = Slot(uri=SAMPLELINK.in_taxon, name="in taxon", curie=SAMPLELINK.curie('in_taxon'),
                   model_uri=SAMPLELINK.in_taxon, domain=None, range=Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]])

slots.has_operational_consequence = Slot(uri=SAMPLELINK.has_operational_consequence, name="has operational consequence", curie=SAMPLELINK.curie('has_operational_consequence'),
                   model_uri=SAMPLELINK.has_operational_consequence, domain=NamedThing, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.association_slot = Slot(uri=SAMPLELINK.association_slot, name="association slot", curie=SAMPLELINK.curie('association_slot'),
                   model_uri=SAMPLELINK.association_slot, domain=Association, range=Optional[str])

slots.association_id = Slot(uri=SAMPLELINK.id, name="association_id", curie=SAMPLELINK.curie('id'),
                   model_uri=SAMPLELINK.association_id, domain=Association, range=Union[str, AssociationId])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.subject, domain=Association, range=Union[str, NamedThingId])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.object, domain=Association, range=Union[str, NamedThingId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.predicate, domain=Association, range=Union[str, PredicateType])

slots.edge_label = Slot(uri=RDF.predicate, name="edge label", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.edge_label, domain=Association, range=Union[str, PredicateType])

slots.relation = Slot(uri=SAMPLELINK.relation, name="relation", curie=SAMPLELINK.curie('relation'),
                   model_uri=SAMPLELINK.relation, domain=Association, range=Union[str, URIorCURIE])

slots.negated = Slot(uri=SAMPLELINK.negated, name="negated", curie=SAMPLELINK.curie('negated'),
                   model_uri=SAMPLELINK.negated, domain=Association, range=Optional[Union[bool, Bool]])

slots.has_confidence_level = Slot(uri=SAMPLELINK.has_confidence_level, name="has confidence level", curie=SAMPLELINK.curie('has_confidence_level'),
                   model_uri=SAMPLELINK.has_confidence_level, domain=Association, range=Optional[Union[str, ConfidenceLevelId]])

slots.has_evidence = Slot(uri=SAMPLELINK.has_evidence, name="has evidence", curie=SAMPLELINK.curie('has_evidence'),
                   model_uri=SAMPLELINK.has_evidence, domain=Association, range=Optional[Union[str, EvidenceTypeId]])

slots.provided_by = Slot(uri=SAMPLELINK.provided_by, name="provided by", curie=SAMPLELINK.curie('provided_by'),
                   model_uri=SAMPLELINK.provided_by, domain=Association, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.association_type = Slot(uri=SAMPLELINK.association_type, name="association type", curie=SAMPLELINK.curie('association_type'),
                   model_uri=SAMPLELINK.association_type, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.chi_squared_statistic = Slot(uri=SAMPLELINK.chi_squared_statistic, name="chi squared statistic", curie=SAMPLELINK.curie('chi_squared_statistic'),
                   model_uri=SAMPLELINK.chi_squared_statistic, domain=Association, range=Optional[float])

slots.p_value = Slot(uri=SAMPLELINK.p_value, name="p value", curie=SAMPLELINK.curie('p_value'),
                   model_uri=SAMPLELINK.p_value, domain=Association, range=Optional[float])

slots.interacting_tasks_category = Slot(uri=SAMPLELINK.interacting_tasks_category, name="interacting tasks category", curie=SAMPLELINK.curie('interacting_tasks_category'),
                   model_uri=SAMPLELINK.interacting_tasks_category, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.quantifier_qualifier = Slot(uri=SAMPLELINK.quantifier_qualifier, name="quantifier qualifier", curie=SAMPLELINK.curie('quantifier_qualifier'),
                   model_uri=SAMPLELINK.quantifier_qualifier, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.catalyst_qualifier = Slot(uri=SAMPLELINK.catalyst_qualifier, name="catalyst qualifier", curie=SAMPLELINK.curie('catalyst_qualifier'),
                   model_uri=SAMPLELINK.catalyst_qualifier, domain=Association, range=Optional[Union[Union[dict, MacrooperationalMachineMixin], List[Union[dict, MacrooperationalMachineMixin]]]])

slots.availability_site = Slot(uri=SAMPLELINK.availability_site, name="availability site", curie=SAMPLELINK.curie('availability_site'),
                   model_uri=SAMPLELINK.availability_site, domain=Association, range=Optional[Union[str, DeploymentEntityId]])

slots.stage_qualifier = Slot(uri=SAMPLELINK.stage_qualifier, name="stage qualifier", curie=SAMPLELINK.curie('stage_qualifier'),
                   model_uri=SAMPLELINK.stage_qualifier, domain=Association, range=Optional[Union[str, LifecycleStageId]])

slots.observable_state = Slot(uri=SAMPLELINK.observable_state, name="observable state", curie=SAMPLELINK.curie('observable_state'),
                   model_uri=SAMPLELINK.observable_state, domain=Association, range=Optional[Union[str, ErrorOrObservableFeatureId]])

slots.qualifiers = Slot(uri=SAMPLELINK.qualifiers, name="qualifiers", curie=SAMPLELINK.curie('qualifiers'),
                   model_uri=SAMPLELINK.qualifiers, domain=Association, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.frequency_qualifier = Slot(uri=SAMPLELINK.frequency_qualifier, name="frequency qualifier", curie=SAMPLELINK.curie('frequency_qualifier'),
                   model_uri=SAMPLELINK.frequency_qualifier, domain=Association, range=Optional[Union[dict, FrequencyValue]])

slots.severity_qualifier = Slot(uri=SAMPLELINK.severity_qualifier, name="severity qualifier", curie=SAMPLELINK.curie('severity_qualifier'),
                   model_uri=SAMPLELINK.severity_qualifier, domain=Association, range=Optional[Union[dict, SeverityValue]])

slots.architectural_style_qualifier = Slot(uri=SAMPLELINK.architectural_style_qualifier, name="architectural style qualifier", curie=SAMPLELINK.curie('architectural_style_qualifier'),
                   model_uri=SAMPLELINK.architectural_style_qualifier, domain=Association, range=Optional[Union[dict, ComputationalArchitecturalStyle]])

slots.onset_qualifier = Slot(uri=SAMPLELINK.onset_qualifier, name="onset qualifier", curie=SAMPLELINK.curie('onset_qualifier'),
                   model_uri=SAMPLELINK.onset_qualifier, domain=Association, range=Optional[Union[dict, Onset]])

slots.empirical_modifier_qualifier = Slot(uri=SAMPLELINK.empirical_modifier_qualifier, name="empirical modifier qualifier", curie=SAMPLELINK.curie('empirical_modifier_qualifier'),
                   model_uri=SAMPLELINK.empirical_modifier_qualifier, domain=Association, range=Optional[Union[dict, EmpiricalModifier]])

slots.sequence_variant_qualifier = Slot(uri=SAMPLELINK.sequence_variant_qualifier, name="sequence variant qualifier", curie=SAMPLELINK.curie('sequence_variant_qualifier'),
                   model_uri=SAMPLELINK.sequence_variant_qualifier, domain=Association, range=Optional[Union[str, SequenceVariantId]])

slots.publications = Slot(uri=SAMPLELINK.publications, name="publications", curie=SAMPLELINK.curie('publications'),
                   model_uri=SAMPLELINK.publications, domain=Association, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.sequence_localization_attribute = Slot(uri=SAMPLELINK.sequence_localization_attribute, name="sequence localization attribute", curie=SAMPLELINK.curie('sequence_localization_attribute'),
                   model_uri=SAMPLELINK.sequence_localization_attribute, domain=ComponentserviceSequenceLocalization, range=Optional[str])

slots.interbase_coordinate = Slot(uri=SAMPLELINK.interbase_coordinate, name="interbase coordinate", curie=SAMPLELINK.curie('interbase_coordinate'),
                   model_uri=SAMPLELINK.interbase_coordinate, domain=ComponentserviceSequenceLocalization, range=Optional[int])

slots.start_interbase_coordinate = Slot(uri=SAMPLELINK.start_interbase_coordinate, name="start interbase coordinate", curie=SAMPLELINK.curie('start_interbase_coordinate'),
                   model_uri=SAMPLELINK.start_interbase_coordinate, domain=ComponentserviceSequenceLocalization, range=Optional[int])

slots.end_interbase_coordinate = Slot(uri=SAMPLELINK.end_interbase_coordinate, name="end interbase coordinate", curie=SAMPLELINK.curie('end_interbase_coordinate'),
                   model_uri=SAMPLELINK.end_interbase_coordinate, domain=ComponentserviceSequenceLocalization, range=Optional[int])

slots.workload_build = Slot(uri=SAMPLELINK.workload_build, name="workload build", curie=SAMPLELINK.curie('workload_build'),
                   model_uri=SAMPLELINK.workload_build, domain=ComponentserviceSequenceLocalization, range=Optional[str])

slots.strand = Slot(uri=SAMPLELINK.strand, name="strand", curie=SAMPLELINK.curie('strand'),
                   model_uri=SAMPLELINK.strand, domain=ComponentserviceSequenceLocalization, range=Optional[str])

slots.phase = Slot(uri=SAMPLELINK.phase, name="phase", curie=SAMPLELINK.curie('phase'),
                   model_uri=SAMPLELINK.phase, domain=CodingSequence, range=Optional[str])

slots.has_taxonomic_rank = Slot(uri=SAMPLELINK.has_taxonomic_rank, name="has taxonomic rank", curie=SAMPLELINK.curie('has_taxonomic_rank'),
                   model_uri=SAMPLELINK.has_taxonomic_rank, domain=None, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.attribute_name = Slot(uri=RDFS.label, name="attribute_name", curie=RDFS.curie('label'),
                   model_uri=SAMPLELINK.attribute_name, domain=Attribute, range=Optional[Union[str, LabelType]])

slots.named_thing_category = Slot(uri=SAMPLELINK.category, name="named thing_category", curie=SAMPLELINK.curie('category'),
                   model_uri=SAMPLELINK.named_thing_category, domain=NamedThing, range=Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]])

slots.system_taxon_has_taxonomic_rank = Slot(uri=SAMPLELINK.has_taxonomic_rank, name="system taxon_has taxonomic rank", curie=SAMPLELINK.curie('has_taxonomic_rank'),
                   model_uri=SAMPLELINK.system_taxon_has_taxonomic_rank, domain=SystemTaxon, range=Optional[Union[str, TaxonomicRankId]], mappings = [WIKIDATA.P105])

slots.system_taxon_subclass_of = Slot(uri=RDFS.subClassOf, name="system taxon_subclass of", curie=RDFS.curie('subClassOf'),
                   model_uri=SAMPLELINK.system_taxon_subclass_of, domain=SystemTaxon, range=Optional[Union[Union[str, SystemTaxonId], List[Union[str, SystemTaxonId]]]])

slots.agent_id = Slot(uri=SAMPLELINK.id, name="agent_id", curie=SAMPLELINK.curie('id'),
                   model_uri=SAMPLELINK.agent_id, domain=Agent, range=Union[str, AgentId])

slots.agent_name = Slot(uri=RDFS.label, name="agent_name", curie=RDFS.curie('label'),
                   model_uri=SAMPLELINK.agent_name, domain=Agent, range=Optional[Union[str, LabelType]])

slots.publication_id = Slot(uri=SAMPLELINK.id, name="publication_id", curie=SAMPLELINK.curie('id'),
                   model_uri=SAMPLELINK.publication_id, domain=Publication, range=Union[str, PublicationId])

slots.publication_name = Slot(uri=RDFS.label, name="publication_name", curie=RDFS.curie('label'),
                   model_uri=SAMPLELINK.publication_name, domain=Publication, range=Optional[Union[str, LabelType]])

slots.publication_type = Slot(uri=DCT.type, name="publication_type", curie=DCT.curie('type'),
                   model_uri=SAMPLELINK.publication_type, domain=Publication, range=str)

slots.publication_pages = Slot(uri=SAMPLELINK.pages, name="publication_pages", curie=SAMPLELINK.curie('pages'),
                   model_uri=SAMPLELINK.publication_pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.book_id = Slot(uri=SAMPLELINK.id, name="book_id", curie=SAMPLELINK.curie('id'),
                   model_uri=SAMPLELINK.book_id, domain=Book, range=Union[str, BookId])

slots.book_type = Slot(uri=RDF.type, name="book_type", curie=RDF.curie('type'),
                   model_uri=SAMPLELINK.book_type, domain=Book, range=str)

slots.book_chapter_published_in = Slot(uri=SAMPLELINK.published_in, name="book chapter_published in", curie=SAMPLELINK.curie('published_in'),
                   model_uri=SAMPLELINK.book_chapter_published_in, domain=BookChapter, range=Union[str, URIorCURIE])

slots.serial_id = Slot(uri=SAMPLELINK.id, name="serial_id", curie=SAMPLELINK.curie('id'),
                   model_uri=SAMPLELINK.serial_id, domain=Serial, range=Union[str, SerialId])

slots.serial_type = Slot(uri=RDF.type, name="serial_type", curie=RDF.curie('type'),
                   model_uri=SAMPLELINK.serial_type, domain=Serial, range=str)

slots.article_published_in = Slot(uri=SAMPLELINK.published_in, name="article_published in", curie=SAMPLELINK.curie('published_in'),
                   model_uri=SAMPLELINK.article_published_in, domain=Article, range=Union[str, URIorCURIE])

slots.article_iso_abbreviation = Slot(uri=SAMPLELINK.iso_abbreviation, name="article_iso abbreviation", curie=SAMPLELINK.curie('iso_abbreviation'),
                   model_uri=SAMPLELINK.article_iso_abbreviation, domain=Article, range=Optional[str])

slots.operational_activity_has_input = Slot(uri=SAMPLELINK.has_input, name="operational activity_has input", curie=SAMPLELINK.curie('has_input'),
                   model_uri=SAMPLELINK.operational_activity_has_input, domain=OperationalActivity, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.operational_activity_has_output = Slot(uri=SAMPLELINK.has_output, name="operational activity_has output", curie=SAMPLELINK.curie('has_output'),
                   model_uri=SAMPLELINK.operational_activity_has_output, domain=OperationalActivity, range=Optional[Union[Union[str, ControlActorId], List[Union[str, ControlActorId]]]])

slots.operational_activity_enabled_by = Slot(uri=SAMPLELINK.enabled_by, name="operational activity_enabled by", curie=SAMPLELINK.curie('enabled_by'),
                   model_uri=SAMPLELINK.operational_activity_enabled_by, domain=OperationalActivity, range=Optional[Union[Union[dict, "MacrooperationalMachineMixin"], List[Union[dict, "MacrooperationalMachineMixin"]]]])

slots.systemic_entity_has_attribute = Slot(uri=SAMPLELINK.has_attribute, name="systemic entity_has attribute", curie=SAMPLELINK.curie('has_attribute'),
                   model_uri=SAMPLELINK.systemic_entity_has_attribute, domain=SystemicEntity, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.macrooperational_machine_mixin_name = Slot(uri=RDFS.label, name="macrooperational machine mixin_name", curie=RDFS.curie('label'),
                   model_uri=SAMPLELINK.macrooperational_machine_mixin_name, domain=None, range=Optional[Union[str, SymbolType]])

slots.sequence_variant_has_componentservice = Slot(uri=SAMPLELINK.has_componentservice, name="sequence variant_has componentservice", curie=SAMPLELINK.curie('has_componentservice'),
                   model_uri=SAMPLELINK.sequence_variant_has_componentservice, domain=SequenceVariant, range=Optional[Union[Union[dict, Componentservice], List[Union[dict, Componentservice]]]])

slots.sequence_variant_has_computational_sequence = Slot(uri=SAMPLELINK.has_computational_sequence, name="sequence variant_has computational sequence", curie=SAMPLELINK.curie('has_computational_sequence'),
                   model_uri=SAMPLELINK.sequence_variant_has_computational_sequence, domain=SequenceVariant, range=Optional[Union[str, ComputationalSequence]])

slots.sequence_variant_id = Slot(uri=SAMPLELINK.id, name="sequence variant_id", curie=SAMPLELINK.curie('id'),
                   model_uri=SAMPLELINK.sequence_variant_id, domain=SequenceVariant, range=Union[str, SequenceVariantId])

slots.empirical_measurement_has_attribute_type = Slot(uri=SAMPLELINK.has_attribute_type, name="empirical measurement_has attribute type", curie=SAMPLELINK.curie('has_attribute_type'),
                   model_uri=SAMPLELINK.empirical_measurement_has_attribute_type, domain=EmpiricalMeasurement, range=Union[str, OntologyClassId])

slots.empirical_finding_has_attribute = Slot(uri=SAMPLELINK.has_attribute, name="empirical finding_has attribute", curie=SAMPLELINK.curie('has_attribute'),
                   model_uri=SAMPLELINK.empirical_finding_has_attribute, domain=EmpiricalFinding, range=Optional[Union[Union[dict, EmpiricalAttribute], List[Union[dict, EmpiricalAttribute]]]])

slots.socioeconomic_exposure_has_attribute = Slot(uri=SAMPLELINK.has_attribute, name="socioeconomic exposure_has attribute", curie=SAMPLELINK.curie('has_attribute'),
                   model_uri=SAMPLELINK.socioeconomic_exposure_has_attribute, domain=SocioeconomicExposure, range=Union[Union[dict, SocioeconomicAttribute], List[Union[dict, SocioeconomicAttribute]]])

slots.association_type = Slot(uri=RDF.type, name="association_type", curie=RDF.curie('type'),
                   model_uri=SAMPLELINK.association_type, domain=Association, range=Optional[str])

slots.association_category = Slot(uri=SAMPLELINK.category, name="association_category", curie=SAMPLELINK.curie('category'),
                   model_uri=SAMPLELINK.association_category, domain=Association, range=Union[Union[str, AssociationId], List[Union[str, AssociationId]]])

slots.contributor_association_subject = Slot(uri=RDF.subject, name="contributor association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.contributor_association_subject, domain=ContributorAssociation, range=Union[str, InformationContentEntityId])

slots.contributor_association_predicate = Slot(uri=RDF.predicate, name="contributor association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.contributor_association_predicate, domain=ContributorAssociation, range=Union[str, PredicateType])

slots.contributor_association_object = Slot(uri=RDF.object, name="contributor association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.contributor_association_object, domain=ContributorAssociation, range=Union[str, AgentId])

slots.contributor_association_qualifiers = Slot(uri=SAMPLELINK.qualifiers, name="contributor association_qualifiers", curie=SAMPLELINK.curie('qualifiers'),
                   model_uri=SAMPLELINK.contributor_association_qualifiers, domain=ContributorAssociation, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.serviceunittype_to_serviceunittype_part_association_predicate = Slot(uri=RDF.predicate, name="serviceunittype to serviceunittype part association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.serviceunittype_to_serviceunittype_part_association_predicate, domain=ServiceunittypeToServiceunittypePartAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_serviceunittype_part_association_subject = Slot(uri=RDF.subject, name="serviceunittype to serviceunittype part association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.serviceunittype_to_serviceunittype_part_association_subject, domain=ServiceunittypeToServiceunittypePartAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_serviceunittype_part_association_object = Slot(uri=RDF.object, name="serviceunittype to serviceunittype part association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.serviceunittype_to_serviceunittype_part_association_object, domain=ServiceunittypeToServiceunittypePartAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_componentservice_association_predicate = Slot(uri=RDF.predicate, name="serviceunittype to componentservice association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.serviceunittype_to_componentservice_association_predicate, domain=ServiceunittypeToComponentserviceAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_componentservice_association_subject = Slot(uri=RDF.subject, name="serviceunittype to componentservice association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.serviceunittype_to_componentservice_association_subject, domain=ServiceunittypeToComponentserviceAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_componentservice_association_object = Slot(uri=RDF.object, name="serviceunittype to componentservice association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.serviceunittype_to_componentservice_association_object, domain=ServiceunittypeToComponentserviceAssociation, range=Union[dict, Componentservice])

slots.serviceunittype_to_variant_association_predicate = Slot(uri=RDF.predicate, name="serviceunittype to variant association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.serviceunittype_to_variant_association_predicate, domain=ServiceunittypeToVariantAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_variant_association_subject = Slot(uri=RDF.subject, name="serviceunittype to variant association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.serviceunittype_to_variant_association_subject, domain=ServiceunittypeToVariantAssociation, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_variant_association_object = Slot(uri=RDF.object, name="serviceunittype to variant association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.serviceunittype_to_variant_association_object, domain=ServiceunittypeToVariantAssociation, range=Union[str, SequenceVariantId])

slots.componentservice_to_componentservice_association_subject = Slot(uri=RDF.subject, name="componentservice to componentservice association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentservice_to_componentservice_association_subject, domain=ComponentserviceToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_componentservice_association_object = Slot(uri=RDF.object, name="componentservice to componentservice association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.componentservice_to_componentservice_association_object, domain=ComponentserviceToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_componentservice_homology_association_predicate = Slot(uri=RDF.predicate, name="componentservice to componentservice homology association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.componentservice_to_componentservice_homology_association_predicate, domain=ComponentserviceToComponentserviceHomologyAssociation, range=Union[str, PredicateType])

slots.componentservice_availability_mixin_quantifier_qualifier = Slot(uri=SAMPLELINK.quantifier_qualifier, name="componentservice availability mixin_quantifier qualifier", curie=SAMPLELINK.curie('quantifier_qualifier'),
                   model_uri=SAMPLELINK.componentservice_availability_mixin_quantifier_qualifier, domain=ComponentserviceAvailabilityMixin, range=Optional[Union[str, OntologyClassId]])

slots.componentservice_to_componentservice_coavailability_association_predicate = Slot(uri=RDF.predicate, name="componentservice to componentservice coavailability association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.componentservice_to_componentservice_coavailability_association_predicate, domain=ComponentserviceToComponentserviceCoavailabilityAssociation, range=Union[str, PredicateType])

slots.pairwise_componentservice_to_componentservice_interaction_predicate = Slot(uri=RDF.predicate, name="pairwise componentservice to componentservice interaction_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.pairwise_componentservice_to_componentservice_interaction_predicate, domain=PairwiseComponentserviceToComponentserviceInteraction, range=Union[str, PredicateType])

slots.pairwise_componentservice_to_componentservice_interaction_relation = Slot(uri=SAMPLELINK.relation, name="pairwise componentservice to componentservice interaction_relation", curie=SAMPLELINK.curie('relation'),
                   model_uri=SAMPLELINK.pairwise_componentservice_to_componentservice_interaction_relation, domain=PairwiseComponentserviceToComponentserviceInteraction, range=Union[str, URIorCURIE])

slots.pairwise_operationally_interaction_subject = Slot(uri=RDF.subject, name="pairwise operationally interaction_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.pairwise_operationally_interaction_subject, domain=PairwiseOperationallyInteraction, range=Union[str, OperationalEntityId])

slots.pairwise_operationally_interaction_id = Slot(uri=SAMPLELINK.id, name="pairwise operationally interaction_id", curie=SAMPLELINK.curie('id'),
                   model_uri=SAMPLELINK.pairwise_operationally_interaction_id, domain=PairwiseOperationallyInteraction, range=Union[str, PairwiseOperationallyInteractionId])

slots.pairwise_operationally_interaction_predicate = Slot(uri=RDF.predicate, name="pairwise operationally interaction_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.pairwise_operationally_interaction_predicate, domain=PairwiseOperationallyInteraction, range=Union[str, PredicateType])

slots.pairwise_operationally_interaction_relation = Slot(uri=SAMPLELINK.relation, name="pairwise operationally interaction_relation", curie=SAMPLELINK.curie('relation'),
                   model_uri=SAMPLELINK.pairwise_operationally_interaction_relation, domain=PairwiseOperationallyInteraction, range=Union[str, URIorCURIE])

slots.pairwise_operationally_interaction_object = Slot(uri=RDF.object, name="pairwise operationally interaction_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.pairwise_operationally_interaction_object, domain=PairwiseOperationallyInteraction, range=Union[str, OperationalEntityId])

slots.component_type_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="component type to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.component_type_to_entity_association_mixin_subject, domain=None, range=Union[str, ComponentTypeId])

slots.component_type_to_error_or_observable_feature_association_subject = Slot(uri=RDF.subject, name="component type to error or observable feature association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.component_type_to_error_or_observable_feature_association_subject, domain=ComponentTypeToErrorOrObservableFeatureAssociation, range=Union[str, ErrorOrObservableFeatureId])

slots.operational_entity_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="operational entity to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.operational_entity_to_entity_association_mixin_subject, domain=None, range=Union[str, OperationalEntityId])

slots.administrative_operational_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="administrative operational to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.administrative_operational_to_entity_association_mixin_subject, domain=None, range=Union[str, AdministrativeOperationId])

slots.orchestration_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="orchestration to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.orchestration_to_entity_association_mixin_subject, domain=None, range=Union[str, ControlActorId])

slots.case_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="case to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.case_to_entity_association_mixin_subject, domain=None, range=Union[str, CaseId])

slots.orchestration_to_orchestration_association_object = Slot(uri=RDF.object, name="orchestration to orchestration association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.orchestration_to_orchestration_association_object, domain=OrchestrationToOrchestrationAssociation, range=Union[str, ControlActorId])

slots.orchestration_to_orchestration_derivation_association_subject = Slot(uri=RDF.subject, name="orchestration to orchestration derivation association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.orchestration_to_orchestration_derivation_association_subject, domain=OrchestrationToOrchestrationDerivationAssociation, range=Union[str, ControlActorId])

slots.orchestration_to_orchestration_derivation_association_object = Slot(uri=RDF.object, name="orchestration to orchestration derivation association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.orchestration_to_orchestration_derivation_association_object, domain=OrchestrationToOrchestrationDerivationAssociation, range=Union[str, ControlActorId])

slots.orchestration_to_orchestration_derivation_association_predicate = Slot(uri=RDF.predicate, name="orchestration to orchestration derivation association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.orchestration_to_orchestration_derivation_association_predicate, domain=OrchestrationToOrchestrationDerivationAssociation, range=Union[str, PredicateType])

slots.orchestration_to_orchestration_derivation_association_catalyst_qualifier = Slot(uri=SAMPLELINK.catalyst_qualifier, name="orchestration to orchestration derivation association_catalyst qualifier", curie=SAMPLELINK.curie('catalyst_qualifier'),
                   model_uri=SAMPLELINK.orchestration_to_orchestration_derivation_association_catalyst_qualifier, domain=OrchestrationToOrchestrationDerivationAssociation, range=Optional[Union[Union[dict, MacrooperationalMachineMixin], List[Union[dict, MacrooperationalMachineMixin]]]])

slots.orchestration_to_error_or_observable_feature_association_object = Slot(uri=RDF.object, name="orchestration to error or observable feature association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.orchestration_to_error_or_observable_feature_association_object, domain=OrchestrationToErrorOrObservableFeatureAssociation, range=Union[str, ErrorOrObservableFeatureId])

slots.orchestration_to_pathway_association_object = Slot(uri=RDF.object, name="orchestration to pathway association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.orchestration_to_pathway_association_object, domain=OrchestrationToPathwayAssociation, range=Union[str, PathwayId])

slots.orchestration_to_componentservice_association_object = Slot(uri=RDF.object, name="orchestration to componentservice association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.orchestration_to_componentservice_association_object, domain=OrchestrationToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.administrative_operational_to_componentservice_association_object = Slot(uri=RDF.object, name="administrative operational to componentservice association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.administrative_operational_to_componentservice_association_object, domain=AdministrativeOperationalToComponentserviceAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.resource_sample_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="resource sample to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.resource_sample_to_entity_association_mixin_subject, domain=None, range=Union[str, ResourceSampleId])

slots.resource_sample_derivation_association_subject = Slot(uri=RDF.subject, name="resource sample derivation association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.resource_sample_derivation_association_subject, domain=ResourceSampleDerivationAssociation, range=Union[str, ResourceSampleId])

slots.resource_sample_derivation_association_object = Slot(uri=RDF.object, name="resource sample derivation association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.resource_sample_derivation_association_object, domain=ResourceSampleDerivationAssociation, range=Union[str, NamedThingId])

slots.resource_sample_derivation_association_predicate = Slot(uri=RDF.predicate, name="resource sample derivation association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.resource_sample_derivation_association_predicate, domain=ResourceSampleDerivationAssociation, range=Union[str, PredicateType])

slots.error_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="error to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.error_to_entity_association_mixin_subject, domain=None, range=Union[str, ErrorId])

slots.entity_to_exposure_event_association_mixin_object = Slot(uri=RDF.object, name="entity to exposure event association mixin_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.entity_to_exposure_event_association_mixin_object, domain=None, range=Union[dict, ExposureEvent])

slots.exposure_event_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="exposure event to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.exposure_event_to_entity_association_mixin_subject, domain=None, range=Union[dict, ExposureEvent])

slots.entity_to_outcome_association_mixin_object = Slot(uri=RDF.object, name="entity to outcome association mixin_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.entity_to_outcome_association_mixin_object, domain=None, range=Union[dict, Outcome])

slots.entity_to_observable_feature_association_mixin_description = Slot(uri=DCT.description, name="entity to observable feature association mixin_description", curie=DCT.curie('description'),
                   model_uri=SAMPLELINK.entity_to_observable_feature_association_mixin_description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.entity_to_observable_feature_association_mixin_object = Slot(uri=RDF.object, name="entity to observable feature association mixin_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.entity_to_observable_feature_association_mixin_object, domain=None, range=Union[str, ObservableFeatureId])

slots.entity_to_error_association_mixin_object = Slot(uri=RDF.object, name="entity to error association mixin_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.entity_to_error_association_mixin_object, domain=None, range=Union[str, ErrorId])

slots.error_or_observable_feature_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="error or observable feature to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.error_or_observable_feature_to_entity_association_mixin_subject, domain=None, range=Union[str, ErrorOrObservableFeatureId])

slots.error_or_observable_feature_association_to_location_association_object = Slot(uri=RDF.object, name="error or observable feature association to location association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.error_or_observable_feature_association_to_location_association_object, domain=ErrorOrObservableFeatureAssociationToLocationAssociation, range=Union[str, DeploymentEntityId])

slots.error_or_observable_feature_to_location_association_object = Slot(uri=RDF.object, name="error or observable feature to location association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.error_or_observable_feature_to_location_association_object, domain=ErrorOrObservableFeatureToLocationAssociation, range=Union[str, DeploymentEntityId])

slots.entity_to_error_or_observable_feature_association_mixin_object = Slot(uri=RDF.object, name="entity to error or observable feature association mixin_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.entity_to_error_or_observable_feature_association_mixin_object, domain=None, range=Union[str, ErrorOrObservableFeatureId])

slots.serviceunittype_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="serviceunittype to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.serviceunittype_to_entity_association_mixin_subject, domain=None, range=Union[str, ServiceunittypeId])

slots.serviceunittype_to_observable_feature_association_predicate = Slot(uri=RDF.predicate, name="serviceunittype to observable feature association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.serviceunittype_to_observable_feature_association_predicate, domain=ServiceunittypeToObservableFeatureAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_observable_feature_association_subject = Slot(uri=RDF.subject, name="serviceunittype to observable feature association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.serviceunittype_to_observable_feature_association_subject, domain=ServiceunittypeToObservableFeatureAssociation, range=Union[str, ServiceunittypeId])

slots.exposure_event_to_observable_feature_association_subject = Slot(uri=RDF.subject, name="exposure event to observable feature association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.exposure_event_to_observable_feature_association_subject, domain=ExposureEventToObservableFeatureAssociation, range=Union[dict, ExposureEvent])

slots.behavior_to_behavioral_feature_association_subject = Slot(uri=RDF.subject, name="behavior to behavioral feature association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.behavior_to_behavioral_feature_association_subject, domain=BehaviorToBehavioralFeatureAssociation, range=Union[str, BehaviorId])

slots.behavior_to_behavioral_feature_association_object = Slot(uri=RDF.object, name="behavior to behavioral feature association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.behavior_to_behavioral_feature_association_object, domain=BehaviorToBehavioralFeatureAssociation, range=Union[str, BehavioralFeatureId])

slots.componentservice_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="componentservice to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentservice_to_entity_association_mixin_subject, domain=None, range=Union[dict, ComponentserviceOrServicetype])

slots.variant_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="variant to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.variant_to_entity_association_mixin_subject, domain=None, range=Union[str, SequenceVariantId])

slots.componentservice_to_observable_feature_association_subject = Slot(uri=RDF.subject, name="componentservice to observable feature association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentservice_to_observable_feature_association_subject, domain=ComponentserviceToObservableFeatureAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_error_association_subject = Slot(uri=RDF.subject, name="componentservice to error association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentservice_to_error_association_subject, domain=ComponentserviceToErrorAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.variant_to_componentservice_association_object = Slot(uri=RDF.object, name="variant to componentservice association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.variant_to_componentservice_association_object, domain=VariantToComponentserviceAssociation, range=Union[dict, Componentservice])

slots.variant_to_componentservice_association_predicate = Slot(uri=RDF.predicate, name="variant to componentservice association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.variant_to_componentservice_association_predicate, domain=VariantToComponentserviceAssociation, range=Union[str, PredicateType])

slots.variant_to_componentservice_availability_association_predicate = Slot(uri=RDF.predicate, name="variant to componentservice availability association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.variant_to_componentservice_availability_association_predicate, domain=VariantToComponentserviceAvailabilityAssociation, range=Union[str, PredicateType])

slots.variant_to_population_association_subject = Slot(uri=RDF.subject, name="variant to population association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.variant_to_population_association_subject, domain=VariantToPopulationAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_population_association_object = Slot(uri=RDF.object, name="variant to population association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.variant_to_population_association_object, domain=VariantToPopulationAssociation, range=Union[str, PopulationOfIndividualSystemsId])

slots.variant_to_population_association_has_quotient = Slot(uri=SAMPLELINK.has_quotient, name="variant to population association_has quotient", curie=SAMPLELINK.curie('has_quotient'),
                   model_uri=SAMPLELINK.variant_to_population_association_has_quotient, domain=VariantToPopulationAssociation, range=Optional[float])

slots.variant_to_population_association_has_count = Slot(uri=SAMPLELINK.has_count, name="variant to population association_has count", curie=SAMPLELINK.curie('has_count'),
                   model_uri=SAMPLELINK.variant_to_population_association_has_count, domain=VariantToPopulationAssociation, range=Optional[int])

slots.variant_to_population_association_has_total = Slot(uri=SAMPLELINK.has_total, name="variant to population association_has total", curie=SAMPLELINK.curie('has_total'),
                   model_uri=SAMPLELINK.variant_to_population_association_has_total, domain=VariantToPopulationAssociation, range=Optional[int])

slots.population_to_population_association_subject = Slot(uri=RDF.subject, name="population to population association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.population_to_population_association_subject, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualSystemsId])

slots.population_to_population_association_object = Slot(uri=RDF.object, name="population to population association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.population_to_population_association_object, domain=PopulationToPopulationAssociation, range=Union[str, PopulationOfIndividualSystemsId])

slots.population_to_population_association_predicate = Slot(uri=RDF.predicate, name="population to population association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.population_to_population_association_predicate, domain=PopulationToPopulationAssociation, range=Union[str, PredicateType])

slots.variant_to_observable_feature_association_subject = Slot(uri=RDF.subject, name="variant to observable feature association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.variant_to_observable_feature_association_subject, domain=VariantToObservableFeatureAssociation, range=Union[str, SequenceVariantId])

slots.variant_to_error_association_subject = Slot(uri=RDF.subject, name="variant to error association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.variant_to_error_association_subject, domain=VariantToErrorAssociation, range=Union[str, NamedThingId])

slots.variant_to_error_association_predicate = Slot(uri=RDF.predicate, name="variant to error association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.variant_to_error_association_predicate, domain=VariantToErrorAssociation, range=Union[str, PredicateType])

slots.variant_to_error_association_object = Slot(uri=RDF.object, name="variant to error association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.variant_to_error_association_object, domain=VariantToErrorAssociation, range=Union[str, NamedThingId])

slots.serviceunittype_to_error_association_subject = Slot(uri=RDF.subject, name="serviceunittype to error association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.serviceunittype_to_error_association_subject, domain=ServiceunittypeToErrorAssociation, range=Union[str, NamedThingId])

slots.serviceunittype_to_error_association_predicate = Slot(uri=RDF.predicate, name="serviceunittype to error association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.serviceunittype_to_error_association_predicate, domain=ServiceunittypeToErrorAssociation, range=Union[str, PredicateType])

slots.serviceunittype_to_error_association_object = Slot(uri=RDF.object, name="serviceunittype to error association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.serviceunittype_to_error_association_object, domain=ServiceunittypeToErrorAssociation, range=Union[str, NamedThingId])

slots.model_to_error_association_mixin_subject = Slot(uri=RDF.subject, name="model to error association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.model_to_error_association_mixin_subject, domain=None, range=Union[str, NamedThingId])

slots.model_to_error_association_mixin_predicate = Slot(uri=RDF.predicate, name="model to error association mixin_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.model_to_error_association_mixin_predicate, domain=None, range=Union[str, PredicateType])

slots.componentservice_as_a_model_of_error_association_subject = Slot(uri=RDF.subject, name="componentservice as a model of error association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentservice_as_a_model_of_error_association_subject, domain=ComponentserviceAsAModelOfErrorAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.variant_as_a_model_of_error_association_subject = Slot(uri=RDF.subject, name="variant as a model of error association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.variant_as_a_model_of_error_association_subject, domain=VariantAsAModelOfErrorAssociation, range=Union[str, SequenceVariantId])

slots.serviceunittype_as_a_model_of_error_association_subject = Slot(uri=RDF.subject, name="serviceunittype as a model of error association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.serviceunittype_as_a_model_of_error_association_subject, domain=ServiceunittypeAsAModelOfErrorAssociation, range=Union[str, ServiceunittypeId])

slots.component_type_as_a_model_of_error_association_subject = Slot(uri=RDF.subject, name="component type as a model of error association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.component_type_as_a_model_of_error_association_subject, domain=ComponentTypeAsAModelOfErrorAssociation, range=Union[str, ComponentTypeId])

slots.systemic_entity_as_a_model_of_error_association_subject = Slot(uri=RDF.subject, name="systemic entity as a model of error association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.systemic_entity_as_a_model_of_error_association_subject, domain=SystemicEntityAsAModelOfErrorAssociation, range=Union[str, SystemicEntityId])

slots.componentservice_has_variant_that_contributes_to_error_association_subject = Slot(uri=RDF.subject, name="componentservice has variant that contributes to error association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentservice_has_variant_that_contributes_to_error_association_subject, domain=ComponentserviceHasVariantThatContributesToErrorAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_availability_site_association_subject = Slot(uri=RDF.subject, name="componentservice to availability site association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentservice_to_availability_site_association_subject, domain=ComponentserviceToAvailabilitySiteAssociation, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_to_availability_site_association_object = Slot(uri=RDF.object, name="componentservice to availability site association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.componentservice_to_availability_site_association_object, domain=ComponentserviceToAvailabilitySiteAssociation, range=Union[str, DeploymentEntityId])

slots.componentservice_to_availability_site_association_predicate = Slot(uri=RDF.predicate, name="componentservice to availability site association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.componentservice_to_availability_site_association_predicate, domain=ComponentserviceToAvailabilitySiteAssociation, range=Union[str, PredicateType])

slots.componentservice_to_availability_site_association_stage_qualifier = Slot(uri=SAMPLELINK.stage_qualifier, name="componentservice to availability site association_stage qualifier", curie=SAMPLELINK.curie('stage_qualifier'),
                   model_uri=SAMPLELINK.componentservice_to_availability_site_association_stage_qualifier, domain=ComponentserviceToAvailabilitySiteAssociation, range=Optional[Union[str, LifecycleStageId]])

slots.componentservice_to_availability_site_association_quantifier_qualifier = Slot(uri=SAMPLELINK.quantifier_qualifier, name="componentservice to availability site association_quantifier qualifier", curie=SAMPLELINK.curie('quantifier_qualifier'),
                   model_uri=SAMPLELINK.componentservice_to_availability_site_association_quantifier_qualifier, domain=ComponentserviceToAvailabilitySiteAssociation, range=Optional[Union[str, OntologyClassId]])

slots.sequence_variant_modulates_repairing_association_subject = Slot(uri=RDF.subject, name="sequence variant modulates repairing association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.sequence_variant_modulates_repairing_association_subject, domain=SequenceVariantModulatesRepairingAssociation, range=Union[str, SequenceVariantId])

slots.sequence_variant_modulates_repairing_association_object = Slot(uri=RDF.object, name="sequence variant modulates repairing association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.sequence_variant_modulates_repairing_association_object, domain=SequenceVariantModulatesRepairingAssociation, range=Union[str, RepairingId])

slots.functional_association_subject = Slot(uri=RDF.subject, name="functional association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.functional_association_subject, domain=FunctionalAssociation, range=Union[dict, MacrooperationalMachineMixin])

slots.functional_association_object = Slot(uri=RDF.object, name="functional association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.functional_association_object, domain=FunctionalAssociation, range=Union[str, ComponentserviceOntologyClassId])

slots.macrooperational_machine_mixin_to_entity_association_mixin_subject = Slot(uri=RDF.subject, name="macrooperational machine mixin to entity association mixin_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.macrooperational_machine_mixin_to_entity_association_mixin_subject, domain=None, range=Union[str, NamedThingId])

slots.macrooperational_machine_mixin_to_operational_activity_association_object = Slot(uri=RDF.object, name="macrooperational machine mixin to operational activity association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.macrooperational_machine_mixin_to_operational_activity_association_object, domain=MacrooperationalMachineMixinToOperationalActivityAssociation, range=Union[str, OperationalActivityId])

slots.macrooperational_machine_mixin_to_computational_process_association_object = Slot(uri=RDF.object, name="macrooperational machine mixin to computational process association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.macrooperational_machine_mixin_to_computational_process_association_object, domain=MacrooperationalMachineMixinToComputationalProcessAssociation, range=Union[str, ComputationalProcessId])

slots.macrooperational_machine_mixin_to_component_association_object = Slot(uri=RDF.object, name="macrooperational machine mixin to component association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.macrooperational_machine_mixin_to_component_association_object, domain=MacrooperationalMachineMixinToComponentAssociation, range=Union[str, ComponentId])

slots.componentservice_to_go_term_association_subject = Slot(uri=RDF.subject, name="componentservice to go term association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentservice_to_go_term_association_subject, domain=ComponentserviceToGoTermAssociation, range=Union[str, OperationalEntityId])

slots.componentservice_to_go_term_association_object = Slot(uri=RDF.object, name="componentservice to go term association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.componentservice_to_go_term_association_object, domain=ComponentserviceToGoTermAssociation, range=Union[str, ComponentserviceOntologyClassId])

slots.componentservice_sequence_localization_subject = Slot(uri=RDF.subject, name="componentservice sequence localization_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentservice_sequence_localization_subject, domain=ComponentserviceSequenceLocalization, range=Union[str, WorkloadEntityId])

slots.componentservice_sequence_localization_object = Slot(uri=RDF.object, name="componentservice sequence localization_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.componentservice_sequence_localization_object, domain=ComponentserviceSequenceLocalization, range=Union[str, WorkloadEntityId])

slots.componentservice_sequence_localization_predicate = Slot(uri=RDF.predicate, name="componentservice sequence localization_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.componentservice_sequence_localization_predicate, domain=ComponentserviceSequenceLocalization, range=Union[str, PredicateType])

slots.sequence_feature_relationship_subject = Slot(uri=RDF.subject, name="sequence feature relationship_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.sequence_feature_relationship_subject, domain=SequenceFeatureRelationship, range=Union[str, WorkloadEntityId])

slots.sequence_feature_relationship_object = Slot(uri=RDF.object, name="sequence feature relationship_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.sequence_feature_relationship_object, domain=SequenceFeatureRelationship, range=Union[str, WorkloadEntityId])

slots.componentserviceinstance_to_componentservice_relationship_subject = Slot(uri=RDF.subject, name="componentserviceinstance to componentservice relationship_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentserviceinstance_to_componentservice_relationship_subject, domain=ComponentserviceinstanceToComponentserviceRelationship, range=Union[str, ComponentserviceinstanceId])

slots.componentserviceinstance_to_componentservice_relationship_object = Slot(uri=RDF.object, name="componentserviceinstance to componentservice relationship_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.componentserviceinstance_to_componentservice_relationship_object, domain=ComponentserviceinstanceToComponentserviceRelationship, range=Union[dict, Componentservice])

slots.componentservice_to_servicetype_relationship_subject = Slot(uri=RDF.subject, name="componentservice to servicetype relationship_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentservice_to_servicetype_relationship_subject, domain=ComponentserviceToServicetypeRelationship, range=Union[dict, Componentservice])

slots.componentservice_to_servicetype_relationship_object = Slot(uri=RDF.object, name="componentservice to servicetype relationship_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.componentservice_to_servicetype_relationship_object, domain=ComponentserviceToServicetypeRelationship, range=Union[dict, ServicetypeMixin])

slots.componentservice_to_servicetype_relationship_predicate = Slot(uri=RDF.predicate, name="componentservice to servicetype relationship_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.componentservice_to_servicetype_relationship_predicate, domain=ComponentserviceToServicetypeRelationship, range=Union[str, PredicateType])

slots.daemon_to_componentserviceinstance_relationship_subject = Slot(uri=RDF.subject, name="daemon to componentserviceinstance relationship_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.daemon_to_componentserviceinstance_relationship_subject, domain=DaemonToComponentserviceinstanceRelationship, range=Union[str, DaemonId])

slots.daemon_to_componentserviceinstance_relationship_object = Slot(uri=RDF.object, name="daemon to componentserviceinstance relationship_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.daemon_to_componentserviceinstance_relationship_object, domain=DaemonToComponentserviceinstanceRelationship, range=Union[str, ComponentserviceinstanceId])

slots.componentservice_regulatory_relationship_predicate = Slot(uri=RDF.predicate, name="componentservice regulatory relationship_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.componentservice_regulatory_relationship_predicate, domain=ComponentserviceRegulatoryRelationship, range=Union[str, PredicateType])

slots.componentservice_regulatory_relationship_subject = Slot(uri=RDF.subject, name="componentservice regulatory relationship_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.componentservice_regulatory_relationship_subject, domain=ComponentserviceRegulatoryRelationship, range=Union[dict, ComponentserviceOrServicetype])

slots.componentservice_regulatory_relationship_object = Slot(uri=RDF.object, name="componentservice regulatory relationship_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.componentservice_regulatory_relationship_object, domain=ComponentserviceRegulatoryRelationship, range=Union[dict, ComponentserviceOrServicetype])

slots.deployment_entity_to_deployment_entity_association_subject = Slot(uri=RDF.subject, name="deployment entity to deployment entity association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.deployment_entity_to_deployment_entity_association_subject, domain=DeploymentEntityToDeploymentEntityAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_association_object = Slot(uri=RDF.object, name="deployment entity to deployment entity association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.deployment_entity_to_deployment_entity_association_object, domain=DeploymentEntityToDeploymentEntityAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_part_of_association_subject = Slot(uri=RDF.subject, name="deployment entity to deployment entity part of association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.deployment_entity_to_deployment_entity_part_of_association_subject, domain=DeploymentEntityToDeploymentEntityPartOfAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_part_of_association_object = Slot(uri=RDF.object, name="deployment entity to deployment entity part of association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.deployment_entity_to_deployment_entity_part_of_association_object, domain=DeploymentEntityToDeploymentEntityPartOfAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_part_of_association_predicate = Slot(uri=RDF.predicate, name="deployment entity to deployment entity part of association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.deployment_entity_to_deployment_entity_part_of_association_predicate, domain=DeploymentEntityToDeploymentEntityPartOfAssociation, range=Union[str, PredicateType])

slots.deployment_entity_to_deployment_entity_ontogenic_association_subject = Slot(uri=RDF.subject, name="deployment entity to deployment entity ontogenic association_subject", curie=RDF.curie('subject'),
                   model_uri=SAMPLELINK.deployment_entity_to_deployment_entity_ontogenic_association_subject, domain=DeploymentEntityToDeploymentEntityOntogenicAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_ontogenic_association_object = Slot(uri=RDF.object, name="deployment entity to deployment entity ontogenic association_object", curie=RDF.curie('object'),
                   model_uri=SAMPLELINK.deployment_entity_to_deployment_entity_ontogenic_association_object, domain=DeploymentEntityToDeploymentEntityOntogenicAssociation, range=Union[str, DeploymentEntityId])

slots.deployment_entity_to_deployment_entity_ontogenic_association_predicate = Slot(uri=RDF.predicate, name="deployment entity to deployment entity ontogenic association_predicate", curie=RDF.curie('predicate'),
                   model_uri=SAMPLELINK.deployment_entity_to_deployment_entity_ontogenic_association_predicate, domain=DeploymentEntityToDeploymentEntityOntogenicAssociation, range=Union[str, PredicateType])
