# Setup

This was built using python 3.6

_Optional but recommended_: Create and activate a python virtual environment

#

To install dependencies:

`$ pip install -r requirements.txt`

To run the server:

`$ flask run`

# Endpoints

`/gene_names`

http://127.0.0.1:5000/gene_names

Returns a list of unique gene names within the testData dataset.

`/gene_names?area=<therapeutic area>`

http://127.0.0.1:5000/gene_names?area=EFO_0000651

Returns a list of unique gene names within the testData dataset which are associated with the provided therapeutic area.

`/gene_name_to_id/<name>`

http://127.0.0.1:5000/gene_name_to_id/STPG1

Returns the ID of the provided gene name

`/gene_name_disease_associations?gene=<geneName>&score=<score>`

http://127.0.0.1:5000/gene_name_disease_associations?gene=STPG1&score=0.04

returns the dict formatted gene -> disease associations. gene is required (no error handling defined), score is optional

# Improvements to be made

Commenting can always be made better

`gene_name_to_disease` return value could be created much more cleanly with a different class structure

query params were handled very naively (no tests for required params or validation of the param values),
better approach would have been to use a package such as [marshmallow](https://marshmallow.readthedocs.io/en/stable/),
this could have also been applied to the return values

No error handling was attempted. This is mainly due to there being a lack of description about how errors should be
handled. Flask abort statements would be very useful for this.

No unit tests provided/created, ideally there would be some!

ds was used as a global variable within app.py, I'd much prefer to pass this through to the classes which used it.
