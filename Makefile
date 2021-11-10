# All artifacts of the build should be preserved
.SECONDARY:

# It can be fairly expensive to regenerate the various png's in the markdown.
# There are three alternatives:
#   1) make imgflags="-i"             -- generate uml images in images subdirectory (default)
#   2) make imgflags="-i --noimages"  -- assume uml images already exist and generate links to them
#   3) make imgflags=""               -- genrate uml images as inline url's
imgflags?=-i


# ----------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------
all: install tests build

# Build the samplelink model python library
python: samplelink/model.py
docs: docs/index.md
jekyll-docs: docs/Classes.md

shex: samplelink-model.shex samplelink-modeln.shex samplelink-model.shexj samplelink-modeln.shexj
json-schema: json-schema/samplelink-model.json
prefix-map: prefix-map/samplelink-model-prefix-map.json

build: python docs/index.md gen-golr-views samplelink-model.graphql gen-graphviz java context.jsonld contextn.jsonld \
json-schema/samplelink-model.json samplelink-model.owl samplelink-model.proto shex samplelink-model.ttl \
prefix-map/samplelink-model-prefix-map.json

# TODO: Get this working
build_contrib: contrib_build_monarch contrib_build_translator contrib_build_go

install: env.lock



# ---------------------------------------
# Install package into build environment
# ---------------------------------------
env.lock:
	echo "env.lock"
	pipenv install --dev
	cp /dev/null env.lock


# ----------------------------------------
# BUILD/COMPILATION
# ----------------------------------------
# ~~~~~~~~~~~~~~~~~~~~
# Python
# ~~~~~~~~~~~~~~~~~~~~
samplelink/model.py: samplelink-model.yaml env.lock
	echo "generate python"
	pipenv run gen-py-classes $< > $@.tmp && pipenv run python $@.tmp &&  mv $@.tmp $@


# ~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/index.md: samplelink-model.yaml env.lock
	echo "generate markdown"
	pipenv run gen-markdown --dir docs $(imgflags) $<

# ~~~~~~~~~~~~~~~~~~~~
# JEKYLL DOCS
# ~~~~~~~~~~~~~~~~~~~~
docs/Classes.md: samplelink-model.yaml env.lock
	echo "generate jekyllmd"
	pipenv run python script/jekyllmarkdowngen.py --dir jekyll_docs --yaml $<


# ~~~~~~~~~~~~~~~~~~~~
# Solr
# ~~~~~~~~~~~~~~~~~~~~
gen-golr-views: samplelink-model.yaml dir-golr-views env.lock
	echo "generate golr-views"
	pipenv run gen-golr-views -d golr-views $<


# ~~~~~~~~~~~~~~~~~~~~
# Graphql
# ~~~~~~~~~~~~~~~~~~~~
samplelink-model.graphql: samplelink-model.yaml env.lock
	echo "generate model graphql"
	pipenv run gen-graphql $< > $@


# ~~~~~~~~~~~~~~~~~~~~
# Graphviz
# ~~~~~~~~~~~~~~~~~~~~
gen-graphviz: samplelink-model.yaml dir-graphviz env.lock
	pipenv run gen-graphviz  -d graphviz $< -f gv
	pipenv run gen-graphviz  -d graphviz $< -f svg


# ~~~~~~~~~~~~~~~~~~~~
# Java
# ~~~~~~~~~~~~~~~~~~~~
java: json-schema/samplelink-model.json dir-java env.lock
	echo "generate java"
	jsonschema2pojo --source $< -T JSONSCHEMA -t java


# ~~~~~~~~~~~~~~~~~~~~
# JSON-LD CONTEXT
# ~~~~~~~~~~~~~~~~~~~~
context.jsonld: samplelink-model.yaml env.lock
	echo "generate context.jsonld"
	pipenv run gen-jsonld-context $< > tmp.jsonld
	# ( pipenv run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld
	mv tmp.jsonld $@

contextn.jsonld: samplelink-model.yaml env.lock
	echo "generate contextn.jsonld"
	pipenv run gen-jsonld-context --metauris $< > tmp.jsonld
	# ( pipenv run comparefiles tmp.jsonld $@ -c "^\s*\"comments\".*\n" && cp tmp.jsonld $@); rm tmp.jsonld
	mv tmp.jsonld $@


# ~~~~~~~~~~~~~~~~~~~~
# JSON-SCHEMA
# ~~~~~~~~~~~~~~~~~~~~
json-schema/samplelink-model.json: samplelink-model.yaml dir-json-schema env.lock
	echo "generate json-schema"
	pipenv run gen-json-schema $< > $@


# ~~~~~~~~~~~~~~~~~~~~
# prefix-map
# ~~~~~~~~~~~~~~~~~~~~

prefix-map/samplelink-model-prefix-map.json: samplelink-model.yaml dir-prefix-map env.lock
	echo "generate prefix-map"
	pipenv run gen-prefix-map $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# Ontology
