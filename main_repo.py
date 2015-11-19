import gridiot_repo

if __name__ == '__main__':
    print 'call gridiot_repo'
    iot_results = gridiot_repo.get_device_query_repo("iotportal")
#    print iot_results['hits']['total']
    web_results = gridiot_repo.get_device_query_repo("webservice")
#    print web_results['hits']['total']
    print 'total his: {0} (Web Service: {1}, IoT Portal: {2})'.format(iot_results['hits']['total']+web_results['hits']['total'], web_results['hits']['total'], iot_results['hits']['total'])
