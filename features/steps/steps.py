from behave import *
from SPARQLWrapper import SPARQLWrapper, JSON, XML, CSV, TSV
import pandas as pd, io
import numpy as np

"""
Given the dataset "https://w3id.org/data2services/graph/biolink/drugbank"
When we get the entity "http://identifiers.org/drugbank:DB00001"
Then its property "bl:name" should be "Lepirudin"
"""


@given('the dataset "{graphUri}"')
def step_impl(context, graphUri):
    context.graphUri = graphUri

@when('we get the entity "{entityUri}"')
def step_impl(context, entityUri):
    context.entityUri = entityUri

@then('its property "{predicate}" should be "{value}"')
def step_impl(context, predicate, value):

    sparql = SPARQLWrapper("http://graphdb.dumontierlab.com/repositories/ncats-red-kg")
    query = """
    PREFIX bl: <http://w3id.org/biolink/vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dct: <http://purl.org/dc/terms/>
    PREFIX dctypes: <http://purl.org/dc/dcmitype/>
    PREFIX idot: <http://identifiers.org/idot/>
    PREFIX dcat: <http://www.w3.org/ns/dcat#>
    PREFIX void: <http://rdfs.org/ns/void#>
    PREFIX void-ext: <http://ldf.fi/void-ext#>
    SELECT ?propertyValue
    WHERE {
        GRAPH <%s> {
            <%s> %s ?propertyValue .
        }
    }
    """

    sparql.setQuery(query % (context.graphUri, context.entityUri, predicate))
    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()
    print(results["results"]["bindings"])
    
    # This loop doesn't work. The result var is empty, even if print shows that results["results"]["bindings"] is a list
    # If anyone can find why Python can't do a for loop on an array I would be interested.
    # We get the first answer directly from array index [0] 
    # See SPARQL example here: https://rdflib.github.io/sparqlwrapper/
    for result in np.asarray(results["results"]["bindings"]):
        print("we don't get into this loop")
    # for i in range(len(results["results"]["bindings"])):
    
    assert value == results["results"]["bindings"][0]["propertyValue"]["value"]
