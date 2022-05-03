from flask import Flask, request
from flask_restful import Resource, Api
from dataQuerying import DataStore

app = Flask(__name__)
api = Api(app)
ds = DataStore("programming_test_data.tsv")

class GeneNames(Resource):
    def get(self):
        # return request.args["area"])
        if "area" in request.args:
            return ds.get_unique_gene_names(request.args["area"])
        else:
            return ds.get_unique_gene_names()

class GeneNameToId(Resource):
    def get(self, name):
        return ds.gene_name_to_id(name)

class GeneAssociations(Resource):
    def get(self):
        if "score" in request.args:
            return ds.gene_name_to_disease(request.args["gene"], request.args["score"])
        else:
            return ds.gene_name_to_disease(request.args["gene"])

api.add_resource(GeneNames, '/gene_names') # optional param: area
api.add_resource(GeneNameToId, '/gene_name_to_id/<name>')
api.add_resource(GeneAssociations, '/gene_name_disease_associations') # required param: gene, optional param: score