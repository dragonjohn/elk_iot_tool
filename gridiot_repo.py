import logging
from datetime import datetime
from elasticsearch import Elasticsearch

def get_device_query_repo():
    es = Elasticsearch()
    
    results = es.search(
        index='gridiot',
        doc_type='postgresql',
        body={
            'query': {
                'filtered':{
                    'query':{
                        'match_all':{}
                    },
                    'filter':{
                        'and':[
                            {'match':{'message' : 'tdevice'}},
                            {'match':{'message' : 'SELECT'}},
                            {"not":{
                                "match":{"message": "COUNT"}
                                }
                            }
                            ]
                        }
                    }
                }
            }
    )
    return results

results = get_device_query_repo()
#print(results)
print('Total %d found in %dms' % (results['hits']['total'], results['took']))
"""
for hit in results['hits']['hits']:
    # get created date for a repo and fallback to authored_date for a commit
    #created_at = parse_date(hit['_source'].get('created_at', hit['_source']['authored_date']))
    print('/%s/%s/%s %s' % (
    hit['_index'], hit['_type'], hit['_id'],
    hit['_source']['message'].replace('\n', ' ')))
print(len(results))
"""
