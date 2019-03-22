import os, base64, re, logging
from elasticsearch_dsl import DocType, Text
from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from . import models

# Log transport details (optional):
logging.basicConfig(level=logging.INFO)

# Parse the auth and host from env:
bonsai = os.environ['BONSAI_URL']
auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')


# Connect to cluster over SSL using auth for best security:
es_header = [{
    'host': host,
    'port': 443,
    'use_ssl': True,
    'http_auth': (auth[0], auth[1])
}]


# Instantiate the new Elasticsearch connection:
es = Elasticsearch(es_header)

# Verify that Python can talk to Bonsai (optional):
es.ping()


class BookIndex(DocType):
    title = Text()

    class Meta:
        index = 'book-index'


connections.create_connection(hosts=os.environ['BONSAI_URL'], port=443)

# Verify that connection is established (optional):
connections.get_connection().cluster.health()


# Indexes all the pre-existing(old) documents in database
# should run only once
def bulk_indexing():
    BookIndex.init()
    bulk(client=es, actions=(b.indexing() for b
                             in models.Book.objects.all().iterator()))
