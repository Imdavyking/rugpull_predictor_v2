import requests
import json
import pandas as pd

def query_the_graph(query):
    url = 'https://gateway-arbitrum.network.thegraph.com/api/e34a8ee6b7924062fceb14f0d69e7c0c/subgraphs/id/HUZDsRpEVP2AvzDCyzDHtdc64dyDxx8FQjzsmqSg4H3B'
    # url = 'https://gateway.thegraph.com/api/45554799c4f941a981c378f5563dca7a/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7'
    request = requests.post(url, json={'query': query})
    if request.status_code == 200:
        response = request.json()
        if 'errors' in response:
            # Print or handle the errors as needed
            print("Errors in GraphQL query:", response['errors'])
            # You might choose to raise an exception or handle it differently depending on your needs
            raise Exception("GraphQL query errors: {}".format(response['errors']))
        return response
    else:
        raise Exception("Query failed with status code {}".format(request.status_code))

def get_all_burn_data():
    all_data = []
    last_id = ""
    while True:
      try:
        print("hey" if last_id == "" else last_id)
        first_query = """
        {
          burns(first: 1000, orderBy: id, orderDirection: asc) {
            amount
            amount0
            amount1
            amountUSD
            id
            logIndex
            origin
            owner
            tickLower
            tickUpper
            timestamp
            pool {
              id
            }
          }
        }
        """
        query = """
        {
          burns(first: 1000, orderBy: id, orderDirection: asc, where: {id_gt: "%s"}) {
            amount
            amount0
            amount1
            amountUSD
            id
            logIndex
            origin
            owner
            tickLower
            tickUpper
            timestamp
            pool {
              id
            }
          }
        }
        """ % last_id

        # print(query)

        if (last_id == ""): 
          result = query_the_graph(first_query)
        else:
          result = query_the_graph(query)
        burn_data = result.get('data', {}).get('burns', [])

        if not burn_data:
            break

        all_data.extend(burn_data)
        # skip_amount += 1000

        if (len(burn_data) < 1000):
          print(len(burn_data))
          break

        last_id = burn_data[-1]["id"]
      except Exception as e:
        print(f"An error occurred: {e}")
        break
    return all_data

def save_to_csv(data):
    df = pd.json_normalize(data)
    df.to_csv('burns.csv', index=False)

all_burn_data = get_all_burn_data()
save_to_csv(all_burn_data)

print("Data Collected Successfully")
