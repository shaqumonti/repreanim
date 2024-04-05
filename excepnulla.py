    from google.cloud import enterpriseknowledgegraph as ekg

    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_GRAPH_LOCATION'    # Values: 'global'
    # wallet_id = 'YOUR_WALLET_ID'

    client = ekg.EnterpriseKnowledgeGraphServiceClient()

    # The full resource name of the wallet
    name = client.wallet_path(project_id, location, wallet_id)

    # Initialize request argument(s)
    request = ekg.GetWalletTransactionsRequest(name=name)

    # Make the request
    response = client.get_wallet_transactions(request=request)

    print(response)  
