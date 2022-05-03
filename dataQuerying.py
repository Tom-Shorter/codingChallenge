import pandas as pd

class DataStore:

	def __init__(self, file):
		self.df = pd.read_csv(file, sep="\t")

	def get_unique_gene_names(self, therapeuticArea: str = None):
		'''

		:param therapeuticArea: OPTIONAL Ontology ID (string)
		:return: List of unique gene names
		'''
		if therapeuticArea:
			df = self.df.query('therapeuticAreas == @therapeuticArea')
		else:
			df = self.df
		return df.approvedSymbol.unique().tolist()

	def gene_name_to_id(self, geneName: str):
		'''

		:param geneName: REQUIRED Gene Name to convert to ID (string)
		:return: ID of provided Gene Name (string)
		'''
		res = self.df.query('approvedSymbol == @geneName')
		return res.get("id").unique()[0]

	def gene_name_to_disease(self, geneName: str, score: float = None):
		'''

		:param geneName: REQUIRED Gene Name (string)
		:param score: OPTIONAL score threshold to apply (float)
		:return: Dictionary of disease associations
		'''
		res = self.df.query("approvedSymbol == @geneName")
		if score:
			score = float(score)
			res = res.query("score > @score")
		return {
			geneName: GeneDiseaseAssociations(res).get_associations()
		}

class GeneDiseaseAssociations:

	def __init__(self, ds):
		self.ds = ds
		self.associations = self.__get_associations()

	def __get_associations(self):
		associations = []
		for idx, row in self.ds.iterrows():
			resDict = row[["datatypeId", "name", "score"]].to_dict()
			if resDict in associations:
				continue
			else:
				associations.append(resDict)
		return associations

	def get_associations(self):
		return self.associations

