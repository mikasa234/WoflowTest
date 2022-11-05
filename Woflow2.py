import requests
import json
from collections import deque, Counter


nodeIDs = []
Queue = deque()
class FetchData:
    url = "https://nodes-on-nodes-challenge.herokuapp.com/nodes/"
    def get(self, ID):
        Queue.append(ID)
        while Queue:
            curr_node_id = Queue.popleft()
            if curr_node_id not in nodeIDs:
                response2 = requests.get(self.url + curr_node_id)
                status_code = response2.status_code
                if status_code == 200:
                    for node_dict in response2.json():
                        curr_id = node_dict["id"]
                        nodeIDs.append(curr_id)
                        children = node_dict["child_node_ids"]

                        for child in children:
                            Queue.append(child)
            else:
                nodeIDs.append(curr_node_id)

        return Counter(nodeIDs)
                            

if __name__ == "__main__":
    getData = FetchData()
    resp = getData.get("c20c063c-99b3-452f-a44f-72e2dac4eec0")
    # unique ids
    unique_IDs = resp.keys()
    print(len(unique_IDs))

    # most common node ID
    most_Common = resp.most_common(1)
    print(most_Common)
    



                        
                                

