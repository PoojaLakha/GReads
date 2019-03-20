from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

# Create a connection to ElasticSearch
connections.create_connection()


# ElasticSearch "model" mapping out what fields to index
class BookIndex(DocType):
    title = Text()

    class Index:
        name = 'book-index'


# Bulk indexing function, run in shell
def bulk_indexing():
    BookIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in
                             models.Book.objects.only('title').iterator()))
