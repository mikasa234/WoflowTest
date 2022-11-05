import requests
import json
from collections import deque, Counter


unique_nodeIDs = []
Queue = deque()
class FetchData:
    url = "https://nodes-on-nodes-challenge.herokuapp.com/nodes/"
    def get(self, ID):
        Queue.append(ID)
        while Queue:
            curr_node_id = Queue.popleft()
            print(curr_node_id)

            response2 = requests.get(self.url + curr_node_id)
            print(response2.json())
            status_code = response2.status_code
            # print(status_code)
            if status_code == 200:
                for node_dict in response2.json():
                    curr_id = node_dict["id"]
                    # print("curr_node = {}".format(curr_id))
                    # if id in unique_nodeIDs:
                    #     unique_nodeIDs[id] += 1
                    # else:
                    unique_nodeIDs.append(curr_id)
                    # Queue.append(id)
                    children = node_dict["child_node_ids"]

                    for child in children:
                        Queue.append(child)
                    # print("queue = {}]\n".format(Queue))
        return Counter(unique_nodeIDs)
                            

if __name__ == "__main__":
    getData = FetchData()
    resp = getData.get("c20c063c-99b3-452f-a44f-72e2dac4eec0")
    # unique ids
    unique_IDs = resp.keys()
    print(unique_IDs)

    most_Common = resp.most_common(1)
    print(most_Common)
    



                        
                                