# ~~~~~~~~~~~~~~~~~~~~
samplelink-model.owl: samplelink-model.yaml env.lock
	echo "generate owl"
	pipenv run gen-owl --no-metaclasses -o $@ $<


# ~~~~~~~~~~~~~~~~~~~~
# Proto
# ~~~~~~~~~~~~~~~~~~~~
samplelink-model.proto: samplelink-model.yaml env.lock
	echo "generate proto"
	pipenv run gen-proto $< > $@

# ~~~~~~~~~~~~~~~~~~~~
# RDF
# ~~~~~~~~~~~~~~~~~~~~
samplelink-model.ttl: samplelink-model.yaml env.lock
	echo "generate rdf"
	pipenv run gen-rdf -f ttl --context https://w3id.org/linkml/context.jsonld $<  > $@

# ~~~~~~~~~~~~~~~~~~~~
# ShEx
# ~~~~~~~~~~~~~~~~~~~~
samplelink-model.shex: samplelink-model.yaml
	echo "generate shex"
	pipenv run gen-shex $< > $@
samplelink-modeln.shex: samplelink-model.yaml
	pipenv run gen-shex --metauris $< > $@
samplelink-model.shexj: samplelink-model.yaml
	pipenv run gen-shex --format json $< > $@
samplelink-modeln.shexj: samplelink-model.yaml
	pipenv run gen-shex --metauris --format json $< > $@


# ----------------------------------------
# Ontology conversion
# ----------------------------------------

# ontology/%.json: ontology/%.ttl
# 	owltools $< -o -f json $@

# ontology/%.obo: ontology/%.ttl
# 	owltools $< -o -f obo --no-check $@

# ontology/%.omn: ontology/%.ttl
# 	owltools $< -o -f omn --prefix '' http://w3id.org/samplelink/vocab/ --prefix def http://purl.obolibrary.org/obo/IAO_0000115 $@

# ontology/%.tree: ontology/%.json
# 	ogr --showdefs -t tree -r $< % > $@

# ontology/%.png: ontology/%.json
# 	ogr-tree -t png -o $@ -r $< %


# ~~~~~~~~~~~~~~~~~~~~
# Contrib
# ~~~~~~~~~~~~~~~~~~~~
contrib_build_%: contrib-dir-% contrib/%/docs/index.md contrib/%/datamodel.py contrib-golr-% contrib/%/%.graphql \
contrib/%/%.owl contrib/%/schema.json contrib-java-% contrib/%/%.shex
	echo
	echo "generate contrib_build"

contrib/%/datamodel.py: contrib-dir-% contrib/%.yaml env.lock
	pipenv run gen-py-classes contrib/$*.yaml > tmp.py && (pipenv run comparefiles tmp.py $@ && cp tmp.py $@); rm tmp.py

contrib/%/docs/index.md: contrib/%.yaml
	pipenv run gen-markdown --dir contrib/$*/docs $<

contrib/%/datamodel.py: contrib/%.yaml
	pipenv run gen-py-classes contrib/$*.yaml > $@

contrib-golr-%: contrib-dir-% contrib/%.yaml
	pipenv run gen-golr-views -d contrib/$*/golr-views contrib/$*.yaml

contrib/%/%.graphql: contrib-dir-% contrib/%.yaml
	pipenv run gen-graphql contrib/$*.yaml > contrib/$*/$*.graphql

contrib-java-%: contrib-dir-% contrib/%/schema.json
	mkdir -p contrib/$*/java
	jsonschema2pojo --source contrib/$*/schema.json -T JSONSCHEMA -t contrib/$*/java

contrib/%/schema.json: contrib-dir-% contrib/%.yaml
	pipenv run gen-json-schema contrib/$*.yaml > $@

contrib/%/%.owl: contrib/%.yaml
	pipenv run gen-owl -o $@ contrib/$*.yaml

contrib/%/%.shex: contrib-dir-% contrib/%.yaml
	pipenv run gen-shex contrib/*.yaml > $@

# ----------------------------------------
# TESTS
# ----------------------------------------
test: tests
tests: samplelink-model.yaml env.lock pytest jsonschema_test
	pipenv run python -m unittest discover -p 'test_*.py'

pytest: samplelink/model.py
	pipenv run python $<

jsonschema_test: json-schema/samplelink-model.json
	echo "jsonschema validate [skip]"
	# jsonschema $<

# ----------------------------------------
# CLEAN
# ----------------------------------------
clean:
	rm -rf contrib/go contrib/monarch contrib/translator docs/images/* docs/*.md golr-views graphql graphviz java json json-schema ontology proto rdf shex
	rm -f env.lock
	pipenv --rm

# ----------------------------------------
# UTILS
# ----------------------------------------
dir-%:
	mkdir -p $*

contrib-dir-%:
	mkdir -p contrib/$*
