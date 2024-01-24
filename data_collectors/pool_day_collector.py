import requests
import json
import pandas as pd

def query_the_graph(query):
    url = 'https://gateway-arbitrum.network.thegraph.com/api/48f7042b8531bbba9a96514ad4e8c7e8/subgraphs/id/HUZDsRpEVP2AvzDCyzDHtdc64dyDxx8FQjzsmqSg4H3B'
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

def get_all_pool_day_data():
    all_data = []
    last_id = ""
    while True:
      try:
        print("hey" if last_id == "" else last_id)
        first_query = """
        {
          poolDayDatas(first: 1000, orderBy: id, orderDirection: asc)  {
            close
            date
            feeGrowthGlobal0X128
            feeGrowthGlobal1X128
            feesUSD
            high
            id
            liquidity
            low
            open
            pool {
                id
            }
            sqrtPrice
            tick
            token0Price
            token1Price
            totalValueLockedUSD
            txCount
            volumeToken0
            volumeToken1
            volumeUSD
        }
        """
        query = """
        {
          poolDayDatas(first: 1000, orderBy: id, orderDirection: asc, where: {id_gt: "%s"}) {
            close
            date
            feeGrowthGlobal0X128
            feeGrowthGlobal1X128
            feesUSD
            high
            id
            liquidity
            low
            open
            pool {
                id
            }
            sqrtPrice
            tick
            token0Price
            token1Price
            totalValueLockedUSD
            txCount
            volumeToken0
            volumeToken1
            volumeUSD
        }
        """ % last_id

        # print(query)

        if (last_id == ""):
          result = query_the_graph(first_query)
        else:
          result = query_the_graph(query)
        pool_day_data = result.get('data', {}).get('pools', [])

        if not pool_day_data:
            break

        if (len(pool_day_data) < 1000):
          print(len(pool_day_data))
          break
        all_data.extend(pool_day_data)
        # skip_amount += 1000
        last_id = pool_day_data[-1]["id"]
      except Exception as e:
        print(f"An error occurred: {e}")
        break
    return all_data

def save_to_csv(data):
    df = pd.json_normalize(data)
    df.to_csv('pool_day_data.csv', index=False)

all_pool_day_data = get_all_pool_day_data()
save_to_csv(all_pool_day_data)

print("Data Collected Successfully")
