from behave import *

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

@then('its property "{property}" should be "{value}"')
def step_impl(context, property, value):
    # Do SPARQL query
    assert context.graphUri == "https://w3id.org/data2services/graph/biolink/drugbank"