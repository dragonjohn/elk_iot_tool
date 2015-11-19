import gridiot_repo

if __name__ == '__main__':
    print 'call gridiot_repo'
    results = gridiot_repo.get_device_query_repo()
    print results['hits']['total']
