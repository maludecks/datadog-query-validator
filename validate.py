import json
from datadog import initialize, api

with open('config.json') as json_file:
    data = json.load(json_file)

    options = {
        'api_key': data['datadog']['api_key'],
        'app_key': data['datadog']['app_key']
    }

    initialize(**options)

    monitor_type = data['validation_input']['monitor_type']
    query = data['validation_input']['query']
    monitor_options = {"thresholds": {"critical": data['validation_input']['threshold']}}

    response = api.Monitor.validate(
        type=monitor_type,
        query=query,
        options=monitor_options,
    )

    if not bool(response):
        print 'Success: The query is valid'

    if 'errors' in response:
        print 'Error:'
        for error in response.get('errors'):
            print '- %s' % error
