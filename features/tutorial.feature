Feature: showing off behave

  # Scenario: run a simple test
  #    Given we have behave installed
  #     When we implement a test
  #     Then behave will test it for us!

  Scenario: Check for DrugBank drug name
    Given the dataset "https://w3id.org/data2services/graph/biolink/drugbank"
    When we get the entity "http://identifiers.org/drugbank:DB00001"
    Then its property "bl:name" should be "Lepirudin"
